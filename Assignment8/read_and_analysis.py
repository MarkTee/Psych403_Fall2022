import pandas as pd

df = pd.read_json('saved_json.json')

# Create a short "read and analysis" script that loads a saved JSON file,
# performs rudimentary analyses on the data, and prints the means.
print("Showing all responses...")
print(df)
print()
print(df.describe())


# Change your "read and analysis" script so that RTs for inaccurate responses
# are removed from analysis.
print("\nRemoving incorrect responses...")
df = df[df.sub_resp == df.corr_resp]  # only select rows with correct responses
print(df)
print()
print(df.describe())


# Change your "read and analysis" script so that any trials without a response
# (0 value) are removed from analysis.
print("\nRemoving trials without responses...")
trials_without_responses = df[df.sub_resp != 0].trial.unique()
df = df[~df.trial.isin(trials_without_responses)]
print(df)
print()
print(df.describe())
