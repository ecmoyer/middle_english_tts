from text_to_phonemes import *
from phonemes_to_audio import *

phrase = input("Enter a Middle English phrase: ")

# Parse phrase and separate into words and phonemes
word_list = read_terminal_input(phrase)
phoneme_list = word_list_to_phonemes(word_list)

# Create list of corresponding audio files and play audio
track_list = phonemes_to_audio_files(phoneme_list)
play_phonemes(track_list)