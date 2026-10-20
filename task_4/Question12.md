# Question-12 The Misleading Conversion Rate-Ambani wants to compete with elon musks starlink 
## Aim
To find what is wrong with averaging the daily rates and to fix the ananlysis bu aggregating the right columns first and computing the rate afterwards

## Code
```python
import numpy as np
import pandas as pd
funnel = pd.DataFrame({'channel': ['A', 'A', 'B', 'B'],
                       'visitors': [10, 490, 100, 100],
                       'signups': [6, 49, 20, 20]})
funnel=funnel.groupby('channel').sum()
funnel['rate'] = funnel['signups'] / funnel['visitors'] * 100
print(funnel)
```

## Output
```text
         visitors  signups  rate
channel                         
A             500       55  11.0
B             200       40  20.0
```

## Explanation
The original code calculates individual rates for each row first, thrn averages those rates together using.mean(). The code avearges these rates: (60+10)/2=35%. this is flawed because 60 % rate only applied to a tiny sample of 10 peopl, while the 10 percent rate applied to a mch larger group of 490 people. Averaging them gives the small group disproportionate weight.


## Decision
Channel B performs better than channel A. So Jio should invest in channel B.