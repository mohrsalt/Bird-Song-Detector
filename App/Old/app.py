# app.py

# Web App
from tkinter import Tk, filedialog
import gradio as gr

# Data processing
import pandas as pd

import os

from audio_processing import load_audio_files_from_folder, update_audio_and_image, list_audio_files_from_folder, extract_time_from_filename, extract_date_from_filename
from species_management import add_suggested_species, get_suggested_species, initialize_suggested_species_file
from data_processing import save_table_to_csv, update_table_with_validation
from ui_components import build_footer, tutorial_tab, on_audio_selected, update_validation, get_sample_audio_and_image

# Global variables
from config import Globals

def on_browse(data_type):
    root = Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    if data_type == "Files":
        filenames = filedialog.askopenfilenames()
        if filenames:
            # Extraer tiempo de audio
            Globals.set_audio_file_list(pd.DataFrame([
                {"Idx": idx + 1, "Specie": f.split(os.sep)[-2], "File": os.path.basename(f), "Validation": -100, "Suggested Specie": " ", "Path": f}
                for idx, f in enumerate(filenames)
            ]))
            Globals.set_root_dir_audio_files(os.path.dirname(filenames[0]))
            root.destroy()
            return Globals.get_audio_file_list().to_string(index=False), Globals.get_audio_file_list()
        else:
            root.destroy()
            return "Files not selected", pd.DataFrame()
    elif data_type == "Folder":
        folder_path = filedialog.askdirectory()
        if folder_path:
            folder_path = os.path.normpath(folder_path)
            with gr.Blocks() as progress:
                gr.Markdown("Loading audio files, please wait...")
                filenames = load_audio_files_from_folder(folder_path)  # Usando caché
            Globals.set_audio_file_list(pd.DataFrame([
                {"Idx": idx+1,"Specie": f.split(os.sep)[-2], "File": os.path.basename(f), "Validation": -100, "Suggested Specie": " ", "Path": f}
                for idx, f in enumerate(filenames)
            ]))
            Globals.set_root_dir_audio_files(folder_path)
            root.destroy()
            return Globals.get_audio_file_list().to_string(index=False), Globals.get_audio_file_list()
        else:
            root.destroy()
            return "Folder not selected", pd.DataFrame()
    else:
        root.destroy()
        return "Please select an upload option", pd.DataFrame()

def on_browse_sample_audio_folder():

    root = Tk()
    root.attributes("-topmost", True)
    root.withdraw()

    folder = filedialog.askdirectory()
    if folder:
        Globals.set_sample_audio_dir(os.path.normpath(folder))
        # print("New sample audio folder selected:", sample_audio_dir)
        root.destroy()
    else:
        root.destroy()

# Use a gr.Dataframe or gr.Dynamic for audio file selection
audio_file_table = gr.Dataframe()

# Function to get the list of sample files
def get_sample_files():
    # return sorted if audio fie .WAV, .wav, .MP3, .mp3
    specie_audio_dir = Globals.get_sample_audio_dir() + os.sep + Globals.get_current_specie_name()
    sample_audio_files = list_audio_files_from_folder(specie_audio_dir)
    return sample_audio_files

def main():
    """
    This function sets up the main user interface for the Label Audios App.
    It creates various UI elements such as audio and image components, data tables, and buttons.
    The function also defines event handlers for user interactions with the UI elements.
    
    Returns:
        gr.Blocks: The main UI component.
    """

    audio_file_table = gr.Dataframe(headers=["Idx", "File", "Specie", "Suggested Specie"], type="pandas", interactive=False)

    with gr.Blocks() as demo:
        with gr.Tab("Bird Song Detector + BirdNET Classifier"):
            gr.Markdown("## Load Audio Files")
            data_type = gr.Radio(choices=["Files", "Folder"], value="Folder", label="Upload Audio Files")
            input_path = gr.Textbox(label="Path of audios", scale=3, interactive=False)
            browse_btn = gr.Button("Browse", min_width=1)
            browse_btn.click(on_browse, inputs=data_type, outputs=[input_path, audio_file_table])
        # with gr.Tab("Validate BirdNET predictions"):
            with gr.Row():
                with gr.Column():
                    gr.Markdown("## Audio Files")
                    audio_file_table.render()
                with gr.Column():
                    gr.Markdown("## Detector")

                with gr.Column():
                    gr.Markdown("## Classifier")
                    # Add folder selection button
                    browse_samplefolder_btn = gr.Button("Select Sample Audio Folder", min_width=1)
                    browse_samplefolder_btn.click(on_browse_sample_audio_folder, inputs=[], outputs=[])

                    # Add observations box to write
                    # gr.Textbox(label="Observations", type="text", placeholder="Write your observations here...", scale=3)
        with gr.Tab("More Information"):
            tutorial_tab()

        with gr.Row():
            # Build and display the footer
            build_footer()

            # GitHub Issues Link
            gr.Markdown("""
                <div style="text-align: center;">
                    <a href="https://github.com/GrunCrow/BirdNET-PredictionsValidator-App/issues" target="_blank" style="display: inline-flex; align-items: center; text-decoration: none; color: inherit;">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" alt="GitHub" width="30" height="30" style="vertical-align: middle; margin-right: 8px;">
                        <span>To report issues or provide feedback, please visit the GitHub repository</span>
                    </a>
                </div>
                """)

    return demo

demo = main()
# launch in port 7864
demo.launch(inbrowser=True, inline=True, show_api=False)