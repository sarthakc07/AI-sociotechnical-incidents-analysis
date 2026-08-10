import glob
import os
import re
import pandas as pd


def classify_hto_dimension(text):
    text_lower = str(text).lower()
    tags = {"human": [], "technology": [], "organization": []}

    # Human friction heuristics
    if re.search(
        r"(trust|operator error|bias|training|misuse|over-reliance|user|human|worker|staff)",
        text_lower,
    ):
        tags["human"].append("Human Oversight / Trust Breakdown")

    # Technology friction heuristics
    if re.search(
        r"(hallucination|data leak|inaccuracy|model error|vulnerability|glitch|bug|accuracy|fail|failure|system)",
        text_lower,
    ):
        tags["technology"].append("System Reliability / Technical Deficit")

    # Organization friction heuristics
    if re.search(
        r"(policy|compliance|gdpr|regulation|silo|unauthorized|shadow|law|legal|management|company|corporate)",
        text_lower,
    ):
        tags["organization"].append("Governance / Organizational Deficit")

    return tags


def process_excel_dataset(file_path):
    df_raw = pd.read_excel(file_path)
    print(f"Loaded {len(df_raw)} raw records from {file_path}.")
    print(f"Detected columns: {list(df_raw.columns[:10])}")

    processed = []
    for idx, row in df_raw.iterrows():
        # Combine text from all non-numeric text columns longer than 15 characters
        text_snippets = []
        for col in df_raw.columns:
            val = str(row[col])
            if len(val) > 15 and not val.isdigit():
                text_snippets.append(val)

        combined_text = " ".join(text_snippets)
        hto_tags = classify_hto_dimension(combined_text)

        processed.append({
            "incident_id": idx + 1,
            "title": str(row.get("Title", f"Incident_{idx+1}")),
            "hto_tags": str(hto_tags),
            "raw_text_snippet": combined_text[:300],
        })

    return pd.DataFrame(processed)


if __name__ == "__main__":
    raw_dir = os.path.join("data", "raw")
    output_file = os.path.join("data", "processed", "ai_incidents_tagged.csv")

    excel_files = glob.glob(os.path.join(raw_dir, "*.xlsx"))

    if excel_files:
        input_file = excel_files[0]
        print(f"Found Excel file: {input_file}")

        df_tagged = process_excel_dataset(input_file)

        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        df_tagged.to_csv(output_file, index=False)
        print(f"Dataset processing complete! Saved to {output_file}")
    else:
        print(
            f"Error: No .xlsx file found in '{os.path.abspath(raw_dir)}'. "
            f"Ensure your Excel file is placed in data/raw."
        )