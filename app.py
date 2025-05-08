import os
import streamlit as st
from src.Chicken_Disease_classification.pipeline.predict import PredicationPipline
import io
from PIL import Image

# Client App for saving the image path
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"  # Default image filename
        self.classifier = None            # Placeholder; set after image upload

clApp = ClientApp()  # Create global instance

# Main Streamlit app
def main():
    st.title("Check for the Chicken Coccidiosis Disease")

    # Upload image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

    if uploaded_file:
        # Convert and save the uploaded image
        image_data = uploaded_file.getvalue()
        image = Image.open(io.BytesIO(image_data))
        image.save(clApp.filename)

        # Display the uploaded image
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Prediction button
        if st.button("Disease Test Result"):
            pipeline = PredicationPipline(clApp.filename)
            result = pipeline.predict()

            if result[0]['image'] == "Healthy":
                st.success("✅ The chicken is healthy.")
            else:
                st.error("⚠️ The chicken is infected with Coccidiosis.")

        # Optional: Train model
        if st.button("Train"):
            os.system("dvc repro")
            st.success("Model retrained successfully!")

if __name__ == "__main__":
    main()