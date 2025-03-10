import os
import gradio as gr
from tkinter import Tk, filedialog
from utils import Globals, segment_audio

def load_audio(data_type):
    root = Tk()
    root.attributes("-topmost", True)
    root.withdraw()

    if data_type == "Files":
        filenames = filedialog.askopenfilenames(filetypes=[("Audio Files", "*.wav")])
        if filenames:
            file_list = pd.DataFrame([
                {"Idx": idx + 1, "File": os.path.basename(f), "Path": f}
                for idx, f in enumerate(filenames)
            ])
            Globals.audio_files = file_list
            Globals.root_audio_dir = os.path.dirname(filenames[0])
            root.destroy()
            return file_list.to_dict(orient="records")
    elif data_type == "Folder":
        folder_path = filedialog.askdirectory()
        if folder_path:
            folder_path = os.path.normpath(folder_path)
            audio_files = segment_audio(folder_path)
            Globals.audio_files = audio_files
            Globals.root_audio_dir = folder_path
            root.destroy()
            return audio_files.to_dict(orient="records")
    else:
        root.destroy()
        return "Invalid selection"

def load_audio_interface():
    with gr.Column():
        gr.Markdown("## Load Audio Files")
        load_choice = gr.Radio(["Files", "Folder"], label="Select input type")
        browse_button = gr.Button("Browse")
        audio_table = gr.DataFrame(headers=["Idx", "File", "Path"], datatype=["number", "str", "str"])
        
        browse_button.click(fn=load_audio, inputs=load_choice, outputs=audio_table)
