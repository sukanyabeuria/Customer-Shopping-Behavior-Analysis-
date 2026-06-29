import pandas as pd


def create_age_group(df):
    """
    Create Age Group column.
    """

    bins = [0, 18, 25, 35, 45, 60, 100]
    labels = [
        "Under 18",
        "18-25",
        "26-35",
        "36-45",
        "46-60",
        "60+"
    ]

    df["Age Group"] = pd.cut(
        df["Age"],
        bins=bins,
        labels=labels,
        include_lowest=True
    )

    return df


def create_spending_category(df):
    """
    Categorize customers based on purchase amount.
    """

    def spending(amount):

        if amount < 30:
            return "Low"

        elif amount < 70:
            return "Medium"

        else:
            return "High"

    df["Spending Category"] = df["Purchase Amount (USD)"].apply(spending)

    return df


def create_purchase_month(df):
    """
    Extract purchase month from Purchase Date.
    """

    if "Purchase Date" in df.columns:

        df["Purchase Date"] = pd.to_datetime(df["Purchase Date"])

        df["Purchase Month"] = df["Purchase Date"].dt.month_name()

    return df


def create_weekend_purchase(df):
    """
    Identify weekend purchases.
    """

    if "Purchase Date" in df.columns:

        df["Weekend Purchase"] = (
            df["Purchase Date"].dt.dayofweek >= 5
        )

    return df


def feature_engineering(df):
    """
    Perform all feature engineering.
    """

    df = create_age_group(df)

    df = create_spending_category(df)

    df = create_purchase_month(df)

    df = create_weekend_purchase(df)

    print("\nFeature Engineering Completed Successfully!")

    return df