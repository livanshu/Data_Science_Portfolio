# Loan Default Prediction (End to End ML using Snowflake & Dataiku)

## Overview

To build a binary classification model that predicts the likelihood of a lender defaulting on a loan. 

![Alt text](https://github.com/livanshu/Data_Science_Portfolio/blob/main/Projects/Loan_Default_Prediction_EndtoEnd_Snowflake_Dataiku/Images/Pipeline.png)

![Alt text](https://github.com/livanshu/Data_Science_Portfolio/blob/main/Projects/Loan_Default_Prediction_EndtoEnd_Snowflake_Dataiku/Images/dakaiku_finaldashboard.png)

## Dataset

- The base data set was derived from loan data from the Lending Club.

- Enriched with unemployment data from Knoema on the Snowflake Data Marketplace.

## Steps:
1. Setting up and loading data in Snowflake
2. Connect Dataiku with Snowflake
3. Dataiku Project
4. Data Preperation
5. Feature Engineering
6. ML training
7. Evaluation
8. Deployment
9. Scoring

### 1. Setting up and loading data in Snowflake

```sql
/*--------------------------------------------------------------------------------
Configure user/roles and create warehouse
----------------------------------------------------------------------------*/


USE ROLE SYSADMIN;

CREATE OR REPLACE WAREHOUSE ML_WH

  WITH WAREHOUSE_SIZE = 'XSMALL'

  AUTO_SUSPEND = 120

  AUTO_RESUME = true

  INITIALLY_SUSPENDED = TRUE;


/* ---------------------------------------------------------------------------
Database Schema and table
----------------------------------------------------------------------------*/


USE WAREHOUSE ML_WH;

CREATE DATABASE IF NOT EXISTS ML_DB;

USE DATABASE ML_DB;

CREATE OR REPLACE TABLE loan_data (
  
        LOAN_ID NUMBER(38,0),
  
        LOAN_AMNT FLOAT,

        FUNDED_AMNT FLOAT,

        TERM VARCHAR(4194304),

        INT_RATE VARCHAR(4194304),

        INSTALLMENT FLOAT,

        GRADE VARCHAR(4194304),

        SUB_GRADE VARCHAR(4194304),

        EMP_TITLE VARCHAR(4194304),

        EMP_LENGTH_YEARS NUMBER(38,0),

        HOME_OWNERSHIP VARCHAR(4194304),

        ANNUAL_INC FLOAT,

        VERIFICATION_STATUS VARCHAR(4194304),

        ISSUE_DATE_PARSED TIMESTAMP_TZ(9),

        LOAN_STATUS VARCHAR(4194304),

        PYMNT_PLAN BOOLEAN,
        
        PURPOSE VARCHAR(4194304),

        TITLE VARCHAR(4194304),
    
        ZIP_CODE VARCHAR(4194304),

        ADDR_STATE VARCHAR(4194304),

        DTI FLOAT,

        DELINQ_2YRS FLOAT,

        EARLIEST_CR_LINE VARCHAR(4194304),

        INQ_LAST_6MTHS FLOAT,

        MTHS_SINCE_LAST_DELINQ FLOAT,

        MTHS_SINCE_LAST_RECORD FLOAT,

        OPEN_ACC FLOAT,

        REVOL_BAL FLOAT,

        REVOL_UTIL FLOAT,

        TOTAL_ACC FLOAT,

        TOTAL_PYMNT FLOAT,

        MTHS_SINCE_LAST_MAJOR_DEROG FLOAT,

        TOT_CUR_BAL FLOAT,

        ISSUE_MONTH NUMBER(38,0),

        ISSUE_YEAR NUMBER(38,0)
  
);




/* ---------------------------------------------------------------------------
Staging
----------------------------------------------------------------------------*/

CREATE OR REPLACE STAGE LOAN_DATA

  url='s3://snowflake-corp-se-workshop/Summit_Snowflake_Dataiku/data/';


 list @LOAN_DATA;
 
 /* ---------------------------------------------------------------------------
Copy into Database
----------------------------------------------------------------------------*/

COPY INTO loan_data FROM @LOAN_DATA/loans_data.csv
FILE_FORMAT = (TYPE = 'CSV' field_optionally_enclosed_by='"',SKIP_HEADER = 1);  


SELECT * FROM loan_data LIMIT 100;
```

![Alt text](https://github.com/livanshu/Data_Science_Portfolio/blob/main/Projects/Loan_Default_Prediction_EndtoEnd_Snowflake_Dataiku/Images/data_loading.png)

Loading Labor and Employment data:

```sql
/*
-----------------------------------------
Unemployment dataset from Knoema (Marketplace)
-----------------------------------------
*/


USE WAREHOUSE ML_WH;

USE DATABASE KNOEMA_LABOR_DATA_ATLAS;

SELECT * 
FROM "LABOR"."DATASETS"
WHERE "DatasetName" ILIKE '%unemployment%' 
AND "DatasetName" ILIKE '%U.S%';


/*
-----------------------------------------
Number of initial claims for unemployment insurance in the US over time
-----------------------------------------
*/

SELECT * FROM "LABOR"."USUID2017Sep" WHERE "Region Name" = 'United States' AND 
      "Indicator Name" = 'Initial Claims' AND "Measure Name" = 'Value' AND 
       "Seasonal Adjustment Name" = 'Seasonally Adjusted' ORDER BY "Date";


/*
-----------------------------------------
Creating "view" of Knoema Employment data from marketplace of year 2018
Using Pivot for different employment metrics
-----------------------------------------
*/

USE DATABASE ML_DB;

CREATE OR REPLACE VIEW KNOEMA_EMPLOYMENT_DATA AS (

SELECT *

FROM (SELECT "Measure Name" MeasureName, "Date", 
      "RegionId" State, 
      AVG("Value") Value 
      FROM "KNOEMA_LABOR_DATA_ATLAS"."LABOR"."BLSLA" WHERE "RegionId" is not null 
      and "Date" >= '2018-01-01' AND "Date" < '2018-12-31' GROUP BY "RegionId", "Measure Name", "Date")
      PIVOT(AVG(Value) FOR MeasureName
      IN ('civilian noninstitutional population', 'employment', 'employment-population ratio', 
          'labor force', 'labor force participation rate', 'unemployment', 'unemployment rate')) AS 
        p (Date, State, civilian_noninstitutional_population, employment, employment_population_ratio, 
           labor_force, labor_force_participation_rate, unemployment, unemployment_rate)
);


SELECT * FROM KNOEMA_EMPLOYMENT_DATA LIMIT 100;


/*
-----------------------------------------
Joining Loan and Employment Data using location and time periods
-----------------------------------------
*/

CREATE OR REPLACE TABLE UNEMPLOYMENT_DATA AS

 SELECT l.LOAN_ID, e.CIVILIAN_NONINSTITUTIONAL_POPULATION, 
        e.EMPLOYMENT, e.EMPLOYMENT_POPULATION_RATIO, e.LABOR_FORCE, 
        e.LABOR_FORCE_PARTICIPATION_RATE, e.UNEMPLOYMENT, e.UNEMPLOYMENT_RATE

  FROM LOAN_DATA l LEFT JOIN KNOEMA_EMPLOYMENT_DATA e

 on l.ADDR_STATE = right(e.state,2) and l.issue_month = month(e.date) and l.issue_year = year(e.date);


SELECT * FROM UNEMPLOYMENT_DATA LIMIT 100;

```
### 2. Connect Dataiku with Snowflake

```sql
/*
-----------------------------------------
Granting Privilages to Dataiku
-----------------------------------------
*/

grant all privileges on database ML_DB to role PC_Dataiku_role;
grant usage on all schemas in database ML_DB to role PC_Dataiku_role;
grant select on all tables in schema ML_DB.public to role PC_Dataiku_role;
grant select on all views in schema ML_DB.public to role PC_Dataiku_role;



USE ROLE PC_DATAIKU_ROLE;

/*
-----------------------------------------
Refresh Page
-----------------------------------------
*/

USE DATABASE PC_DATAIKU_DB;
USE WAREHOUSE PC_DATAIKU_WH;

CREATE OR REPLACE TABLE LOANS_ENRICHED CLONE ML_DB.PUBLIC.LOAN_DATA;
CREATE OR REPLACE TABLE UNEMPLOYMENT_DATA CLONE ML_DB.PUBLIC.UNEMPLOYMENT_DATA;

SELECT * FROM LOANS_ENRICHED LIMIT 10;
```
![Alt text](https://github.com/livanshu/Data_Science_Portfolio/blob/main/Projects/Loan_Default_Prediction_EndtoEnd_Snowflake_Dataiku/Images/dataiku.png)

### 3. Dataiku Project

![Alt text](https://github.com/livanshu/Data_Science_Portfolio/blob/main/Projects/Loan_Default_Prediction_EndtoEnd_Snowflake_Dataiku/Images/dataiku_dashboard.png)

### 4. Data Preperation

![Alt text](https://github.com/livanshu/Data_Science_Portfolio/blob/main/Projects/Loan_Default_Prediction_EndtoEnd_Snowflake_Dataiku/Images/dataiku_loans_data.png)
![Alt text](https://github.com/livanshu/Data_Science_Portfolio/blob/main/Projects/Loan_Default_Prediction_EndtoEnd_Snowflake_Dataiku/Images/join_data.png)

### 5. Feature Engineering

![Alt text](https://github.com/livanshu/Data_Science_Portfolio/blob/main/Projects/Loan_Default_Prediction_EndtoEnd_Snowflake_Dataiku/Images/data_prep_allsteps.png)

```python
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
from snowflake.snowpark import functions as F
from snowflake.snowpark.types import IntegerType
from dataiku.snowpark import DkuSnowpark
from snowflake.snowpark import Session
from snowflake.snowpark.functions import udf
from snowflake.snowpark.session import Session
from snowflake.snowpark import functions as F
from snowflake.snowpark import version
from snowflake.snowpark.types import *
from snowflake.snowpark.functions import when, col, lit, avg, stddev, stddev_pop , round, log

dku_snowpark = DkuSnowpark()

LOANS = dataiku.Dataset("LOANS_ENRICHED_joined_prepared")
snowdf = dku_snowpark.get_dataframe(LOANS)
snowdf.count()

snowdf_pandas=snowdf.toPandas()
snowdf_pandas.head(5)

snowdf_pandas['EMP_TITLE'].value_counts()

snowdf = snowdf.withColumn('EMP_BUCKET',
                               when(snowdf.EMP_TITLE == 'Teacher','Teacher' )
                               .when(snowdf.EMP_TITLE == 'Manager', 'Manager')
                              .when(snowdf.EMP_TITLE == 'Registered Nurse', 'Registered Nurse')
                           .when(snowdf.EMP_TITLE == 'Driver', 'Driver')
                            .when(snowdf.EMP_TITLE == 'Owner', 'Owner')
                               .otherwise('NA'))

# Select the first set of columns
snowdf.select("EMP_TITLE","EMP_BUCKET").filter(snowdf.EMP_BUCKET == 'NA').show()

# Define max and min values and collect them

mean_installement = snowdf.agg({'INSTALLMENT': 'mean'}).collect()[0][0]
stddev_installement = snowdf.agg({'INSTALLMENT': 'stddev'}).collect()[0][0]

# Create a new column based off the scaled data

snowdf = snowdf.withColumn('INSTALL_NORM',
                  ((snowdf['INSTALLMENT'] - mean_installement) / stddev_installement))

snowdf.select("INSTALLMENT","INSTALL_NORM").show()

# Count missing rows
missing_emp_length_years = snowdf.where(snowdf['EMP_LENGTH_YEARS'].isNull()).count()
missing_emp_length_years

# Calculate the median value

col_median = int(snowdf.agg({'EMP_LENGTH_YEARS': 'median'}).collect()[0][0])

# Replacing with the median value for that column
snowdf=snowdf.na.fill({'EMP_LENGTH_YEARS': col_median})
snowdf.select("EMP_LENGTH_YEARS").show()

# Count missing rows
missing_emp_length_years = snowdf.where(snowdf['EMP_LENGTH_YEARS'].isNull()).count()
missing_emp_length_years

# Drop the columns
snowdf = snowdf.drop('INSTALLMENT')

snowdf.select("INSTALL_NORM","EMP_LENGTH_YEARS","EMP_BUCKET").show()

# get output dataset
LOANS_FE = dataiku.Dataset("LOANS_FE")

# write input dataframe to output dataset
dku_snowpark.write_with_schema(LOANS_FE,snowdf)

```

### 6. ML training

Train-Test Split:
![Alt text](https://github.com/livanshu/Data_Science_Portfolio/blob/main/Projects/Loan_Default_Prediction_EndtoEnd_Snowflake_Dataiku/Images/train_test_split.png)

Baseline Model:
![Alt text](https://github.com/livanshu/Data_Science_Portfolio/blob/main/Projects/Loan_Default_Prediction_EndtoEnd_Snowflake_Dataiku/Images/baseline_model.png)

Class Balanced:
![Alt text](https://github.com/livanshu/Data_Science_Portfolio/blob/main/Projects/Loan_Default_Prediction_EndtoEnd_Snowflake_Dataiku/Images/ML_algorithms.png)


### 7. Evaluation

![Alt text](https://github.com/livanshu/Data_Science_Portfolio/blob/main/Projects/Loan_Default_Prediction_EndtoEnd_Snowflake_Dataiku/Images/MLperformance.png)

![Alt text](https://github.com/livanshu/Data_Science_Portfolio/blob/main/Projects/Loan_Default_Prediction_EndtoEnd_Snowflake_Dataiku/Images/MLeval.png)

![Alt text](https://github.com/livanshu/Data_Science_Portfolio/blob/main/Projects/Loan_Default_Prediction_EndtoEnd_Snowflake_Dataiku/Images/MLeval2.png)

### 8. Deployment

![Alt text](https://github.com/livanshu/Data_Science_Portfolio/blob/main/Projects/Loan_Default_Prediction_EndtoEnd_Snowflake_Dataiku/Images/flow5.png)

### 9. Scoring

![Alt text](https://github.com/livanshu/Data_Science_Portfolio/blob/main/Projects/Loan_Default_Prediction_EndtoEnd_Snowflake_Dataiku/Images/scoring.png)
