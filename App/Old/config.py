# config.py

CURRENT_VERSION = "v1.6"  # Replace with your current app version
GITHUB_REPO = "GrunCrow/BirdNET-PredictionsValidator-App"  # Replace with your GitHub repo
SUGGESTED_SPECIES_FILE = "suggested_species.txt"  # File to store suggested species

class Globals:
    _root_dir_audio_files = ""
    _audio_file_list = []
    _current_row_index = -1
    
    @classmethod
    def set_root_dir_audio_files(cls, value):
        cls._root_dir_audio_files = value

    @classmethod
    def get_root_dir_audio_files(cls):
        return cls._root_dir_audio_files
    
    @classmethod
    def set_audio_file_list(cls, value):
        cls._audio_file_list = value

    @classmethod
    def get_audio_file_list(cls):
        return cls._audio_file_list
    
    @classmethod
    def set_current_row_index(cls, value):
        cls._current_row_index = value

    @classmethod
    def get_current_row_index(cls):
        return cls._current_row_index
