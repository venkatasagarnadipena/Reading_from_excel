# Step 1: Install the Required Library

To read Excel files in Databricks, you need to use the `spark-excel` library, which is an external library that allows reading `.xlsx` and `.xls` files into a Spark DataFrame.

1. **Go to the Libraries section in Databricks:**
   - In the Databricks workspace, navigate to **Clusters**.
   - Click on your cluster.
   - Under the **Libraries** tab, click **Install New** > **Maven**.

2. **Install the `spark-excel` library:**
   - In the **Maven coordinate** field, enter the following:
   
     ```
     com.crealytics:spark-excel_2.12:0.13.7
     ```

   - This is the Maven coordinate for the `spark-excel` library.
   - Click **Install**.

---
Once the library is installed, you can use the notebook attached to read Excel files
