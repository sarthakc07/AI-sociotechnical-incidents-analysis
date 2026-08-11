import os
import pandas as pd


def process_oecd_data(file_path):
    # Load OECD CSV ignoring header comment lines starting with '#'
    df = pd.read_csv(file_path, comment="#")

    # Clean column names
    df.columns = df.columns.str.strip()

    # Extract Year and Month features
    df["Year"] = pd.to_datetime(df["Date"]).dt.year
    df["Month_Num"] = pd.to_datetime(df["Date"]).dt.month

    # Calculate Incident Intensity Rate (Incidents & Hazards per 1,000 AI Events)
    df["Incident_Rate_Per_1k_Events"] = (
        df["Total Incidents & Hazards"] / df["Total AI events"]
    ) * 1000

    print("=" * 60)
    print("OECD AI INCIDENTS & HAZARDS MONITOR (AIM) SUMMARY")
    print("=" * 60)
    print(
        f"Time Period Analyzed:       {df['Date'].min()} to {df['Date'].max()} ({len(df)} months)"
    )
    print(f"Total Cumulative Incidents: {df['Total Incidents & Hazards'].sum():,}")
    print(f"Total Monitored AI Events:  {df['Total AI events'].sum():,}")
    print("=" * 60)

    # Annual Breakdown Table
    yearly_summary = (
        df.groupby("Year")
        .agg(
            Total_Incidents=("Total Incidents & Hazards", "sum"),
            Total_AI_Events=("Total AI events", "sum"),
            Avg_Monthly_Incidents=("Total Incidents & Hazards", "mean"),
        )
        .reset_index()
    )

    yearly_summary["Incidents_Per_1k_Events"] = (
        yearly_summary["Total_Incidents"] / yearly_summary["Total_AI_Events"]
    ) * 1000

    print("\nANNUAL TRAJECTORY SUMMARY:")
    print(yearly_summary.to_string(index=False))

    return df, yearly_summary


if __name__ == "__main__":
    input_path = os.path.join("data", "raw", "oecd", "aim-incidents.csv")
    output_df_path = os.path.join(
        "data", "processed", "oecd_monthly_processed.csv"
    )
    output_yearly_path = os.path.join(
        "data", "processed", "oecd_yearly_summary.csv"
    )

    if os.path.exists(input_path):
        df_monthly, df_yearly = process_oecd_data(input_path)

        os.makedirs(os.path.dirname(output_df_path), exist_ok=True)
        df_monthly.to_csv(output_df_path, index=False)
        df_yearly.to_csv(output_yearly_path, index=False)

        print(f"\nProcessed datasets successfully saved to 'data/processed/'")
    else:
        print(f"Error: Could not find '{input_path}'. Check file location.")