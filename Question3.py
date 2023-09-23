# Q3. Define covariance and explain why it is important in statistical analysis. How is covariance calculated?

# Answer - 

# Covariance is used to find the relationship between features to determine the output. its important to statistical analysis as an example ,
#if the X is Increasing and Y is also increating then its +ve covariance.
# if the X is increasing and Y is decreasing then its having a -ve coviance.

import pandas as pd

# Covariance 
import numpy as np
# np.cov()
data = [[10,12,13],[34,23,45],[32,34,21]]

df = pd.DataFrame(data,columns=["A","B","C"])
print(df.cov())