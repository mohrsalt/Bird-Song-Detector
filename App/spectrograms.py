import os
import librosa
import librosa.display
import matplotlib.pyplot as plt
from utils import Globals

def create_spectrogram(audio_file):
    y, sr = librosa.load(audio_file, sr=None)
    output_image_path = audio_file.replace('Audios', 'Images').replace(".wav", ".png")
    os.makedirs(os.path.dirname(output_image_path), exist_ok=True)

    fmin, fmax = 1, 16000
    fig, ax = plt.subplots(figsize=(12, 6))
    D = librosa.amplitude_to_db(librosa.stft(y), ref=np.max)
    librosa.display.specshow(D, sr=sr, x_axis="time", y_axis="log", fmin=fmin, fmax=fmax, ax=ax)
    ax.axis('off')
    fig.savefig(output_image_path, bbox_inches='tight', pad_inches=0, transparent=True)
    plt.close(fig)
    return output_image_path

def generate_spectrograms():
    audio_files = Globals.audio_files
    if audio_files is not None:
        spectrogram_paths = [create_spectrogram(row["Path"]) for _, row in audio_files.iterrows()]
        return "Spectrograms generated", spectrogram_paths
    else:
        return "No audio files loaded"

def spectrogram_interface():
    with gr.Column():
        gr.Markdown("## Generate Mel Spectrograms")
        generate_button = gr.Button("Generate")
        download_button = gr.Button("Download Mel Spectrograms")
        status = gr.Textbox(label="Status", lines=1)
        
        generate_button.click(fn=generate_spectrograms, outputs=status)
        # Note: Implement download logic for spectrograms
