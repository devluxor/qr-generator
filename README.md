# QR Code Generator

This is a simple Python program for generating QR codes using the `qrcode` library. Users can customize the size, padding, and colors of the QR code and save it as an image file.

## Features

- Accepts user input to encode in the QR code.
- Allows customization of QR code size, padding, and colors.
- Saves the QR code image in PNG format.
- Provides default configurations for ease of use.

## Prerequisites

- Python 3.x installed.
- `qrcode` library installed.
- `Pillow` library installed.

### Install Required Library

```bash
pip install qrcode Pillow
```

## Usage

1. Clone this repository or download the script.
2. Run the script using the following command:

```bash
python main.py
```

3. Enter the text you want to encode in the QR code when prompted.
4. The QR code image will be saved as `sample.png` in the same directory.

## Configuration

You can modify the following default settings in the code:

- **Size**: Controls the size of each box in the QR code grid. Default is `30`.
- **Padding**: Sets the border thickness around the QR code. Default is `2`.
- **Foreground Color**: The color of the QR code itself. Default is `#000` (black).
- **Background Color**: The color of the QR code background. Default is `#FFF` (white).

Example to change default configurations:

```python
DEFAULT_SIZE = 40
DEFAULT_PADDING = 4
DEFAULT_FG_COLOR = '#FF0000'  # Red
DEFAULT_BG_COLOR = '#00FF00'  # Green
```

## Error Handling

The program includes error handling for common issues such as:

- Invalid input data.
- File I/O errors when saving the QR code image.

## Example Output

After running the script, a sample QR code image will be created in the directory with the name `sample.png`.
