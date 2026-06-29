from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def customer_segmentation(df):
    """
    Perform Customer Segmentation using K-Means Clustering.
    """

    # Select features
    X = df[["Age", "Purchase Amount (USD)"]]

    # Create KMeans model
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)

    # Fit model
    df["Cluster"] = kmeans.fit_predict(X)

    # Plot clusters
    plt.figure(figsize=(8, 6))

    plt.scatter(
        df["Age"],
        df["Purchase Amount (USD)"],
        c=df["Cluster"],
        cmap="viridis"
    )

    plt.scatter(
        kmeans.cluster_centers_[:, 0],
        kmeans.cluster_centers_[:, 1],
        color="red",
        marker="X",
        s=200,
        label="Centroids"
    )

    plt.title("Customer Segmentation")
    plt.xlabel("Age")
    plt.ylabel("Purchase Amount (USD)")
    plt.legend()
    plt.grid(True)

    plt.show()

    print("\nCustomer Segmentation Completed Successfully!")

    return df