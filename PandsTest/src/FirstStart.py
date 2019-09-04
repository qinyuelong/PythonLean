import numpy as np
import pandas as pd



def genArray():
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    print(s)


    dates = pd.date_range('20130101', periods=6)
    print(dates)


    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    print(df)

    df2 = pd.DataFrame({'A' : 1.,
                        'B' : pd.Timestamp('20130102'),
                        'C' : pd.Series(1, index=list(range(4)), dtype='f4'),
                        'D' : np.array([3] * 4, dtype='i4'),
                        'E' : pd.Categorical(['test', 'train', 'test', 'train']),
                        'F' : 'foo'
                        })

    print(df2)
    print('\n')
    print(df2.dtypes)





def lookData():
    dates = pd.date_range('20130101', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    print(df.head())

    print('\n')

    print(df.tail(3))

    print('\n')

    print(df.index)

    print('\n')

    print(df.columns)

    print('\n')


    # df.to_numpy()  报错 应该是改为了 values
    print(df.values)
    print('\n')
    print(df.get_values())

    print('\n')

    print(df.describe())

    print('\n')

    print(df.T)

    print('\n')

    # 按轴排序
    print(df.sort_index(axis=1, ascending=False))

    print('\n  按值排序 ')

    # 按值排序
    print(df.sort_values(by='B'))



def chooseValue():
    dates = pd.date_range('20130101', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    a = df['A']
    print(a)

    print('\n  切片选择')

    b = df[0:3]
    print(b)

    print('\n')

    c = df['20130102' : '20130106' :  2]
    print(c)

    print('\n  按标签选择')
    d = df.loc[dates[0]]
    print(d)

    print('\n')
    e = df.loc[:, ['A', 'B']]
    print(e)

    print('\n')
    f = df.loc['20130102' : '20130104', ['A', 'B']]
    print(f)

    print('\n')
    g = df.loc['20130102', ['A', 'B']]
    print(g)

    print('\n')
    h = df.loc[dates[0], 'A']
    print(h)

    print('\n')
    i = df.at[dates[0], 'A']
    print(i)

    print('\n')
    j = df.iloc[3]
    print(j)

    print('\n')
    k = df.iloc[3:5, 0:2]
    print(k)

    print('\n')
    l = df.iloc[[1,2,4], [0, 2]]
    print(l)

    print('\n')
    j = df.iloc[1:3, :]
    print(j)

    print('\n')
    r1 = df.iloc[1, 1]
    print(r1)

    r2 = df.iat[1,1]
    print(r2)


# 生成数组
# genArray()

# 查看数据
# lookData()


# 选择值
chooseValue()
