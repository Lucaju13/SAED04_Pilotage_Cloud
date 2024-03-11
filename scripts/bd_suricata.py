import json
import os
from pymongo import MongoClient

class SuricataLogAnalyzer:
    def __init__(self, log_directory, mongodb_uri, mongodb_database, mongodb_collection):
        self.log_directory = log_directory
        self.mongodb_uri = mongodb_uri
        self.mongodb_database = mongodb_database
        self.mongodb_collection = mongodb_collection
        self.seen_src_ips = set()

    def analyze_logs(self, file_prefix, num_files):
        client = MongoClient(self.mongodb_uri)
        db = client[self.mongodb_database]
        collection = db[self.mongodb_collection]

        for i in range(1, num_files + 1):
            input_file = os.path.join(self.log_directory, f"{file_prefix}.json.{i}")
            self.process_log_file(input_file, collection)

        client.close()

    def process_log_file(self, input_file, collection):
        with open(input_file, 'r') as file:
            for line in file:
                try:
                    json_data = json.loads(line)
                    self.extract_and_store_info(json_data, collection)
                except json.JSONDecodeError:
                    print(f"Skipping invalid JSON in {input_file}")

    def extract_and_store_info(self, json_data, collection):
        event_type = json_data.get('event_type', '')

        if event_type == 'alert':
            # Extract relevant fields
            log_entry = {
                'src_ip': json_data.get('src_ip', ''),
                'timestamp': json_data.get('timestamp', ''),
                'dest_port': json_data.get('dest_port', ''),
                'proto': json_data.get('proto', ''),
                'alert_signature_id': json_data.get('alert', {}).get('signature_id', ''),
                'alert_signature': json_data.get('alert', {}).get('signature', ''),
                'alert_category': json_data.get('alert', {}).get('category', ''),
                'alert_severity': json_data.get('alert', {}).get('severity', ''),
            }

            # Check if the entry already exists based on src_ip
            existing_entry = collection.find_one({'src_ip': log_entry['src_ip']})
            
            if existing_entry:
                # If the entry exists, update it
                collection.update_one({'src_ip': log_entry['src_ip']}, {'$set': log_entry})
            else:
                # If the entry does not exist, insert it
                collection.insert_one(log_entry)

# Utilisation de la classe SuricataLogAnalyzer
log_directory = "/home/linux/Bureau/SAE-Cloud/logs/"
mongodb_uri = "mongodb://10.202.9.1:27017/"
mongodb_database = "root"
mongodb_collection = "suricata"
file_prefix = "eve"
num_files_per_day = 1

analyzer = SuricataLogAnalyzer(log_directory, mongodb_uri, mongodb_database, mongodb_collection)
analyzer.analyze_logs(file_prefix, num_files_per_day)
