from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from summary import summarize_text_using_percentage,summarize_text_using_no_of_sentences



app = FastAPI()

@app.get("/ping")
async def health_check():
    # You can add more checks like database, external services, etc.
    return JSONResponse(content={"status": "Ok"}, status_code=200)

@app.post("/v1/summary/percentage")
async def summary_text_using_percentage(request: Request):
    data = await request.json()  # Read JSON as dictionary
    # Define required keys
    required_keys = ["text", "percentage"]
    # Check for missing keys
    missing_keys = [key for key in required_keys if key not in data]
    if missing_keys:
        return JSONResponse(content={"error":"text and percentage keys are required"}, status_code=404)
    if data["percentage"].isdigit():
      data["percentage"]=int(data["percentage"])
    else:
        return JSONResponse(content={"error":"percentage key is always integer"}, status_code=404)
    summary=summarize_text_using_percentage(data['text'],percentage=data["percentage"])
    return JSONResponse(content={"summary":summary }, status_code=200)


@app.post("/v1/summary")
async def summary_text_using_num_sentences(request: Request):
    data = await request.json()  # Read JSON as dictionary
    # Define required keys
    required_keys = ["text", "num_sentences"]
    # Check for missing keys
    missing_keys = [key for key in required_keys if key not in data]
    if missing_keys:
        return JSONResponse(content={"error":"text and num_sentences keys are required"}, status_code=404)
    if data["num_sentences"].isdigit():
      data["num_sentences"]=int(data["num_sentences"])
    else:
        return JSONResponse(content={"error":"num_sentences key is always integer"}, status_code=404)
    summary=summarize_text_using_no_of_sentences(data['text'],num_sentences=data["num_sentences"])
    return JSONResponse(content={"summary":summary }, status_code=200)