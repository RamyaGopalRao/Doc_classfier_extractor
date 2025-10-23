import base64

def encode_image_to_base64(file) -> str:
    with open(file.name, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

