from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from summary import summarize_text_using_percentage, summarize_text_using_no_of_sentences,summarize_text_using_words

app = FastAPI()

@app.get("/ping")
async def health_check():
    return JSONResponse(content={"status": "Ok"}, status_code=200)

@app.post("/v1/summary/percentage")
async def summary_text_using_percentage_endpoint(request: Request):
    data = await request.json()

    required_keys = ["text", "percentage"]
    missing_keys = [key for key in required_keys if key not in data]
    if missing_keys:
        return JSONResponse(content={"error": "text and percentage keys are required"}, status_code=400)

    if not isinstance(data["percentage"], int):
        return JSONResponse(content={"error": "percentage key must be an integer"}, status_code=400)

    summary = summarize_text_using_percentage(data["text"], percentage=data["percentage"])
    return JSONResponse(content={"summary": summary}, status_code=200)

@app.post("/v1/summary/words")
async def summary_text_using_words_endpoint(request: Request):
    data = await request.json()

    required_keys = ["text", "words"]
    missing_keys = [key for key in required_keys if key not in data]
    if missing_keys:
        return JSONResponse(content={"error": "text and words keys are required"}, status_code=400)

    if not isinstance(data["words"], int):
        return JSONResponse(content={"error": "words key must be an integer"}, status_code=400)

    summary = summarize_text_using_words(data["text"], num_words=data["words"])
    return JSONResponse(content={"summary": summary}, status_code=200)

@app.post("/v1/summary")
async def summary_text_using_num_sentences_endpoint(request: Request):
    data = await request.json()

    required_keys = ["text", "num_sentences"]
    missing_keys = [key for key in required_keys if key not in data]
    if missing_keys:
        return JSONResponse(content={"error": "text and num_sentences keys are required"}, status_code=400)

    if not isinstance(data["num_sentences"], int):
        return JSONResponse(content={"error": "num_sentences key must be an integer"}, status_code=400)

    summary = summarize_text_using_no_of_sentences(data["text"], num_sentences=data["num_sentences"])
    return JSONResponse(content={"summary": summary}, status_code=200)
