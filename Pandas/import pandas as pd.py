import pandas as pd
import numpy as np

O = pd.Series([1,3,5,7,9])
E = pd.Series([2,4,6,8,10])

OE = O + E
OE = OE.astype(str)
print(OE)


d = {'a': 200, 'b': 400, 'c': 600}

ds = pd.Series(d)
print(ds)


D = {
    'col1': [1,2,3],
    'col2': [4,5,6],
    'col3': pd.Series([8,9], index = [0,1]),

}

df = pd.DataFrame(D, index = [2,3,4])

print(df)
print(df.iloc[2])


s = pd.Series([
    ['Red', 'Green', 'White'],
    ['Red', 'Black'],
    ['Yellow']])
print("Original Series of list")
print(s)
s = s.apply(pd.Series).stack().reset_index(drop=True)
print("One Series")
print(s)

OE = OE.astype(int)
OE.sort_values(ascending=False, inplace=True)
print(OE)

COE = pd.concat([OE, pd.Series([23,27,31])], ignore_index=True)
print(COE)

sCOE = COE < 20
print(sCOE)


print(COE.mean())
print(COE.std())

C = COE[~COE.isin(OE)]
print(C)

COEOE = pd.concat([COE, OE], ignore_index=True)
print(COEOE)

E = COEOE[~COEOE.isin(OE) | ~COEOE.isin(COE)]
print(E)

L = [COE.min(), COE.quantile(), COE.median()]
print(L)


print(COEOE.value_counts())





X = pd.Series(np.random.randint(1, 10, 20))
Cho = pd.Series(
    np.random.choice(np.arange(0,20), size = 5, replace=False)
)
print(X[Cho])



print(COEOE.to_frame().reset_index())