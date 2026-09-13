import pandas as pd

CATEGORY_RULES = {
    "User Lifecycle": [
        "leaver",
        "user deletion",
        "user deactivation",
        "joiner",
        "mover",
    ],
    "Identity Management": [
        "identity",
        "access",
        "password",
        "account",
        "idm",
    ],
    "Application Support": [
        "application",
        "app support",
        "software",
        "portal",
    ],
    "Service Request": [
        "service request",
        "request",
        "standard service",
    ],
}

def _contains_any(values: list[str], keywords: list[str]) -> bool:
    text = " ".join(values).lower()
    return any(keyword in text for keyword in keywords)

def classify_work_orders(df: pd.DataFrame) -> pd.DataFrame:
    """Apply deterministic business rules and add an Automation_Category column."""
    classified = df.copy()

    def classify_row(row) -> str:
        values = [
            str(row.get("Work_Order_Type", "")),
            str(row.get("Category", "")),
            str(row.get("Assigned_Group", "")),
            str(row.get("Product_Name", "")),
            str(row.get("Description", "")),
        ]

        for category, keywords in CATEGORY_RULES.items():
            if _contains_any(values, keywords):
                return category

        return "Business as Usual"

    classified["Automation_Category"] = classified.apply(classify_row, axis=1)
    return classified
