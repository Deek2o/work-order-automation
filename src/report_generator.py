from pathlib import Path
from datetime import datetime
import pandas as pd

def generate_reports(df: pd.DataFrame, output_dir: Path) -> list[Path]:
    """Generate one timestamped Excel report per automation category."""
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    generated_files = []

    for category, group in df.groupby("Automation_Category", sort=True):
        safe_name = category.lower().replace(" ", "_")
        output_file = output_dir / f"{safe_name}_{timestamp}.xlsx"
        group.to_excel(output_file, index=False)
        generated_files.append(output_file)

    # Always produce a summary report for quick operational review.
    summary = (
        df["Automation_Category"]
        .value_counts()
        .rename_axis("Automation_Category")
        .reset_index(name="Record_Count")
    )
    summary_file = output_dir / f"summary_{timestamp}.xlsx"
    summary.to_excel(summary_file, index=False)
    generated_files.append(summary_file)

    return generated_files
