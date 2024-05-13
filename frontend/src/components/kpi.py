""" This module contains functions to display financial KPIs as gauges. """

import streamlit as st
from src.utils.plot_components import plot_gauge, plot_metrics, plot_hist


class KPI:
    def __init__(
        self,
        name=None,
        type_graph=None,
        value=None,
        benchmark=1,
        good_above=True,
        score_pertinence=0,
    ):
        self.name = name
        self.type_graph = type_graph
        self.value = value
        self.benchmark = benchmark
        self.good_above = good_above
        self.score_pertinence = score_pertinence

    def display(self):
        if self.type_graph == "gauge":
            figure = plot_gauge(self.value, self.name, 0, 5, self.benchmark, self.good_above)
            st.plotly_chart(figure)

        elif self.type_graph == "hist":
            figure = plot_hist(self.value, self.name, self.benchmark)
            st.plotly_chart(figure)

