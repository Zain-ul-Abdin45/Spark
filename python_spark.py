from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, count, broadcast

# Initialize Spark session
spark = SparkSession.builder \
    .appName("CreditCardAnalysis") \
    .config("spark.hadoop.fs.defaultFS", "file:///") \
    .getOrCreate()

# Load DataFrames
transactions_df = spark.read.csv('transactions_2000.csv', header=True, inferSchema=True)
accounts_df = spark.read.csv('accounts.csv', header=True, inferSchema=True)
people_df = spark.read.csv('people_1000.csv', header=True, inferSchema=True)
merchants_df = spark.read.csv('merchants.csv', header=True, inferSchema=True)

# **1. Broadcast Join: Transactions and Accounts**

account_spending_df = transactions_df.groupBy('account_id') \
    .agg(sum('amount_in_actual_currency').alias('total_spending'))

broadcast_accounts_df = broadcast(accounts_df)
account_high_value_df = account_spending_df.join(broadcast_accounts_df, on='account_id', how='inner') \
    .withColumn('is_high_value', col('total_spending') > 2000)

# Save result to desktop
account_high_value_df.write.csv('C:/Users/ZAIN UL ABDIN/Desktop/account_high_value', header=True)

# **2. Shuffle Join: People and Accounts**

people_account_df = people_df.join(accounts_df, on='account_id', how='inner')
people_account_summary_df = people_account_df.groupBy('person_id', 'name') \
    .agg(count('account_id').alias('number_of_accounts'))

# Save result to desktop
people_account_summary_df.write.csv('C:/Users/ZAIN UL ABDIN/Desktop/people_account_summary', header=True)

# **3. Sort Merge Join: Transactions and Merchants**

transactions_merchant_summary_df = transactions_df.groupBy('merchant_id') \
    .agg(sum('final_amount').alias('total_spending'))

transactions_merchant_summary_df = transactions_merchant_summary_df.sort('merchant_id')
merchants_df = merchants_df.sort('merchant_id')

merchant_summary_df = transactions_merchant_summary_df.join(merchants_df, on='merchant_id', how='inner')
top_merchants_df = merchant_summary_df.orderBy(col('total_spending').desc())

# Save result to desktop
top_merchants_df.write.csv('C:/Users/ZAIN UL ABDIN/Desktop/top_merchants', header=True)
