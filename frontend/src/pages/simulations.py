import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def monte_carlo_simulation(
    investissement=100,
    operating_costs=100,
    revenue_growth=8.0,
    years=5,
    n_simulations=100,
):
    base_revenue = 2656
    expected_roi = 0.2  # Assuming an average expected ROI of 20%

    revenue_paths = np.zeros((years, n_simulations))

    for i in range(n_simulations):
        annual_revenue = base_revenue
        current_investment = investissement
        current_operating_costs = operating_costs

        for year in range(years):
            # Simulate ROI for the current year
            current_roi = np.random.normal(
                loc=expected_roi, scale=0.05
            )  # 5% standard deviation

            # Simulate yearly investment change and operating cost fluctuations
            current_investment += current_investment * np.random.uniform(-0.01, 0.02)
            current_operating_costs += current_operating_costs * np.random.normal(
                0, 0.05
            )  # 5% std dev

            # Simulate yearly revenue growth
            growth_rate = np.random.normal(
                loc=revenue_growth, scale=2
            )  # Standard deviation of 2%

            # Calculate revenue growth factoring in ROI
            growth_factor = 1 + growth_rate / 100
            investment_return = current_investment * current_roi
            cost_factor = current_operating_costs / annual_revenue

            # Apply the net effect of growth, investment return, and costs on revenue
            annual_revenue = (
                annual_revenue * growth_factor
                + investment_return
                - current_operating_costs
            )

            revenue_paths[year, i] = annual_revenue

    return revenue_paths


def visualize_simulation(revenue_paths, years=5):
    # Creating the figure and axis objects
    fig, (ax1, ax2) = plt.subplots(
        1, 2, gridspec_kw={"width_ratios": [3, 1]}, figsize=(6, 3)
    )

    # Plotting all simulation paths with high transparency
    for i in range(revenue_paths.shape[1]):
        ax1.plot(revenue_paths[:, i], lw=0.5, alpha=0.2, color="gray")

    # Calculate and plot the quartile paths
    median_path = np.median(revenue_paths, axis=1)
    first_quartile_path = np.percentile(revenue_paths, 25, axis=1)
    third_quartile_path = np.percentile(revenue_paths, 75, axis=1)

    # Plot quartile paths
    ax1.plot(median_path, lw=2, alpha=0.8, color="black", label="Chemin Median")
    ax1.plot(
        first_quartile_path,
        lw=1.5,
        alpha=0.7,
        color="blue",
        linestyle="--",
        label="1er Quartile",
    )
    ax1.plot(
        third_quartile_path,
        lw=1.5,
        alpha=0.7,
        color="green",
        linestyle="--",
        label="3eme Quartile",
    )

    ax1.set_title("Simulation du Chiffre d'Affaires sur 5 ans", fontsize=6)
    ax1.set_xlabel("Années", fontsize=5)
    ax1.set_ylabel("Chiffre d'Affaires (en K€)", fontsize=5)
    ax1.tick_params(axis="both", labelsize=5)
    ax1.legend(fontsize=5)

    # Plot histogram of final year revenues with modifications
    n, bins, patches = ax2.hist(
        revenue_paths[-1, :],
        bins=30,
        orientation="horizontal",
        alpha=0.2,  # Light transparency
        color="gray",
    )
    median_final_year = np.median(revenue_paths[-1, :])
    first_quartile_final_year = np.percentile(revenue_paths[-1, :], 25)
    third_quartile_final_year = np.percentile(revenue_paths[-1, :], 75)

    # Mark quartile values on the histogram
    ax2.axhline(median_final_year, color="black", linewidth=2, label="Median")
    ax2.set_xlim(right=ax2.get_xlim()[1] + 5)  # Extend x-axis to make room for text
    ax2.text(
        ax2.get_xlim()[1] + 1,
        median_final_year,
        f"{median_final_year:.2f} K€",
        verticalalignment="center",
        fontsize=4,
    )

    ax2.axhline(
        first_quartile_final_year,
        color="blue",
        linestyle="--",
        linewidth=2,
        label="1st Quartile",
    )
    ax2.axhline(
        third_quartile_final_year,
        color="green",
        linestyle="--",
        linewidth=2,
        label="3rd Quartile",
    )

    ax2.set_title(f"Distribution du Chiffre d'Affaires sur {years} ans", fontsize=6)
    ax2.set_xlabel("Fréquence", fontsize=5)
    ax2.tick_params(axis="both", labelsize=5)
    ax2.legend(fontsize=5)

    ax2.set_ylim(ax1.get_ylim())

    plt.tight_layout()
    st.pyplot(fig)

    # Calculate annual growth rates of the median path
    median_growth_rates = (median_path[1:] - median_path[:-1]) / median_path[:-1] * 100
    median_average_growth_rate = np.mean(median_growth_rates)

    # Calculate annual growth rates of the median path
    first_quartile_growth_rates = (
        (first_quartile_path[1:] - first_quartile_path[:-1])
        / first_quartile_path[:-1]
        * 100
    )
    first_quartile_average_growth_rate = np.mean(first_quartile_growth_rates)

    # Calculate annual growth rates of the median path
    third_quartile_growth_rates = (
        (third_quartile_path[1:] - third_quartile_path[:-1])
        / third_quartile_path[:-1]
        * 100
    )
    third_quartile_average_growth_rate = np.mean(third_quartile_growth_rates)

    col1, col2, col3 = st.columns(3)
    # Display the metric in Streamlit
    col1.metric(
        label="Taux de Croissance Annuel Moyen du Chiffre d'Affaires 1er Quartile",
        value=f"{first_quartile_average_growth_rate:.2f} %",
    )
    col2.metric(
        label="Taux de Croissance Annuel Moyen du Chiffre d'Affaires Médian",
        value=f"{median_average_growth_rate:.2f} %",
    )
    col3.metric(
        label="Taux de Croissance Annuel Moyen du Chiffre d'Affaires 3eme Quartile",
        value=f"{third_quartile_average_growth_rate:.2f} %",
    )


def display_simulation():
    # Inputs
    investissement = st.slider(
        "Investissements (en K€ / an)",
        min_value=0.0,
        max_value=1000.0,
        value=30.0,
        step=10.0,
    )

    # Button to run the simulation
    if st.button("Lancer la Simulation"):
        revenue_paths = monte_carlo_simulation(investissement, years=5)
        with st.expander("Afficher les données de la simulation", expanded=True):
            visualize_simulation(revenue_paths, years=5)
