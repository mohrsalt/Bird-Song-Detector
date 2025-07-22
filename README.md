Please follow these to run the inference for one audio file

conda env create -f birdsongenv.yml
python3 /home/FYP/mohor001/Bird-Song-Detector/Code/predict_on_audio.py

Note-:
Please remember to change the model path and audio path in predict_on_audio.py. 
To find all the locations to change, just do Ctrl+f to search "mohor001" and replace those strings with your local paths
The model checkpoint best.pt is inside Bird-Song-Detector/Models/Bird Song Detector/weights directory. 
Audio examples as wav files are inside Bird-Song-Detector/Data/Audios directory.
