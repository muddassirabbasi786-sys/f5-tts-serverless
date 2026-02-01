import runpod
import numpy as np
import soundfile as sf
import uuid

from f5_tts.infer.utils import infer_process

DEVICE = "cuda" if torch.cude.is_available() else "cpu"

print("Loading F5-TTS model...")
model = infer_process.load_model(ckpt_path=None, device=DEVICE)
print("Model Loaded")
def handler(event):
  text = event["input"].get("text","")

  if text == "":
    return {"error": "Text is required"}

wav, sr = infer_process.infer(
  text=text,
  model=model,
  device=DEVICE
)

filename = f"tmp/
{uuid.uuid4()}.wav"
sf.write(filename, audio, 24000)

return {"message": "Server works", "audiop_path": filename
       }
runpod.serverless.start({"handler": handler})
