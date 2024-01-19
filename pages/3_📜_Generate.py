from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import streamlit as st
import openai
import os
from PyPDF2 import PdfReader
from dotenv import load_dotenv
from io import BytesIO

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_summary(content):
    try:# Use OpenAI to generate a summary of the content
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=content,
            max_tokens=400,
            temperature=0.5
        )
        summary = response["choices"][0]["text"].strip()
        return summary
    except Exception as e:
        print(f"Error generating summary: {e}")
        return None


def generate_pdf(topic, content):
    try:
        description = generate_summary(content)

        if description is None:
            print("PDF generation failed. No description available.")
            return None
        
        # Create a PDF document
        pdf_buffer = BytesIO()
        pdf = canvas.Canvas(pdf_buffer, pagesize=letter)
        
        # Set metadata
        pdf.setTitle(topic)

        font_name = "Helvetica"
        font_size = 16  # Adjust as needed
        pdf.setFont(font_name, font_size)

        page_width, page_height = letter

        # Calculate width and height of the text box
        text_width = pdf.stringWidth(content, font_name, font_size)

        font = pdf._fontname

        # Calculate center position
        center_x = (page_width - text_width) / 2
        center_y = (page_height - font_size) / 2

        # Add content to the PDF at the center
        pdf.drawString(center_x, center_y, content)

                
        description_start_y = center_y - 20  # Adjust as needed for spacing
        pdf.drawString(100, description_start_y, "Detailed Description:")
        pdf.drawString(100, description_start_y - 20, description)

        
        # Save the PDF to the buffer
        pdf.save()
        
        # Move the buffer's cursor to the beginning
        pdf_buffer.seek(0)
        
        print("PDF generation complete.")
        return pdf_buffer
    
    except Exception as e:
        print(f"Error generating PDF: {e}")
        raise


def extract_text_from_pdf(pdf_buffer):
    # Extract text from the generated PDF
    pdf_reader = PdfReader(pdf_buffer)
    text = ""
    for page_num in range(pdf_reader.pages):
        text += pdf_reader.pages[page_num].extractText()
    return text



st.title("PDF Generator App")

# User input for the topic
topic = st.text_input("Enter the topic for the PDF:")

# User input for the content
content = st.text_area("Enter the content for the PDF:")

generate_pdf_button = st.button("Generate PDF")



if generate_pdf_button and topic and content:
    generated_pdf = generate_pdf(topic, content)
    generated_text=extract_text_from_pdf(generated_pdf)

    st.download_button(
        label="Download Generated PDF",
        key="download_generated_pdf",
        data=generated_pdf.read(),
        mime="application/pdf",
        on_click=None,
        help="Click to download the generated PDF"
    )
    st.success("pdf generated")
elif generate_pdf_button:
    st.warning("Please enter both topic and content before generating PDF.")
