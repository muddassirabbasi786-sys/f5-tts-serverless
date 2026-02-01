import runpod
import numpy as np
import soundfile as sf
import uuid

def handler(event):
  text = event["input"].get("text","")

  if text == "":
    return {"error": "Text is required"}

#fake audio for testing

audio = np.zeros(24000)

filename = f"tmp/
{uuid.uuid4()}.wav"
sf.write(filename, audio, 24000)

return {"message": "Server works", "audiop_path": filename
       }
runpod.serverless.start({"handler": handler})
