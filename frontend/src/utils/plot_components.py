""" This module contains utility functions for the frontend. """

import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go


def plot_ratio(data, date, benchmark, title, ylabel, comment, ratio_type="line"):
    """Plot a financial ratio and display relevant metrics."""
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        fig, axis = plt.subplots()
        if ratio_type == "line":
            axis.plot(date, data, label="Client")
            axis.plot(date, benchmark, label="Benchmark", linestyle="--")
        elif ratio_type == "bar":
            axis.bar(date, data, label="Client")
        axis.set_title(title)
        axis.set_ylabel(ylabel)
        axis.legend()
        st.pyplot(fig)

    with col2:
        current_value = data.iloc[-1]
        previous_year_value = data.iloc[-2]  # Assuming yearly data
        variation = (current_value - previous_year_value) / previous_year_value * 100
        st.metric(title, f"${current_value:,.0f}", f"{variation:.2f}%")

    with col3:
        if st.button("Analyse", key=title):
            st.info(comment)


def plot_kpi(figure: go.Figure, key_analyse: str, comment: str):
    """Plot a KPI."""
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(figure)
    with col2:
        if st.button("Analyse", key=key_analyse):
            st.info(comment)


def plot_metrics(data, key_analyse, comment):
    """Plot a metric"""
    col1, col2 = st.columns(2)
    fake_benchmark = 100
    col1.metric(
        key_analyse,
        f"${data:,.0f}",
        f"${fake_benchmark - data:,.0f}",
    )
    with col2:
        if st.button("Analyse", key=key_analyse):
            st.info(comment)


def plot_gauge(value, title, range_min, range_max, threshold, good_above=True):
    """Plot a thermometer gauge with gradient coloring based on value and threshold"""
    # Calculate color based on value relative to threshold
    if good_above and value >= threshold:
        # Calculate how far above the threshold and adjust green intensity
        relative_value = (value - threshold) / (range_max - threshold)
        color = (
            f"rgb({255 * (1 - relative_value)}, {255}, {100 * (1 - relative_value)})"
        )
    elif not good_above and value <= threshold:
        # Calculate how far below the threshold and adjust green intensity
        relative_value = (threshold - value) / (threshold - range_min)
        color = (
            f"rgb({255 * (1 - relative_value)}, {255}, {100 * (1 - relative_value)})"
        )
    elif good_above:
        # Calculate how far below the threshold and adjust red intensity
        relative_value = (threshold - value) / (threshold - range_min)
        color = (
            f"rgb({255}, {255 * (1 - relative_value)}, {100 * (1 - relative_value)})"
        )
    else:
        # Calculate how far above the threshold and adjust red intensity
        relative_value = (value - threshold) / (range_max - threshold)
        color = (
            f"rgb({255}, {255 * (1 - relative_value)}, {100 * (1 - relative_value)})"
        )

    # Configure the gauge
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=value,
            domain={"x": [0, 1], "y": [0, 1]},
            title={"text": title},
            gauge={
                "axis": {
                    "range": [range_min, range_max],
                    "tickwidth": 1,
                    "tickcolor": "darkblue",
                },
                "bar": {"color": color},
                "steps": [
                    {"range": [range_min, threshold], "color": "lightgrey"},
                    {"range": [threshold, range_max], "color": "lightgrey"},
                ],
                "threshold": {
                    "line": {"color": "black", "width": 4},
                    "thickness": 0.75,
                    "value": threshold,
                },
            },
        )
    )

    fig.update_layout(height=400)
    return fig




def plot_hist(value, title, threshold):
    """Plot a vertical histogram with bars for value and threshold"""
    # Configure bar colors and names
    color_value = "#299ADC"
    color_threshold = "#1E70AA"
    name_value = "Client"
    name_threshold = "Secteur"

    # Configure the histogram
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=[name_value, name_threshold],
            y=[value, threshold],
            marker_color=[color_value, color_threshold],
            text=[f"{round(value, 2)}", f"{round(threshold, 2)}"],
            textposition="auto",
            width=0.3
        )
    )

    fig.update_layout(
        title=title,
        yaxis=dict(title="Valeur"),
        bargap=0.2,
        height=300,
        width=300
    )

    return fig