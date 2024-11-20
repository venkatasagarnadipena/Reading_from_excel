# Databricks notebook source
#If we have to read the datd from default single sheet
path=""
df = spark.read.format("com.crealytics.spark.excel").option("Header", "true").option("treatEmptyValuesAsNulls", "false").option("inferSchema", "false").load(path)
df.show()

# COMMAND ----------

#If we have to read the datd from specific single sheet
sheet_name=""
path=""
df = spark.read.format("com.crealytics.spark.excel").option("Header", "true").option("treatEmptyValuesAsNulls", "false").option("inferSchema", "false").option("dataAddress",f'{sheet_name}!').load(path)
df.show()

# COMMAND ----------

#If we have to read the datd from multiple sheet with same schema
sheet=[]
path=""

# COMMAND ----------

df = spark.read.format("com.crealytics.spark.excel").option("Header", "true").option("treatEmptyValuesAsNulls", "false").option("inferSchema", "false").option("dataAddress",f'{sheet[0]}!').load(path)
for i in range(1,len(sheet)):
    df2=spark.read.format("com.crealytics.spark.excel").option("Header", "true").option("treatEmptyValuesAsNulls", "false").option("inferSchema", "false").option("dataAddress",f'{sheet[i]}!').load(path)
    union_df=df.union(df2)
    df=union_df
