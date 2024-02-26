import pytube

url = input('enter video url:')

on_progress
path = ''

pytube.YouTube(url).streams.get_highest_resolution().download(path)