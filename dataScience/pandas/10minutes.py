# %%
import pandas  as pd
import numpy as np

# %%
s = pd.Series([1, 3, 5, np.nan, 6, 8])
s

# %%
dates = pd.date_range("20010102",periods=6)
print(type(dates))
dates
df = pd.DataFrame(np.random.randn(6,4),columns=list("ABCD"),index=dates)
df

# %%
df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(list(range(10,14)), index=list(range(4)), dtype="float32"),
        "D": np.array([3,2] * 2, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
df2

# %%
print(df.head(2))
print(df.tail(2))

# %%
print(df.index)
print(df.columns)

# %%
df.to_numpy()

# %%
df.describe()

# %%
df.T

# %%
df.sort_index(axis=1,ascending=False)

# %%
df.sort_values(by="B")

# %%
df1=df.T
df1.sort_values(by="20010102",ascending=False)

# %%
df["A"]

# %%
df[0::2]

# %%
df["20010102":"20010106":2]

# %%
df.loc[dates[0]]

# %%
df.loc[:,list("AB")]

# %%
df.loc[dates[0],"A"]

# %%
df.iloc[3]

# %%
df.iloc[0:5,0:2]

# %%
df.iloc[[1,2,4],[0,2]]

# %%
df.iloc[0,0]

# %%
df[df["A"]>0]

# %%
df[df>0]

# %%
df.count().iloc[0]

# %%
df2=df.copy()
df2['E']=["one","one","two","three","four","five"]
df2

# %%
df2[df2["E"].isin(["one"])]

# %%
s1 = pd.Series(list(range(6)),index=pd.date_range("20010102",periods=6))
df["F"]=s1
df

# %%
df.loc[dates[1],"A"]=10
df.iloc[2,2]=10
df

# %%
df.loc[:,"D"]=np.array([4]*len(df))
df

# %%
df[df>0]=-df
df

# %%
df[df.iloc[list(range(3,6))]<0]=-df
df

# %%
df1=df.reindex(index=dates[0:4],columns=list(df.columns).append("E"))
df1.loc[dates[0]:dates[1],"E"]=1
df1

# %%
df1.dropna(how="any")

# %%
df1.fillna(value=5)

# %%
df1.isna()

# %%
df.mean()

# %%
df.mean(axis=1)

# %%
s=pd.Series([1,2,3,np.nan,4,5],index=dates).shift(2)
s

# %%
df.sub(s,axis=0)

# %%
df.agg(lambda x: np.mean(x) * 5.3)

# %%
df.transform(lambda x:x*101)

# %%
s=pd.Series(np.random.randint(0,7,size=10))
s

# %%
s.value_counts()

# %%
s=pd.Series(["A","B","C",np.nan,"AA","AB"])
s.str.lower()

# %%
df=pd.DataFrame(np.random.randn(10,4))
pieces = [df[:3],df[4:7],df[8:]]
pieces
pd.concat(pieces)

# %%
left = pd.DataFrame({"key":["poo","poo"],"lval":[1,2]})
right = pd.DataFrame({"key":["poo","poo"],"rval":[3,4]})
pd.merge(left,right,on="key")

# %%
df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    },
    )
df

# %%
df.groupby("A")[["C","D"]].sum()

# %%
df.groupby(["A","B"]).sum()

# %%
arrays = [
    ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
    ["one", "two", "one", "two", "one", "two", "one", "two"]]
index = pd.MultiIndex.from_arrays(arrays, names=["first", "second"])
df=pd.DataFrame(np.random.randn(8,2), index=index, columns=["A","B"])
df2=df[:5]
df2

# %%
stacked=df2.stack(future_stack=True)
stacked

# %%
stacked.unstack()

# %%
stacked.unstack(1)

# %%
df = pd.DataFrame(
    {
        "A": ["one", "one", "two", "three"] * 3,
        "B": ["A", "B", "C"] * 4,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
        "D": np.random.randn(12),
        "E": np.random.randn(12),
    }
)
df

# %%
pd.pivot_table(df, values=["D"],index=["A","B"],columns=["C"])

# %%
rng=pd.date_range("20010102",periods=100,freq="s")
ts=pd.Series(np.random.randint(0,500,len(rng)),index=rng)
ts.resample("1Min").sum()

# %%
rng =pd.date_range("01/02/2001 00:00",periods=5,freq="D")
ts=pd.Series(np.random.randn(len(rng)),rng)
ts

# %%
tz=ts.tz_localize("UTC")
tz

# %%
tz.tz_convert("US/Eastern")

# %%
rng

# %%
rng+pd.offsets.BusinessDay(5)

# %%
df = pd.DataFrame({"id":[1,2,3,4,5,6],"raw_grade":["a","b","b","a","a","e"]})
df

# %%
df["grade"]=df["raw_grade"].astype("category")
df["grade"]

# %%
new_categories = ["very good","good","very bad"]
df["grade"]=df["grade"].cat.rename_categories(new_categories)
df["grade"]

# %%
df["grade"]=df["grade"].cat.set_categories(["very bad","bad","medium","good","very good"])
df["grade"]

# %%
df.sort_values(by="grade")

# %%
df.groupby("grade",observed=False).size()

# %%
import matplotlib.pyplot as plt
plt.close("all")

# %%
ts=pd.Series(np.random.randn(1000),pd.date_range("02/01/2001",periods=1000))
ts=ts.cumsum()
ts.plot()

# %%
df=pd.DataFrame(np.random.randn(1000,4),index=ts.index,columns=["A","B","C","D"])
df=df.cumsum()
plt.figure();
df.plot();
plt.legend(loc="best");

# %%
df=pd.DataFrame(np.random.randint(0,5,(10,5)))
df.to_csv("foo.csv")

# %%
pd.read_csv("foo.csv")

# %%
df.to_parquet("foo.parquet")

# %%
df.to_excel('foo.xlsx',sheet_name="sheet1")

# %%
pd.read_excel("foo.xlsx","sheet1",index_col=None,na_values=["NA"])

# %%



