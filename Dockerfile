FROM runpod/pytorch:2.1.0-cuda12.1-runtime-ubuntu22.04

WORKDIR /app

RUN apt update && apt install -y ffmpeg
libsndfile1

COPY requirements.txt .
RUN pip install --no-cache-dir- -r requirements.txt

COPY . .

CMD ["python", "handler.py"]
