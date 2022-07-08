import numpy as np
import pandas as pd


# A function to cause missingness in a given column optionally
def clobber(df, column, probability, depends=[]):
    """
    This clobbers a given column in a dataframe.
    Missingness can optionally be dependent on other column(s)
    :param df: The dataframe to clobber
    :param column: The column to clobber
    :param probability: The probability if certain conditions are met to clobber
    :param depends: Clobbering depends on listed columns. (Empty = MCAR)
    :return: Returns a copy of the dataset after it is clobbered
    """
    clob = df[column] == df[column]  # Always True
    for dep_column in depends:
        clob &= df[dep_column] > df[dep_column].median()
    clob *= probability
    rand = np.random.uniform(0, 1, size=len(clob))
    ret = df.copy()  # We copy to avoid clobbering the original
    ret[column] = np.where(clob < rand, df[column], np.nan)
    return ret


def stat_comparison(original, missing, column):
    """
    Compares the statistics two datasets of a certain column
    :param original: Original dataset
    :param missing: Dataset with missing or imputed values
    :param column: Column to compare
    :return: A nicely formatted panda's dataframe
    """
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
    """
    Spotlights specific cells in a panda's data frame to indicate which celss are donors.
    This is for the hot deck imputation demo
    :param df: The dataframe
    :param donors: Collection of rows that are indicies
    :param missing: Highlight the missing value
    :return: Returns the colorized dataframe
    """
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
        s = s.applymap(green, subset=pd.IndexSlice[each, 'distance']).applymap(lightgreen,
                                                                               subset=pd.IndexSlice[each, 'feature a'])
        if 'regression' in df.columns:
            s = s.applymap(darkgreen, subset=pd.IndexSlice[each, 'regression'])
            if missing:
                s = s.applymap(yellow, subset=pd.IndexSlice[missing, 'regression'])
    return s


class ImputationDisplayer:
    """
    This class attaches to a Panda's dataframe a displayer class. When invoked,
    it displays the first N lines of the dataframe with imputed values highlighted
    """

    def __init__(self, df):
        self.missingness = df.applymap(lambda x: "background-color: paleturquoise" if pd.isnull(x) else "")
        df.displayer = self  # attach to dataframe

    def __call__(self, df, rows):
        """
        :param df: The dataframe to color
        :param rows: Number of rows (N) to display
        :return: first N rows of a dataframe with imputed values highlighted
        """
        return df.iloc[0:rows].style.apply(lambda x: self.missingness.iloc[0:rows], axis=None)
