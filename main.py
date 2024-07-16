import icon
import replicate
import streamlit as st
import requests
import zipfile
import io
from streamlit_image_select import image_select

st.set_page_config(
    page_title="Knight Image Generation",
    page_icon="ai-generated-8084555_1280.png"
)
st.markdown("# :rainbow[Text to Image Ai Studio]")

REPLICATE_API_TOKEN = st.secrets["r8_8OkB1Mm6nUhpHkjrADspP1WCjy3dcGV4FP8sh"]
REPLICATE_MODEL_ENDPOINTSTABILITY = st.secrets["REPLICATE_MODEL_ENDPOINTSTABILITY"]

replicate_text="Stability AI SDXL model on Model"
replicate_link="https://replicate.com/stability-ai/sdxl"
replicate_logo="https://storage.googleapis.com/llama2_release/Screen%20Shot%202023-07-21%20at%2012.34.05%20PM.png"