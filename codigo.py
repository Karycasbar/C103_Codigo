import sys
import random
import time
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/Nala1/Downloads"

#Clase event handler
class FileMovementHandler(FileSystemEventHandler):
    #Codigo para manejar el evento de creación de un archivo de directorio
    def on_created(self, event):
        print(event)


#Inicia la clase event
event_handler = FileMovementHandler()

#Inicializa Observer
observer = Observer()

#Programa observer
observer.schedule(event_handler, from_dir, recursive=True)

#Inicia Onserver
observer.start()

while True:
    time.sleep(2)
    print("ejecutando...")
