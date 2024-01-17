# OCR Image Conversion Tool

This FastAPI-based tool performs Optical Character Recognition (OCR) on images, allowing conversion to text or PDF.

## Features

- **Img2Text**: Reads text from an uploaded image.
- **Img2pdf**: Converts an image to a PDF with the extracted text.

## Prerequisites

Before running the project, make sure you have the following installed on your system:

- [Python](https://www.python.org/) (version 3.6 or higher)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [uvicorn](https://www.uvicorn.org/)

## Installation

1. Download Tesseract OCR for Windows from [https://community.chocolatey.org/packages/tesseract-ocr#files](https://community.chocolatey.org/packages/tesseract-ocr#files). Choose the `tesseract-ocr-w64-setup` package.

2. Install Tesseract OCR by following the installation instructions provided on the [download page](https://community.chocolatey.org/packages/tesseract-ocr#files).

3. Add Tesseract to your system PATH:
   - Open the Control Panel.
   - Click on "System and Security."
   - Click on "System."
   - Click on "Advanced system settings" on the left.
   - Click on the "Environment Variables" button.
   - Under "System variables," find and select the "Path" variable, then click on "Edit."
   - Click on "New" and add the path to the Tesseract installation directory (usually `C:\Program Files\Tesseract-OCR`).

4. Open a terminal and navigate to the project directory.

5. Create a virtual environment (optional but recommended):

    ```
    python -m venv venv
    ```

6. Activate the virtual environment:

   - On Windows:

     ```
     .\venv\Scripts\activate
     ```

   - On Linux/macOS:

     ```
     source venv/bin/activate
     ```

7. Install the required Python packages:

    ```
    pip install -r requirements.txt
    ```

## Run the Application

Once the installation is complete, you can run the FastAPI application using the following command:

```
uvicorn main:app --reload
 ```

## Usage
Follow the API documentation to interact with the OCR endpoint and extract text from images.

## License
This project is licensed under the MIT License. Feel free to use and modify as needed.
