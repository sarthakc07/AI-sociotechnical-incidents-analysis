import ast
import os
import matplotlib.pyplot as plt
import pandas as pd


def analyze_dataset(file_path):
    df = pd.read_csv(file_path)
    total_records = len(df)

    human_count = 0
    tech_count = 0
    org_count = 0
    multi_tag_count = 0

    for _, row in df.iterrows():
        try:
            tags = ast.literal_eval(row["hto_tags"])

            has_human = len(tags.get("human", [])) > 0
            has_tech = len(tags.get("technology", [])) > 0
            has_org = len(tags.get("organization", [])) > 0

            if has_human:
                human_count += 1
            if has_tech:
                tech_count += 1
            if has_org:
                org_count += 1

            if sum([has_human, has_tech, has_org]) > 1:
                multi_tag_count += 1

        except Exception:
            continue

    human_pct = (human_count / total_records) * 100
    tech_pct = (tech_count / total_records) * 100
    org_pct = (org_count / total_records) * 100
    multi_pct = (multi_tag_count / total_records) * 100

    print("=" * 50)
    print("EMPIRICAL ANALYSIS: AI INCIDENT HTO DISTRIBUTION")
    print("=" * 50)
    print(f"Total Incidents Analyzed: {total_records}")
    print(
        f"Human Friction / Trust Breakdown: {human_count} ({human_pct:.1f}%)"
    )
    print(
        f"Technical Deficit / Reliability:  {tech_count} ({tech_pct:.1f}%)"
    )
    print(
        f"Organizational / Governance:      {org_count} ({org_pct:.1f}%)"
    )
    print(
        f"Cross-Dimensional Overlap:       {multi_tag_count} ({multi_pct:.1f}%)"
    )
    print("=" * 50)

    # Plot Distribution (Including Cross-Dimensional Overlap)
    categories = [
        "Human Oversight /\nTrust Breakdown",
        "System Reliability /\nTechnical Deficit",
        "Governance /\nOrganizational Deficit",
        "Cross-Dimensional\nOverlap",
    ]
    counts = [human_count, tech_count, org_count, multi_tag_count]
    colors = ["#2b5c8f", "#d95f02", "#7570b3", "#e7298a"]

    plt.figure(figsize=(11, 6))
    bars = plt.bar(categories, counts, color=colors, width=0.55)

    plt.title(
        f"Socio-Technical Breakdown of AI Incidents (N={total_records})",
        fontsize=13,
        pad=15,
        fontweight="bold",
    )
    plt.ylabel("Incident Count", fontsize=11)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Add count and percentage labels above bars
    for bar in bars:
        height = bar.get_height()
        pct = (height / total_records) * 100
        plt.text(
            bar.get_x() + bar.get_width() / 2.0,
            height + 25,
            f"{height}\n({pct:.1f}%)",
            ha="center",
            va="bottom",
            fontsize=9.5,
            fontweight="bold",
        )

    # Adjust vertical Y-axis limit to prevent label clipping
    plt.ylim(0, max(counts) * 1.18)
    plt.tight_layout()

    output_img_path = os.path.join(
        "data", "processed", "hto_distribution_chart.png"
    )
    plt.savefig(output_img_path, dpi=300)
    print(f"Distribution plot successfully saved to {output_img_path}")
    plt.show()


if __name__ == "__main__":
    csv_input = os.path.join("data", "processed", "ai_incidents_tagged.csv")
    if os.path.exists(csv_input):
        analyze_dataset(csv_input)
    else:
        print(f"Error: {csv_input} not found.")