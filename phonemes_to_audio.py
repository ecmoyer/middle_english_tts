from pydub import AudioSegment
from pydub.playback import play

# Take list containing lists of phonemes, create list of audio files to be played
def phonemes_to_audio_files(phoneme_list):
    all_tracks = []
    for word in phoneme_list:
        combined_sounds = AudioSegment.empty()

        for phoneme in word:
            file_path = "phonemes/" + phoneme + ".wav"
            sound = AudioSegment.from_wav(file_path)
            combined_sounds += sound
            
        all_tracks.append(combined_sounds)

    return all_tracks

# Take list storing all audio file objects, play files
def play_phonemes(all_tracks):
    for track in all_tracks:
        play(track)
