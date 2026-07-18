from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    # Read metadata
    filename = file.filename
    content_type = file.content_type
    
    # Read the actual contents (async)
    contents = await file.read()
    
    return {
        "filename": filename,
        "content_type": content_type,
        "file_size_bytes": len(contents)
    }
