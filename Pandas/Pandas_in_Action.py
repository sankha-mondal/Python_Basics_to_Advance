## Pandas - a library used for working with data sets
## returns <class 'pandas.core.series.Series'> type
## --------------------------------------------------

import pandas as pd

## == :Working with Series: ==

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

print(reviews.describe())
'''
    count    5.000000
    mean     4.620000
    std      0.356371
    min      4.200000
    25%      4.300000
    50%      4.700000
    75%      4.900000
    max      5.000000
'''

# Custom indexing:
reviews = pd.Series([4.9, 4.3, 5, 4.7, 4.2], index=['python','c++','java','django','ruby'])
print(reviews)
'''
    python    4.9
    c++       4.3
    java      5.0
    django    4.7
    ruby      4.2
    dtype: float64
'''

reviews = pd.Series({'python':4.6, 'java':4.5, 'ruby':4.8, 'c++':5})
print(reviews)
'''
    python    4.6
    java      4.5
    ruby      4.8
    c++       5.0
    dtype: float64
'''
# Accessing value by indexing:
print(reviews['python'])  # 4.6
print(reviews.python)  # 4.6
print(reviews.java)    # 4.5
print(reviews.index)   # Index(['python', 'java', 'ruby', 'c++'], dtype='object')
print(reviews.values)  # [4.6 4.5 4.8 5. ]

cources = pd.Series(['Java','Python','Ruby'])
print(cources)
'''
    0      Java
    1    Python
    2      Ruby
    dtype: object
'''
print(cources.str.upper())
'''
    0      JAVA
    1    PYTHON
    2      RUBY
    dtype: object
'''
print(cources.str.contains('y'))
'''
    0    False
    1     True
    2     True
    dtype: bool
'''




