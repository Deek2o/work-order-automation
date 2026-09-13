import pandas as pd
from src.classifier import classify_work_orders

def test_classification_rules():
    df = pd.DataFrame({
        "Work_Order_Type": ["Request", "Request", "Incident", "Request", "Task"],
        "Category": ["User Deletion", "Access", "Application", "Service Request", "General"],
        "Assigned_Group": ["IAM", "IAM", "Apps", "Service Desk", "Operations"],
        "Product_Name": ["Identity", "Identity", "Portal", "Standard Service", "Monitoring"],
        "Description": ["Leaver account", "Access change", "Application issue",
                        "New request", "Routine operational task"],
    })

    result = classify_work_orders(df)

    assert result["Automation_Category"].tolist() == [
        "User Lifecycle",
        "Identity Management",
        "Application Support",
        "Service Request",
        "Business as Usual",
    ]
