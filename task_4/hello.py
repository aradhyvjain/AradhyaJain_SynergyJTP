import pandas as pd
regs = pd.DataFrame({
    'reg_id': range(1, 12),
    'student': ['Anu', 'Bala', 'Chitra', 'Anu', 'Dev', 'Esha', 'Farhan', 'Gita', 'Bala', 'Hari', 'Ira'],
    'event': [' city landscaping ', 'city landscaping ', 'salutes and ladders ', ' city landscaping ', 
              'Open Mic', 'open mic', 'ROBO RACE', 'Quiz Night', 'hackathon', 'Quiz Night', 'Hackathon'],
    'dept': ['CSE', 'cse', 'ECE', 'CSE', 'MECH', 'CSE', 'ECE', None, 'CSE', ' ECE', 'ECE']
})

fees = pd.DataFrame({
    'event': ['Hackathon', 'Robo Race', 'Open Mic', 'Quiz Night'],
    'fee': [200, 150, 0, 50]
})

# 2. Clean event and dept text
regs['event'] = regs['event'].str.strip().str.title()
regs['dept'] = regs['dept'].str.strip().str.upper()
fees['event'] = fees['event'].str.strip().str.title()
regs['dept'] = regs['dept'].fillna('Unknown')
regs_unique = regs.drop_duplicates(subset=['student', 'event'])
print(regs_unique)
merged_unique = pd.merge(regs_unique, fees, on='event', how='left').fillna({'fee': 0})
regs_per_event = merged_unique['event'].value_counts()
rev_per_dept_unique = merged_unique.groupby('dept')['fee'].sum()
merged_dup = pd.merge(regs, fees, on='event', how='left').fillna({'fee': 0})
rev_per_dept_dup = merged_dup.groupby('dept')['fee'].sum()
print("Registrations Per Event (Unique)")
print(regs_per_event.to_string())
print("Revenue Per Department (Duplicates Removed)")
print(rev_per_dept_unique.to_string())
print("Revenue Per Department (With Duplicates Kept)")
print(rev_per_dept_dup.to_string())


