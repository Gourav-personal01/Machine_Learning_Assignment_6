# Q6. You are working on a machine learning project with a dataset containing several categorical
# variables, including "Gender" (Male/Female), "Education Level" (High School/Bachelor's/Master's/PhD),
# and "Employment Status" (Unemployed/Part-Time/Full-Time). Which encoding method would you use for
# each variable, and why?

# Answer - 
# 1. Gender (Male/Female - Label and One hot Encoding 
#  Since "Gender" is a binary categorical variable (Male/Female) with no inherent order,
#  you can use either label encoding (Male → 0, Female → 1) or one-hot encoding (two binary columns: "Male" and "Female")

# 2. Education Level (High School/Bachelor's/Master's/PhD) - Ordinal - 
# "Education Level" represents an ordinal categorical variable with a clear order or hierarchy (e.g., "High School" < "Bachelor's" < "Master's" < "PhD"). 

# 3. Employment Status (Nominal Categorical Variable - No Order)
# "Employment Status" is a nominal categorical variable with no inherent order (e.g., "Unemployed," "Part-Time," "Full-Time").