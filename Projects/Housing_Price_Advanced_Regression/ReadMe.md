# Project Overview
To predict house prices for samples in test.csv file using advanced regression techniques. For each Id in the test set, predicting the value of the **SalePrice** variable.

**Datasets:**
- train.csv Contains House sales samples (1460 sample) with 79 variables including SalePrice which is the dependent variable
- test.csv Contains House sales samples (1460 sample) without SalePrice which is the variable we should predict
- data_description.txt full description of each variable


**Features:**

1. SalePrice - the property's sale price in dollars. This is the target variable that you're trying to predict.
2. MSSubClass: The building class
3. MSZoning: The general zoning classification
4. LotFrontage: Linear feet of street connected to property
5. LotArea: Lot size in square feet
6. Street: Type of road access
7. Alley: Type of alley access
8. LotShape: General shape of property
9. LandContour: Flatness of the property
10. Utilities: Type of utilities available
11. LotConfig: Lot configuration
12. LandSlope: Slope of property
13. Neighborhood: Physical locations within Ames city limits
14. Condition1: Proximity to main road or railroad
15. Condition2: Proximity to main road or railroad (if a second is present)
16. BldgType: Type of dwelling
17. HouseStyle: Style of dwelling
18. OverallQual: Overall material and finish quality
19. OverallCond: Overall condition rating
20. YearBuilt: Original construction date
21. YearRemodAdd: Remodel date
22. RoofStyle: Type of roof
23. RoofMatl: Roof material
24. Exterior1st: Exterior covering on house
25. Exterior2nd: Exterior covering on house (if more than one material)
26. MasVnrType: Masonry veneer type
27. MasVnrArea: Masonry veneer area in square feet
28. ExterQual: Exterior material quality
29. ExterCond: Present condition of the material on the exterior
30. Foundation: Type of foundation
31. BsmtQual: Height of the basement
32. BsmtCond: General condition of the basement
33. BsmtExposure: Walkout or garden level basement walls
34. BsmtFinType1: Quality of basement finished area
35. BsmtFinSF1: Type 1 finished square feet
36. BsmtFinType2: Quality of second finished area (if present)
37. BsmtFinSF2: Type 2 finished square feet
38. BsmtUnfSF: Unfinished square feet of basement area
39. TotalBsmtSF: Total square feet of basement area
40. Heating: Type of heating
41. HeatingQC: Heating quality and condition
42. CentralAir: Central air conditioning
43. Electrical: Electrical system
44. 1stFlrSF: First Floor square feet
45. 2ndFlrSF: Second floor square feet
46. LowQualFinSF: Low quality finished square feet (all floors)
47. GrLivArea: Above grade (ground) living area square feet
48. BsmtFullBath: Basement full bathrooms
49. BsmtHalfBath: Basement half bathrooms
50. FullBath: Full bathrooms above grade
51. HalfBath: Half baths above grade
52. Bedroom: Number of bedrooms above basement level
53. Kitchen: Number of kitchens
54. KitchenQual: Kitchen quality
55. TotRmsAbvGrd: Total rooms above grade (does not include bathrooms)
56. Functional: Home functionality rating
57. Fireplaces: Number of fireplaces
58. FireplaceQu: Fireplace quality
59. GarageType: Garage locatio
60. GarageYrBlt: Year garage was built
61. GarageFinish: Interior finish of the garage
62. GarageCars: Size of garage in car capacity
63. GarageArea: Size of garage in square feet
64. GarageQual: Garage quality
65. GarageCond: Garage condition
66. PavedDrive: Paved driveway
67. WoodDeckSF: Wood deck area in square feet
68. OpenPorchSF: Open porch area in square feet
69. EnclosedPorch: Enclosed porch area in square feet
70. 3SsnPorch: Three season porch area in square feet
71. ScreenPorch: Screen porch area in square feet
72. PoolArea: Pool area in square feet
73. PoolQC: Pool quality
74. Fence: Fence quality
75. MiscFeature: Miscellaneous feature not covered in other categories
76. MiscVal: $Value of miscellaneous feature
77. MoSold: Month Sold
78. YrSold: Year Sold
79. SaleType: Type of sale
80. SaleCondition: Condition of sale



### Steps:
1. Importing libraries and reading data
2. Dealing with missing data
3. Checking correlations
4. Important features Distribution
5. Feature engineering and Log Transformation
6. Encoding Categorical Features
7. Discovering Outliers using Z-score
8. Modelling
9. Stacking ensemble of models
10. Feature Importance & Prediction

***For Outputs, open .ipynb file***



<div class="cell markdown" id="e230a2c3"
papermill="{&quot;duration&quot;:9.3873e-2,&quot;end_time&quot;:&quot;2022-01-27T17:12:25.938055&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:25.844182&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

</div>

<div class="cell markdown" id="30b93eda"
papermill="{&quot;duration&quot;:8.5639e-2,&quot;end_time&quot;:&quot;2022-01-27T17:12:26.110118&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:26.024479&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

## **1. Importing libraries and reading datasets**

</div>

<div class="cell markdown" id="1aed1919"
papermill="{&quot;duration&quot;:8.5767e-2,&quot;end_time&quot;:&quot;2022-01-27T17:12:26.281210&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:26.195443&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

### Importing libraries

</div>

<div class="cell code" _cell_guid="b1076dfc-b9ad-4769-8c92-a6c4dae69d19"
_kg_hide-input="true" _uuid="8f2839f25d086af736a60e9eeb907d3b93b6e0e5"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:26.470175Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:26.469177Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:28.036005Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:28.035043Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T12:00:12.122526Z&quot;}"
id="a127dc32"
papermill="{&quot;duration&quot;:1.66801,&quot;end_time&quot;:&quot;2022-01-27T17:12:28.036200&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:26.368190&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from xgboost import XGBRegressor
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import StackingRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.ensemble import ExtraTreesRegressor
from scipy import stats

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

sns.set()
```

</div>

<div class="cell markdown" id="63e1ab1f"
papermill="{&quot;duration&quot;:8.6568e-2,&quot;end_time&quot;:&quot;2022-01-27T17:12:28.211787&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:28.125219&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

### Reading datasets

#### After reading train and test dataset, I'll combine them to for preprocessing

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:28.388267Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:28.387588Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:28.530781Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:28.530189Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T12:00:17.285587Z&quot;}"
id="a8d476ca"
papermill="{&quot;duration&quot;:0.23318,&quot;end_time&quot;:&quot;2022-01-27T17:12:28.530931&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:28.297751&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Reading datasets
train=pd.read_csv('../input/house-prices-advanced-regression-techniques/train.csv')
test=pd.read_csv('../input/house-prices-advanced-regression-techniques/test.csv')

#define train target
target=train['SalePrice']

#Combining train and test dataset for preprocessing
all_df=pd.concat([train,test], ignore_index=True,sort=False)

#Dropping SalePrice
all_df.drop('SalePrice',axis=1,inplace=True)
```

</div>

<div class="cell markdown" id="b91e26af"
papermill="{&quot;duration&quot;:8.5934e-2,&quot;end_time&quot;:&quot;2022-01-27T17:12:28.702850&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:28.616916&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

## **2. Dealing with missing values </h1>**

</div>

<div class="cell markdown" id="b4d96ae1"
papermill="{&quot;duration&quot;:8.5629e-2,&quot;end_time&quot;:&quot;2022-01-27T17:12:28.874571&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:28.788942&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

## Visualizing missing data

</div>

<div class="cell code" _kg_hide-input="true"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:29.052622Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:29.051977Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:29.103837Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:29.104386Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T12:00:20.193456Z&quot;}"
id="e8d7c5c0"
papermill="{&quot;duration&quot;:0.143791,&quot;end_time&quot;:&quot;2022-01-27T17:12:29.104569&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:28.960778&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
missings_df={}
for key in all_df.columns:
    if all_df[key].isnull().sum() > 0:
        missings_df[key]=(all_df[key].isnull().sum()  /  len(all_df[key]) ) * 100

#Create missing values dataframe
missings_df=pd.DataFrame(missings_df,index=['MissingValues']).T.sort_values(by='MissingValues',ascending=False)
```

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:29.279390Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:29.278707Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:30.035260Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:30.034623Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T12:00:21.593449Z&quot;}"
id="7ba3efd7" outputId="271aa0e6-ec2d-4ed0-febd-28950b54328d"
papermill="{&quot;duration&quot;:0.84526,&quot;end_time&quot;:&quot;2022-01-27T17:12:30.035410&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:29.190150&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Plotting the percentage of missing values per column
plt.figure(figsize=(15,7),dpi=100)
plt.xticks(rotation=90)
sns.barplot(y=missings_df.MissingValues,x=missings_df.index, orient='v').set_title('The percentage of missing values per column')
```

<div class="output execute_result" execution_count="4">

    Text(0.5, 1.0, 'The percentage of missing values per column')

</div>

<div class="output display_data">

![](14c42e3fca1a0f4870d0a7b91e51d2a141dd56f5.png)

</div>

</div>

<div class="cell markdown" id="73a2a59b"
papermill="{&quot;duration&quot;:8.9986e-2,&quot;end_time&quot;:&quot;2022-01-27T17:12:30.215614&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:30.125628&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

## Missing values - Categorical features

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:30.402544Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:30.396771Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:30.508641Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:30.508058Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-25T23:19:19.418056Z&quot;}"
id="31894e1a" outputId="d46b8d2a-c9f0-4919-8ef2-e908d6848387"
papermill="{&quot;duration&quot;:0.205087,&quot;end_time&quot;:&quot;2022-01-27T17:12:30.508839&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:30.303752&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Sort transposed describe() by count
all_df.describe(include='object').T.sort_values(by=['count']).head(10)
```

<div class="output execute_result" execution_count="5">

                 count unique     top  freq
    PoolQC          10      3      Ex     4
    MiscFeature    105      4    Shed    95
    Alley          198      2    Grvl   120
    Fence          571      4   MnPrv   329
    FireplaceQu   1499      5      Gd   744
    GarageCond    2760      5      TA  2654
    GarageQual    2760      5      TA  2604
    GarageFinish  2760      3     Unf  1230
    GarageType    2762      6  Attchd  1723
    BsmtExposure  2837      4      No  1904

</div>

</div>

<div class="cell markdown" id="66907d88"
papermill="{&quot;duration&quot;:8.9079e-2,&quot;end_time&quot;:&quot;2022-01-27T17:12:30.687802&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:30.598723&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

#### By looking at the data description I realized that the most missing values in the categorical features were supposed to be labeled as 'NA' (Not Available) .

#### There are numeric variables related to the categorical ones which can assure us to fill them with 'NA'

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:30.872429Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:30.871443Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:30.886091Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:30.886558Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-25T23:19:33.520175Z&quot;}"
id="7a649ce6" outputId="fc226842-af55-437b-8376-d9db57f339ba"
papermill="{&quot;duration&quot;:0.109076,&quot;end_time&quot;:&quot;2022-01-27T17:12:30.886777&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:30.777701&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Get the number of FirePlaces where Fire Place quality is missing
all_df[['FireplaceQu','Fireplaces']][all_df.FireplaceQu.isnull()]
```

<div class="output execute_result" execution_count="6">

         FireplaceQu  Fireplaces
    0            NaN           0
    5            NaN           0
    10           NaN           0
    12           NaN           0
    15           NaN           0
    ...          ...         ...
    2912         NaN           0
    2913         NaN           0
    2914         NaN           0
    2915         NaN           0
    2917         NaN           0

    [1420 rows x 2 columns]

</div>

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:31.079741Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:31.078730Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:31.319210Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:31.319722Z&quot;}"
id="2bbc80f6" outputId="1aaadb33-6b4d-4d87-de4d-2d1666a3b43f"
papermill="{&quot;duration&quot;:0.343363,&quot;end_time&quot;:&quot;2022-01-27T17:12:31.319948&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:30.976585&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Countplot the number of fireplaces
sns.countplot(x=all_df['Fireplaces'])
plt.ylabel('The number of houses')
```

<div class="output execute_result" execution_count="7">

    Text(0, 0.5, 'The number of houses')

</div>

<div class="output display_data">

![](fa71f6eb7315daa7c82791aedb88f24905eab4bb.png)

</div>

</div>

<div class="cell markdown" id="b4c6532d"
papermill="{&quot;duration&quot;:9.0209e-2,&quot;end_time&quot;:&quot;2022-01-27T17:12:31.502183&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:31.411974&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

### There are 1420 houses without fireplace

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:31.690806Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:31.690042Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:31.702417Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:31.703034Z&quot;}"
id="db6d59ac" outputId="801726cc-5cd3-40b2-bafc-a90d62caeee2"
papermill="{&quot;duration&quot;:0.109495,&quot;end_time&quot;:&quot;2022-01-27T17:12:31.703227&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:31.593732&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Get Garage car capacity where GarageQual is missing
all_df[['GarageQual','GarageCars']][all_df.GarageQual.isnull()]
```

<div class="output execute_result" execution_count="8">

         GarageQual  GarageCars
    39          NaN         0.0
    48          NaN         0.0
    78          NaN         0.0
    88          NaN         0.0
    89          NaN         0.0
    ...         ...         ...
    2893        NaN         0.0
    2909        NaN         0.0
    2913        NaN         0.0
    2914        NaN         0.0
    2917        NaN         0.0

    [159 rows x 2 columns]

</div>

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:31.895973Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:31.895278Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:32.152238Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:32.151568Z&quot;}"
id="15cf0b21" outputId="c8d3ed4d-89ec-4e0a-d453-2777c138b075"
papermill="{&quot;duration&quot;:0.352227,&quot;end_time&quot;:&quot;2022-01-27T17:12:32.152414&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:31.800187&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Countplot the capacity of garages
sns.countplot(x=all_df['GarageCars'])
plt.ylabel('The number of houses')
plt.xlabel('The car capacity of garage')
```

<div class="output execute_result" execution_count="9">

    Text(0.5, 0, 'The car capacity of garage')

</div>

<div class="output display_data">

![](7a1450315fdea94203567325689ec8c5be0990c0.png)

</div>

</div>

<div class="cell markdown" id="387d02bf"
papermill="{&quot;duration&quot;:9.3344e-2,&quot;end_time&quot;:&quot;2022-01-27T17:12:32.339792&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:32.246448&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

### There are 159 houses without garage

</div>

<div class="cell markdown" id="9d2a0679"
papermill="{&quot;duration&quot;:9.3217e-2,&quot;end_time&quot;:&quot;2022-01-27T17:12:32.527659&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:32.434442&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

### So let's fill categorical variables with 'Na'

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:32.718400Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:32.717718Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:32.734684Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:32.735276Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T12:00:51.503282Z&quot;}"
id="33b9026c"
papermill="{&quot;duration&quot;:0.114202,&quot;end_time&quot;:&quot;2022-01-27T17:12:32.735504&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:32.621302&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Filling missing values for categorical features
all_df['Alley'].fillna('NA',inplace=True)
all_df['PoolQC'].fillna('NA',inplace=True)
all_df['Fence'].fillna('NA',inplace=True)
all_df['MiscFeature'].fillna('NA',inplace=True)
all_df['FireplaceQu'].fillna('NA',inplace=True)
all_df['GarageCond'].fillna('NA',inplace=True)
all_df['GarageQual'].fillna('NA',inplace=True)
all_df['GarageFinish'].fillna('NA',inplace=True)
all_df['GarageType'].fillna('NA',inplace=True)
all_df['BsmtExposure'].fillna('NA',inplace=True)
all_df['BsmtFinType2'].fillna('NA',inplace=True)
all_df['BsmtFinType1'].fillna('NA',inplace=True)
all_df['BsmtQual'].fillna('NA',inplace=True)
all_df['BsmtCond'].fillna('NA',inplace=True)
```

</div>

<div class="cell markdown" id="a1dad54d"
papermill="{&quot;duration&quot;:9.3207e-2,&quot;end_time&quot;:&quot;2022-01-27T17:12:32.930055&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:32.836848&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

#### According to data dictionary there are features that do not contain the 'NA' category :

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:33.124931Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:33.124217Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:33.130646Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:33.131203Z&quot;}"
id="5418a16b" outputId="e775f841-8ad9-4daf-d3a4-59f963e989a6"
papermill="{&quot;duration&quot;:0.104649,&quot;end_time&quot;:&quot;2022-01-27T17:12:33.131444&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:33.026795&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Number of missing values for MasVnrType + unique categories
print("Number of missing values : ", all_df['MasVnrType'].isnull().sum())
print("Categories:", all_df['MasVnrType'].unique() )
```

<div class="output stream stdout">

    Number of missing values :  24
    Categories: ['BrkFace' 'None' 'Stone' 'BrkCmn' nan]

</div>

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:33.323202Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:33.322564Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:33.326728Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:33.327247Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T12:00:54.014323Z&quot;}"
id="31980ecf"
papermill="{&quot;duration&quot;:0.101272,&quot;end_time&quot;:&quot;2022-01-27T17:12:33.327444&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:33.226172&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Fill MasVnrType missing values with 'None'
all_df['MasVnrType'].fillna('None',inplace=True)
```

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:33.525986Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:33.525040Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:33.528732Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:33.529375Z&quot;}"
id="6b2efd32" outputId="68aefd43-7389-46f8-c857-e0620d243881"
papermill="{&quot;duration&quot;:0.10675,&quot;end_time&quot;:&quot;2022-01-27T17:12:33.529634&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:33.422884&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Getting categories for Electrical feature
print("Number of missing values : ", all_df['Electrical'].isnull().sum())
print("Categories:", all_df['Electrical'].unique() )
```

<div class="output stream stdout">

    Number of missing values :  1
    Categories: ['SBrkr' 'FuseF' 'FuseA' 'FuseP' 'Mix' nan]

</div>

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:33.724591Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:33.723949Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:33.728116Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:33.728559Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T12:00:55.719714Z&quot;}"
id="6057e6f8"
papermill="{&quot;duration&quot;:0.102548,&quot;end_time&quot;:&quot;2022-01-27T17:12:33.728778&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:33.626230&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Fill with top freq
all_df['Electrical'].fillna('SBrkr',inplace=True)
```

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:33.923341Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:33.922600Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:33.933878Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:33.934360Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T12:00:57.639197Z&quot;}"
id="1536e7b3"
papermill="{&quot;duration&quot;:0.110549,&quot;end_time&quot;:&quot;2022-01-27T17:12:33.934578&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:33.824029&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Fill with top freq
all_df['MSZoning'].fillna('RL',inplace=True)
all_df['Utilities'].fillna('AllPub',inplace=True)
all_df['Functional'].fillna('Typ',inplace=True)
all_df['SaleType'].fillna('WD',inplace=True)
all_df['Exterior2nd'].fillna('VinylSd',inplace=True)
all_df['Exterior1st'].fillna('VinylSd',inplace=True)
all_df['KitchenQual'].fillna('TA',inplace=True)
```

</div>

<div class="cell markdown" id="bd392fa8"
papermill="{&quot;duration&quot;:9.5534e-2,&quot;end_time&quot;:&quot;2022-01-27T17:12:34.127084&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:34.031550&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

## Missing values - numeric features

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:34.324123Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:34.323401Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:34.412353Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:34.411777Z&quot;}"
id="eba83b82" outputId="36ecf9a5-d1ba-4324-f8f3-808e9995c0a7"
papermill="{&quot;duration&quot;:0.19136,&quot;end_time&quot;:&quot;2022-01-27T17:12:34.412507&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:34.221147&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#sorting transposed describe() by count
all_df.describe().T.sort_values(by='count').head(10)
```

<div class="output execute_result" execution_count="16">

                   count         mean         std     min     25%     50%     75%  \
    LotFrontage   2433.0    69.305795   23.344905    21.0    59.0    68.0    80.0   
    GarageYrBlt   2760.0  1978.113406   25.574285  1895.0  1960.0  1979.0  2002.0   
    MasVnrArea    2896.0   102.201312  179.334253     0.0     0.0     0.0   164.0   
    BsmtHalfBath  2917.0     0.061364    0.245687     0.0     0.0     0.0     0.0   
    BsmtFullBath  2917.0     0.429894    0.524736     0.0     0.0     0.0     1.0   
    GarageCars    2918.0     1.766621    0.761624     0.0     1.0     2.0     2.0   
    GarageArea    2918.0   472.874572  215.394815     0.0   320.0   480.0   576.0   
    TotalBsmtSF   2918.0  1051.777587  440.766258     0.0   793.0   989.5  1302.0   
    BsmtUnfSF     2918.0   560.772104  439.543659     0.0   220.0   467.0   805.5   
    BsmtFinSF2    2918.0    49.582248  169.205611     0.0     0.0     0.0     0.0   

                     max  
    LotFrontage    313.0  
    GarageYrBlt   2207.0  
    MasVnrArea    1600.0  
    BsmtHalfBath     2.0  
    BsmtFullBath     3.0  
    GarageCars       5.0  
    GarageArea    1488.0  
    TotalBsmtSF   6110.0  
    BsmtUnfSF     2336.0  
    BsmtFinSF2    1526.0  

</div>

</div>

<div class="cell markdown" id="46342a06"
papermill="{&quot;duration&quot;:0.107767,&quot;end_time&quot;:&quot;2022-01-27T17:12:34.615227&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:34.507460&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

### LotFrontage :

#### There are other features related to the LotFrontage such as LotArea, Neighborhood,...

**Let's see how they related**

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:34.826941Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:34.826237Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:36.610394Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:36.609819Z&quot;}"
id="357b0b27" outputId="9d2df903-0122-44ad-a4f8-1bb59cdb9abb"
papermill="{&quot;duration&quot;:1.892568,&quot;end_time&quot;:&quot;2022-01-27T17:12:36.610573&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:34.718005&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Plot Lotfrontage and LotArea distribution
fig,ax = plt.subplots(1,2, figsize=(20,5))
fig.suptitle('LotFrontage And LotArea Distribution',size=15)
sns.histplot(x=all_df.LotFrontage,kde=True, ax=ax[0])
sns.histplot(x=all_df.LotArea,kde=True, ax=ax[1])
```

<div class="output execute_result" execution_count="17">

    <AxesSubplot:xlabel='LotArea', ylabel='Count'>

</div>

<div class="output display_data">

![](27cce6f425e5a7286b458b9cf70e2d88f619f7d2.png)

</div>

</div>

<div class="cell markdown" id="e5241b1d"
papermill="{&quot;duration&quot;:9.6269e-2,&quot;end_time&quot;:&quot;2022-01-27T17:12:36.803969&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:36.707700&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

### Plot without outliers

</div>

<div class="cell code" execution_count="1"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:232}"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:37.009498Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:37.008886Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:37.018086Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:37.017531Z&quot;}"
id="0504c9ad" outputId="0903e75b-df76-4f88-e0cb-511d2bcd53ca"
papermill="{&quot;duration&quot;:0.116137,&quot;end_time&quot;:&quot;2022-01-27T17:12:37.018226&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:36.902089&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Temp dataframe
Lot_tmp=all_df[['LotFrontage','LotArea']][~all_df.LotFrontage.isnull()]
#Calculating z-score to remove outliers
z = np.abs(stats.zscore(Lot_tmp))
#remove outliers
Lot_tmp_Z=Lot_tmp[(z < 3).all(axis=1)]
```

<div class="output error" ename="NameError" evalue="ignored">

    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    <ipython-input-1-f3086df9b8d8> in <cell line: 2>()
          1 #Temp dataframe
    ----> 2 Lot_tmp=all_df[['LotFrontage','LotArea']][~all_df.LotFrontage.isnull()]
          3 #Calculating z-score to remove outliers
          4 z = np.abs(stats.zscore(Lot_tmp))
          5 #remove outliers

    NameError: name 'all_df' is not defined

</div>

</div>

<div class="cell markdown" id="3516cef6"
papermill="{&quot;duration&quot;:9.6168e-2,&quot;end_time&quot;:&quot;2022-01-27T17:12:37.211183&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:37.115015&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

#### since they have diffrent range of numbers I'll take the sqrt of lotArea

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:37.438927Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:37.423660Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:38.168916Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:38.168162Z&quot;}"
id="1f20038c"
papermill="{&quot;duration&quot;:0.861317,&quot;end_time&quot;:&quot;2022-01-27T17:12:38.169102&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:37.307785&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
##Plot Lotfrontage and LotArea distribution without outliers
fig,ax = plt.subplots(1,2, figsize=(20,5))
fig.suptitle('LotFrontage And sqrt(LotArea) Distribution Without outliers',size=15)
sns.histplot(x=Lot_tmp_Z.LotFrontage,kde=True, ax=ax[0])
sns.histplot(x=Lot_tmp_Z.LotArea.apply(np.sqrt),kde=True, ax=ax[1])
```

</div>

<div class="cell markdown" id="94fb8210"
papermill="{&quot;duration&quot;:9.7617e-2,&quot;end_time&quot;:&quot;2022-01-27T17:12:38.367736&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:38.270119&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

### Relation between LotFrontage and LotArea

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:38.573607Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:38.572973Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:39.107543Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:39.106987Z&quot;}"
id="b13aac50" outputId="8540a13b-ecf9-4092-e751-a2b6cb0138d0"
papermill="{&quot;duration&quot;:0.641166,&quot;end_time&quot;:&quot;2022-01-27T17:12:39.107717&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:38.466551&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
# Plotting LotFrontage and LotArea
plt.figure(figsize=(10,5))
sns.regplot(x=Lot_tmp_Z.LotArea.apply(np.sqrt),y=Lot_tmp_Z.LotFrontage,
            line_kws={"color": "red"}).set(title='Relation Between LotFrontage And Sqrt(LotArea)')
```

<div class="output execute_result" execution_count="20">

    [Text(0.5, 1.0, 'Relation Between LotFrontage And Sqrt(LotArea)')]

</div>

<div class="output display_data">

![](a951b42dff82f3cbe576b9619f8771729ef198f0.png)

</div>

</div>

<div class="cell markdown" id="936a8030"
papermill="{&quot;duration&quot;:0.102583,&quot;end_time&quot;:&quot;2022-01-27T17:12:39.314553&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:39.211970&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

#### so there is a rise for LotFrontage as the sqrt(LotArea) increases.

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:39.547788Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:39.536967Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:40.112619Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:40.113208Z&quot;}"
id="2ca9cb76" outputId="1a43976a-471a-4eba-8177-f68db3b28efb"
papermill="{&quot;duration&quot;:0.696068,&quot;end_time&quot;:&quot;2022-01-27T17:12:40.113414&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:39.417346&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Relation between BldgType and LotFrontage
fig,ax = plt.subplots(1,2, figsize=(20,6))
sns.boxplot(x=all_df.BldgType,y=Lot_tmp_Z.LotFrontage, ax=ax[0]).set_title('BldgType (Type of dwelling) and LotFrontage',fontsize = 20)
sns.boxplot(x=all_df.GarageCars,y=Lot_tmp_Z.LotFrontage, ax=ax[1]).set_title('GarageCars and LotFrontage',fontsize = 20)
```

<div class="output execute_result" execution_count="21">

    Text(0.5, 1.0, 'GarageCars and LotFrontage')

</div>

<div class="output display_data">

![](46ed220090a094ffeae7d6a04b7f4992ab3e8487.png)

</div>

</div>

<div class="cell markdown" id="e35608a3"
papermill="{&quot;duration&quot;:0.104252,&quot;end_time&quot;:&quot;2022-01-27T17:12:40.321750&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:40.217498&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

### Relation between neighborhood, LotFrontage, LotArea

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:40.544879Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:40.539139Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:42.194646Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:42.195176Z&quot;}"
id="71b8ff2d" outputId="c43ec47b-7a2b-4423-8d84-5b582d8fccef"
papermill="{&quot;duration&quot;:1.769329,&quot;end_time&quot;:&quot;2022-01-27T17:12:42.195361&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:40.426032&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
# Plotting LotFrontage, LotArea and Neighborhood
fig,ax=plt.subplots(2,1,figsize=(25,15))
sns.boxplot(x=all_df.Neighborhood,y=Lot_tmp_Z.LotFrontage,ax=ax[0]).set_title('LotFrontage And Neighborhood',fontsize=20)
sns.boxplot(x=all_df.Neighborhood,y=Lot_tmp_Z.LotArea.apply(np.sqrt),ax=ax[1]).set_title('LotArea And Neighborhood',fontsize=20)
```

<div class="output execute_result" execution_count="22">

    Text(0.5, 1.0, 'LotArea And Neighborhood')

</div>

<div class="output display_data">

![](1bf6bdaa4d93d58836c83d63288f315814c0d231.png)

</div>

</div>

<div class="cell markdown" id="ba6752bd"
papermill="{&quot;duration&quot;:0.106175,&quot;end_time&quot;:&quot;2022-01-27T17:12:42.408928&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:42.302753&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

### How about SalePrice and Neighborhood

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:42.640274Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:42.639536Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:43.407038Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:43.407550Z&quot;}"
id="cad159c4" outputId="4c3f19aa-f303-4f20-ebdd-b3c1568b58c9"
papermill="{&quot;duration&quot;:0.890295,&quot;end_time&quot;:&quot;2022-01-27T17:12:43.407888&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:42.517593&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
fig,ax=plt.subplots(1,1,figsize=(25,8))
sns.boxplot(x=all_df[:1460].Neighborhood , y=target).set_title('Neighborhood And SalePrice',fontsize=20)
```

<div class="output execute_result" execution_count="23">

    Text(0.5, 1.0, 'Neighborhood And SalePrice')

</div>

<div class="output display_data">

![](f5991e789cf37709520cdc2fe7dfb83cf96cb55c.png)

</div>

</div>

<div class="cell markdown" id="f1248a7e"
papermill="{&quot;duration&quot;:0.109109,&quot;end_time&quot;:&quot;2022-01-27T17:12:43.629140&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:43.520031&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

#### Overally, Houses in MeadowV, NPkVill, Blmngtn and Blueste neighborhoods have lower prices, lower LotArea and lower LotFrontage

</div>

<div class="cell markdown" id="&quot;88164739&quot;"
papermill="{&quot;duration&quot;:0.110376,&quot;end_time&quot;:&quot;2022-01-27T17:12:43.848891&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:43.738515&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

## Training a model to predict missing values for LotFrontage

#### - I'll take a few columns as predictors

#### - Then I'll compare the Mean absolute error for imputing with simple Median/Mean And regression Model

</div>

<div class="cell code" _kg_hide-input="true"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:44.077214Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:44.076512Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:45.076776Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:45.077293Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T12:01:18.994918Z&quot;}"
id="f8397d76" outputId="7d48a144-2c4b-4641-847d-76bde60371d0"
papermill="{&quot;duration&quot;:1.119424,&quot;end_time&quot;:&quot;2022-01-27T17:12:45.077508&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:43.958084&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Creating temp dataframe and converting objects to dummies
LotFrontage_df=pd.get_dummies(all_df[['LandSlope','BldgType','Alley','LotConfig','MSZoning','Neighborhood','LotArea','LotFrontage']].copy())
#Replace Lotarea with it's Sqrt
LotFrontage_df['LotArea']=LotFrontage_df['LotArea'].apply(np.sqrt)

#Mask to access part of the dataframe with available LotFrontage
mask=~LotFrontage_df.LotFrontage.isnull()
#train dataset (including LotFrontage)
LotFrontage_train=LotFrontage_df.loc[mask]
#test dataset (Missing LotFrontage)
LotFrontage_Test=LotFrontage_df.loc[~mask].drop('LotFrontage',axis=1)
#Removing outliers from Train Dataframe
z = np.abs(stats.zscore(LotFrontage_train[['LotFrontage','LotArea']]))
LotFrontage_train=LotFrontage_train[(z < 3).all(axis=1)]

#Define scaler
Scaler_L=StandardScaler()
#standardizing features
X=Scaler_L.fit_transform(LotFrontage_train.drop('LotFrontage',axis=1))
#Define target
y=LotFrontage_train['LotFrontage']
#Splitting Train dataframe
x_train,x_valid,y_train,y_valid=train_test_split(X, y ,test_size=0.3 , random_state=42)
#Defining model
model=GradientBoostingRegressor(n_estimators= 100, min_samples_split= 26, min_samples_leaf= 17, max_features='auto', max_depth= None)
#Fitting model on train data
model.fit(x_train,y_train)
#predicting validation target
y_pred=model.predict(x_valid)
#Storing mean absolute error for single mean, median and Gradien Boosting Regressor
GBoost_results= mean_absolute_error(y_valid,y_pred)
Mean_result= mean_absolute_error(y_valid,[y_valid.mean()]*len(y_valid))
Median_result= mean_absolute_error(y_valid,[y_valid.median()]*len(y_valid))
print("MEAN ABSOLUTE ERROR : ", GBoost_results)
```

<div class="output stream stdout">

    MEAN ABSOLUTE ERROR :  7.813693999636768

</div>

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:45.322173Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:45.321071Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:45.933306Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:45.933846Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T12:01:50.212756Z&quot;}"
id="47b8b989" outputId="4a227c7f-a692-49ad-d096-09e19a2d7b2d"
papermill="{&quot;duration&quot;:0.744274,&quot;end_time&quot;:&quot;2022-01-27T17:12:45.934053&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:45.189779&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Plotting train/validation results
fig, ax= plt.subplots(1,2,figsize=(20,6))
#Show results
sns.regplot(x=y_pred,y=y_valid, line_kws={'color':'red'} , ax=ax[0]).set(title='G-BOOOSTING Regressor Train and Validation Results',xlabel='LotFrontage (Predictions)',ylabel='LotFrontage (True)')
sns.barplot(x=["Mean","Median","GradientBoostingRegressor"],y=[Mean_result,Median_result,GBoost_results], ax=ax[1]).set(title='LotFrontage Imputation - Mean/Median Vs. GradientBoostingRegressor',ylabel='Mean absolute error')
```

<div class="output execute_result" execution_count="25">

    [Text(0.5, 1.0, 'LotFrontage Imputation - Mean/Median Vs. GradientBoostingRegressor'),
     Text(0, 0.5, 'Mean absolute error')]

</div>

<div class="output display_data">

![](22b1226d16e83b875c7413a2a03df4df4e817c26.png)

</div>

</div>

<div class="cell markdown" id="827b181a"
papermill="{&quot;duration&quot;:0.11511,&quot;end_time&quot;:&quot;2022-01-27T17:12:46.165282&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:46.050172&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

#### Mean absolute error is twice lower for Gradient Boosting Regressor compared to the simple mean or median.

</div>

<div class="cell markdown" id="4a46e9cb"
papermill="{&quot;duration&quot;:0.113106,&quot;end_time&quot;:&quot;2022-01-27T17:12:46.391996&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:46.278890&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

### Predict missing values for LotFrontage using trained model

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:46.630558Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:46.629410Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:46.639627Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:46.640189Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T12:02:04.643059Z&quot;}"
id="3aa2c8bb"
papermill="{&quot;duration&quot;:0.13169,&quot;end_time&quot;:&quot;2022-01-27T17:12:46.640401&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:46.508711&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Predicting Missing values for Lotfrontage
LotFrontage_Test=Scaler_L.transform(LotFrontage_Test)
LotFrontage_missings=model.predict(LotFrontage_Test)

#Fill Missing values
all_df.loc[~mask,'LotFrontage']=LotFrontage_missings
```

</div>

<div class="cell markdown" id="c11df23b"
papermill="{&quot;duration&quot;:0.148521,&quot;end_time&quot;:&quot;2022-01-27T17:12:46.903406&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:46.754885&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

### Fill Other missing values

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:47.149937Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:47.148893Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:47.247264Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:47.246633Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T12:02:51.340061Z&quot;}"
id="c134bd87" outputId="aa130672-6941-4a01-8735-fc5670a83980"
papermill="{&quot;duration&quot;:0.221558,&quot;end_time&quot;:&quot;2022-01-27T17:12:47.247437&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:47.025879&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Exploring dataset to discover missing values
all_df.describe().T.sort_values(by='count').head(10)
```

<div class="output execute_result" execution_count="27">

                   count         mean         std     min     25%     50%     75%  \
    GarageYrBlt   2760.0  1978.113406   25.574285  1895.0  1960.0  1979.0  2002.0   
    MasVnrArea    2896.0   102.201312  179.334253     0.0     0.0     0.0   164.0   
    BsmtHalfBath  2917.0     0.061364    0.245687     0.0     0.0     0.0     0.0   
    BsmtFullBath  2917.0     0.429894    0.524736     0.0     0.0     0.0     1.0   
    GarageCars    2918.0     1.766621    0.761624     0.0     1.0     2.0     2.0   
    GarageArea    2918.0   472.874572  215.394815     0.0   320.0   480.0   576.0   
    TotalBsmtSF   2918.0  1051.777587  440.766258     0.0   793.0   989.5  1302.0   
    BsmtUnfSF     2918.0   560.772104  439.543659     0.0   220.0   467.0   805.5   
    BsmtFinSF1    2918.0   441.423235  455.610826     0.0     0.0   368.5   733.0   
    BsmtFinSF2    2918.0    49.582248  169.205611     0.0     0.0     0.0     0.0   

                     max  
    GarageYrBlt   2207.0  
    MasVnrArea    1600.0  
    BsmtHalfBath     2.0  
    BsmtFullBath     3.0  
    GarageCars       5.0  
    GarageArea    1488.0  
    TotalBsmtSF   6110.0  
    BsmtUnfSF     2336.0  
    BsmtFinSF1    5644.0  
    BsmtFinSF2    1526.0  

</div>

</div>

<div class="cell markdown" id="661c8980"
papermill="{&quot;duration&quot;:0.122262,&quot;end_time&quot;:&quot;2022-01-27T17:12:47.490327&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:47.368065&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

### GarageYrBlt

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:47.732242Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:47.731548Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:47.745289Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:47.744796Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T12:02:08.245573Z&quot;}"
id="08c21132" outputId="97488b0e-2a8e-4086-9616-4f3d08936510"
papermill="{&quot;duration&quot;:0.136688,&quot;end_time&quot;:&quot;2022-01-27T17:12:47.745434&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:47.608746&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
# Cheking GarageType where GarageYrBlt is missing
all_df[['GarageYrBlt','GarageType']].loc[all_df.GarageYrBlt.isnull()]
```

<div class="output execute_result" execution_count="28">

          GarageYrBlt GarageType
    39            NaN         NA
    48            NaN         NA
    78            NaN         NA
    88            NaN         NA
    89            NaN         NA
    ...           ...        ...
    2893          NaN         NA
    2909          NaN         NA
    2913          NaN         NA
    2914          NaN         NA
    2917          NaN         NA

    [159 rows x 2 columns]

</div>

</div>

<div class="cell markdown" id="64ef97e7"
papermill="{&quot;duration&quot;:0.11585,&quot;end_time&quot;:&quot;2022-01-27T17:12:47.974804&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:47.858954&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

#### Since there is no garage for these houses, it's not a good idea to fill these NaNs with the mean or median, it makes sense to fill it with 0

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:48.210657Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:48.209965Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:48.212823Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:48.213324Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T12:02:11.454609Z&quot;}"
id="56dd3126"
papermill="{&quot;duration&quot;:0.122766,&quot;end_time&quot;:&quot;2022-01-27T17:12:48.213491&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:48.090725&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
# fill GarageYrBlt missings with the mean
all_df['GarageYrBlt'].fillna(0, inplace=True)
```

</div>

<div class="cell markdown" id="e2cf3920"
papermill="{&quot;duration&quot;:0.113947,&quot;end_time&quot;:&quot;2022-01-27T17:12:48.443321&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:48.329374&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

### Fill the rest of few missing values with median or 0

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:48.682761Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:48.682089Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:48.689245Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:48.689757Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T12:02:39.458033Z&quot;}"
id="7902e3e9"
papermill="{&quot;duration&quot;:0.131417,&quot;end_time&quot;:&quot;2022-01-27T17:12:48.689943&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:48.558526&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#fill with median or 0
all_df['BsmtHalfBath'].fillna(all_df.BsmtHalfBath.median(), inplace=True)
all_df['BsmtFullBath'].fillna(all_df.BsmtFullBath.median(), inplace=True)
all_df['GarageCars'].fillna(0, inplace=True)
all_df['TotalBsmtSF'].fillna(all_df.TotalBsmtSF.median(), inplace=True)
all_df['BsmtUnfSF'].fillna(0 , inplace=True)
all_df['BsmtFinSF2'].fillna(all_df.BsmtFinSF2.median(), inplace=True)
all_df['GarageArea'].fillna(0, inplace=True)
all_df['BsmtFinSF1'].fillna(all_df.BsmtFinSF1.median(), inplace=True)
all_df['MasVnrArea'].fillna(all_df['MasVnrArea'].median(), inplace=True)
```

</div>

<div class="cell markdown" id="e59b3f83"
papermill="{&quot;duration&quot;:0.115297,&quot;end_time&quot;:&quot;2022-01-27T17:12:48.919426&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:48.804129&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

#### save dataframe without missing values

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:49.154147Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:49.153266Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:49.273766Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:49.273083Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T12:02:46.786378Z&quot;}"
id="2177762b"
papermill="{&quot;duration&quot;:0.239112,&quot;end_time&quot;:&quot;2022-01-27T17:12:49.273941&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:49.034829&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Saving dataframe
all_df.to_csv('Imputed_data_all.csv')
```

</div>

<div class="cell markdown" id="e86084ea"
papermill="{&quot;duration&quot;:0.126071,&quot;end_time&quot;:&quot;2022-01-27T17:12:49.524331&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:49.398260&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

## **3. Checking Correlations </h1>**

</div>

<div class="cell markdown" id="7ced6e15"
papermill="{&quot;duration&quot;:0.123603,&quot;end_time&quot;:&quot;2022-01-27T17:12:49.773560&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:49.649957&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

## Correlation Matrix

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:50.028177Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:50.025016Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:51.347098Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:51.347638Z&quot;}"
id="433db6dc" outputId="ad7ee77f-a1bd-4c63-8e8f-f298d5d089fc"
papermill="{&quot;duration&quot;:1.449838,&quot;end_time&quot;:&quot;2022-01-27T17:12:51.347851&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:49.898013&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Get the correlation matrix
corr=train.corr()

# Getting the Upper Triangle of the co-relation matrix
UpperT = np.triu(corr)
plt.figure(figsize=(20,15))
plt.title('Correlation Matrix')
sns.heatmap(corr, mask=UpperT)
```

<div class="output execute_result" execution_count="32">

    <AxesSubplot:title={'center':'Correlation Matrix'}>

</div>

<div class="output display_data">

![](a14797fa796fb1e177c656af0c433114fa2effd5.png)

</div>

</div>

<div class="cell markdown" id="a7ecb310"
papermill="{&quot;duration&quot;:0.125272,&quot;end_time&quot;:&quot;2022-01-27T17:12:51.597744&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:51.472472&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

<h2> <a style="color:black" href="https://www.kaggle.com/mehrdadsadeghi/house-price-advanced-regression-techniques">Sort highly correlated features </a> with SalePrice </h2>

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:51.851920Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:51.851131Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:51.878096Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:51.877452Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T12:07:19.323573Z&quot;}"
id="70962b5a" outputId="c9c31db9-1fb5-4888-ff88-e25baa8b2071"
papermill="{&quot;duration&quot;:0.156196,&quot;end_time&quot;:&quot;2022-01-27T17:12:51.878258&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:51.722062&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Getting sorted correlation between features and SalePrice
train.corrwith(target).sort_values(ascending=False).head(50)
```

<div class="output execute_result" execution_count="33">

    SalePrice        1.000000
    OverallQual      0.790982
    GrLivArea        0.708624
    GarageCars       0.640409
    GarageArea       0.623431
    TotalBsmtSF      0.613581
    1stFlrSF         0.605852
    FullBath         0.560664
    TotRmsAbvGrd     0.533723
    YearBuilt        0.522897
    YearRemodAdd     0.507101
    GarageYrBlt      0.486362
    MasVnrArea       0.477493
    Fireplaces       0.466929
    BsmtFinSF1       0.386420
    LotFrontage      0.351799
    WoodDeckSF       0.324413
    2ndFlrSF         0.319334
    OpenPorchSF      0.315856
    HalfBath         0.284108
    LotArea          0.263843
    BsmtFullBath     0.227122
    BsmtUnfSF        0.214479
    BedroomAbvGr     0.168213
    ScreenPorch      0.111447
    PoolArea         0.092404
    MoSold           0.046432
    3SsnPorch        0.044584
    BsmtFinSF2      -0.011378
    BsmtHalfBath    -0.016844
    MiscVal         -0.021190
    Id              -0.021917
    LowQualFinSF    -0.025606
    YrSold          -0.028923
    OverallCond     -0.077856
    MSSubClass      -0.084284
    EnclosedPorch   -0.128578
    KitchenAbvGr    -0.135907
    dtype: float64

</div>

</div>

<div class="cell markdown" id="63d3dcf2"
papermill="{&quot;duration&quot;:0.122592,&quot;end_time&quot;:&quot;2022-01-27T17:12:52.124740&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:52.002148&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

Correlation \> 0.60 :

-   OverallQual : (Rates the overall material and finish of the house -
    1 to 9 )
-   GrLivArea : (Above grade (ground) living area square feet)
-   GarageCars : (Size of garage in car capacity)
-   GarageArea : (Size of garage in square feet)
-   TotalBsmtSF : (Total square feet of basement area)
-   1stFlrSF : (First Floor square feet)

</div>

<div class="cell markdown" id="e157620c"
papermill="{&quot;duration&quot;:0.119045,&quot;end_time&quot;:&quot;2022-01-27T17:12:52.362478&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:52.243433&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

## Correlation between features

#### following function calculates correlation in pairs and returns a dataframe

</div>

<div class="cell code" _kg_hide-input="true"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:52.611942Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:52.611056Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:52.618969Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:52.619513Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T12:08:23.987483Z&quot;}"
id="16f8ce56"
papermill="{&quot;duration&quot;:0.138186,&quot;end_time&quot;:&quot;2022-01-27T17:12:52.619731&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:52.481545&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
def highly_correlated(df, features, threshold=0.5):
    corr_df = df[features].corr() # get correlations
    correlated_features = np.where(np.abs(corr_df) > threshold) # select ones above the abs threshold
    correlated_features = [(corr_df.iloc[x,y], x, y) for x, y in zip(*correlated_features) if x != y and x < y] # avoid duplication
    s_corr_list = sorted(correlated_features, key=lambda x: -abs(x[0])) # sort by correlation value
    correlation_df={}
    if s_corr_list == []:
        print("There are no highly correlated features with correlation above", threshold)
    else:
        for v, i, j in s_corr_list:
            correlation_df[corr_df.index[i] +" and "+ corr_df.columns[j]]= v
        correlation_df=pd.DataFrame(correlation_df,index=['Correlation'])
    return  correlation_df.T.sort_values(by='Correlation',ascending=False)
```

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:52.867351Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:52.866637Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:52.960813Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:52.960061Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T12:16:01.162235Z&quot;}"
id="977936ed" outputId="417614c2-204e-4c73-b1f6-6c2a172d4751"
papermill="{&quot;duration&quot;:0.221468,&quot;end_time&quot;:&quot;2022-01-27T17:12:52.960977&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:52.739509&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#print correlation between features
highly_correlated(all_df,all_df.columns).style.set_properties(**{'background-color': 'black','color': 'white'})
```

<div class="output execute_result" execution_count="35">

    <pandas.io.formats.style.Styler at 0x7f9301f1e410>

</div>

</div>

<div class="cell markdown" id="3f3e1f34"
papermill="{&quot;duration&quot;:0.120452,&quot;end_time&quot;:&quot;2022-01-27T17:12:53.204525&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:53.084073&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

## **4. Distribution of Important features**

</div>

<div class="cell code" _kg_hide-input="true"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:53.500148Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:53.470760Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:58.128111Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:58.128630Z&quot;}"
id="9c2ca819" outputId="84954257-189f-4458-e38e-a23fe450ace1"
papermill="{&quot;duration&quot;:4.804174,&quot;end_time&quot;:&quot;2022-01-27T17:12:58.128855&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:53.324681&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#plotting histogram chart for highly correlated features
fig, ax = plt.subplots(5,2,figsize=(20,22),dpi=100)
fig.suptitle('Distribution of Highly Correlated Features',size=20)
sns.histplot(all_df['GarageCars'],ax=ax[0,0])
sns.histplot(all_df.GarageArea,ax=ax[0,1])
sns.histplot(all_df.YearBuilt,ax=ax[1,0])
sns.histplot(all_df.GarageYrBlt ,ax=ax[1,1])
sns.histplot(all_df.GrLivArea,ax=ax[2,0])
sns.histplot(all_df['TotRmsAbvGrd'],ax=ax[2,1])
sns.histplot(all_df['TotalBsmtSF'],ax=ax[3,0])
sns.histplot(all_df['1stFlrSF'],ax=ax[3,1])
sns.histplot(all_df['BedroomAbvGr'],ax=ax[4,0])
sns.histplot(all_df['2ndFlrSF'],ax=ax[4,1])
```

<div class="output execute_result" execution_count="36">

    <AxesSubplot:xlabel='2ndFlrSF', ylabel='Count'>

</div>

<div class="output display_data">

![](a71fc5d44da9ab61c57fe3dbd63b1851f51e94a9.png)

</div>

</div>

<div class="cell markdown" id="20f4810b"
papermill="{&quot;duration&quot;:0.126477,&quot;end_time&quot;:&quot;2022-01-27T17:12:58.386057&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:58.259580&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

## **5. Feature engineering and log transformation**

</div>

<div class="cell markdown" id="84be96ce"
papermill="{&quot;duration&quot;:0.129462,&quot;end_time&quot;:&quot;2022-01-27T17:12:58.641500&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:58.512038&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

<b> Since there is high correlation between Yearbuilt and GarageYrBlt
I'll drop the GarageYrBlt. </b>

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:58.906637Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:58.905946Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:58.911355Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:58.911978Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T13:38:01.023772Z&quot;}"
id="d58b9614"
papermill="{&quot;duration&quot;:0.13939,&quot;end_time&quot;:&quot;2022-01-27T17:12:58.912173&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:58.772783&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Creating a copy of data
all_df_copy=all_df.copy()
#Drop GarageYrBlt
all_df_copy.drop('GarageYrBlt', axis=1,inplace=True)
```

</div>

<div class="cell markdown" id="a957dfa2"
papermill="{&quot;duration&quot;:0.129343,&quot;end_time&quot;:&quot;2022-01-27T17:12:59.167502&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:59.038159&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

#### I dont want to drop other features for now, instead of that I'll use them to create new features like Log-scaled GrLivArea, Total_Square_Feet , ...

</div>

<div class="cell markdown" id="6cea3660"
papermill="{&quot;duration&quot;:0.125676,&quot;end_time&quot;:&quot;2022-01-27T17:12:59.419627&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:59.293951&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

### Adding new predictors

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:12:59.680182Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:12:59.679461Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:12:59.699582Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:12:59.700178Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T13:38:02.316689Z&quot;}"
id="e6e16ed3"
papermill="{&quot;duration&quot;:0.154497,&quot;end_time&quot;:&quot;2022-01-27T17:12:59.700392&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:59.545895&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
all_df_copy['Log_GrLivArea'] = all_df_copy['GrLivArea'].apply(np.log)
all_df_copy['Log_1stFlrSF'] = all_df_copy['1stFlrSF'].apply(np.log)
all_df_copy['Log_LotFrontage']= all_df_copy['LotFrontage'].apply(np.log)
all_df_copy['Sqrt_LotArea']=all_df_copy['LotArea'].apply(np.log)
all_df_copy['HouseAge']=all_df_copy['YrSold']-all_df_copy['YearBuilt']
all_df_copy['Total_Rooms']= all_df_copy['BedroomAbvGr'] + all_df_copy['TotRmsAbvGrd']
all_df_copy['GrLivArea_Score']= np.sqrt(all_df_copy['OverallQual']) * all_df_copy['GrLivArea']
all_df_copy['Total_Square_Feet'] = all_df_copy.TotalBsmtSF + all_df_copy['1stFlrSF'] + all_df_copy['2ndFlrSF']
all_df_copy['Total_Porch'] = all_df_copy.ScreenPorch + all_df_copy.EnclosedPorch + all_df_copy.OpenPorchSF + all_df_copy.WoodDeckSF + all_df_copy['3SsnPorch']
all_df_copy['OverallQualCond'] = (all_df_copy['OverallCond'] * all_df_copy.OverallQual)
all_df_copy['BsmtFinSF']=all_df_copy['BsmtFinSF1'] + all_df_copy['BsmtFinSF2']
all_df_copy['TotalBath_Abv']=2*all_df_copy['FullBath']+all_df_copy['HalfBath']*0.5
all_df_copy['TotalBath_Bsmt']=2*all_df_copy['BsmtFullBath']+all_df_copy['BsmtHalfBath']*0.5
```

</div>

<div class="cell markdown" id="2cab5ac9"
papermill="{&quot;duration&quot;:0.127041,&quot;end_time&quot;:&quot;2022-01-27T17:12:59.954936&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:12:59.827895&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

### Get columns containing Na, Fa, Ta, Gd, Ex,..

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:13:00.208357Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:13:00.207702Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:13:00.246210Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:13:00.246809Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T13:38:04.82403Z&quot;}"
id="78e37567" outputId="f70f7bd7-7a02-44bf-ae79-0dba9aa17566"
papermill="{&quot;duration&quot;:0.167296,&quot;end_time&quot;:&quot;2022-01-27T17:13:00.247013&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:00.079717&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
tmp_cols=all_df_copy.columns[all_df_copy.isin(['Gd']).any()]
tmp_cols
```

<div class="output execute_result" execution_count="39">

    Index(['ExterQual', 'ExterCond', 'BsmtQual', 'BsmtCond', 'BsmtExposure',
           'HeatingQC', 'KitchenQual', 'FireplaceQu', 'GarageQual', 'GarageCond',
           'PoolQC'],
          dtype='object')

</div>

</div>

<div class="cell markdown" id="54b1d2fe"
papermill="{&quot;duration&quot;:0.123989,&quot;end_time&quot;:&quot;2022-01-27T17:13:00.495943&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:00.371954&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

### Replace marks with numbers

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:13:00.751789Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:13:00.751107Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:13:00.777950Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:13:00.777312Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T13:38:07.183014Z&quot;}"
id="8387f27f"
papermill="{&quot;duration&quot;:0.156024,&quot;end_time&quot;:&quot;2022-01-27T17:13:00.778101&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:00.622077&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Make a dict
marks = {'No':0,'None':0,'NA':0,'Mn':1,'Av':3, "Po": 1, 'Fa': 2, "TA": 3, 'Gd': 4, 'Ex': 5}
#Apply map for each column
for column in tmp_cols:
    all_df_copy[column]=all_df_copy[column].map(marks)
```

</div>

<div class="cell markdown" id="e9fbf976"
papermill="{&quot;duration&quot;:0.125219,&quot;end_time&quot;:&quot;2022-01-27T17:13:01.028931&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:00.903712&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

### Combine ExterCond,ExterQual and GarageQual,GarageCond

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:13:01.288273Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:13:01.287579Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:13:01.290485Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:13:01.289968Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T13:38:08.729557Z&quot;}"
id="29f98ebd"
papermill="{&quot;duration&quot;:0.136597,&quot;end_time&quot;:&quot;2022-01-27T17:13:01.290697&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:01.154100&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
all_df_copy['Exter_Overall'] = all_df_copy['ExterCond'] * all_df_copy['ExterQual']
all_df_copy['Garage_Overall'] = all_df_copy['GarageQual'] * all_df_copy['GarageCond']
```

</div>

<div class="cell markdown" id="c871b87a"
papermill="{&quot;duration&quot;:0.125303,&quot;end_time&quot;:&quot;2022-01-27T17:13:01.540555&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:01.415252&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

### Important features price chart

</div>

<div class="cell code" _kg_hide-input="true"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:13:01.832349Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:13:01.831702Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:13:04.412082Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:13:04.412685Z&quot;}"
id="9c3ca410" outputId="7540429a-ba6c-44e4-a7a6-5361267a3eeb"
papermill="{&quot;duration&quot;:2.744753,&quot;end_time&quot;:&quot;2022-01-27T17:13:04.412905&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:01.668152&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#plotting most correlated features based on SalePrice
fig, ax = plt.subplots(3,2,figsize=(20,18))
fig.suptitle('Important features and Sale Price',size=20)
sns.regplot(x=target,y=all_df_copy[:1460].OverallQual,ax=ax[0,0])
sns.regplot(x=target,y=all_df_copy[:1460].GrLivArea,ax=ax[0,1])
sns.regplot(x=target,y=all_df_copy[:1460].GarageCars,ax=ax[1,0])
sns.regplot(x=target,y=all_df_copy[:1460]['1stFlrSF'],ax=ax[1,1])
sns.regplot(x=target,y=all_df_copy[:1460].FullBath,ax=ax[2,0])
sns.regplot(x=target,y=all_df_copy[:1460]['YearBuilt'],ax=ax[2,1])
```

<div class="output execute_result" execution_count="42">

    <AxesSubplot:xlabel='SalePrice', ylabel='YearBuilt'>

</div>

<div class="output display_data">

![](57f2424a0f1f5b0a41021c75c35648f27f6bc3c5.png)

</div>

</div>

<div class="cell markdown" id="ba0ff942"
papermill="{&quot;duration&quot;:0.139782,&quot;end_time&quot;:&quot;2022-01-27T17:13:04.691840&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:04.552058&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

#### As a result of Non-normal distribution of X-axis (SalePrice) samples are concentrated on the left

</div>

<div class="cell markdown" id="03db648d"
papermill="{&quot;duration&quot;:0.134634,&quot;end_time&quot;:&quot;2022-01-27T17:13:04.960398&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:04.825764&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

## Sale Price Log Transformation

</div>

<div class="cell code" _kg_hide-input="true"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:13:05.250981Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:13:05.245062Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:13:06.044838Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:13:06.045372Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T12:17:57.514857Z&quot;}"
id="dd2b33c8" outputId="1de8f43e-bcca-4cf3-8647-4c9cadd6876d"
papermill="{&quot;duration&quot;:0.950868,&quot;end_time&quot;:&quot;2022-01-27T17:13:06.045585&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:05.094717&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Plotting Sale Price distribiution
fig,ax=plt.subplots(1,2,figsize=(20,5),dpi=100)
fig.suptitle('Distribution of SalePrice',size=15)
sns.histplot(target, ax=ax[0],kde=True).set_title('SalePrice')
sns.histplot(target.apply(np.log),kde=True, ax=ax[1]).set_title('SalePrice - Log-Scale')
```

<div class="output execute_result" execution_count="43">

    Text(0.5, 1.0, 'SalePrice - Log-Scale')

</div>

<div class="output display_data">

![](a1f0a5beb2d0c5de315fa1ed04ab8af3127ae563.png)

</div>

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:13:06.325554Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:13:06.324828Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:13:06.328517Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:13:06.329136Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T12:18:20.01189Z&quot;}"
id="6318d1db"
papermill="{&quot;duration&quot;:0.145584,&quot;end_time&quot;:&quot;2022-01-27T17:13:06.329330&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:06.183746&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#taking SalePrice into logarithmic scale
target=target.apply(np.log)
```

</div>

<div class="cell markdown" id="db49e6f3"
papermill="{&quot;duration&quot;:0.135385,&quot;end_time&quot;:&quot;2022-01-27T17:13:06.599904&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:06.464519&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

## **6. Encoding Categorical Features Using Pandas**

</div>

<div class="cell markdown" id="5c36b2e0"
papermill="{&quot;duration&quot;:0.136062,&quot;end_time&quot;:&quot;2022-01-27T17:13:06.874989&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:06.738927&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

<h3>  Change the type of strings into category data type </h3>

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:13:07.155482Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:13:07.154807Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:13:07.206430Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:13:07.205828Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T13:38:12.40038Z&quot;}"
id="d948636e"
papermill="{&quot;duration&quot;:0.194049,&quot;end_time&quot;:&quot;2022-01-27T17:13:07.206575&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:07.012526&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Create copy
all_df_copy_en=all_df_copy.copy()

#Converting objects data type to category data type
for key,value in all_df_copy_en.items():
    if pd.api.types.is_string_dtype(value):
        all_df_copy_en[key] = value.astype("category").cat.as_ordered()
```

</div>

<div class="cell markdown" id="e7da81c7"
papermill="{&quot;duration&quot;:0.133685,&quot;end_time&quot;:&quot;2022-01-27T17:13:07.474783&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:07.341098&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

<h3> Replace categories with their codes  </h3>

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:13:07.822010Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:13:07.821308Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:13:07.848600Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:13:07.849180Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T13:38:13.344603Z&quot;}"
id="7079a0dd"
papermill="{&quot;duration&quot;:0.174996,&quot;end_time&quot;:&quot;2022-01-27T17:13:07.849370&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:07.674374&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Replace categories with their code
for key,value in all_df_copy_en.items():
     if not pd.api.types.is_numeric_dtype(value):
        all_df_copy_en[key] = pd.Categorical(value).codes+1

#Get Dummy variables
#all_df_copy_D=pd.get_dummies(all_df_copy).drop('Id',axis=1) # not used
```

</div>

<div class="cell markdown" id="136b5440"
papermill="{&quot;duration&quot;:0.151993,&quot;end_time&quot;:&quot;2022-01-27T17:13:08.149244&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:07.997251&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

### Splitting data to train/test

</div>

<div class="cell markdown" id="65ec1508"
papermill="{&quot;duration&quot;:0.13539,&quot;end_time&quot;:&quot;2022-01-27T17:13:08.422386&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:08.286996&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

#### Before dealing with outliers I have to split the combined dataframes to train and test, because we want to remove outliers only from train dataset

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:13:08.710496Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:13:08.709629Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:13:08.718081Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:13:08.718660Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T13:38:16.631008Z&quot;}"
id="&quot;39039950&quot;"
papermill="{&quot;duration&quot;:0.153005,&quot;end_time&quot;:&quot;2022-01-27T17:13:08.718890&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:08.565885&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Drop id column
all_df_copy_en.drop('Id',axis=1,inplace=True)
#Split data after encoding
train_df=all_df_copy_en[:1460].copy()
train_df['SalePrice']=target
test_df=all_df_copy_en[1460:].copy()
```

</div>

<div class="cell markdown" id="79d7135d"
papermill="{&quot;duration&quot;:0.147309,&quot;end_time&quot;:&quot;2022-01-27T17:13:09.023075&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:08.875766&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

## **7. Discovering Outliers using Z-score**

</div>

<div class="cell markdown" id="de13fba5"
papermill="{&quot;duration&quot;:0.135073,&quot;end_time&quot;:&quot;2022-01-27T17:13:09.571652&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:09.436579&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

### What is Z-score ?

#### Also called standard score. This score helps to understand if a data value is greater or smaller than mean and how far away it is from the mean. More specifically, Z score tells how many standard deviations away a data point is from the mean.

#### Z score = (x -mean) / std

</div>

<div class="cell markdown" id="a6a59f09"
papermill="{&quot;duration&quot;:0.137933,&quot;end_time&quot;:&quot;2022-01-27T17:13:09.858910&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:09.720977&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

#### Calculating z-score :

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:13:10.136110Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:13:10.135377Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:13:10.166875Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:13:10.167370Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T13:38:19.080673Z&quot;}"
id="b52ae206"
papermill="{&quot;duration&quot;:0.171844,&quot;end_time&quot;:&quot;2022-01-27T17:13:10.167575&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:09.995731&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#columns for z-score calculation
numeric_columns=train_df.columns
#Calculating z-score using stats library
z = np.abs(stats.zscore( train_df[numeric_columns]))

#train_df.select_dtypes(include=[np.number]).columns.values  // Returns only numeric columns
```

</div>

<div class="cell markdown" id="a327f80e"
papermill="{&quot;duration&quot;:0.137278,&quot;end_time&quot;:&quot;2022-01-27T17:13:10.444597&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:10.307319&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

#### I'll define a Temporary dataframe and keep the previous one safe

#### With the knowledge we have gained from the data so far, By changing Z value for several times and observing results we can finally decide what should be the right value for Z

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:13:10.727518Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:13:10.726809Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:13:10.737991Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:13:10.738905Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T13:38:21.094801Z&quot;}"
id="033620e9" outputId="2c0fd7cb-6297-4f21-cbc2-19fcebf3bf26"
papermill="{&quot;duration&quot;:0.156891,&quot;end_time&quot;:&quot;2022-01-27T17:13:10.739218&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:10.582327&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Removing outliers on temporary dataframe
train_df_z=train_df.copy()[(z < 10).all(axis=1)]

print('Rows,columns Before removing outliers : ', train_df.shape )
print('Rows,columns After removing outliers : ', train_df_z.shape )
```

<div class="output stream stdout">

    Rows,columns Before removing outliers :  (1460, 94)
    Rows,columns After removing outliers :  (1422, 94)

</div>

</div>

<div class="cell markdown" id="6e77ddd6"
papermill="{&quot;duration&quot;:0.140407,&quot;end_time&quot;:&quot;2022-01-27T17:13:11.017498&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:10.877091&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

#### Plot features after removing outliers

</div>

<div class="cell code" _kg_hide-input="true"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:13:11.303750Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:13:11.302982Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:13:14.666606Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:13:14.667207Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T11:10:05.160098Z&quot;}"
id="e7f0b7db" outputId="9d6b869d-938e-491f-f946-2293003049ad"
papermill="{&quot;duration&quot;:3.510966,&quot;end_time&quot;:&quot;2022-01-27T17:13:14.667467&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:11.156501&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#plotting important features
fig, ax = plt.subplots(4,2,figsize=(18,18))
fig.suptitle('Log-SalePrice and Important Features Without Outliers', size=20)
sns.regplot(x=train_df_z['SalePrice'],y=train_df_z.OverallQual,ax=ax[0,0], line_kws={'color':'red'})
sns.regplot(x=train_df_z['SalePrice'],y=train_df_z.Log_GrLivArea,ax=ax[0,1], line_kws={'color':'red'})
sns.regplot(x=train_df_z['SalePrice'],y=train_df_z.GarageCars,ax=ax[1,0], line_kws={'color':'red'})
sns.regplot(x=train_df_z['SalePrice'],y=train_df_z['Log_1stFlrSF'],ax=ax[1,1], line_kws={'color':'red'})
sns.regplot(x=train_df_z['SalePrice'],y=train_df_z.TotalBsmtSF ,ax=ax[2,0], line_kws={'color':'red'})
sns.regplot(x=train_df_z['SalePrice'],y=train_df_z['YearBuilt'],ax=ax[2,1], line_kws={'color':'red'})
sns.regplot(x=train_df_z['SalePrice'],y=train_df_z.FullBath ,ax=ax[3,0], line_kws={'color':'red'})
sns.regplot(x=train_df_z['SalePrice'],y=train_df_z['TotRmsAbvGrd'],ax=ax[3,1], line_kws={'color':'red'})
```

<div class="output execute_result" execution_count="50">

    <AxesSubplot:xlabel='SalePrice', ylabel='TotRmsAbvGrd'>

</div>

<div class="output display_data">

![](b931912321f2b5b00a3cbc100e3866a4edadb464.png)

</div>

</div>

<div class="cell markdown" id="6d6e3da3"
papermill="{&quot;duration&quot;:0.144571,&quot;end_time&quot;:&quot;2022-01-27T17:13:14.961765&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:14.817194&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

## **8. Modeling**

</div>

<div class="cell markdown" id="972f9a6f"
papermill="{&quot;duration&quot;:0.142241,&quot;end_time&quot;:&quot;2022-01-27T17:13:15.245968&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:15.103727&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

### Making a to_drop list

</div>

<div class="cell code" _kg_hide-input="true"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:13:15.546655Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:13:15.545915Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:13:15.547304Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:13:15.547910Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T13:40:51.786442Z&quot;}"
id="2754e233"
papermill="{&quot;duration&quot;:0.154847,&quot;end_time&quot;:&quot;2022-01-27T17:13:15.548112&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:15.393265&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Add features to dropFullBath
to_drop=['SalePrice','Fence',
                    'HalfBath',
                    'FullBath',
                    'BsmtFullBath',
                     'BsmtHalfBath',
                     'LotConfig',
                     'Foundation',
                     'BsmtFinSF2',
                     'LotShape',
                     'MSSubClass',
                     'PoolArea',
                     'LandContour',
                     'LandSlope',
                     'BsmtHalfBath',
                     'MasVnrArea',
                     'PavedDrive',
                     'GarageFinish',
                     'MasVnrType',
                     'HeatingQC',
                     'SaleType',
                     '3SsnPorch',
                     'PoolQC',
                     'ScreenPorch',
                     'MiscFeature',
                     'Street',
                     'MiscVal',
                     'GarageArea',
                     'YearRemodAdd',
                     'YearBuilt',
                     'LotArea',
                     'GrLivArea',
                     'LotFrontage',
                     'RoofMatl',
                     'Alley',
                     'RoofStyle',
                     'Heating',
                     'BsmtFinType2',
                     'BsmtFinType1',
                     'LowQualFinSF',
                     'MoSold',
                     '1stFlrSF',
                     '2ndFlrSF',
                     'OverallQual',
                     'OverallCond',
                     'TotalBsmtSF',
                     'YrSold',
                     'BsmtFinSF1',
                     'ExterCond',
                     'ExterQual',
                     'GarageQual',
                     'GarageCond',
                     'BsmtFinSF2']
#will be dropped from test data
to_drop_t=to_drop[1:]
```

</div>

<div class="cell markdown" id="34f8d5f2"
papermill="{&quot;duration&quot;:0.144373,&quot;end_time&quot;:&quot;2022-01-27T17:13:15.837544&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:15.693171&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

## Define dependent and independent variables

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:13:16.138532Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:13:16.137176Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:13:16.146641Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:13:16.146101Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T13:40:57.053327Z&quot;}"
id="94f73d81"
papermill="{&quot;duration&quot;:0.16443,&quot;end_time&quot;:&quot;2022-01-27T17:13:16.146839&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:15.982409&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Independent variables
X=train_df_z.drop(to_drop,axis=1)
#Dependent variable
y=train_df_z['SalePrice']

#scaling features
scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)

#spliting train dataset to train and validation
from sklearn.model_selection import train_test_split
X_train, X_valid, y_train, y_valid = train_test_split(X_scaled, y, test_size=0.25, random_state=42)
```

</div>

<div class="cell markdown" id="5305c1fc"
papermill="{&quot;duration&quot;:0.142492,&quot;end_time&quot;:&quot;2022-01-27T17:13:16.434130&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:16.291638&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

## Define score functions

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:13:16.729065Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:13:16.728292Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:13:16.730363Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:13:16.730841Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T13:40:58.794819Z&quot;}"
id="b88278d1"
papermill="{&quot;duration&quot;:0.154445,&quot;end_time&quot;:&quot;2022-01-27T17:13:16.731064&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:16.576619&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
# evaluate a given model by making predictions on X_valid
def get_v_score(model):
    valid_predictions=model.predict(X_valid)
    score=np.sqrt(mean_squared_error(y_valid, valid_predictions))
    return score

# evaluate a given model using cross-validation
def get_cv_score(model, X, y):
    #cv = KFold(n_splits=5, shuffle=True, random_state=1)
    scores = np.sqrt(-cross_val_score(model, X, y, scoring='neg_mean_squared_error', cv=5, n_jobs=-1))
    return np.mean(scores)
```

</div>

<div class="cell markdown" id="59d3bc2b"
papermill="{&quot;duration&quot;:0.143686,&quot;end_time&quot;:&quot;2022-01-27T17:13:17.020179&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:16.876493&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

## Define models

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:13:17.316759Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:13:17.316061Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:13:17.318747Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:13:17.319217Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T13:40:59.928618Z&quot;}"
id="9924f48b"
papermill="{&quot;duration&quot;:0.154188,&quot;end_time&quot;:&quot;2022-01-27T17:13:17.319414&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:17.165226&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
# Models name
models_name=['RandomForestRegressor',
             'GradientBoostingRegressor',
             'XGBRegressor',
             'svm.SVR',
             'ExtraTreesRegressor',
             'Lasso']
# Models
models=[RandomForestRegressor(),
        GradientBoostingRegressor(),
        XGBRegressor(),
        svm.SVR(),
        ExtraTreesRegressor(),
        Lasso(alpha=0.0005,tol=0.001)]
```

</div>

<div class="cell markdown" id="0e292217"
papermill="{&quot;duration&quot;:0.140803,&quot;end_time&quot;:&quot;2022-01-27T17:13:17.602858&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:17.462055&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

## Get score for each model

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:13:17.893336Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:13:17.890647Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:13:21.433446Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:13:21.434037Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T13:42:42.392038Z&quot;}"
id="a996a17a"
papermill="{&quot;duration&quot;:3.688546,&quot;end_time&quot;:&quot;2022-01-27T17:13:21.434247&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:17.745701&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Fit and get scores for each model
scores_list=[]
for model in models:
    model.fit(X_train,y_train)
    scores_list.append(get_v_score(model))
```

</div>

<div class="cell code" _kg_hide-input="true"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:13:21.796084Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:13:21.795232Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:13:21.798579Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:13:21.799084Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T13:42:45.771812Z&quot;}"
id="4ed89efa" outputId="f7f43b8d-b0c4-454e-d288-bbd80fa61f9c"
papermill="{&quot;duration&quot;:0.167199,&quot;end_time&quot;:&quot;2022-01-27T17:13:21.799269&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:21.632070&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Convert list to dataframe
data={'Model':models_name,'RMSE': scores_list}
scores_df=pd.DataFrame(data)
#Sort by valid RMSLE
scores_df.sort_values(by='RMSE').round(5).style.set_properties(**{'background-color': 'black','color': 'white'})
```

<div class="output execute_result" execution_count="56">

    <pandas.io.formats.style.Styler at 0x7f92f1da1790>

</div>

</div>

<div class="cell markdown" id="&quot;00861426&quot;"
papermill="{&quot;duration&quot;:0.143105,&quot;end_time&quot;:&quot;2022-01-27T17:13:22.085215&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:21.942110&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

## Hyperparameter tuning

</div>

<div class="cell markdown" id="8648d9cb"
papermill="{&quot;duration&quot;:0.141492,&quot;end_time&quot;:&quot;2022-01-27T17:13:22.368509&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:22.227017&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

#### I've used RandomizedSearchCv to get the best parameters for each model and use them in the next section

</div>

<div class="cell code" _kg_hide-input="false"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:13:22.665926Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:13:22.665228Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:13:22.668934Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:13:22.669564Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T09:21:56.150252Z&quot;}"
id="5ab46ebc"
papermill="{&quot;duration&quot;:0.156838,&quot;end_time&quot;:&quot;2022-01-27T17:13:22.669772&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:22.512934&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Hyperparameter tuning with RandomizedSearchC
#GBOOST_grid = {"max_depth" :  np.arange(2, 10, 1),
               #"splitter" : ['best','random'],
#               "min_samples_split": np.arange(2, 100, 1),
#               "min_samples_leaf" : np.arange(2, 100, 1),}
#GBOOST_model = RandomizedSearchCV(GradientBoostingRegressor(), param_distributions=GBOOST_grid, n_iter=100, cv=5, verbose=True)
#GBOOST_model.fit(X_train, y_train)
#Show best parameters
#print("Best Params : ", GBOOST_model.best_params_)
```

</div>

<div class="cell markdown" id="c824ec8f"
papermill="{&quot;duration&quot;:0.142532,&quot;end_time&quot;:&quot;2022-01-27T17:13:22.959633&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:22.817101&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

## **9. Stacking models with best parameters**

</div>

<div class="cell markdown" id="1e079d5f"
papermill="{&quot;duration&quot;:0.141096,&quot;end_time&quot;:&quot;2022-01-27T17:13:23.242793&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:23.101697&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

### Stacking Models

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:13:23.530106Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:13:23.529442Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:13:23.540957Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:13:23.540325Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T13:34:00.052926Z&quot;}"
id="d52b4a97"
papermill="{&quot;duration&quot;:0.156459,&quot;end_time&quot;:&quot;2022-01-27T17:13:23.541101&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:23.384642&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
# get a stacking ensemble of models
def get_stacking():

    # define the base models with tuned parameters
    level0 = list()
    level0.append(('GBOOST', GradientBoostingRegressor(min_samples_split=90, min_samples_leaf=26)))
    level0.append(('RandomForest', RandomForestRegressor(min_samples_split=14, min_samples_leaf=8)))
    level0.append(('XGB', XGBRegressor(colsample_bytree=0.6, gamma=0.4 )))
    level0.append(('ExtraTrees', ExtraTreesRegressor(min_samples_split=14, min_samples_leaf=2)))
    level0.append(('svm.SVR', svm.SVR(kernel='poly',gamma='scale',degree=1,coef0=0.30000000000000004)))
    level0.append(('ElasticNet', ElasticNet(alpha=0.0005, l1_ratio=0.9, random_state=0,tol=0.001)))
    level0.append(('Lasso', Lasso(alpha=0.0005, tol=0.001)))

    # define meta learner model
    level1 = LinearRegression()
    # define the stacking ensemble
    model = StackingRegressor(estimators=level0, final_estimator=level1, cv=5)
    return model

#Add to models list
models_name.append('StackingRegressor')
models.append(get_stacking())
```

</div>

<div class="cell markdown" id="c56dbc6d"
papermill="{&quot;duration&quot;:0.143946,&quot;end_time&quot;:&quot;2022-01-27T17:13:23.826505&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:23.682559&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

## Fit stacked model and get validation score

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:13:24.118032Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:13:24.117362Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:13:36.835066Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:13:36.836553Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T13:41:11.055969Z&quot;}"
id="f3e2949b" outputId="d516cf1d-005a-4bfe-c1d1-04319049c61f"
papermill="{&quot;duration&quot;:12.867429,&quot;end_time&quot;:&quot;2022-01-27T17:13:36.836875&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:23.969446&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Fit stacked model and get validation score
Stackedmodel=get_stacking()
Stackedmodel.fit(X_train,y_train)
print('RMSE : ', get_v_score(Stackedmodel))
```

<div class="output stream stdout">

    RMSE :  0.09971116582860676

</div>

</div>

<div class="cell code" _kg_hide-input="true"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:13:37.186196Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:13:37.185235Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:13:37.683732Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:13:37.684416Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T13:41:28.173837Z&quot;}"
id="d0cd1d88" outputId="6d399e87-f634-4c03-826d-0ad6dd627079"
papermill="{&quot;duration&quot;:0.650704,&quot;end_time&quot;:&quot;2022-01-27T17:13:37.684620&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:37.033916&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
y_pred=Stackedmodel.predict(X_valid)
sns.regplot(x=y_pred, y=y_valid).set_title("Stackedmodel Results")
plt.xlabel("Predicted")
plt.ylabel("True values")
```

<div class="output execute_result" execution_count="60">

    Text(0, 0.5, 'True values')

</div>

<div class="output display_data">

![](e261fc3b5c2edbc25fc796e42747a2a34ea309b4.png)

</div>

</div>

<div class="cell markdown" id="fe1f128d"
papermill="{&quot;duration&quot;:0.144781,&quot;end_time&quot;:&quot;2022-01-27T17:13:37.981001&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:37.836220&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

## **10. Feature importance**

</div>

<div class="cell markdown" id="312cac11"
papermill="{&quot;duration&quot;:0.145328,&quot;end_time&quot;:&quot;2022-01-27T17:13:38.275204&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:38.129876&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

#### Feature importance by gradient boosting regressor

</div>

<div class="cell code" _kg_hide-input="true"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:13:38.572897Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:13:38.572190Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:13:39.696278Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:13:39.696826Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T13:41:40.412806Z&quot;}"
id="40a9f5a9" outputId="cae7f719-85c7-428f-92da-95500044c28c"
papermill="{&quot;duration&quot;:1.277569,&quot;end_time&quot;:&quot;2022-01-27T17:13:39.697010&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:38.419441&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
Gboost=GradientBoostingRegressor(min_samples_split=26, min_samples_leaf=29)
Gboost.fit(X_train,y_train)

#create feature importance dataframe
FI_df=pd.DataFrame({'Features': X.columns, 'Importance': Gboost.feature_importances_})
FI_df=FI_df.sort_values(by='Importance', ascending=False).head(100)

#plot feature importance
plt.figure(figsize=(15,10),dpi=100)
sns.barplot(x=FI_df[:30].Importance,y=FI_df[:30].Features,orient = 'h').set_title('Feature Importance')
```

<div class="output execute_result" execution_count="61">

    Text(0.5, 1.0, 'Feature Importance')

</div>

<div class="output display_data">

![](31f331a0fc66e8d12113422de98f3602a04f19c4.png)

</div>

</div>

<div class="cell markdown" id="9ccf1497"
papermill="{&quot;duration&quot;:0.150625,&quot;end_time&quot;:&quot;2022-01-27T17:13:39.999745&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:39.849120&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

## **11. Making prediction on test data**

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:13:40.312808Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:13:40.312048Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:13:40.426329Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:13:40.427382Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T13:41:53.195554Z&quot;}"
id="5d93c272" outputId="8885c9e7-977c-4f3b-9e2a-42f3b8921f68"
papermill="{&quot;duration&quot;:0.277088,&quot;end_time&quot;:&quot;2022-01-27T17:13:40.427721&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:40.150633&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Scaling Test data
test_df_Scaled=scaler.transform(test_df.drop(to_drop_t,axis=1))
#Getting predictions
test_df_preds=Stackedmodel.predict(test_df_Scaled)

#Adding Id column
test_preds=pd.DataFrame({'Id':test['Id'],'SalePrice':(np.exp(test_df_preds))})
test_preds
```

<div class="output execute_result" execution_count="62">

            Id      SalePrice
    0     1461  127212.734054
    1     1462  160369.102059
    2     1463  174018.266905
    3     1464  196204.074836
    4     1465  189078.817252
    ...    ...            ...
    1454  2915   86872.410296
    1455  2916   81861.750988
    1456  2917  150203.891003
    1457  2918  124040.029783
    1458  2919  222239.292462

    [1459 rows x 2 columns]

</div>

</div>

<div class="cell code"
execution="{&quot;iopub.execute_input&quot;:&quot;2022-01-27T17:13:40.856727Z&quot;,&quot;iopub.status.busy&quot;:&quot;2022-01-27T17:13:40.855798Z&quot;,&quot;iopub.status.idle&quot;:&quot;2022-01-27T17:13:40.862619Z&quot;,&quot;shell.execute_reply&quot;:&quot;2022-01-27T17:13:40.863212Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2022-01-27T13:23:58.006646Z&quot;}"
id="f29b42fb"
papermill="{&quot;duration&quot;:0.222307,&quot;end_time&quot;:&quot;2022-01-27T17:13:40.863392&quot;,&quot;exception&quot;:false,&quot;start_time&quot;:&quot;2022-01-27T17:13:40.641085&quot;,&quot;status&quot;:&quot;completed&quot;}"
tags="[]">

``` python
#Save predictions
test_preds.to_csv('submission.csv', index=False)
```

</div>


