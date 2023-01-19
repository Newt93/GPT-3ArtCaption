import openai_secret_manager

# Get the API key for the OpenAI service
secrets = openai_secret_manager.get_secrets("openai")
api_key = secrets["api_key"]

# Import the OpenAI library
import openai

# Set the API key
openai.api_key = api_key

# Define the image URL
image_url = "https://images.pexels.com/photos/373543/pexels-photo-373543.jpeg"

# Generate a caption for the image
response = openai.ImageCaption.create(
    prompt='Generate a caption for this image',
    image=image_url
)
caption = response["data"][0]["caption"]
print(caption)
