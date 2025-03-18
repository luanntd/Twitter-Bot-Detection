import pandas as pd

# Raw data
base_data = pd.read_json('data/user.json')

# Extract data from public metrics column
list_of_public_metrics = list(base_data['public_metrics'])
public_metrics_data = pd.DataFrame(list_of_public_metrics)

# Merge data
data = pd.concat([base_data, public_metrics_data], axis=1)
data = data.drop('public_metrics', axis=1)

# Load data label
label = pd.read_csv('data/label.csv')

# Labeled data
labeled_data = pd.merge(data, label, on='id')

# Save to .csv file
labeled_data.to_csv('TwiBot22_datasets.csv', index=False)
