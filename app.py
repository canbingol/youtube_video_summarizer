import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
from fpdf import FPDF

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = """ Sen bir YouTube video özetleyicisisin.
Görevin, üniversite öğrencilerinin sınav çalışmalarına yardımcı olmak için bir videonun metin transkriptini alıp en önemli bilgileri özetlemektir.
Bu özeti 250 kelimeyi geçmeyecek şekilde, sınavda çıkabilecek önemli maddeleri vurgulayarak hazırla. Açık, anlaşılır ve konuyu kavramaya yardımcı olacak şekilde yaz!"""

def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id, languages=['tr'])
        
        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]
        
        return transcript   
             
    except TranscriptsDisabled:
        return "Bu video için transkript alınamıyor. Videonun altyazıları devre dışı bırakılmış olabilir."
    except NoTranscriptFound:
        return "Bu video için seçilen dilde transkript bulunamadı. Alternatif bir video deneyebilirsiniz."
    except Exception as e:
        return f"Beklenmeyen bir hata oluştu: {str(e)}"

def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt + transcript_text)
    return response.text

def create_pdf(summary):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, summary)
    pdf_file = "summary.pdf"
    pdf.output(pdf_file)
    return pdf_file

def create_txt(summary):
    txt_file = "summary.txt"
    with open(txt_file, "w", encoding="utf-8") as file:
        file.write(summary)
    return txt_file

st.title("YouTube Videosundan Sınav Notları Oluşturucu")

youtube_link = st.text_input("YouTube Video Bağlantısını Girin:")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", width=300, use_column_width=False)

if st.button("Notları Al"):
    transcript_text = extract_transcript_details(youtube_link)
    
    if "Bu video için" in transcript_text or "Beklenmeyen bir hata" in transcript_text:
        st.error(transcript_text)
    else:
        summary = generate_gemini_content(transcript_text, prompt)
        st.markdown('## Detaylı Notlar:')
        st.write(summary)
        
        pdf_path = create_pdf(summary)
        txt_path = create_txt(summary)
        
        with open(pdf_path, "rb") as pdf_file:
            st.download_button("PDF Olarak İndir", data=pdf_file, file_name="summary.pdf", mime="application/pdf")
        
        with open(txt_path, "r", encoding="utf-8") as txt_file:
            st.download_button("TXT Olarak İndir", data=txt_file, file_name="summary.txt", mime="text/plain")
