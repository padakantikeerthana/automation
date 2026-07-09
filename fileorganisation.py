import os
import shutil

source_folder = r"C:\Users\YourName\Downloads"

for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):
        extension = os.path.splitext(file)[1][1:]

        if extension:
            destination = os.path.join(source_folder, extension.upper())

            if not os.path.exists(destination):
                os.makedirs(destination)

            shutil.move(file_path, os.path.join(destination, file))

print("Files organized successfully!")