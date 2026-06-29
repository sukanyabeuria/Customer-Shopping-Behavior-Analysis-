import pandas as pd


def load_data(file_path):
    """
    Load the dataset from a CSV file.
    Tries UTF-8 first, then Latin-1 if needed.
    """
    try:
        df = pd.read_csv(file_path, encoding="utf-8")
    except UnicodeDecodeError:
        try:
            df = pd.read_csv(file_path, encoding="utf-8-sig")
        except UnicodeDecodeError:
            df = pd.read_csv(file_path, encoding="latin1")

    return df


def display_info(df):
    """
    Display basic dataset information.
    """
    print("\n" + "=" * 60)
    print("DATASET OVERVIEW")
    print("=" * 60)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nDataset Shape:")
    print(df.shape)

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nStatistical Summary:")
    print(df.describe(include="all"))


def clean_data(df):
    """
    Perform basic data cleaning.
    """
    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove rows with missing values
    df = df.dropna()

    # Reset index
    df.reset_index(drop=True, inplace=True)

    return df