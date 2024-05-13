import streamlit as st


class Thermometer:

    def __init__(self, client_value, benchmark_value=50):
        self.client_value = client_value
        self.benchmark_value = benchmark_value

        # Ensure values are within a valid range
        self.min_val = max(min(client_value, benchmark_value) - 10, 0)
        self.max_val = min(max(client_value, benchmark_value) + 10, 100)

        # Normalize values to a 0-100 scale
        self.client_pos = (client_value - self.min_val) / (self.max_val - self.min_val) * 100
        self.benchmark_pos = (benchmark_value - self.min_val) / (self.max_val - self.min_val) * 100

    def display(self):
        self.html = f"""
        <style>
            .scale-container {{
                display: flex;
                flex-direction: column;
                width: 100%;
            }}
            .scale-bar {{
                height: 20px;
                background: linear-gradient(to right, red, yellow, green);
                position: relative;
            }}
            .marker {{
                position: absolute;
                top: -5px;
                width: 2px;
                height: 30px;
                background-color: black;
            }}
            .client-label {{
                position: absolute;
                top: 30px;
                left: {self.client_pos}%;
                transform: translateX(-50%);
                background-color: white;
                padding: 2px;
                color: blue;
            }}
            .benchmark-label {{
                position: absolute;
                top: 30px;
                left: {self.benchmark_pos}%;
                transform: translateX(-50%);
                background-color: white;
                padding: 2px;
            }}
        </style>
        <div class="scale-container">
            <div class="scale-bar">
                <div class="marker" style="left: {self.client_pos}% ; background-color: blue;"></div>
                <div class="marker" style="left: {self.benchmark_pos}%"></div>
                <div class="client-label">{f"Client : {self.client_value:,.2f} %"}</div>
                <div class="benchmark-label">{f"Secteur : {self.benchmark_value:,.2f} %"}</div>
            </div>
        </div>
        """

        st.markdown(self.html, unsafe_allow_html=True)

        st.markdown("***")
