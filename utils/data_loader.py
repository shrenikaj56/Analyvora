import pandas as pd


def load_dataset(uploaded_file):
    """
    Loads a CSV or Excel file and returns a Pandas DataFrame.
    """

    if uploaded_file.name.endswith(".csv"):

        # Try UTF-8 first
        try:
            return pd.read_csv(uploaded_file, encoding="utf-8")

        # If UTF-8 fails, try Latin-1
        except UnicodeDecodeError:
            uploaded_file.seek(0)
            return pd.read_csv(uploaded_file, encoding="latin1")

    elif uploaded_file.name.endswith(".xlsx"):
        return pd.read_excel(uploaded_file)

    else:
        raise ValueError("Unsupported file format!")