import pandas as pd


def line():
    print("\n" + "═" * 70)


def dataset_summary(df):
    line()
    print("📊 DATASET SUMMARY")
    line()

    print(f"\n📌 Shape            : {df.shape}")
    print(f"\n📋 Columns          : {df.columns.tolist()}")

    print("\n🧩 Data Types")
    print(df.dtypes)

    print("\n❌ Missing Values")
    print(df.isnull().sum())

    print("\n🔁 Duplicate Rows")
    print(df.duplicated().sum())

    print("\n📈 Summary Statistics")
    print(df.describe(include="all"))


def sales_by_gender(df):
    line()
    print("👨‍🦰 SALES BY GENDER")
    line()

    if "Gender" in df.columns:
        result = (
            df.groupby("Gender")["Purchase Amount (USD)"]
            .sum()
            .sort_values(ascending=False)
        )

        print(result)


def sales_by_category(df):
    line()
    print("🛍️ SALES BY CATEGORY")
    line()

    if "Category" in df.columns:
        result = (
            df.groupby("Category")["Purchase Amount (USD)"]
            .sum()
            .sort_values(ascending=False)
        )

        print(result)


def average_purchase(df):
    line()
    print("💰 AVERAGE PURCHASE")
    line()

    average = df["Purchase Amount (USD)"].mean()

    print(f"\nAverage Purchase Amount : ${average:.2f}")


def highest_purchase(df):
    line()
    print("🏆 HIGHEST PURCHASE")
    line()

    highest = df.loc[df["Purchase Amount (USD)"].idxmax()]

    print(highest)


def lowest_purchase(df):
    line()
    print("📉 LOWEST PURCHASE")
    line()

    lowest = df.loc[df["Purchase Amount (USD)"].idxmin()]

    print(lowest)


def perform_eda(df):

    dataset_summary(df)

    sales_by_gender(df)

    sales_by_category(df)

    average_purchase(df)

    highest_purchase(df)

    lowest_purchase(df)

    line()
    print("✅ EDA COMPLETED SUCCESSFULLY")
    line()