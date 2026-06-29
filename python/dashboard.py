import plotly.express as px


def sales_dashboard(df):
    """
    Interactive Dashboard using Plotly
    """

    print("Opening Dashboard...")

    # Sales by Category
    fig1 = px.bar(
        df,
        x="Category",
        y="Purchase Amount (USD)",
        color="Category",
        title="Total Sales by Category"
    )
    fig1.show()

    # Sales by Gender
    fig2 = px.pie(
        df,
        names="Gender",
        values="Purchase Amount (USD)",
        title="Sales Distribution by Gender"
    )
    fig2.show()

    # Sales by Age
    fig3 = px.scatter(
        df,
        x="Age",
        y="Purchase Amount (USD)",
        color="Category",
        title="Age vs Purchase Amount"
    )
    fig3.show()

    print("Dashboard Loaded Successfully!")
  