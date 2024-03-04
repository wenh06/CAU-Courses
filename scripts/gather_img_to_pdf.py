import argparse
import os
from pathlib import Path
from typing import List

from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def resize_image(image_path: str, output_path: str) -> None:
    """
    Resize the image to fit A4 size and save it.
    """
    img = Image.open(image_path)
    img.thumbnail(A4)
    img.save(output_path, "PNG")


def create_pdf(folder_path: str, output_file: str, extensions: List[str]) -> None:
    """
    Create a PDF file containing resized images from the folder.
    """
    image_files = sorted([file for file in os.listdir(folder_path) if file.lower().endswith(tuple(extensions))])
    c = canvas.Canvas(output_file, pagesize=A4)

    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        resized_image_path = os.path.join(folder_path, "resized_" + image_file)
        resize_image(image_path, resized_image_path)
        c.drawImage(resized_image_path, 0, 0, A4[0], A4[1])
        c.showPage()

    c.save()
    print(f"PDF file '{output_file}' created successfully!")

    # remove resized images
    for image_file in image_files:
        resized_image_path = os.path.join(folder_path, "resized_" + image_file)
        os.remove(resized_image_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a PDF file from images in a folder")
    parser.add_argument("folder", help="Path to the folder containing images")
    parser.add_argument("--output", help="Name of the output PDF file", default=None)
    parser.add_argument(
        "--extensions", nargs="+", default=[".png", ".jpg", ".jpeg"], help="List of image file extensions to include"
    )
    args = parser.parse_args()

    folder_path = args.folder
    output_file = args.output
    if output_file is None:
        # if output file name is not provided, use the folder name
        output_file = os.path.join(folder_path, Path(folder_path).expanduser().resolve().name + ".pdf")
    extensions = args.extensions

    create_pdf(folder_path, output_file, extensions)
