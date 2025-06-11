from groq import Groq
import os
import base64

# Initialize client
client = Groq(api_key="YOUR_KEY_HERE")  # Replace with your actual API key

# Load and encode the image
image_path = "./YOUR_TEST_IMAGE.jpg"
with open(image_path, "rb") as img_file:
    base64_image = base64.b64encode(img_file.read()).decode("utf-8")
    image_data_url = f"data:image/jpeg;base64,{base64_image}"

# Send image in the request
completion = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Return Text from this image as json."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": image_data_url
                    }
                }
            ]
        }
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=False,
    stop=None,
)

# Print response
print(completion.choices[0].message.content)
