import pandas as pd
import numpy as np

# Parameters
num_people = 1000  # 500 accounts with each having 2 people
num_accounts = 500

# Generate account IDs
account_ids = np.arange(1001, 1001 + num_accounts)

# Create a list of people with primary and secondary users for each account
people_data = {
    'person_id': [],
    'name': [],
    'age': [],
    'address': [],
    'account_id': [],
    'relationship': []
}

# Generate people data
for account_id in account_ids:
    primary_person_id = len(people_data['person_id']) + 1
    secondary_person_id = primary_person_id + 1

    # Assign primary user
    people_data['person_id'].append(primary_person_id)
    people_data['name'].append(f'Primary User {primary_person_id}')
    people_data['age'].append(np.random.randint(18, 80))
    people_data['address'].append(f'{np.random.randint(100, 999)} Main Street')
    people_data['account_id'].append(account_id)
    people_data['relationship'].append('Primary')

    # Assign secondary user
    people_data['person_id'].append(secondary_person_id)
    people_data['name'].append(f'Secondary User {secondary_person_id}')
    people_data['age'].append(np.random.randint(18, 80))
    people_data['address'].append(f'{np.random.randint(100, 999)} Elm Street')
    people_data['account_id'].append(account_id)
    people_data['relationship'].append('Secondary')

# Create DataFrame
people_df = pd.DataFrame(people_data)

# Save to CSV
people_df.to_csv('people_1000.csv', index=False)
