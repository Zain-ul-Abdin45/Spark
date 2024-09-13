import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Parameters
num_transactions = 1000
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)
date_range = (end_date - start_date).days + 1

# Generate transaction IDs
transaction_ids = np.arange(1, num_transactions + 1)

# Generate account IDs (assuming 2000 unique accounts)
account_ids = np.random.randint(1001, 3001, size=num_transactions)

# Generate random merchant IDs (assuming 1000 unique merchants)
merchant_ids = np.random.randint(2001, 3001, size=num_transactions)

# Generate random amounts and conversion rates
amounts_in_actual_currency = np.round(np.random.uniform(10, 500, size=num_transactions), 2)
conversion_rates = np.round(np.random.uniform(0.9, 1.1, size=num_transactions), 2)

# Generate random transaction dates
tran_dates = [start_date + timedelta(days=np.random.randint(0, date_range)) for _ in range(num_transactions)]
settle_dates = [tran_date + timedelta(days=np.random.randint(1, 5)) for tran_date in tran_dates]

# Generate transaction types
transaction_types = np.random.choice(['Debit', 'Credit'], size=num_transactions)

# Create DataFrame
transactions_df = pd.DataFrame({
    'transaction_id': transaction_ids,
    'account_id': account_ids,
    'tran_date': tran_dates,
    'settle_date': settle_dates,
    'merchant_id': merchant_ids,
    'transaction_type': transaction_types,
    'amount_in_actual_currency': amounts_in_actual_currency,
    'conversion_rate': conversion_rates
})

# Save to CSV
transactions_df.to_csv('transactions_1000.csv', index=False)
