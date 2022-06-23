import pandas as pd
import numpy as np
# A function to cause missingness in a given column optionally
def clobber(df, column, probability, depends=[]):
    clob = df[column] == df[column]  # Always True
    for dep_column in depends:
        clob &= df[dep_column] > df[dep_column].median()
    clob *= probability
    rand = np.random.uniform(0, 1, size=len(clob))
    ret = df.copy()  # We copy to avoid clobbering the original
    ret[column] = np.where(clob < rand, df[column], np.nan)
    return ret

def stat_comparison(original, missing, column):
    df = pd.DataFrame.from_dict(
        dict(
            mean=[original[column].mean(), missing[column].mean()],
            median=[original[column].median(), missing[column].median()],
            stdev=[original[column].std(), missing[column].std()],
        ),
        orient="index",
        columns=["Original", "With Missing Data"],
    )
    df["difference"] = (df["Original"] - df["With Missing Data"]).abs()
    df["percentage"] = df["difference"] / df["Original"] * 100
    return df

#
# Helps highlight cells for hot deck imputation demonstration
#

def spotlight_donors(df, donors, missing=None):
    s = df.style
    def green(x):
        return 'background-color: green; color: white'
    def darkgreen(x):
        return 'background-color: darkgreen; color: white'
    def lightgreen(x):
        return 'background-color: lightgreen'
    def yellow(x):
        return 'background-color: yellow'
    for each in donors.index:
        s=s.applymap(green, subset=pd.IndexSlice[each, 'distance']).applymap(lightgreen, subset=pd.IndexSlice[each,'feature a'])
        if 'regression' in df.columns:
            s=s.applymap(darkgreen, subset=pd.IndexSlice[each, 'regression'])
            if missing:
                s=s.applymap(yellow, subset=pd.IndexSlice[missing, 'regression'])
    return s

class ImputationDisplayer:
    def __init__(self, df):
        self.missingness = df.applymap(lambda x: "background-color: paleturquoise" if np.isnan(x) else "")
    
    def __call__(self, df, rows):
        return df.iloc[0:rows].style.apply(lambda x: self.missingness.iloc[0:rows], axis=None)