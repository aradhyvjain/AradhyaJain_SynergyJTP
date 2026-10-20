# Question-10 Do MidSem Averages hide Inconsistency
## Aim
To group the data by subject and compute mean,std,minimum,amximum marks in one aggreagate call and to rank the subjects by mean and standard deviation.

## Code
```python
import numpy as np
import pandas as pd
marks = pd.DataFrame({
    'subject': ['Maths']*4 + ['Physics']*4 + ['Pps']*4,
    'marks': [72, 74, 70, 73, 60, 95, 50, 85, 80, 78, 82, 84]})
# subjects by mean
stats_marks=marks.groupby('subject')['marks'].describe()
print(stats_marks.sort_values(by='mean',ascending=False))
# subjects by std
print(stats_marks.sort_values(by='std', ascending=False))
```

## Output
```text
         count   mean        std   min   25%   50%    75%   max
subject                                                        
Pps        4.0  81.00   2.581989  78.0  79.5  81.0  82.50  84.0
Physics    4.0  72.50  21.015867  50.0  57.5  72.5  87.50  95.0
Maths      4.0  72.25   1.707825  70.0  71.5  72.5  73.25  74.0
         count   mean        std   min   25%   50%    75%   max
subject                                                        
Physics    4.0  72.50  21.015867  50.0  57.5  72.5  87.50  95.0
Pps        4.0  81.00   2.581989  78.0  79.5  81.0  82.50  84.0
Maths      4.0  72.25   1.707825  70.0  71.5  72.5  73.25  74.0
```

## Explanation
groupby() function is used to create groups of the data based on the attributes you provide. sort_values() is used to sort the data in ascending or descending order.


## Interpretation
The teacher needs to investigate the subject with higher standard deviation as it shows higher degree of variability.