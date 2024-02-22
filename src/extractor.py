from moviepy.editor import VideoFileClip
from decorators import timing_decorator


@timing_decorator
def convert_video_to_audio(video_file_path):
    # Открываем видео файл
    with VideoFileClip(video_file_path) as video:
        # Получаем длительность видео в секундах
        duration = video.duration
        print(f"Длительность видео: {duration} секунд")

        # Извлекаем аудио
        audio = video.audio

        audio_file_path = f"{video_file_path[:-4]}.mp3"

        # Сохраняем аудио
        audio.write_audiofile(audio_file_path)

        # Закрываем видео файл
        video.close()

    # Возвращаем путь к аудио файлу
    return audio_file_path
