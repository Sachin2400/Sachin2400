from PIL import Image

ASCII_CHARS = "@%#*+=-:. "

WIDTH = 120


def resize_image(image):
    width, height = image.size
    ratio = height / width
    new_height = int(WIDTH * ratio * 0.55)
    return image.resize((WIDTH, new_height))


def gray(image):
    return image.convert("L")


def pixels_to_ascii(image):
    pixels = image.getdata()

    chars = ""

    for pixel in pixels:
        chars += ASCII_CHARS[pixel * len(ASCII_CHARS) // 256]

    return chars


from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
IMAGE_PATH = BASE_DIR / "assets" / "profile-photo.png"

image = Image.open(IMAGE_PATH)

image = resize_image(image)

image = gray(image)

ascii_str = pixels_to_ascii(image)

pixel_count = len(ascii_str)

ascii_image = ""

for i in range(0, pixel_count, WIDTH):
    ascii_image += ascii_str[i:i + WIDTH] + "\n"

OUTPUT_PATH = BASE_DIR / "assets" / "ascii.txt"

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(ascii_image)

print("ASCII portrait generated!")
