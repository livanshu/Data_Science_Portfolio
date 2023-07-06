# Project Overview
The following project details describe the utilization of graph databases for fraud detection, specifically focusing on the implementation of IBM's AMLSim project dataset. The objective is to classify banking transactions as either fraudulent or legitimate by leveraging the capabilities of **TigerGraph's graph** databases. 

**IBM AMLSim**

- IBM AMLSim: The AMLSim project is intended to provide a multi-agent based simulator that generates synthetic banking transaction data together with a set of known money laundering patterns - mainly for the purpose of testing machine learning models and graph algorithms.

- This dataset is an example dataset generated from IBM AMLSim.
 
**Datasets:**

There are 3 datasets mentioned here: alerts, transactions and accounts.

- Accounts dataset: Contains the information about all the bank accounts whose transactions are monitored.
- Alerts dataset: Contains the transactions which triggered an alert according to AML guidelines.
- Transactions dataset: Contains the list of all the transactions with information about sender and receiver accounts.

### Steps:
1. Connecting to TigerCloud
2. Create Design Schema
3. Load Data
4. Write and Install Queries
5. Explore graph and Built Patterns
6. ML Modelling
7. Results and Conclusion



## 1. Connecting to TigerGraph Cloud

![Alt text](https://github.com/livanshu/Data_Science_Portfolio/blob/main/Projects/AML_TigerGraph_GSQL/TG_Setup.png)

![Alt text](https://github.com/livanshu/Data_Science_Portfolio/blob/main/Projects/AML_TigerGraph_GSQL/TG_Connection.png)

## 2. Create Design Schema

I used TigerCloud's Graph Studio to create a Design Schema for connecting Customers, Alerts and Transactions.
Created Vertexes, Undirected and Directed Edges.

![Alt text](https://github.com/livanshu/Data_Science_Portfolio/blob/main/Projects/AML_TigerGraph_GSQL/AML_Design%20Schema.png)

## 3. Loading Data

Upserted alerts, account and transactions data. 

![Alt text](https://github.com/livanshu/Data_Science_Portfolio/blob/main/Projects/AML_TigerGraph_GSQL/AML_DataLoading.png)

## 4. Create & Install Queries

### Query 1: Account Info

![Alt text](https://github.com/livanshu/Data_Science_Portfolio/blob/main/Projects/AML_TigerGraph_GSQL/AML_GSQL_AccInfo.png)
![Alt text](https://github.com/livanshu/Data_Science_Portfolio/blob/main/Projects/AML_TigerGraph_GSQL/TG_AccInfo.png)

### Query 2: Account Activity

![Alt text](https://github.com/livanshu/Data_Science_Portfolio/blob/main/Projects/AML_TigerGraph_GSQL/AML_GSQL_AccActivity.png)
![Alt text](https://github.com/livanshu/Data_Science_Portfolio/blob/main/Projects/AML_TigerGraph_GSQL/TG_AccActivity.png)

### Query 3: Label Prop

The Label Propagation algorithm (LPA) is a rapid and effective method for identifying communities within a graph. Unlike other approaches, LPA solely relies on the network structure without the need for a predefined objective function or prior knowledge about the communities.

The fundamental principle behind LPA involves the propagation of labels throughout the network, ultimately leading to the formation of communities. The algorithm's intuition is based on the observation that a label can quickly dominate a densely connected group of nodes but struggles to cross sparsely connected regions. Consequently, labels become trapped within densely connected groups, enabling identification of nodes belonging to the same community.

The algorithm operates as follows:

Initialization: Each node is assigned a unique community label (identifier).
Propagation: Labels propagate through the network.
Iteration: At each iteration, every node updates its label to match the label that the highest number of its neighbors possess. In case of ties, the label selection is arbitrary but deterministic.
Convergence: LPA achieves convergence when each node adopts the majority label among its neighbors.
Stopping Criteria: The algorithm halts if convergence is reached or if the maximum number of iterations specified by the user is reached.
By following these steps, the LPA algorithm effectively discovers communities within the graph without relying on external information or complex optimization objectives.

![Alt text](https://github.com/livanshu/Data_Science_Portfolio/blob/main/Projects/AML_TigerGraph_GSQL/AML_GSQL_LabelProp2.png)
![Alt text](https://github.com/livanshu/Data_Science_Portfolio/blob/main/Projects/AML_TigerGraph_GSQL/TG_LabelProp.png)

### Query 4: Page Rank

The PageRank algorithm measures the importance of each node within the graph, based on the number incoming relationships and the importance of the corresponding source nodes. The underlying assumption roughly speaking is that a page is only as important as the pages that link to it.
PageRank is introduced in the original Google paper as a function that solves the following equation:
![Alt text](https://github.com/livanshu/Data_Science_Portfolio/blob/main/Projects/AML_TigerGraph_GSQL/PageRank_Equation.png)
where,
we assume that a page A has pages T1 to Tn which point to it.
d is a damping factor which can be set between 0 (inclusive) and 1 (exclusive). It is usually set to 0.85.
C(A) is defined as the number of links going out of page A.
This equation is used to iteratively update a candidate solution and arrive at an approximate solution to the same equation.

![Alt text](https://github.com/livanshu/Data_Science_Portfolio/blob/main/Projects/AML_TigerGraph_GSQL/AML_GSQL_PageRank.png)
![Alt text](https://github.com/livanshu/Data_Science_Portfolio/blob/main/Projects/AML_TigerGraph_GSQL/TG_PageRank.png)

### Query 5: Multihop


The final query we will be utilizing is designed to extract the desired attributes from the dataset. This query retrieves the first 1,000 transactions, ordered based on their fraudulent or non-fraudulent status.

![Alt text](https://github.com/livanshu/Data_Science_Portfolio/blob/main/Projects/AML_TigerGraph_GSQL/TG_MultiHop.png)


## 5. Explore graph and Build Patterns

![Alt text](https://github.com/livanshu/Data_Science_Portfolio/blob/main/Projects/AML_TigerGraph_GSQL/AML_ExploreGraph.png)
![Alt text](https://github.com/livanshu/Data_Science_Portfolio/blob/main/Projects/AML_TigerGraph_GSQL/AML_BuildGraphPatterns.png)
![ALt text](https://github.com/livanshu/Data_Science_Portfolio/blob/main/Projects/AML_TigerGraph_GSQL/AML_BuildGraphPatterns2.png)

## 6. Create ML Model

![Alt text](https://github.com/livanshu/Data_Science_Portfolio/blob/main/Projects/AML_TigerGraph_GSQL/TG_DfDesc.png)

## 7. Results

![Alt text](https://github.com/livanshu/Data_Science_Portfolio/blob/main/Projects/AML_TigerGraph_GSQL/TG_Results.png)

## 8. Conclusion

For the model, I chose ROC-AUC as the evaluation metric because we need to lower false positives as we do not want okay transactions to be marked as Fraud.
The ROC score was **0.78** on Test Data.


