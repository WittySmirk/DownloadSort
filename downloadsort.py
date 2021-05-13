from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
from os import path
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            extension = os.path.splitext(filename)
            if extension[1] == '.txt' or extension[1] == '.docx':
                new_destination = text_destination + "/" + filename
            elif extension[1] == '.png' or extension[1] == '.jpg':
                new_destination = picture_destination + "/" + filename
            elif extension[1] == '.mp4' or extension[1] == '.mkv':
                new_destination = video_destination + "/" + filename
            elif extension[1] == '.mp3':
                new_destination = music_destination + "/" + filename
            else:
                new_destination = default_destination + "/" + filename
            os.rename(src, new_destination)

if path.exists("settings.txt"):
    print("Sorting Downloads...")
    lines = []

    with open('settings.txt') as f:
        lines = f.readlines()
    count = 0
    for line in lines:
        count += 1
        if count == 1:
            folder_to_track = line.rstrip()
            default_destination = line.rstrip()
        elif count == 2:
            text_destination = line.rstrip()
        elif count == 3:
            picture_destination = line.rstrip()
        elif count == 4:
            video_destination = line.rstrip()
        elif count == 5:
            music_destination = line.rstrip()
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_to_track, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

else:
    fh = open("settings.txt", "w")
    print("We need to configure the application, just answer with directories to the specified folder. Ex: C:/users/wyatt/Documents")
    d = input("What is the path for downloads?")
    fh.write(d + "\n")
    do = input("What is the path for documents?")
    fh.write(do + "\n")
    p = input("What is the path for pictures?")
    fh.write(p + "\n")
    v = input("What is the path for videos?")
    fh.write(v + "\n")
    m = input("What is the path for music?")
    fh.write(m)
    print("Thank you! Now all you have to do is restart the program and you're set!")
