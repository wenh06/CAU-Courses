import argparse
import os
from typing import Union

from pdf2image import convert_from_path
from PIL import Image


def convert_pdf_to_image(
    pdf_path: Union[str, bytes, os.PathLike], output_folder: Union[str, bytes, os.PathLike], combine_pages: bool = False
) -> None:
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    pages = convert_from_path(pdf_path)

    if len(pages) == 0:
        print("No pages found in the PDF")
        return

    if combine_pages:
        images = []
        for page in pages:
            images.append(page)

        mean_width = sum(img.width for img in images) // len(images)
        total_height = sum([int(img.height * (mean_width / img.width)) for img in images])

        # Combine images vertically
        combined_image = Image.new("RGB", (mean_width, total_height))
        y_offset = 0
        for img in images:
            # Resize the image to the mean width
            scale = mean_width / img.width
            img = img.resize((mean_width, int(img.height * scale)))
            combined_image.paste(img, (0, y_offset))
            y_offset += img.height

        combined_image.save(f"{output_folder}/combined_image.png", "PNG")
    else:
        for i, page in enumerate(pages):
            page.save(f"{output_folder}/page_{i+1}.png", "PNG")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert PDF to PNG images")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("-o", "--output-folder", help="Folder to save images")
    parser.add_argument("-c", "--combine-pages", action="store_true", help="Combine all pages into one image")

    args = parser.parse_args()

    if args.output_folder is None:
        pdf_dir, pdf_filename = os.path.split(args.pdf_path)
        output_folder = os.path.join(pdf_dir, os.path.splitext(pdf_filename)[0])
    else:
        output_folder = args.output_folder

    convert_pdf_to_image(args.pdf_path, output_folder, args.combine_pages)
