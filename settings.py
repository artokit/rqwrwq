from aiogram import Bot, Dispatcher
import os

_token = '6681667923:AAHNd2vwObvWwgFqF2-hgM2W1lxcuZdDD5E'
bot = Bot(_token)
dp = Dispatcher()
IMAGE_PATH = os.path.join(os.path.dirname(__file__), 'img')
VIDEO_PATH = os.path.join(os.path.dirname(__file__), 'videos')
