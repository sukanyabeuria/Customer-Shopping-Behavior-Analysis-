import pandas as pd


def dataset_summary(df):
    print("\n" + "=" * 60)
    print("DATASET SUMMARY")
    print("=" * 60)

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nSummary Statistics:")
    print(df.describe(include="all"))


def sales_by_gender(df):
    print("\n" + "=" * 60)
    print("SALES BY GENDER")
    print("=" * 60)

    if "Gender" in df.columns:
        result = (
            df.groupby("Gender")["Purchase Amount (USD)"]
            .sum()
            .sort_values(ascending=False)
        )
        print(result)


def sales_by_category(df):
    print("\n" + "=" * 60)
    print("SALES BY CATEGORY")
    print("=" * 60)

    if "Category" in df.columns:
        result = (
            df.groupby("Category")["Purchase Amount (USD)"]
            .sum()
            .sort_values(ascending=False)
        )
        print(result)


def average_purchase(df):
    print("\n" + "=" * 60)
    print("AVERAGE PURCHASE")
    print("=" * 60)

    average = df["Purchase Amount (USD)"].mean()

    print(f"Average Purchase Amount : ${average:.2f}")


def highest_purchase(df):
    print("\n" + "=" * 60)
    print("HIGHEST PURCHASE")
    print("=" * 60)

    highest = df.loc[df["Purchase Amount (USD)"].idxmax()]

    print(highest)


def lowest_purchase(df):
    print("\n" + "=" * 60)
    print("LOWEST PURCHASE")
    print("=" * 60)

    lowest = df.loc[df["Purchase Amount (USD)"].idxmin()]

    print(lowest)


def perform_eda(df):

    dataset_summary(df)

    sales_by_gender(df)

    sales_by_category(df)

    average_purchase(df)

    highest_purchase(df)

    lowest_purchase(df)

    print("\nEDA Completed Successfully!")
