# Question-15 TechTatva Revenue Investigation
## Aim
Clean event and dept text, treat a repeated (student, event) pair as one registration, fill the missing department with Unknown, merge with fees, and compute registrations per event and revenue per department. Then repeat the department revenue calculation without removing duplicates. Interpret: how would the duplicates have changed the committee’s conclusion?

## Code
```python
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
```

## Output
```text
    reg_id student                event     dept
0        1     Anu     City Landscaping      CSE
1        2    Bala     City Landscaping      CSE
2        3  Chitra  Salutes And Ladders      ECE
4        5     Dev             Open Mic     MECH
5        6    Esha             Open Mic      CSE
6        7  Farhan            Robo Race      ECE
7        8    Gita           Quiz Night  Unknown
8        9    Bala            Hackathon      CSE
9       10    Hari           Quiz Night      ECE
10      11     Ira            Hackathon      ECE
Registrations Per Event (Unique)
event
City Landscaping       2
Open Mic               2
Hackathon              2
Quiz Night             2
Salutes And Ladders    1
Robo Race              1
Revenue Per Department (Duplicates Removed)
dept
CSE        200.0
ECE        400.0
MECH         0.0
Unknown     50.0
Revenue Per Department (With Duplicates Kept)
dept
CSE        200.0
ECE        400.0
MECH         0.0
Unknown     50.0
```

## Explanation
.str.strip() removes accidental leading and trailing whitespaces (e.g., converting " city landscaping " into "city landscaping").
.str.title() capitalizes the first letter of each word and lowers the rest. This ensures that "ROBO RACE" and "open mic" properly match their entries in the fee table ("Robo Race", "Open Mic").
.str.upper() converts all text to uppercase, fixing inconsistencies where a department was typed in lowercase (e.g., combining "cse" and "CSE").

.fillna('Unknown') replaces any None or NaN values in the department column with the placeholder string 'Unknown' as requested by the prompt.
regs_dedup = regs.drop_duplicates(subset=["student", "event"])
Use code with caution.
drop_duplicates() looks for repeated pairs of strings in the student and event columns.
In this dataset, it flags the second time Anu appears registered for City Landscaping and drops that row entirely, creating a cleaned dataframe (regs_dedup).

how='left' performs a left outer join. This ensures that every single event registration remains in our table, even if that event does not exist in the fees table (like City Landscaping or Salutes and Ladders).
.fillna({'fee': 0}) automatically changes the resulting NaN price tags for those free events into a numerical value of 0 so we can perform math on them.

groupby('dept') splits the dataset into separate piles based on the department name.
['fee'].sum() looks at the price column for each individual pile and calculates the total sum, giving the final revenue generated per department.

## Interpretation
The duplicate registrations would not have changed the committee's financial conclusions at all. However, if the committee relied strictly on raw participant counts to estimate logistics, the uncleaned dataset would have falsely inflated the registration figures for the "City Landscaping" event by 1.
