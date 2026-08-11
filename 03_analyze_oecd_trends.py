import os
import matplotlib.pyplot as plt
import pandas as pd


def generate_oecd_visualizations(csv_path):
    df = pd.read_csv(csv_path)

    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Plot monthly incident counts and 6-month moving average
    ax1.plot(
        df["Date"],
        df["Total Incidents & Hazards"],
        color="#2b5c8f",
        linewidth=1.8,
        label="Monthly Incidents & Hazards",
    )
    ax1.plot(
        df["Date"],
        df["6-month moving average"],
        color="#d95f02",
        linewidth=2.2,
        linestyle="--",
        label="6-Month Moving Average",
    )

    ax1.set_title(
        "OECD Global AI Incidents & Hazards Longitudinal Trajectory (2020–2026)",
        fontsize=13,
        fontweight="bold",
        pad=15,
    )
    ax1.set_xlabel("Timeline (Year-Month)", fontsize=11)
    ax1.set_ylabel("Monthly Incident & Hazard Count", fontsize=11)

    # Display every 6th month on the x-axis for clean formatting
    tick_indices = range(0, len(df), 6)
    ax1.set_xticks([df["Date"].iloc[i] for i in tick_indices])
    ax1.set_xticklabels(
        [df["Date"].iloc[i] for i in tick_indices], rotation=45
    )

    ax1.grid(True, linestyle="--", alpha=0.5)
    ax1.legend(loc="upper left", frameon=True)

    plt.tight_layout()

    output_img_path = os.path.join(
        "data", "processed", "oecd_longitudinal_trends.png"
    )
    plt.savefig(output_img_path, dpi=300)
    print(f"Longitudinal trend chart saved to {output_img_path}")
    plt.show()


if __name__ == "__main__":
    monthly_csv = os.path.join(
        "data", "processed", "oecd_monthly_processed.csv"
    )
    if os.path.exists(monthly_csv):
        generate_oecd_visualizations(monthly_csv)
    else:
        print(
            f"Error: Processed data not found. Run 02_parse_and_code_oecd.py first."
        )