from sklearn.linear_model import LinearRegression

def sales_prediction(df):

    X = df[["Age"]]

    y = df["Purchase Amount (USD)"]

    model = LinearRegression()

    model.fit(X, y)

    print("Model trained successfully!")

    return model