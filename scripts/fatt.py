import os
import subprocess
import gzip
import shutil

class FileDownloader:
    def __init__(self, base_url, username, password, output_directory):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.output_directory = output_directory

    def download_files(self, file_prefix, num_files):
        for i in range(1, num_files + 1):
            file_name = f"{file_prefix}.log.{i}.gz"
            url = f'{self.base_url}/{file_name}'
            output_file = os.path.join(self.output_directory, file_name)
            curl_command = f'curl -u {self.username}:{self.password} -H "X-Requested-With: XMLHttpRequest" -o {output_file} {url}'
            subprocess.run(curl_command, shell=True)
        print("Fichier téléchargé avec succès!!")

    def extract_files(self, file_prefix, num_files):
        for i in range(1, num_files + 1):
            input_file = os.path.join(self.output_directory, f"{file_prefix}.log.{i}.gz")
            output_file = os.path.join(self.output_directory, f"{file_prefix}.log.{i}")

            with gzip.open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
            print("Unzip success!")

            # Supprimer le fichier .gz après l'extraction
            os.remove(input_file)
            print(f"Fichier {input_file} supprimé avec succès!")

# Utilisation de la classe FileDownloader
base_url = "https://registry.iutbeziers.fr:4443/public.php/webdav/fatt/log"
username = "NyKsYaWd7fYe4pC"
password = "iutbrtcloud2024"
output_directory = "/home/linux/Bureau/SAE-Cloud/logs/"
file_prefix = "fatt"
num_files_per_day = 1

downloader = FileDownloader(base_url, username, password, output_directory)
downloader.download_files(file_prefix, num_files_per_day)
downloader.extract_files(file_prefix, num_files_per_day)
