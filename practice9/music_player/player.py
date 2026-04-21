import pygame
import os

class MusicPlayer:
    def __init__(self, music_folder):
        pygame.mixer.init()

        self.music_folder = music_folder
        self.playlist = self.load_music()
        self.current_index = 0
        self.is_playing = False

    def load_music(self):
        files = []
        for file in os.listdir(self.music_folder):
            if file.endswith(".wav") or file.endswith(".mp3"):
                files.append(os.path.join(self.music_folder, file))
        return files

    def play(self):
        if not self.playlist:
            print("Playlist is empty")
            return

        track = self.playlist[self.current_index]
        pygame.mixer.music.load(track)  #загружает файл в плеер
        pygame.mixer.music.play()   #начинает проигрывание
        self.is_playing = True
        print(f"Playing: {os.path.basename(track)}")

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        print("Stopped")

    def next(self):
        if not self.playlist:
            return

        self.current_index = (self.current_index + 1) % len(self.playlist)  #% len(...) → зацикливание (после последнего снова первый)
        self.play()

    def previous(self):
        if not self.playlist:
            return

        self.current_index = (self.current_index - 1) % len(self.playlist) #идёт назад по списку и тоже зацикливается
        self.play()

    def get_current_track(self):
        if not self.playlist:
            return "No track"
        return os.path.basename(self.playlist[self.current_index])

    def get_position(self):  #в милисекундах
        return pygame.mixer.music.get_pos() // 1000 #возвращает время в секундах