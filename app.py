import streamlit as st
import pytesseract
from PIL import Image
import json

# Streamlit App
st.title("OCR and Keyword Search Application")

# File uploader widget
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# Function to perform OCR using pytesseract
def perform_tesseract_ocr(image):
    extracted_text = pytesseract.image_to_string(image, lang="hin+eng")
    return extracted_text

# If an image is uploaded
if uploaded_file is not None:
    # Open and display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Perform OCR and display extracted text
    st.write("Extracting text from the image...")
    extracted_text = perform_tesseract_ocr(image)
    
    # Display the extracted text
    st.subheader("Extracted Text")
    st.text(extracted_text)
    
    # Search functionality
    st.subheader("Keyword Search")
    keyword = st.text_input("Enter a keyword to search in the extracted text")

    if keyword:
        # Highlight keyword in the text
        st.write(f"Search results for **{keyword}**:")
        if keyword.lower() in extracted_text.lower():
            st.markdown(f"<span style='color:green'>{keyword}</span> found in the extracted text!", unsafe_allow_html=True)
        else:
            st.markdown(f"<span style='color:red'>{keyword}</span> not found in the extracted text.", unsafe_allow_html=True)
