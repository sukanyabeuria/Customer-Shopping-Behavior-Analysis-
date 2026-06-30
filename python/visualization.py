import matplotlib.pyplot as plt
import seaborn as sns

# Professional Theme
plt.style.use("dark_background")
sns.set_palette("magma")


def sales_by_category(df):
    plt.figure(figsize=(12, 6))

    category_sales = (
        df.groupby("Category")["Purchase Amount (USD)"]
        .sum()
        .sort_values()
    )

    ax = category_sales.plot(
        kind="barh",
        color="#ff4da6",
        edgecolor="white"
    )

    plt.title(
        "🛍 Sales by Category",
        fontsize=18,
        fontweight="bold",
        color="white"
    )

    plt.xlabel("Total Sales (USD)", fontsize=12)
    plt.ylabel("Category", fontsize=12)

    for i, value in enumerate(category_sales):
        ax.text(
            value + 50,
            i,
            f"${value:,.0f}",
            color="white",
            va="center",
            fontsize=10
        )

    plt.grid(axis="x", linestyle="--", alpha=0.3)
    plt.tight_layout()
    plt.show()


def sales_by_age_group(df):
    plt.figure(figsize=(10, 5))

    age_sales = (
        df.groupby("Age Group")["Purchase Amount (USD)"]
        .sum()
    )

    ax = age_sales.plot(
        kind="bar",
        color="#b266ff",
        edgecolor="white"
    )

    plt.title(
        "👥 Sales by Age Group",
        fontsize=18,
        fontweight="bold"
    )

    plt.xlabel("Age Group")
    plt.ylabel("Sales (USD)")
    plt.xticks(rotation=0)

    for p in ax.patches:
        ax.annotate(
            f"${p.get_height():,.0f}",
            (p.get_x() + p.get_width()/2, p.get_height()),
            ha="center",
            va="bottom",
            fontsize=9
        )

    plt.grid(axis="y", linestyle="--", alpha=0.3)
    plt.tight_layout()
    plt.show()


def top_10_customers(df):

    if "Customer ID" not in df.columns:
        return

    plt.figure(figsize=(12,6))

    top = (
        df.groupby("Customer ID")["Purchase Amount (USD)"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    ax = top.plot(
        kind="bar",
        color="#ff66c4",
        edgecolor="white"
    )

    plt.title(
        "🏆 Top 10 Customers",
        fontsize=18,
        fontweight="bold"
    )

    plt.xlabel("Customer ID")
    plt.ylabel("Purchase Amount (USD)")
    plt.xticks(rotation=45)

    plt.grid(axis="y", linestyle="--", alpha=0.3)
    plt.tight_layout()
    plt.show()


def purchase_distribution(df):

    plt.figure(figsize=(10,5))

    sns.histplot(
        df["Purchase Amount (USD)"],
        bins=20,
        kde=True,
        color="#ff4da6"
    )

    plt.title(
        "📈 Purchase Amount Distribution",
        fontsize=18,
        fontweight="bold"
    )

    plt.xlabel("Purchase Amount (USD)")
    plt.grid(alpha=0.3)

    plt.tight_layout()
    plt.show()


def correlation_heatmap(df):

    numeric_df = df.select_dtypes(include=["number"])

    plt.figure(figsize=(8,6))

    sns.heatmap(
        numeric_df.corr(),
        annot=True,
        cmap="magma",
        linewidths=1,
        linecolor="black"
    )

    plt.title(
        "🔥 Correlation Heatmap",
        fontsize=18,
        fontweight="bold"
    )

    plt.tight_layout()
    plt.show()


def visualize_all(df):

    sales_by_category(df)
    sales_by_age_group(df)
    top_10_customers(df)
    purchase_distribution(df)
    correlation_heatmap(df)