# Cluster Customer

I Split this task into two portions 

## SECTION 1. Using KMeans to predict Cluster the customers. 

DETAILS : 

To cluster the customer I have used the Kmeans Model
- [X] STEP 1 - EDA : 
The dataset was fairly clean.
I used the execution_size and execution_price to cluster data using Kmeans.

- [X] STEP 2 - Machine Learning :
So I used the Standard Scaler to scale the numerical data and ran the model. 

- [X] STEP 3 - Choosing K :
The model suggests to have k=7 but after visualisation we can see that k=5 is more efficient

- [X] STEP 4 - Visualisat & Validation
Since TR makes money from trades our ideal customer will be the ones making the most trades and that would make cluster_id=1 our target customers followed by cluster_id=3 

![2021-06-27 (8)](https://user-images.githubusercontent.com/81169091/123558250-8c5df980-d795-11eb-9351-aeb5c49a59b0.png)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## SECTION 2. Analysis on the Clustered Customers.
 

- [X] **PART 1 - CLUSTERED CUSTOMER PERFORMANCE**
- 
Cluster 1 is the our cluster of our ideal customers and we can see that they are the ones with the high Volume of trades throughout 

![2021-06-27 (16)](https://user-images.githubusercontent.com/81169091/123558280-bfa08880-d795-11eb-8f46-da2a4decce26.png)

- [X] PART 2: ACTIVE CUSTOMERS OVER TIME

Customers clustered in cluster_id 0 are the largest number of active users followed by cluster_id 3.
And customer with cluster_id 1 come in at 3rd place and from a marketing view we would want to improve these numbers to make more profit

![2021-06-27 (18)](https://user-images.githubusercontent.com/81169091/123558309-e363ce80-d795-11eb-94c5-02515aa5881b.png)

- [X] PART 3 - PATTERN IN TRADE TIMING

From the data we can see that high volume of trades happen at 0700 and 1400HR.
High Number of trades is done by customers in the cluster_id 1 followed by customers in cluster 4. 

![2021-06-27 (22)](https://user-images.githubusercontent.com/81169091/123558340-f8406200-d795-11eb-89a6-bd286108202b.png)

- [X] PART 4 - MONEY INVESTED / PROFITED BY CLUSTER OF CUSTOMERS

The data tells us that customers with high in/out flow in the trade market are customers in cluster_id = 0
We can be sure that customers in cluster 1 who trade the most, bring lesser money to the table compared the other clusters. 

![2021-06-27 (20)](https://user-images.githubusercontent.com/81169091/123558362-10b07c80-d796-11eb-88cb-d677c456be91.png)

- [X] PART 5 - CONCLUSION 

OUR IDEAL CLUSTER OF CUSTOMER IS CLUSTER ID 1 AS THESE ARE THEY CUSTOMERS WITH HIGH NUMBER OF TRADES AND THEY ARE ALSO RANKED THIRD IN BEING ACTIVE USERS THROUGH THE YEAR.





