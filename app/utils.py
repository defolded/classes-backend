# # utils.py
# import pdfplumber

# def scrape_transcript(pdf_path: str):
#     with pdfplumber.open(pdf_path) as pdf:
#         text = ""
#         for page in pdf.pages:
#             text += page.extract_text()
#     # Further processing of text to extract course information
#     return parsed_data
