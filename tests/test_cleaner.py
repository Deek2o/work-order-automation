import pandas as pd
from src.cleaner import clean_work_orders

def test_clean_work_orders_removes_duplicate_and_normalizes_status():
    df = pd.DataFrame({
        "WO_Number": ["WO-001", "WO-001", "WO-002"],
        "Created_Date": ["2026-09-01", "2026-09-01", "2026-09-02"],
        "Status": [" open ", "open", "IN PROGRESS"],
        "Work_Order_Type": ["Request", "Request", "Request"],
        "Category": ["Access", "Access", "App"],
        "Assigned_Group": ["IAM", "IAM", "Apps"],
        "Product_Name": ["Identity Portal", "Identity Portal", "Portal"],
        "Description": ["Access request", "Access request", "Application issue"],
    })

    result = clean_work_orders(df)

    assert len(result) == 2
    assert result.loc[0, "Status"] == "Open"
