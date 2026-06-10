from flask import Flask, render_template
import pandas as pd
import plotly.express as px

from sklearn.linear_model import LinearRegression
import numpy as np

app = Flask(__name__)

# Load Dataset
df = pd.read_csv(
    "dataset/Sample - Superstore.csv",
    encoding="latin1"
)

# Convert Order Date
df["Order Date"] = pd.to_datetime(df["Order Date"])


@app.route("/")
def dashboard():

    # ==========================
    # KPI CARDS
    # ==========================
    total_sales = round(df["Sales"].sum(), 2)
    total_profit = round(df["Profit"].sum(), 2)
    total_orders = df["Order ID"].nunique()
    avg_discount = round(df["Discount"].mean() * 100, 2)

    # ==========================
    # SALES BY CATEGORY
    # ==========================
    category_sales = (
        df.groupby("Category")["Sales"]
        .sum()
        .reset_index()
    )

    fig1 = px.bar(
        category_sales,
        x="Category",
        y="Sales",
        title="Sales by Category",
        template="plotly_dark"
)

    fig1.update_layout(height=500)
    graph1 = fig1.to_html(
    full_html=False,
    config={"displayModeBar": False}
)

    # ==========================
    # PROFIT BY REGION
    # ==========================
    region_profit = (
        df.groupby("Region")["Profit"]
        .sum()
        .reset_index()
    )

    fig2 = px.pie(
        region_profit,
        names="Region",
        values="Profit",
        title="Profit by Region",
        template="plotly_dark"
)
    fig2.update_layout(height=500)
    graph2 = fig2.to_html(
    full_html=False,
    config={"displayModeBar": False}
)


    # ==========================
    # MONTHLY SALES TREND
    # ==========================
    monthly_sales = (
        df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
        .sum()
        .reset_index()
    )

    monthly_sales["Order Date"] = monthly_sales["Order Date"].astype(str)

    fig3 = px.line(
        monthly_sales,
        x="Order Date",
        y="Sales",
        title="Monthly Sales Trend",
        markers=True,
        template="plotly_dark"
)
    fig3.update_layout(height=500)
    graph3 = fig3.to_html(
    full_html=False,
    config={"displayModeBar": False}
)

    # ==========================
    # TOP 10 PRODUCTS
    # ==========================
    top_products = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig4 = px.bar(
        top_products,
        x="Sales",
        y="Product Name",
        orientation="h",
        title="Top 10 Products by Sales",
        template="plotly_dark"
)

    fig4.update_layout(height=600)
    graph4 = fig4.to_html(
    full_html=False,
    config={"displayModeBar": False}
)

    return render_template(
        "index.html",
        total_sales=total_sales,
        total_profit=total_profit,
        total_orders=total_orders,
        avg_discount=avg_discount,
        graph1=graph1,
        graph2=graph2,
        graph3=graph3,
        graph4=graph4
    )

@app.route("/insights")
def insights():

    category_sales = df.groupby("Category")["Sales"].sum()

    best_category = category_sales.idxmax()
    worst_category = category_sales.idxmin()

    region_profit = df.groupby("Region")["Profit"].sum()

    best_region = region_profit.idxmax()

    best_product = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .idxmax()
    )

    recommendation = (
        f"Focus on expanding {best_category} products "
        f"within the {best_region} region. "
        f"Review strategies for {worst_category} "
        f"as it generates the lowest sales."
    )

    return render_template(
        "insights.html",
        best_category=best_category,
        worst_category=worst_category,
        best_region=best_region,
        best_product=best_product,
        recommendation=recommendation
    )

@app.route("/forecast")
def forecast():

    monthly = (
        df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
        .sum()
        .reset_index()
    )

    monthly["Order Date"] = monthly["Order Date"].astype(str)

    monthly["Month"] = np.arange(len(monthly))

    X = monthly[["Month"]]
    y = monthly["Sales"]

    model = LinearRegression()
    model.fit(X, y)

    # Predict next 12 months
    future_months = np.arange(
        len(monthly),
        len(monthly) + 12
    ).reshape(-1, 1)

    future_predictions = model.predict(future_months)

    # Next month forecast
    next_month_sales = round(future_predictions[0], 2)

    current_sales = monthly["Sales"].iloc[-1]

    growth_rate = round(
        ((next_month_sales - current_sales) / current_sales) * 100,
        2
    )

    # Future dates
    last_period = pd.Period(
        monthly["Order Date"].iloc[-1],
        freq="M"
    )

    future_dates = [
        str(last_period + i)
        for i in range(1, 13)
    ]

    # Historical
    historical_df = monthly[["Order Date", "Sales"]].copy()
    historical_df["Type"] = "Actual"

    # Forecast
    forecast_df = pd.DataFrame({
        "Order Date": future_dates,
        "Sales": future_predictions,
        "Type": "Forecast"
    })

    # Combine
    chart_df = pd.concat(
        [historical_df, forecast_df],
        ignore_index=True
    )

    fig = px.line(
        chart_df,
        x="Order Date",
        y="Sales",
        color="Type",
        markers=True,
        title="Actual vs Forecast Sales (12 Months)",
        template="plotly_dark"
    )

    fig.update_layout(
        height=600,
        paper_bgcolor="#1e1e1e",
        plot_bgcolor="#1e1e1e",
        font_color="white"
    )

    forecast_graph = fig.to_html(
    full_html=False,
    config={
        "displayModeBar": False
    }
)

    return render_template(
        "forecast.html",
        forecast_value=next_month_sales,
        growth_rate=growth_rate,
        forecast_graph=forecast_graph
    )


if __name__ == "__main__":
    app.run(debug=True)