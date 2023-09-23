# Q4. For a dataset with the following categorical variables: Color (red, green, blue), Size (small, medium,
# large), and Material (wood, metal, plastic), perform label encoding using Python's scikit-learn library.
# Show your code and explain the output.

import pandas as pd

from sklearn.preprocessing import LabelEncoder

df = pd.DataFrame({
    'color' : ['red','blue','green','green','red','blue'],
    'size' : ['small','medium','large','medium','small','large']
})

print(df)

# Create an instance of Label encoder

encoder = LabelEncoder()

colour = encoder.fit_transform(df['color'])
size = encoder.fit_transform(df['size'])
print(colour)
print(size)