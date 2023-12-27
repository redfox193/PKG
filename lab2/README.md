# Image Viewer with Information

Presented here is a straightforward Python program that leverages the Tkinter library to showcase image data and enables you to inspect chosen images from a designated directory. This utility offers the following functionalities:

- **Select a directory**: Opt for a folder housing image files (JPG, GIF, TIF, BMP, PNG, PCX).
- **Exhibit image details**: Examine essential image particulars such as name, size, dots per inch, color depth, compression, and entropy in a tabulated format.
- **Instant viewing**: A simple click on a table row triggers the display of the selected image in a distinct window.

## Prerequisites

Before commencing, make certain you have the subsequent components in place:

- Python 3.x
- Tkinter library (`tkinter`)
- Pillow library (`PIL`)

To install Pillow, execute the following command via pip:
```bash
pip install Pillow tk
```

## Usage

1. Initiate the script by running it with Python.

2. Press the "Choose Folder" button to specify a directory containing your image files.

3. The table will populate with image information, encompassing all valid images found in the chosen directory.

4. Simply click on a row within the table to open the corresponding image in a separate window.