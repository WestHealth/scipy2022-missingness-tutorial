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
