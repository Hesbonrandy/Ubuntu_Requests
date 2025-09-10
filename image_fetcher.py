import os
import requests
from urllib.parse import urlparse
from pathlib import Path

def fetch_image():
    print(" In the spirit of Ubuntu: 'I am because we are.'")
    print("Let’s respectfully fetch an image shared with the world.\n")

    # Prompt user for URL
    url = input("Please enter the image URL: ").strip()

    if not url:
        print("No URL provided. Exiting with respect.")
        return

    try:
        print(f"🔗 Connecting to {url}...")

        # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises HTTPError for bad responses

        # Check if content is an image
        content_type = response.headers.get('content-type', '')
        if not content_type.startswith('image/'):
            print("❌ The URL does not point to an image. Please check and try again.")
            return

        # Create directory if it doesn't exist
        directory = "Fetched_Images"
        os.makedirs(directory, exist_ok=True)

        # Extract or generate filename
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # Fallback filename if none exists
        if not filename or '.' not in filename:
            extension = content_type.split('/')[-1] or 'jpg'
            filename = f"image_{hash(url) % 10000}.{extension}"

        # Full path to save
        filepath = os.path.join(directory, filename)

        # Avoid overwriting — append number if file exists
        counter = 1
        original_filepath = filepath
        while os.path.exists(filepath):
            name, ext = os.path.splitext(original_filepath)
            filepath = f"{name}_{counter}{ext}"
            counter += 1

        # Save image in binary mode
        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"✅ Image saved successfully to: {filepath}")
        print("🙏 Thank you for sharing with the global community!")

    except requests.exceptions.MissingSchema:
        print("❌ Invalid URL format. Please include http:// or https://")
    except requests.exceptions.ConnectionError:
        print("❌ Connection failed. Please check your internet or the URL.")
    except requests.exceptions.Timeout:
        print("❌ Request timed out. The server is taking too long.")
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e}")
    except Exception as e:
        print(f"❌ Something unexpected happened: {e}")
    finally:
        print("\n✨ Done. Walked with respect through the digital community.")

if __name__ == "__main__":
    fetch_image()
    