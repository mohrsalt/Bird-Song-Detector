# Import libraries
import pandas as pd
import librosa
import os
import matplotlib.pyplot as plt
import numpy as np

def save_spectrogram_from_audio(audio_file):
    """
    Generate a spectrogram image from an audio file and save it to the Images folder."
    """

    y, sr = librosa.load(audio_file, sr=16000)
    
    # Create the output path for the image
    output_image_path = audio_file.replace('Audios', 'Images').replace(".WAV", ".PNG")
    
    # Ensure the output folder exists
    os.makedirs(os.path.dirname(output_image_path), exist_ok=True)
    
    # Define the frequency range
    fmin = 1
    fmax = 16000

    fig, ax = plt.subplots(figsize=(12, 6))  # Set the background color to black
    D = librosa.amplitude_to_db(librosa.stft(y), ref=np.max)
    librosa.display.specshow(D, sr=sr, x_axis="time", y_axis="log", fmin=fmin, fmax=fmax, ax=ax)  # Specify frequency range
    ax.axis('off')  # Remove axes

    # Save the figure using the output_image_path
    fig.savefig(output_image_path, bbox_inches='tight', pad_inches=0, transparent=True)
    
    # Close the figure to release memory resources
    plt.close(fig)

    return output_image_path
