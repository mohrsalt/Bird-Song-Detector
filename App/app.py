import gradio as gr
from file_loader import load_audio_interface
from spectrograms import spectrogram_interface
from detection import detection_interface
from classification import classification_interface

# Main App
with gr.Blocks() as app:
    gr.Markdown("# Bird Song Detector")
    
    with gr.Tab("Bird Song Detector"):
        with gr.Row():
            # Column 1: Load Files
            load_audio_interface()

            # Column 2: Generate Mel Spectrograms
            spectrogram_interface()

            # Column 3: Bird Song Detection
            detection_interface()

            # Column 4: BirdNET Classification
            classification_interface()

app.launch()
