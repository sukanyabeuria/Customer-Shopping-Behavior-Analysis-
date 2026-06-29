import plotly.express as px

def sales_dashboard(df):

    fig = px.bar(
        df,
        x="Category",
        y="Purchase Amount (USD)",
        color="Gender",
        title="Customer Shopping Dashboard"
    )

    fig.show()