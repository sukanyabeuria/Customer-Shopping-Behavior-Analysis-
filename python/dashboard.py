import plotly.express as px
import plotly.graph_objects as go


def sales_dashboard(df):
    """
    Professional Interactive Dashboard
    """

    print("\n🚀 Launching Professional Dashboard...")

    # -----------------------------
    # Sales by Category
    # -----------------------------
    category_sales = (
        df.groupby("Category")["Purchase Amount (USD)"]
        .sum()
        .reset_index()
    )

    fig1 = px.bar(
        category_sales,
        x="Category",
        y="Purchase Amount (USD)",
        color="Purchase Amount (USD)",
        color_continuous_scale="Plasma",
        text="Purchase Amount (USD)",
        title="🛍 Sales by Category"
    )

    fig1.update_layout(
        template="plotly_dark",
        title_font_size=24,
        title_x=0.5,
        paper_bgcolor="#111111",
        plot_bgcolor="#111111",
        font=dict(color="white")
    )

    fig1.update_traces(
        texttemplate="$%{text:.0f}",
        textposition="outside"
    )

    fig1.show()

    # -----------------------------
    # Gender Distribution
    # -----------------------------
    gender_sales = (
        df.groupby("Gender")["Purchase Amount (USD)"]
        .sum()
        .reset_index()
    )

    fig2 = px.pie(
        gender_sales,
        names="Gender",
        values="Purchase Amount (USD)",
        hole=0.55,
        color_discrete_sequence=[
            "#ff4da6",
            "#8a2be2"
        ],
        title="👨‍🦰 Sales by Gender"
    )

    fig2.update_layout(
        template="plotly_dark",
        title_font_size=24,
        title_x=0.5,
        paper_bgcolor="#111111",
        font=dict(color="white")
    )

    fig2.show()

    # -----------------------------
    # Age vs Purchase
    # -----------------------------
    fig3 = px.scatter(
        df,
        x="Age",
        y="Purchase Amount (USD)",
        color="Category",
        size="Purchase Amount (USD)",
        hover_data=["Payment Method", "Location"],
        color_discrete_sequence=px.colors.qualitative.Bold,
        title="📈 Age vs Purchase Amount"
    )

    fig3.update_layout(
        template="plotly_dark",
        title_font_size=24,
        title_x=0.5,
        paper_bgcolor="#111111",
        plot_bgcolor="#111111",
        font=dict(color="white")
    )

    fig3.show()

    # -----------------------------
    # KPI Dashboard
    # -----------------------------
    total_sales = df["Purchase Amount (USD)"].sum()
    total_customers = len(df)
    average_purchase = df["Purchase Amount (USD)"].mean()
    average_rating = df["Review Rating"].mean()

    fig4 = go.Figure()

    fig4.add_trace(go.Indicator(
        mode="number",
        value=total_sales,
        title={"text": "💰 Total Revenue"},
        domain={'x': [0, 0.25], 'y': [0, 1]}
    ))

    fig4.add_trace(go.Indicator(
        mode="number",
        value=total_customers,
        title={"text": "👥 Customers"},
        domain={'x': [0.25, 0.5], 'y': [0, 1]}
    ))

    fig4.add_trace(go.Indicator(
        mode="number",
        value=average_purchase,
        title={"text": "🛒 Avg Purchase"},
        domain={'x': [0.5, 0.75], 'y': [0, 1]}
    ))

    fig4.add_trace(go.Indicator(
        mode="number",
        value=average_rating,
        title={"text": "⭐ Avg Rating"},
        domain={'x': [0.75, 1], 'y': [0, 1]}
    ))

    fig4.update_layout(
        template="plotly_dark",
        paper_bgcolor="#111111",
        height=250,
        title="📊 Dashboard Overview",
        title_font_size=24,
        title_x=0.5
    )

    fig4.show()

    print("\n✨ Professional Dashboard Loaded Successfully!")