import whisper
import json
from decorators import timing_decorator

MODEL_PATHS = {
    "tiny": "models/tiny.pt",
    "base": "models/base.pt",
    "small": "models/small.pt",
    "medium": "models/medium.pt",
    "large": "models/large-v3.pt",
}


@timing_decorator
def transcribe(audio_file_path, model_size):
    model_path = MODEL_PATHS.get(model_size)
    model = whisper.load_model(model_path)
    result = model.transcribe(audio_file_path, fp16=False)

    result_json = json.dumps(result, ensure_ascii=False, indent=4)
    with open(f"{audio_file_path[:-4]}-{model_size}.json", 'w', encoding="utf8") as file:
        file.write(result_json)

    output_text = result["text"]
    with open(f"{audio_file_path[:-4]}-{model_size}.txt", 'w', encoding="utf8") as file:
        file.write(output_text)
    return result
