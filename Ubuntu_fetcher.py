import requests
import os
from urllib.parse import urlparse
import hashlib

def is_safe_image(response):
    """
    Check HTTP headers before saving.
    Ensures file is an image and not too large (5MB limit).
    """
    content_type = response.headers.get("Content-Type", "")
    if not content_type.startswith("image/"):
        print("✗ Not an image. Skipping download.")
        return False
    
    content_length = response.headers.get("Content-Length")
    if content_length and int(content_length) > 5_000_000:  # 5 MB limit
        print("✗ File too large. Skipping download.")
        return False
    
    return True

def generate_file_hash(content):
    """
    Prevent duplicate downloads by hashing the image content.
    """
    return hashlib.md5(content).hexdigest()

def fetch_image(url, saved_hashes):
    try:
        # Fetch image from the web
        response = requests.get(url, timeout=10, stream=True)
        response.raise_for_status()
        
        # Check HTTP headers for safety
        if not is_safe_image(response):
            return
        
        # Read image content
        content = response.content
        file_hash = generate_file_hash(content)
        
        # Prevent duplicate images
        if file_hash in saved_hashes:
            print("✗ Duplicate image detected. Skipping download.")
            return
        saved_hashes.add(file_hash)
        
        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename:
            filename = "downloaded_image.jpg"
        
        # Save image in Fetched_Images directory
        filepath = os.path.join("Fetched_Images", filename)
        with open(filepath, "wb") as f:
            f.write(content)
        
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
    
    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Handle multiple URLs
    urls = input("Please enter one or more image URLs (comma-separated): ").split(",")
    urls = [u.strip() for u in urls if u.strip()]
    
    # Ensure directory exists
    os.makedirs("Fetched_Images", exist_ok=True)
    saved_hashes = set()
    
    # Process each URL
    for url in urls:
        print(f"\nFetching: {url}")
        fetch_image(url, saved_hashes)
    
    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
