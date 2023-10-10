import telegram
import asyncio
import logging
from PIL import Image, ImageDraw, ImageFont
import io
import os


def add_watermark(image_path, watermark_text):
    # Load the image
    image = Image.open(image_path).convert("RGBA")
    width, height = image.size

    # Create a transparent overlay image with the same size as the input image
    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))

    # Calculate the size and position of the watermark text
    watermark_font = ImageFont.truetype("arial.ttf", 1)  # Initial font size
    text_bbox = watermark_font.getbbox(watermark_text)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    target_width = int(width * 0.75) - 100  # 100 pixels for the margins
    font_size = 1
    while text_width < target_width:
        font_size += 1
        watermark_font = ImageFont.truetype("arial.ttf", font_size)
        text_bbox = watermark_font.getbbox(watermark_text)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

    # Calculate the position of the watermark text
    x = width - text_width - 50  # 50 pixels from the right edge
    y = height - text_height - 50  # 50 pixels from the bottom edge

    # Draw the watermark text on the overlay image
    draw = ImageDraw.Draw(overlay)
    draw.text((x, y), watermark_text, font=watermark_font, fill=(255, 255, 255, 128), align="right")

    # Composite the input image and the overlay image
    watermarked_image = Image.alpha_composite(image, overlay)

    # Convert the image to RGB mode
    watermarked_image = watermarked_image.convert("RGB")

    # Save the watermarked image
    watermarked_image_path = os.path.join('D:/watermarked', os.path.basename(image_path))
    watermarked_image.save(watermarked_image_path)

    return watermarked_image_path


async def send_photo_to_channel(image_path, bot_token, channel_id):
    bot = telegram.Bot(token=bot_token)

    # Load the image
    image = Image.open(image_path)

    # Compress the image
    compressed_image = io.BytesIO()
    image.save(compressed_image, format='JPEG', quality=90)
    compressed_image.seek(0)

    # Send the compressed image to the Telegram channel
    await bot.send_photo(chat_id=channel_id, photo=compressed_image)


async def process_image(image_path, watermark_text, bot_token, channel_id):
    try:
        logging.info(f"Adding watermark to image: {image_path}")
        watermarked_image_path = add_watermark(image_path, watermark_text)
        logging.info(f"Watermark added to image: {watermarked_image_path}")
        await send_photo_to_channel(watermarked_image_path, bot_token, channel_id)
        logging.info("Image uploaded to Telegram channel")
        return True
    except Exception as e:
        logging.error(f"Error processing image: {image_path}")
        logging.error(e)
        return False


async def export_images_with_watermark(directory_path, watermark_text, bot_token, channel_id):
    for filename in os.listdir(directory_path):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            image_path = os.path.join(directory_path, filename)
            await process_image(image_path, watermark_text, bot_token, channel_id)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    directory_path = 'ENTER YOUR PATH HERE'
    watermark_text = "YOUR TEXT"
    bot_token = ""
    channel_id = ""

    loop = asyncio.get_event_loop()
    loop.run_until_complete(export_images_with_watermark(directory_path, watermark_text, bot_token, channel_id))
