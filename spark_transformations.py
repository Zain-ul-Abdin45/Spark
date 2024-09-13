from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, count, broadcast, expr
from pyspark.sql.types import IntegerType, DoubleType
import random


# Save result to desktop




spark = SparkSession.builder \
    .appName("CreditCardAnalysis") \
    .getOrCreate()

transactions_df = spark.read.csv('transactions_2000.csv', header=True, inferSchema=True)
accounts_df = spark.read.csv('accounts.csv', header=True, inferSchema=True)
people_df = spark.read.csv('people_1000.csv', header=True, inferSchema=True)
merchants_df = spark.read.csv('merchants.csv', header=True, inferSchema=True)

# **1. Broadcast Join: Transactions and Accounts**

# Calculate total spending per account and filter high-value accounts
account_spending_df = transactions_df.groupBy('account_id') \
    .agg(sum('amount_in_actual_currency').alias('total_spending'))

# Join with account details
broadcast_accounts_df = broadcast(accounts_df)
account_high_value_df = account_spending_df.join(broadcast_accounts_df, on='account_id', how='inner') \
    .withColumn('is_high_value', col('total_spending') > 2000)

# account_high_value_df.show()

# Optional: Save the result
account_high_value_df.write.csv('C:/Users/data/account_high_value.csv', header=True)

# **2. Shuffle Join: People and Accounts**

# Analyze account ownership and count number of accounts per person
people_account_df = people_df.join(accounts_df, on='account_id', how='inner')
people_account_summary_df = people_account_df.groupBy('person_id', 'name') \
    .agg(count('account_id').alias('number_of_accounts'))

# Show results
# people_account_summary_df.show()

# Optional: Save the result
people_account_summary_df.write.csv('C:/Users/data/people_account_summary.csv', header=True)

# **3. Sort Merge Join: Transactions and Merchants**

# Calculate total spending per merchant and identify top merchants
transactions_merchant_summary_df = transactions_df.groupBy('merchant_id') \
    .agg(sum('final_amount').alias('total_spending'))


# Optionally, sort both DataFrames by the join key
transactions_merchant_summary_df = transactions_merchant_summary_df.sort('merchant_id')
merchants_df = merchants_df.sort('merchant_id')

# Perform the join
merchant_summary_df = transactions_merchant_summary_df.join(merchants_df, on='merchant_id', how='inner')

# Identify top merchants by total spending
top_merchants_df = merchant_summary_df.orderBy(col('total_spending').desc())

# Show results
# top_merchants_df.show()

# Optional: Save the result
top_merchants_df.write.csv('C:/Users/data/top_merchants.csv', header=True)

