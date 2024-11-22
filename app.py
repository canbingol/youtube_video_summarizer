import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
from fpdf import FPDF

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = """ You are a YouTube video summarizer.
Your task is to help university students study for exams by taking a video's text transcript and summarizing the most important information.
Prepare this summary in no more than 400 words, highlighting important points that might appear in the exam. Write it in a clear, understandable way that helps grasp the subject!"""

def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id, languages=['tr'])
        
        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]
        
        return transcript
        
    except TranscriptsDisabled:
        return "Cannot get transcript for this video. Subtitles might be disabled."
    except NoTranscriptFound:
        return "No transcript found in the selected language for this video. You might try an alternative video."
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt + transcript_text)
    return response.text

def create_pdf(summary_text):
    pdf = FPDF()
    pdf.add_page()
    
    font_path = os.path.join(os.path.dirname(__file__), "fonts", "FreeSerif.ttf")
    pdf.add_font("FreeSerif", '', font_path, uni=True)
    pdf.set_font("FreeSerif", size=12)
    
    pdf.multi_cell(0, 10, txt=summary_text)
    
    pdf_file = "summary.pdf"
    pdf.output(pdf_file)
    return pdf_file

def create_txt(summary_text):
    txt_file = "summary.txt"
    with open(txt_file, "w", encoding="utf-8") as f:
        f.write(summary_text)
    return txt_file

st.title("Study Notes Generator from YouTube Video")

youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", width=300, use_column_width=False)

if st.button("Get Notes"):
    transcript_text = extract_transcript_details(youtube_link)
    
    if "Cannot get transcript" in transcript_text or "An unexpected error" in transcript_text:
        st.error(transcript_text)
    else:
        summary = generate_gemini_content(transcript_text, prompt)
        st.markdown('## Detailed Notes:')
        st.write(summary)
        
        pdf_path = create_pdf(summary)
        txt_path = create_txt(summary)
        
        with open(pdf_path, "rb") as pdf_file:
            st.download_button("Download as PDF", data=pdf_file, file_name="summary.pdf", mime="application/pdf")
        
        with open(txt_path, "r", encoding="utf-8") as txt_file:
            st.download_button("Download as TXT", data=txt_file, file_name="summary.txt", mime="text/plain")
