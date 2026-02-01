FROM runpod/pytorch:2.1.0-cuda12.1-runtime-ubuntu22.04

WORKDIR /app

RUN apt update && apt install -y
\

git \
ffmpeg \
libsndfile1 \
&& rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir- -r requirements.txt

COPY . .

CMD ["python", "handler.py"]
