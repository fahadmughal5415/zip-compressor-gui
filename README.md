# Zip-Compressor-GUI

## Overview
Zip-Compressor-GUI is a simple graphical user interface (GUI) application that allows users to compress multiple files into a single zip file. This tool is built using Python and the FreeSimpleGUI library.

## Features
- Select multiple files to compress.
- Choose a destination folder for the compressed zip file.
- User-friendly interface with clear instructions.
- Error handling for missing file or folder selections.

## Requirements
- Python 3.x
- FreeSimpleGUI library

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/fahadmughal5415/zip-compressor-gui.git
    ```
2. Navigate to the project directory:
    ```sh
    cd zip-compressor-gui
    ```
3. Install the required dependencies:
    ```sh
    pip install FreeSimpleGUI
    ```

## Usage
1. Run the main application:
    ```sh
    python main.py
    ```
2. In the GUI, select the files you want to compress by clicking the "Choose" button next to "Select files to compress".
3. Select the destination folder by clicking the "Choose" button next to "Select folder destination".
4. Click the "Compress" button to create the zip file in the selected destination folder.
5. A message will be displayed indicating the success of the compression process.

## Code Structure
- `main.py`: Contains the GUI implementation and handles user interactions.
- `zip_creator.py`: Contains the logic for compressing files into a zip file.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements
- [FreeSimpleGUI](https://pypi.org/project/FreeSimpleGUI/) for providing the GUI framework.
