🌍 Ubuntu Image Fetcher
“I am because we are.” — Ubuntu Philosophy 

A respectful, community-minded Python script that fetches images from the web and saves them locally — honoring the spirit of Ubuntu: connection, sharing, and graceful coexistence in the digital world.

✨ Features
Prompts user for an image URL
Creates a local folder Fetched_Images (if it doesn’t exist)
Downloads and saves the image with an appropriate filename
Avoids overwriting existing files by appending numbers
Gracefully handles errors (no crashes!)
Validates that the URL actually returns an image
Respects servers with timeout and proper HTTP error handling
🧰 Requirements
Python 3.6+
requests library
Install dependencies:
1 pip install requests
▶️ How to Use
Clone or download this repository.
Open your terminal in the project folder.
Run the script:
bash
1 python image_fetcher.py
Enter an image URL when prompted (e.g., https://picsum.photos/200/300).
The image will be saved in the Fetched_Images folder.
✅ Example Output:

🌍 In the spirit of Ubuntu: 'I am because we are.'
Let’s respectfully fetch an image shared with the world.

Please enter the image URL: https://picsum.photos/200/300
🔗 Connecting to https://picsum.photos/200/300...
✅ Image saved successfully to: Fetched_Images/300
🙏 Thank you for sharing with the global community!

🛠️ Code Highlights
Uses requests.get() with timeout and error handling
Checks Content-Type header to ensure it’s an image
Uses os.makedirs(..., exist_ok=True) to safely create directories
Generates fallback filenames using content type and URL hash
Avoids filename collisions by appending _1, _2, etc.
💡 Example URLs to Try
https://source.unsplash.com/random/400x300
https://picsum.photos/500/500.jpg
https://images.pexels.com/photos/356378/pexels-photo-356378.jpeg (if allowed by server)
⚠️ Some sites block automated downloads — always respect robots.txt and terms of service. 












