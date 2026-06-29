from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def customer_segmentation(df):

    features = df[["Age", "Purchase Amount (USD)"]]

    kmeans = KMeans(n_clusters=4, random_state=42)

    df["Cluster"] = kmeans.fit_predict(features)

    plt.figure(figsize=(8,6))

    plt.scatter(
        df["Age"],
        df["Purchase Amount (USD)"],
        c=df["Cluster"]
    )

    plt.title("Customer Segmentation")

    plt.xlabel("Age")

    plt.ylabel("Purchase Amount")

    plt.show()

    return df