import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")


def sales_by_category(df):
    plt.figure(figsize=(10, 6))
    category_sales = df.groupby("Category")["Purchase Amount (USD)"].sum().sort_values()

    category_sales.plot(kind="barh", color="skyblue")

    plt.title("Sales by Category")
    plt.xlabel("Total Sales (USD)")
    plt.ylabel("Category")
    plt.tight_layout()
    plt.show()


def sales_by_age_group(df):
    plt.figure(figsize=(8, 5))

    age_sales = df.groupby("Age Group")["Purchase Amount (USD)"].sum()

    age_sales.plot(kind="bar", color="orange")

    plt.title("Sales by Age Group")
    plt.xlabel("Age Group")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def top_10_customers(df):
    if "Customer ID" not in df.columns:
        return

    plt.figure(figsize=(12, 6))

    top = (
        df.groupby("Customer ID")["Purchase Amount (USD)"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    top.plot(kind="bar", color="green")

    plt.title("Top 10 Customers")
    plt.xlabel("Customer ID")
    plt.ylabel("Purchase Amount (USD)")
    plt.tight_layout()
    plt.show()


def purchase_distribution(df):
    plt.figure(figsize=(8, 5))

    sns.histplot(
        df["Purchase Amount (USD)"],
        bins=20,
        kde=True
    )

    plt.title("Purchase Amount Distribution")
    plt.xlabel("Purchase Amount (USD)")
    plt.tight_layout()
    plt.show()


def correlation_heatmap(df):

    numeric_df = df.select_dtypes(include=["number"])

    plt.figure(figsize=(8, 6))

    sns.heatmap(
        numeric_df.corr(),
        annot=True,
        cmap="coolwarm"
    )

    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()


def visualize_all(df):

    sales_by_category(df)

    sales_by_age_group(df)

    top_10_customers(df)

    purchase_distribution(df)

    correlation_heatmap(df)