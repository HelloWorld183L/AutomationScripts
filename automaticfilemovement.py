import os
import shutil
import sys

sourceDirectory = input("What is the source directory?")
directoryExists(sourceDirectory)

destinationDirectory = input("What is the directory you want to move your files to?")
directoryExists(destinationDirectory)

fileExtension = input("What is the file extension of the files you wish to move?")

for file in os.listdir(sourceDirectory):
    if file.endswith(fileExtension):
        filePath = os.path.join(sourceDirectory, file)
        shutil.move(filePath, destinationDirectory)

def directoryExists(directory):
    if not os.path.isdir(directory):
        print(f"Directory not found: {directory}")
        sys.exit(1)
