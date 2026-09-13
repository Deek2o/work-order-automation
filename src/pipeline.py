import argparse
from pathlib import Path

from .cleaner import clean_work_orders
from .config import PipelineConfig
from .reader import read_work_orders
from .classifier import classify_work_orders
from .report_generator import generate_reports

def run_pipeline(config: PipelineConfig):
    raw = read_work_orders(config.input_file)
    cleaned = clean_work_orders(raw)
    classified = classify_work_orders(cleaned)
    generated = generate_reports(classified, config.output_dir)

    print(f"Input records: {len(raw)}")
    print(f"Records after cleaning: {len(cleaned)}")
    print(f"Reports generated: {len(generated)}")
    for path in generated:
        print(f"  - {path}")

def main():
    parser = argparse.ArgumentParser(description="Work Order Automation Pipeline")
    parser.add_argument("--input", required=True, help="Path to XLSX or CSV input")
    parser.add_argument("--output", default="output", help="Output directory")
    args = parser.parse_args()

    config = PipelineConfig.from_values(args.input, args.output)
    run_pipeline(config)

if __name__ == "__main__":
    main()
