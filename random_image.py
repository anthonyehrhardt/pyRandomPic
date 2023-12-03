# be sure to  pip install pillow

from PIL import Image
import requests
from io import BytesIO

# Fetch the image from the URL
url = "https://picsum.photos/200/300"
response = requests.get(url)
img = Image.open(BytesIO(response.content))

# Display the image
img.show()
