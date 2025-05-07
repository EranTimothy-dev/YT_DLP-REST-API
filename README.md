# YouTube Video and Audio Downloader Backend

A robust backend service built with **FastAPI**, **yt-dlp**, and **FFmpeg** for downloading YouTube videos and audio. It features both REST APIs and WebSocket support for efficient and real-time data communication.

## ✨ Features

- 🎥 Download YouTube videos in multiple formats  
- 🎧 Extract audio using FFmpeg  
- ⚡ Fast and lightweight API built with FastAPI  
- 🔁 Real-time download progress via WebSockets  
- 📦 Modular and scalable architecture  

## 🛠️ Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/) - Web framework for building APIs  
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - YouTube downloader  
- [FFmpeg](https://ffmpeg.org/) - Tool for handling multimedia data  
- [WebSockets](https://fastapi.tiangolo.com/advanced/websockets/) - Real-time communication  

## 🚀 Getting Started

### Prerequisites

- Python 3.8+  
- FFmpeg installed and available in system path  

### Installation

```bash
git clone https://github.com/EranTimothy-dev/YT_VAD-Backend.git
```
```bash
cd YT_VAD-Backend
```
```bash
pip install -r requirements.txt
```
```bash
setup.sh
```

### Running the server

```bash
uvicorn app.app_fastapi:app --reload
```