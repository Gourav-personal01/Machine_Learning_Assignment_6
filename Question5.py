# Q5. Calculate the covariance matrix for the following variables in a dataset: Age, Income, and Education
# level. Interpret the results.

import pandas as pd
df = pd.DataFrame({
    'Age' : [1,2,3,4,5],
    'Income' : [6,7,8,9,10],
    'Education' : [11,12,13,14,15]
})

print(df.cov())