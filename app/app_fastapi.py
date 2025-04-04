from fastapi import  FastAPI

app = FastAPI()



@app.get("/video")
def extract_video_information():
    pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)