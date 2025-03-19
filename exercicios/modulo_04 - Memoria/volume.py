import sys
from pydub import AudioSegment # type: ignore

def main(argv):
    
    # abrindo arquivo mp3
    audio = AudioSegment.from_file(argv[1], format="mp3")
    
    # definindo volume
    volume_increase = argv[3]
    audio_loud = audio + volume_increase
    
    # exportando arquivo mp3
    audio_loud.export(argv[2], format="mp3")
    


if __name__ == "__main__":
    main(sys.argv)