from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from backend.chat_parser import parse_chat
from backend.keyword_analyzer import extract_keywords
from backend.summarizer import generate_summary

app = FastAPI()

@app.post("/summarize/")
async def summarize_chat(file: UploadFile = File(...)):
    content = (await file.read()).decode("utf-8")
    parsed_data = parse_chat(content)
    keywords = extract_keywords(parsed_data["all_messages"])
    summary = generate_summary(parsed_data, keywords)
    return JSONResponse(content=summary)