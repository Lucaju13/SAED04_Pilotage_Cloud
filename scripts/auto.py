import os
import requests
import subprocess
import gzip
from datetime import datetime, timedelta
import pandas as pd
import json
import ipaddress

class DownloaderSuricataLogs:
    def __init__(self, username, password, url, output_directory, num_files_per_day, start_date, end_date):
        self.username = username
        self.password = password
        self.url = url
        self.headers = {"X-Requested-With": "XMLHttpRequest"}
        self.output_directory = output_directory
        self.num_files_per_day = num_files_per_day
        self.start_date = start_date
        self.end_date = end_date
        self.arquivos_baixados = set()

    def download_logs(self, filename, file_url, output_file_path):
        curl_command = f'curl -u {self.username}:{self.password} -H "X-Requested-With: XMLHttpRequest" -o {output_file_path} {file_url}'
        subprocess.run(curl_command, shell=True)

    def extract_gzip(self, input_path, output_path):
        with gzip.open(input_path, 'rb') as f_in:
            with open(output_path, 'wb') as f_out:
                f_out.write(f_in.read())

    def analyze_logs(self, logs_data):
        df = pd.json_normalize(logs_data)

        protocols = df['proto'].unique()
        for protocol in protocols:
            protocol_df = df[df['proto'] == protocol]

            print(f"\nInformations importantes pour le protocole {protocol} :\n")

            # Détection d'anomalies basée sur le réseau
            if 'src_ip' in protocol_df.columns and 'dest_ip' in protocol_df.columns:
                for _, row in protocol_df.iterrows():
                    src_ip = row['src_ip']
                    dest_ip = row['dest_ip']

                    if not (ipaddress.ip_address(src_ip) in ipaddress.IPv4Network('10.202.0.0/16') and
                            ipaddress.ip_address(dest_ip) in ipaddress.IPv4Network('10.202.0.0/16')):
                        print(f"Anomalie détectée - IP non autorisée : {src_ip} - {dest_ip}")

            # Si le protocole est DNS, afficher les informations spécifiques
            if protocol == 'UDP' or protocol == 'TCP':
                dns_info = protocol_df[['timestamp', 'src_ip', 'src_port', 'dest_ip', 'dest_port', 'dns.type', 'dns.id', 'dns.rrname', 'dns.rrtype', 'dns.tx_id']]
                print(dns_info)

            # Si le protocole est TCP, afficher les informations spécifiques
            if protocol == 'TCP':
                tcp_info = protocol_df[['timestamp', 'src_ip', 'src_port', 'dest_ip', 'dest_port', 'alert.action', 'alert.signature', 'alert.severity']]
                print(tcp_info)

            # Filtrer les données du protocole ICMP
            icmp_df = df[df['proto'] == 'ICMP']
            # Afficher les informations spécifiques à ICMP
            icmp_info = icmp_df[['timestamp', 'src_ip', 'dest_ip', 'icmp_type', 'icmp_code', 'alert.action', 'alert.signature', 'alert.severity']]
            print(icmp_info)

    def run(self):
        current_date = self.start_date
        while current_date <= self.end_date:
            for i in range(1, self.num_files_per_day + 1):
                filename = f"eve.json.{i}.gz"
                output_file_path = os.path.join(self.output_directory, filename)

                # Verificar se o arquivo já foi baixado e processado no dia atual
                if filename not in self.arquivos_baixados:
                    # Construir o comando curl
                    file_url = self.url + filename
                    curl_command = f'curl -u {self.username}:{self.password} -H "X-Requested-With: XMLHttpRequest" -o {output_file_path} {file_url}'

                    # Executar o comando curl usando subprocess
                    subprocess.run(curl_command, shell=True)

                    # Adicionar o arquivo à lista de arquivos baixados
                    self.arquivos_baixados.add(filename)

                    # Verificar se o arquivo já existe no diretório
                    if os.path.exists(output_file_path):
                        print(f"Le fichier {filename} a été téléchargé avec succès pour la journée actuelle.")

                        # Extrair o arquivo Gzip
                        with gzip.open(output_file_path, 'rb') as f_in:
                            with open(output_file_path[:-3], 'wb') as f_out:
                                f_out.write(f_in.read())

                        print(f"Le fichier {filename} a été extrait avec succès pour la journée actuelle.")

                        # Charger les données JSON depuis le fichier de logs
                        with open(output_file_path[:-3], 'r') as file:
                            logs_data = [json.loads(line) for line in file]

                        # Analyser les logs
                        self.analyze_logs(logs_data)
                    else:
                        print(f"Erreur : Échec du téléchargement du fichier {filename} pour la journée actuelle.")
                else:
                    print(f"Le fichier {filename} a déjà été téléchargé et traité pour la journée actuelle. Ignorer le téléchargement et l'extraction pour la journée actuelle.")

            # Incrementar para o próximo dia
            current_date += timedelta(days=1)

# Informações de autenticação e URL
username = "NyKsYaWd7fYe4pC"
password = "iutbrtcloud2024"
url = "https://registry.iutbeziers.fr:4443/public.php/webdav/suricata/log/"

# Diretório de destino para os logs baixados
output_directory = "/home/test/Bureau/cloud/logs_suricata/log/"

# Quantidade de arquivos a serem baixados por dia
num_files_per_day = 1

# Data inicial e final para baixar logs
start_date = datetime.now() - timedelta(days=5)  # Data de 5 dias atrás
end_date = datetime.now()

# Créer une instance de la classe et exécuter le téléchargement
downloader = DownloaderSuricataLogs(username, password, url, output_directory, num_files_per_day, start_date, end_date)
downloader.run()
