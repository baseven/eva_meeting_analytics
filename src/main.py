import argparse
from extractor import convert_video_to_audio
from transcriber import transcribe


def setup_cli_parser():
    parser = argparse.ArgumentParser(
        description='Creating meeting minutes based on an audio or video file')
    parser.add_argument('file_path')
    parser.add_argument('-ms', "--model_size", help='Model size', default='small')
    args = parser.parse_args()
    return args


def main():
    args = setup_cli_parser()
    audio_file_path = convert_video_to_audio(args.file_path)
    text = transcribe(audio_file_path=audio_file_path, model_size=args.model_size)


if __name__ == '__main__':
    main()
