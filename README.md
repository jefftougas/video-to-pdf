# Video to PDF with OCR Processing

This Python script extracts unique frames from a video, removes any watermarks from those frames, and uses Optical Character Recognition (OCR) to generate a text-searchable PDF. The intermediate images and PDFs are processed in a temporary work directory, and the final PDF is saved at the specified location.

## Prerequisites

Before you can run this project, you'll need to install the following software:

- **Python 3.7 or higher**: Make sure Python is installed and accessible in your environment.
- **FFmpeg**: Used to extract unique frames from the video. You can install FFmpeg [here](https://ffmpeg.org/download.html).
- **ImageMagick**: Used to remove watermarks from images. You can download and install it from [here](https://imagemagick.org/script/download.php).
- **Tesseract-OCR**: Used for Optical Character Recognition (OCR) to convert images into text-searchable PDFs. You can install it from [here](https://github.com/tesseract-ocr/tesseract).
- **Ghostscript**: Used to combine multiple PDFs into a single file. Install it from [here](https://www.ghostscript.com/download/gsdnld.html).

## Installation

1. Install the required Python packages:



## Usage

1. Clone this repo
2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Run the script using the following command:

```bash
./convert.py --video-path <path_to_video> --output-pdf <output_pdf_path>
```

- **`<path_to_video>`**: Path to the video file you want to process.
- **`<output_pdf_path>`**: The desired path where the final text-searchable PDF will be saved.

### Example

```bash
./convert.py --video-path ./videos/sample.mov --output-pdf ./output/final_output.pdf
```

This will perform the following steps:

1. Extract unique frames from `sample.mov`.
2. Remove watermarks from the extracted frames.
3. Perform OCR on each frame to convert the images into searchable PDF documents.
4. Combine all the individual PDFs into a single searchable PDF saved as `final_output.pdf`.

## How It Works

1. **Extract Frames**: The script uses FFmpeg to extract unique frames from the input video using the command `ffmpeg -vf mpdecimate -vsync vfr`.
2. **Remove Watermark**: The script processes each frame with ImageMagick to remove non-white watermarks.
3. **OCR Processing**: Each frame is passed through Tesseract to convert the image into a searchable PDF.
4. **Combine PDFs**: Finally, Ghostscript is used to combine all the individual PDFs into one PDF file.

## Temporary Work Directory

The script creates a temporary working directory to store intermediate image and PDF files, which is cleaned up after the final PDF is generated. This ensures no unnecessary files are left on your system after execution.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
