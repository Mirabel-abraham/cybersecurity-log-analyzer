import pandas as pd
# Dataset
data = {
    "User": ["A", "B", "A", "C", "B", "A", "D", "C", "B", "A"],
    "LoginAttempts": [1, 3, 5, 2, 8, 10, 1, 4, 7, 12],
    "Location": ["NG", "US", "NG", "UK", "US", "NG", "NG", "UK", "US", "FR"]
}
df = pd.DataFrame(data)

# Analysis
total_attempts = df.groupby("User")["LoginAttempts"].sum()
locations = df.groupby("User")["Location"].nunique()
suspicious = (total_attempts > 15) | (locations > 1)
high_risk = total_attempts > 20

# Output
print("CYBERSECURITY LOG ANALYSIS")
for user in suspicious[suspicious].index:
    print(f"User {user} is suspicious")

print(" \nHIGH RISK USERS ")
for user in high_risk[high_risk].index:
    print(f"User {user} is HIGH RISK")