import zipfile
import pathlib

def zip_compressor(filepaths, dest_dir):
    dest_dir = pathlib.Path(dest_dir, "compressor.zip")
    with zipfile.ZipFile(dest_dir, "w") as file:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            file.write(filepath, arcname=filepath.name)

if __name__ == "__main__":
    filepaths = ["main.py", "zip_creator.py"]  # Corrected filepaths list
    zip_compressor(filepaths, "files")