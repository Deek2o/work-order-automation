from pathlib import Path
import pandas as pd

REQUIRED_COLUMNS = {
    "WO_Number",
    "Created_Date",
    "Status",
    "Work_Order_Type",
    "Category",
    "Assigned_Group",
    "Product_Name",
    "Description",
}

def read_work_orders(file_path: Path) -> pd.DataFrame:
    """Read an XLSX or CSV work-order report and validate its schema."""
    if not file_path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    suffix = file_path.suffix.lower()
    if suffix in {".xlsx", ".xls"}:
        df = pd.read_excel(file_path)
    elif suffix == ".csv":
        df = pd.read_csv(file_path)
    else:
        raise ValueError("Supported input formats are .xlsx, .xls and .csv")

    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    return df
