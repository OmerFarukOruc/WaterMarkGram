# WaterMarkGram
This script adds watermarks to images and shares them on Telegram. It's easy to use, accepts a directory path, and processes images by adding customizable watermarks. The watermarked images are then uploaded to a Telegram channel using a Telegram bot. Protect and brand your images effortlessly.

# Image Watermarking and Telegram Upload Script

This script adds a watermark to images and sends them to a Telegram channel. It is useful for adding branding or attribution to images before sharing them on social media or other platforms.

## Features

- Adds a customizable watermark to images
- Positions the watermark at the bottom right corner of the image
- Supports popular image formats such as PNG and JPEG
- Compresses the images before uploading to Telegram for faster transmission
- Provides logging statements for tracking the progress and any errors that occur during the process

## Prerequisites

- Python 3.6 or higher
- Python Imaging Library (PIL)
- python-telegram-bot library

## Installation

1. Clone the repository:

git clone https://github.com/OmerFarukOruc/WaterMarkGram.git


2. Install the required dependencies:

pip install pillow python-telegram-bot


## Usage

1. Replace the placeholder values in the script with your actual values:
   - `directory_path`: The path to the directory containing the images to be processed.
   - `watermark_text`: The text to be used as the watermark.
   - `bot_token`: Your Telegram bot token.
   - `channel_id`: The ID of the Telegram channel where you want to upload the watermarked images.

2. Run the script:

python watermark_and_upload.py


3. The script will process all the images in the specified directory, add the watermark, and upload the watermarked images to the Telegram channel.

## Customization

- Watermark Position: By default, the watermark is positioned at the bottom right corner of the image. If you want to change the position, you can modify the `add_watermark` function in the script.
- Watermark Style: The script uses the Arial font for the watermark text. If you want to use a different font or customize the style further, you can modify the `add_watermark` function in the script.

## License

This project is licensed under the [MIT License](LICENSE).
Feel free to customize the README file further to include any additional information or instructions specific to your use case.
