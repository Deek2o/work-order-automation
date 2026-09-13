import pandas as pd

def clean_work_orders(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and normalize raw work-order records."""
    cleaned = df.copy()

    # Remove completely empty rows and duplicate work orders.
    cleaned = cleaned.dropna(how="all")
    cleaned = cleaned.drop_duplicates(subset=["WO_Number"], keep="first")

    # Normalize text fields.
    text_columns = cleaned.select_dtypes(include=["object", "string"]).columns
    for column in text_columns:
        cleaned[column] = cleaned[column].fillna("").astype(str).str.strip()

    # Normalize dates where present.
    if "Created_Date" in cleaned.columns:
        cleaned["Created_Date"] = pd.to_datetime(
            cleaned["Created_Date"], errors="coerce"
        )

    # Standardize common status values.
    if "Status" in cleaned.columns:
        cleaned["Status"] = (
            cleaned["Status"].str.replace(r"\s+", " ", regex=True).str.title()
        )

    return cleaned.reset_index(drop=True)
