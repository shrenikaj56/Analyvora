import pandas as pd


def remove_duplicates(df):
    """
    Removes duplicate rows from the dataset.
    """
    return df.drop_duplicates()

def fill_missing_values(df, method):
    """
    Fill missing values using the selected method.
    """

    cleaned_df = df.copy()

    numeric_columns = cleaned_df.select_dtypes(include=["number"]).columns

    if method == "Mean":
        cleaned_df[numeric_columns] = cleaned_df[numeric_columns].fillna(
            cleaned_df[numeric_columns].mean()
        )

    elif method == "Median":
        cleaned_df[numeric_columns] = cleaned_df[numeric_columns].fillna(
            cleaned_df[numeric_columns].median()
        )

    elif method == "Mode":
        cleaned_df = cleaned_df.fillna(cleaned_df.mode().iloc[0])

    return cleaned_df



def fill_missing_values(df, method):
    """
    Fills missing values using the selected method.
    """

    cleaned_df = df.copy()

    numeric_columns = cleaned_df.select_dtypes(include=["number"]).columns

    if method == "Mean":
        cleaned_df[numeric_columns] = cleaned_df[numeric_columns].fillna(
            cleaned_df[numeric_columns].mean()
        )

    elif method == "Median":
        cleaned_df[numeric_columns] = cleaned_df[numeric_columns].fillna(
            cleaned_df[numeric_columns].median()
        )

    elif method == "Mode":
        cleaned_df = cleaned_df.fillna(cleaned_df.mode().iloc[0])

    return cleaned_df