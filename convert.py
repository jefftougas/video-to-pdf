import os
import subprocess
from PIL import Image
import pytesseract

def extract_frames(video_path, output_pattern):
    """Extract unique frames from a video using ffmpeg."""
    ffmpeg_command = f'ffmpeg -i "{video_path}" -vf "mpdecimate" -vsync vfr {output_pattern}'
    subprocess.run(ffmpeg_command, shell=True)
    print("Frames extracted successfully.")

def remove_watermark(image_path):
    """Remove non-white watermark background using ImageMagick."""
    convert_command = f'mogrify -fill white -fuzz 20% -draw "color 0,0 floodfill" "{image_path}"'
    subprocess.run(convert_command, shell=True)
    print(f"Processed {image_path} to remove watermark.")

def ocr_image_to_pdf(image_path, pdf_path):
    """Convert an image to a PDF with OCR using Tesseract."""
    img = Image.open(image_path)
    ocr_pdf = pytesseract.image_to_pdf_or_hocr(img, extension='pdf')
    with open(pdf_path, 'wb') as f:
        f.write(ocr_pdf)
    print(f"OCR completed for {image_path}, saved as {pdf_path}.")

def combine_pdfs(pdf_list, output_pdf):
    """Combine multiple PDFs into a single PDF using Ghostscript."""
    gs_command = f'gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile="{output_pdf}" {" ".join(pdf_list)}'
    subprocess.run(gs_command, shell=True)
    print(f"Combined all PDFs into {output_pdf}.")

def process_video_to_pdf(video_path, output_pdf):
    """Main function to process video and create a text-searchable PDF."""
    output_pattern = "output_image_%03d.png"
    extract_frames(video_path, output_pattern)
    
    image_files = sorted([f for f in os.listdir('.') if f.startswith('output_image_') and f.endswith('.png')])
    pdf_files = []
    
    for image_file in image_files:
        remove_watermark(image_file)
        pdf_file = image_file.replace('.png', '_ocr.pdf')
        ocr_image_to_pdf(image_file, pdf_file)
        pdf_files.append(pdf_file)
    
    combine_pdfs(pdf_files, output_pdf)
    
    # Clean up intermediate files
    for image_file in image_files:
        os.remove(image_file)
    for pdf_file in pdf_files:
        os.remove(pdf_file)
    
    print(f"Processing complete. Final PDF saved as {output_pdf}.")

# Replace these with your input video path and desired output PDF path
video_path = "input.mov"
output_pdf = "output.pdf"

process_video_to_pdf(video_path, output_pdf)

