## Pandas - a library used for working with data sets
## --------------------------------------------------

import pandas as pd

## Working with Series:

reviews = pd.Series([4.9, 4.3, 5, 4.7, 4.2])
print(reviews)
'''
    0    4.9
    1    4.3
    2    5.0
    3    4.7
    4    4.2
    dtype: float64
'''
print(reviews[0])       # 4.9

print(reviews.count())  # 5
print(reviews.mean())   # 4.619999999999999
print(reviews.min())    # 4.2
print(reviews.max())    # 5.0
print(reviews.std())    # 0.3563705936241093


