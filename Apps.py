import streamlit as st
from src.pipeline.prediction_pipeline import CustomData, PredictPipeline

st.set_page_config(page_title="Diamond Price Predictor", layout="centered")

class DiamondPriceApp:
    def __init__(self):
        self.title = "Diamond Price Prediction"
        self.label_info = "Please enter the diamond features below:"

    def user_input_form(self):
        st.title(self.title)
        with st.form("diamond_form"):
            st.subheader(self.label_info)

            carat = st.number_input("Carat", step=0.01)
            depth = st.number_input("Depth", step=0.1)
            table = st.number_input("Table", step=0.1)
            x = st.number_input("Length (x)", step=0.01)
            y = st.number_input("Width (y)", step=0.01)
            z = st.number_input("Depth (z)", step=0.01)

            cut = st.text_input("Cut")
            color = st.text_input("Color")
            clarity = st.text_input("Clarity")

            submitted = st.form_submit_button("Predict")

        return submitted, carat, depth, table, x, y, z, cut, color, clarity

    def predict(self, carat, depth, table, x, y, z, cut, color, clarity):
        try:
            data = CustomData(
                carat=carat,
                depth=depth,
                table=table,
                x=x,
                y=y,
                z=z,
                cut=cut,
                color=color,
                clarity=clarity
            )
            df = data.get_data_as_dataframe()
            pipeline = PredictPipeline()
            prediction = pipeline.predict(df)
            return round(prediction[0], 2)

        except Exception as e:
            st.error(f" Error during prediction: {e}")
            return None

    def run(self):
        submitted, carat, depth, table, x, y, z, cut, color, clarity = self.user_input_form()

        if submitted:
            result = self.predict(carat, depth, table, x, y, z, cut, color, clarity)
            if result is not None:
                st.success(f"Predicted Diamond Price: **${result}**")


if __name__ == "__main__":
    app = DiamondPriceApp()
    app.run()
