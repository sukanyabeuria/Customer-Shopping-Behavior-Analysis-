import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# Professional Theme
plt.style.use("dark_background")


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

    print("\n" + "═" * 70)
    print("🤖 SALES PREDICTION MODEL")
    print("═" * 70)

    print(f"📉 Mean Squared Error : {mse:.2f}")
    print(f"🎯 R² Score           : {r2:.2f}")

    plt.figure(figsize=(10, 7))

    # Actual vs Predicted Points
    plt.scatter(
        y_test,
        y_pred,
        s=80,
        color="#ff4da6",
        edgecolors="white",
        linewidth=0.8,
        alpha=0.9,
        label="Predicted"
    )

    # Perfect Prediction Line
    plt.plot(
        [y_test.min(), y_test.max()],
        [y_test.min(), y_test.max()],
        color="#00FFFF",
        linewidth=3,
        linestyle="--",
        label="Perfect Prediction"
    )

    plt.title(
        "📈 Actual vs Predicted Purchase Amount",
        fontsize=20,
        fontweight="bold",
        color="white"
    )

    plt.xlabel(
        "Actual Purchase Amount (USD)",
        fontsize=13,
        fontweight="bold"
    )

    plt.ylabel(
        "Predicted Purchase Amount (USD)",
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

    print("\n✨ Sales Prediction Completed Successfully!")

    return model