Ubuntu Requests

Ubuntu Image Fetcher — a Python tool for mindfully collecting images from the web while following Ubuntu principles of community and responsibility.

Features

Fetch multiple image URLs at once

Validate HTTP headers (Content-Type, Content-Length) before saving

Prevent duplicate downloads using file hashing

Save images safely in a Fetched_Images/ folder

Clear error handling for connection and file issues

How to Run

Clone or download this repository.

Make sure you have Python installed.

Install the required library:
pip install requests

Run the program:
python3 ubuntu_fetcher.py

Enter one or more image URLs (comma-separated).

Example

Input:
https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png
, https://upload.wikimedia.org/wikipedia/commons/3/3f/JPEG_example_flower.jpg

Output:
✓ Successfully fetched: PNG_transparency_demonstration_1.png
✓ Image saved to Fetched_Images/PNG_transparency_demonstration_1.png

✓ Successfully fetched: JPEG_example_flower.jpg
✓ Image saved to Fetched_Images/JPEG_example_flower.jpg

“A person is a person through other persons.” – Ubuntu Philosophy 🌍
