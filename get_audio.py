import os
import sys
import yt_dlp


CURRENT_DIR = os.getcwd()
OUTPUT_DIR = os.path.join(CURRENT_DIR, 'motivational-speeches')
FFMPEG_DIR = os.path.join(CURRENT_DIR, 'ffmpeg/ffmpeg.exe')


def main():
    n = len(os.listdir(OUTPUT_DIR)) + 1
    output_file = os.path.join(OUTPUT_DIR, f'motivational-speech{n}')

    yt_options = {
        'outtmpl': output_file,
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'ffmpeg_location': FFMPEG_DIR
    }

    ydl = yt_dlp.YoutubeDL(yt_options)

    if len(sys.argv) != 2:
        raise IndexError('Wrong number of arguments')
    
    url = sys.argv[1]
    ydl.download(url)


if __name__ == '__main__':
    main()
