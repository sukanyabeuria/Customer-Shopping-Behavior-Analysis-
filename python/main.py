from sqlalchemy import text

from data_cleaning import load_data, display_info
from feature_engineering import create_age_group
from visualization import sales_by_category
from eda import perform_eda
from customer_segmentation import customer_segmentation
from sales_prediction import sales_prediction
from dashboard import sales_dashboard
from database import connect_database


def line():
    print("=" * 70)


def main():

    line()
    print("🛍️ CUSTOMER SHOPPING BEHAVIOR ANALYSIS PROJECT")
    line()

    try:

        # ==========================
        # Load Dataset
        # ==========================

        dataset_path = "data/customer_shopping_behavior.csv"
        df = load_data(dataset_path)

        print("\n✅ Dataset Loaded Successfully!")

        # ==========================
        # Dataset Information
        # ==========================

        display_info(df)

        # ==========================
        # Feature Engineering
        # ==========================

        df = create_age_group(df)

        print("\n✅ Feature Engineering Completed!")

        # ==========================
        # Exploratory Data Analysis
        # ==========================

        perform_eda(df)

        # ==========================
        # Data Visualization
        # ==========================

        print("\n📊 Creating Charts...")

        sales_by_category(df)

        # ==========================
        # Machine Learning
        # ==========================

        print("\n🤖 Customer Segmentation...")

        df = customer_segmentation(df)

        print("\n📈 Sales Prediction...")

        sales_prediction(df)

        # ==========================
        # Dashboard
        # ==========================

        print("\n📊 Opening Interactive Dashboard...")

        sales_dashboard(df)

        # ==========================
        # PostgreSQL Database
        # ==========================

        print("\n🗄️ Connecting to PostgreSQL...")

        connection = connect_database()

        result = connection.execute(
            text("SELECT COUNT(*) FROM customer_shopping")
        )

        for row in result:
            print(f"\n✅ Total Rows in Database : {row[0]}")

        connection.close()

        # ==========================
        # Project Completed
        # ==========================

        line()
        print("🎉 PROJECT COMPLETED SUCCESSFULLY")
        line()

    except FileNotFoundError:

        print("\n❌ Dataset not found!")
        print("➡️ Place customer_shopping_behavior.csv inside the data folder.")

    except Exception as error:

        print("\n❌ Error:", error)


if __name__ == "__main__":
    main()