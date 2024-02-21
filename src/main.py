import argparse


def setup_cli_parser():
    parser = argparse.ArgumentParser(
        description='Creating meeting minutes based on an audio or video file')
    parser.add_argument('file_path')
    args = parser.parse_args()
    return args


def main():
    args = setup_cli_parser()


if __name__ == '__main__':
    main()
