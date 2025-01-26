import FreeSimpleGUI as sg
import zip_creator

files_label = sg.Text("Select files to compressed:")
files_input = sg.Input()
files_button = sg.FilesBrowse("Choose", key="files")


folder_label = sg.Text("Select folder destination:")
folder_input = sg.Input()
folder_button = sg.FolderBrowse("Choose", key="folder")

col1 = sg.Column([[files_label], [folder_label]])
col2 = sg.Column([[files_input], [folder_input]])
col3 = sg.Column([[files_button], [folder_button]])

compress_button = sg.Button("Compress")
exit_button = sg.Button("Exit")
output_label = sg.Text(key="output")


window = sg.Window("File Compressor", layout=[[col1, col2, col3], [compress_button, exit_button, output_label]])

while True:
    event, values = window.read()
    match event:
        case "Compress":
            filepaths = values["files"].split(";")
            folderpath = values["folder"]
            if not filepaths[0] or not folderpath:
                sg.popup("Please select files and folder before compressing.")
            else:
                zip_creator.zip_compressor(filepaths, folderpath)
                output_message = "Zip Compressed Successfully"
                window["output"].update(value=output_message)
        
        case "Exit":
            break
        
        case sg.WINDOW_CLOSED:
            break
        
window.close()