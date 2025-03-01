import requests
import io
from PIL import Image
import os

token = os.environ["HFTOKEN"]

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
HEADERS = {"Authorization": f"Bearer {token}"}

def generate_image(prompt):
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        image = Image.open(io.BytesIO(response.content))
        image.save("generated_image.png")  # Save to file
        image.show()  # Open the image
    else:
        print("Error:", response.json())

prompt = "A futuristic city at sunset, cyberpunk style"
generate_image(prompt)
