from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


# Professional Theme
plt.style.use("dark_background")


def customer_segmentation(df):
    """
    Customer Segmentation using K-Means Clustering
    """

    # Select Features
    X = df[["Age", "Purchase Amount (USD)"]]

    # Train Model
    kmeans = KMeans(
        n_clusters=3,
        random_state=42,
        n_init=10
    )

    df["Cluster"] = kmeans.fit_predict(X)

    # Create Figure
    plt.figure(figsize=(11, 7))

    # Scatter Plot
    plt.scatter(
        df["Age"],
        df["Purchase Amount (USD)"],
        c=df["Cluster"],
        cmap="plasma",
        s=90,
        alpha=0.85,
        edgecolors="white",
        linewidth=0.8
    )

    # Centroids
    plt.scatter(
        kmeans.cluster_centers_[:, 0],
        kmeans.cluster_centers_[:, 1],
        marker="*",
        s=500,
        color="#00FFFF",
        edgecolors="white",
        linewidth=2,
        label="Centroids"
    )

    plt.title(
        "✨ Customer Segmentation using K-Means",
        fontsize=20,
        fontweight="bold",
        color="white"
    )

    plt.xlabel(
        "Age",
        fontsize=13,
        fontweight="bold"
    )

    plt.ylabel(
        "Purchase Amount (USD)",
        fontsize=13,
        fontweight="bold"
    )

    plt.grid(
        linestyle="--",
        alpha=0.3
    )

    plt.legend(
        facecolor="black",
        edgecolor="white",
        fontsize=11
    )

    plt.tight_layout()
    plt.show()

    print("\n✨ Customer Segmentation Completed Successfully!")

    return df