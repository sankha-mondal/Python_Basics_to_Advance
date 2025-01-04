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

## ==================================================================================

## == :Working with Data-Frames: ==

scores_dict = {'Kohli':[100,50,70,81], 'Rohit':[100,88,45,71], 
               'Surya':[77,110,20,57], 'Jadeja':[99,120,58,93],
               'Rahul':[33,89,107,28]}
scores = pd.DataFrame(scores_dict)
print(scores)
'''
        Kohli  Rohit  Surya  Jadeja  Rahul
    0    100    100     77      99     33
    1     50     88    110     120     89
    2     70     45     20      58    107
    3     81     71     57      93     28
'''

scores = pd.DataFrame(scores_dict, index=['I1','I2','I3','I4'])
print(scores)
'''
        Kohli  Rohit  Surya  Jadeja  Rahul
    I1    100    100     77      99     33
    I2     50     88    110     120     89
    I3     70     45     20      58    107
    I4     81     71     57      93     28
'''

# Access Column data:
print("Kohli's Scores:")
print(scores['Kohli'])
'''
    Kohli's Scores:
    I1    100
    I2     50
    I3     70
    I4     81
    Name: Kohli, dtype: int64
'''
print(scores.Kohli)
'''
    I1    100
    I2     50
    I3     70
    I4     81
    Name: Kohli, dtype: int64
'''

# Access Row data:
print(scores.loc['I1'])
'''
    Kohli     100
    Rohit     100
    Surya      77
    Jadeja     99
    Rahul      33
    Name: I1, dtype: int64
'''
print(scores.iloc[0])
'''
    Kohli     100
    Rohit     100
    Surya      77
    Jadeja     99
    Rahul      33
    Name: I1, dtype: int64
'''

# Use Slicing and Lists:
print(scores.loc['I1':'I3'])  # returns data from I1 to I2
'''
        Kohli  Rohit  Surya  Jadeja  Rahul
    I1    100    100     77      99     33
    I2     50     88    110     120     89
    I3     70     45     20      58    107
'''
print(scores.iloc[1:3]) # returns n to (m-1)
'''
        Kohli  Rohit  Surya  Jadeja  Rahul
    I2     50     88    110     120     89
    I3     70     45     20      58    107
'''
print(scores.loc[['I1','I3']])  # returns particular rows
'''
        Kohli  Rohit  Surya  Jadeja  Rahul
    I1    100    100     77      99     33
    I3     70     45     20      58    107
'''
print(scores.iloc[[0,2]])  # returns particular rows 
'''
        Kohli  Rohit  Surya  Jadeja  Rahul
    I1    100    100     77      99     33
    I3     70     45     20      58    107
'''

# Getting Subset:
print(scores.loc['I1':'I3',['Kohli','Surya']])
'''
        Kohli  Surya
    I1    100     77
    I2     50    110
    I3     70     20
'''
print(scores.iloc[[0,2],0:3])
'''
        Kohli  Rohit  Surya
    I1    100    100     77
    I3     70     45     20
'''

# Playing with conditions:
print(scores[scores >= 90])
'''
        Kohli  Rohit  Surya  Jadeja  Rahul
    I1  100.0  100.0    NaN    99.0    NaN
    I2    NaN    NaN  110.0   120.0    NaN
    I3    NaN    NaN    NaN     NaN  107.0
    I4    NaN    NaN    NaN    93.0    NaN            
'''
print(scores[(scores>=80) & (scores<=90)])
'''
        Kohli  Rohit  Surya  Jadeja  Rahul
    I1    NaN    NaN    NaN     NaN    NaN
    I2    NaN   88.0    NaN     NaN   89.0
    I3    NaN    NaN    NaN     NaN    NaN
    I4   81.0    NaN    NaN     NaN    NaN
'''

# Accessing a cell data:
print(scores.at['I2','Kohli'])  # 50
print(scores.iat[2,0])   # 70

# Override a data:
scores.at['I2','Kohli'] = 150
print(scores.at['I2','Kohli'])  # 150 - Updated

scores.iat[2,0] = 200
print(scores.iat[2,0])  # 200 - Updated


# Working with Statistics:
print(scores.mean())
'''
    Kohli     132.75
    Rohit      76.00
    Surya      66.00
    Jadeja     92.50
    Rahul      64.25
    dtype: float64
'''
print(scores.describe())
'''
            Kohli       Rohit       Surya      Jadeja      Rahul
    count    4.000000    4.000000    4.000000    4.000000    4.00000
    mean   132.750000   76.000000   66.000000   92.500000   64.25000
    std     53.450133   23.846733   37.656341   25.748786   39.71041
    min     81.000000   45.000000   20.000000   58.000000   28.00000
    25%     95.250000   64.500000   47.750000   84.250000   31.75000
    50%    125.000000   79.500000   67.000000   96.000000   61.00000
    75%    162.500000   91.000000   85.250000  104.250000   93.50000
    max    200.000000  100.000000  110.000000  120.000000  107.00000
'''

# Data show upto 2 decimel points:
pd.set_option('display.precision',2)
print(scores.describe())
'''
            Kohli   Rohit   Surya  Jadeja   Rahul
    count    4.00    4.00    4.00    4.00    4.00
    mean   132.75   76.00   66.00   92.50   64.25
    std     53.45   23.85   37.66   25.75   39.71
    min     81.00   45.00   20.00   58.00   28.00
    25%     95.25   64.50   47.75   84.25   31.75
    50%    125.00   79.50   67.00   96.00   61.00
    75%    162.50   91.00   85.25  104.25   93.50
    max    200.00  100.00  110.00  120.00  107.00
'''

# Colums becomes Rows & vice-versa OR Transpose:
print(scores.T)
'''
            I1   I2   I3  I4
    Kohli   100  150  200  81
    Rohit   100   88   45  71
    Surya    77  110   20  57
    Jadeja   99  120   58  93
    Rahul    33   89  107  28
'''
print(scores.T.describe())
'''
            I1      I2      I3     I4
    count    5.00    5.00    5.00   5.00
    mean    81.80  111.40   86.00  66.00
    std     28.99   25.57   71.17  25.02
    min     33.00   88.00   20.00  28.00
    25%     77.00   89.00   45.00  57.00
    50%     99.00  110.00   58.00  71.00
    75%    100.00  120.00  107.00  81.00
    max    100.00  150.00  200.00  93.00
'''

#  Working eith Sorting:

# Based on Row-index:
print(scores.sort_index())  # by-default
'''
        Kohli  Rohit  Surya  Jadeja  Rahul
    I1    100    100     77      99     33
    I2    150     88    110     120     89
    I3    200     45     20      58    107
    I4     81     71     57      93     28
'''
print(scores.sort_index(ascending=False))  # Decending order
'''
        Kohli  Rohit  Surya  Jadeja  Rahul
    I4     81     71     57      93     28
    I3    200     45     20      58    107
    I2    150     88    110     120     89
    I1    100    100     77      99     33 
'''

# Based on Colume-index:
print(scores.sort_index(axis=1, ascending=False))
'''
        Surya  Rohit  Rahul  Kohli  Jadeja
    I1     77    100     33    100      99
    I2    110     88     89    150     120
    I3     20     45    107    200      58
    I4     57     71     28     81      93
'''

# Based on Row-Values:
print(scores.sort_values(by='I1',axis=1))
'''
        Rahul  Surya  Jadeja  Rohit  Kohli
    I1     33     77      99    100    100
    I2     89    110     120     88    150
    I3    107     20      58     45    200
    I4     28     57      93     71     81
'''
print(scores.sort_values(by='I1',axis=1,ascending=False))
'''
        Kohli  Rohit  Jadeja  Surya  Rahul
    I1    100    100      99     77     33
    I2    150     88     120    110     89
    I3    200     45      58     20    107
    I4     81     71      93     57     28
'''


# Read data from CSV file:
custom_df = pd.read_csv('customer.csv',
            names=['FirstName','LastName','Email','PhoneNo'] )
print(custom_df)
'''
    FirstName   LastName             Email           PhoneNo
0   first_name  last_name            email           phone
1        John        Doe       john.doe@example.com  1234567890
2        Jane      Smith     jane.smith@example.com  9876543210
3       Alice    Johnson  alice.johnson@example.com  5555555555
4         Bob      Brown      bob.brown@example.com  4444444444
'''

# Write data in CSV file:
# Create a new csv(custom_df.csv) file & copied the date from customer.csv 
custom_df.to_csv('custom_df.csv', index=False)


