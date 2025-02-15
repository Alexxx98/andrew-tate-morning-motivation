from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

import pygame
import os
import random
import keyboard
import pytz


pygame.mixer.init()

CURRENT_DIR = os.getcwd()
AUDIO_DIR = os.path.join(os.getcwd(), 'motivational-speeches')


def playaudio():
    audio_file = os.listdir(AUDIO_DIR)[random.randint(0, len(os.listdir(AUDIO_DIR)) - 1)]
    pygame.mixer.music.load(os.path.join(AUDIO_DIR, audio_file))
    pygame.mixer.music.play()

def main():
    timezone = pytz.timezone('Europe/Warsaw')
    scheduler = BackgroundScheduler(timezone=timezone)
    scheduler.add_job(
        func=playaudio,
        trigger=CronTrigger(day_of_week='mon-sat', hour=10, minute=5),
    )

    running = True
    scheduler.start()
    while running:
        if keyboard.is_pressed('p') and pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()


if __name__ == '__main__':
    main()
