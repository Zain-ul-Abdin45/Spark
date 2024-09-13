import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Parameters
num_transactions = 2000
num_merchants = 20  # Number of unique merchants

# Generate Merchant Data
merchant_ids = np.arange(2001, 2001 + num_merchants)
merchant_names = [f'Merchant {i}' for i in range(1, num_merchants + 1)]
merchant_locations = ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Miami', 'Houston', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville', 'Fort Worth', 'Columbus', 'Indianapolis', 'Charlotte', 'San Francisco', 'Seattle', 'Denver']
currencies = ['USD'] * num_merchants

merchants_df = pd.DataFrame({
    'merchant_id': merchant_ids,
    'merchant_name': merchant_names,
    'merchant_location': np.random.choice(merchant_locations, num_merchants),
    'currency': currencies
})

# Generate Transaction Data
account_ids = np.random.choice(range(1001, 1101), size=num_transactions)
merchant_ids_trans = np.random.choice(merchant_ids, size=num_transactions)
tran_dates = [datetime(2024, 1, 1) + timedelta(days=np.random.randint(0, 365)) for _ in range(num_transactions)]
settle_dates = [tran_date + timedelta(days=np.random.randint(1, 5)) for tran_date in tran_dates]
transaction_types = np.random.choice(['Debit', 'Credit'], size=num_transactions)
amounts_in_actual_currency = np.round(np.random.uniform(10, 500, size=num_transactions), 2)
conversion_rates = np.round(np.random.uniform(0.9, 1.1, size=num_transactions), 2)
final_amounts = np.round(amounts_in_actual_currency * conversion_rates, 2)
amounts_settled = np.round(amounts_in_actual_currency, 2)

transactions_df = pd.DataFrame({
    'transaction_id': np.arange(1, num_transactions + 1),
    'account_id': account_ids,
    'tran_date': tran_dates,
    'settle_date': settle_dates,
    'merchant_id': merchant_ids_trans,
    'transaction_type': transaction_types,
    'amount_in_actual_currency': amounts_in_actual_currency,
    'conversion_rate': conversion_rates,
    'final_amount': final_amounts,
    'amount_settled': amounts_settled
})

# Save to CSV
merchants_df.to_csv('merchants.csv', index=False)
transactions_df.to_csv('transactions_2000.csv', index=False)
