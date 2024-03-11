import json
import csv
import os

class SuricataLogAnalyzer:
    def __init__(self, log_directory, output_csv_file):
        self.log_directory = log_directory
        self.output_csv_file = output_csv_file

    def analyze_logs(self, file_prefix, num_files):
        with open(self.output_csv_file, 'w', newline='') as output_csv:
            csv_writer = csv.writer(output_csv)
            self.write_csv_header(csv_writer)

            for i in range(1, num_files + 1):
                input_file = os.path.join(self.log_directory, f"{file_prefix}.json.{i}")
                self.process_log_file(input_file, csv_writer)

    def process_log_file(self, input_file, csv_writer):
        with open(input_file, 'r') as file:
            for line in file:
                try:
                    json_data = json.loads(line)
                    self.extract_and_write_alert_info(json_data, csv_writer)
                except json.JSONDecodeError:
                    print(f"Skipping invalid JSON in {input_file}")

    def extract_and_write_alert_info(self, json_data, csv_writer):
        event_type = json_data.get('event_type', '')

        if event_type == 'alert':
            self.write_csv_row(json_data, csv_writer)

    def write_csv_header(self, csv_writer):
        csv_writer.writerow([
            'timestamp', 'src_ip', 'dest_port', 'proto',
            'alert_signature_id', 'alert_signature', 'alert_category', 'alert_severity'
        ])

    def write_csv_row(self, json_data, csv_writer):
        row = [
            json_data.get('timestamp', ''),
            json_data.get('src_ip', ''),
            json_data.get('dest_port', ''),
            json_data.get('proto', ''),
            json_data.get('alert', {}).get('signature_id', ''),
            json_data.get('alert', {}).get('signature', ''),
            json_data.get('alert', {}).get('category', ''),
            json_data.get('alert', {}).get('severity', '')
        ]
        csv_writer.writerow(row)

# Utilisation de la classe SuricataLogAnalyzer
log_directory = "/home/linux/Bureau/SAE-Cloud/logs/"
output_csv_file = "/home/linux/Bureau/SAE-Cloud/suricata_analysis.csv"
file_prefix = "eve"
num_files_per_day = 1

analyzer = SuricataLogAnalyzer(log_directory, output_csv_file)
analyzer.analyze_logs(file_prefix, num_files_per_day)
