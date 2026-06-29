import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


def sales_prediction(df):
    """
    Train a Linear Regression model to predict Purchase Amount.
    """

    X = df[["Age"]]
    y = df["Purchase Amount (USD)"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = LinearRegression()

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("\n" + "=" * 60)
    print("SALES PREDICTION MODEL")
    print("=" * 60)

    print(f"Mean Squared Error : {mse:.2f}")
    print(f"R² Score           : {r2:.2f}")

    plt.figure(figsize=(8, 6))

    plt.scatter(
        y_test,
        y_pred,
        color="blue"
    )

    plt.plot(
        [y_test.min(), y_test.max()],
        [y_test.min(), y_test.max()],
        color="red",
        linewidth=2
    )

    plt.title("Actual vs Predicted Purchase Amount")

    plt.xlabel("Actual Purchase Amount")

    plt.ylabel("Predicted Purchase Amount")

    plt.grid(True)

    plt.tight_layout()

    plt.show()

    print("\nSales Prediction Completed Successfully!")

    return model