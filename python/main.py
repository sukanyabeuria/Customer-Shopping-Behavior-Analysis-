from data_cleaning import load_data, display_info
from feature_engineering import create_age_group
from visualization import sales_by_category
from eda import sales_by_gender
from customer_segmentation import customer_segmentation
from sales_prediction import sales_prediction
from dashboard import sales_dashboard
from database import connect_database

def main():
    connection = connect_database
    
    print("=" * 60)
    print(" CUSTOMER SHOPPING BEHAVIOR ANALYSIS PROJECT ")
    print("=" * 60)

    try:
        # Load Dataset
        dataset_path = "data/customer_shopping_behavior.csv"
        df = load_data(dataset_path)

        print("\n✅ Dataset Loaded Successfully!")

        # Dataset Information
        display_info(df)

        # Feature Engineering
        df = create_age_group(df)
        print("\n✅ Feature Engineering Completed!")

        # Data Visualization
        print("\n📊 Creating Charts...")
        sales_by_gender(df)
        sales_by_category(df)

        # Machine Learning
        print("\n🤖 Customer Segmentation...")
        df = customer_segmentation(df)

        print("\n📈 Sales Prediction...")
        model = sales_prediction(df)

        # Dashboard
        print("\n📊 Opening Interactive Dashboard...")
        sales_dashboard(df)

        # Database
        print("\n🗄 Connecting to PostgreSQL...")
        connect_database()

        print("\n" + "=" * 60)
        print(" PROJECT COMPLETED SUCCESSFULLY ")
        print("=" * 60)

    except FileNotFoundError:
        print("\n❌ Dataset not found!")
        print("Place customer_shopping_behavior.csv inside the data folder.")

    except Exception as error:
        print("\n❌ Error:", error)


if __name__ == "__main__":
    main()