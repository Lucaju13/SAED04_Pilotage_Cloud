import boto3
from botocore.exceptions import NoCredentialsError
from botocore.client import Config

def main():
    # Créez un client avec les informations d'identification de votre serveur S3
    s3 = boto3.client('s3',
                      endpoint_url='https://10.202.0.53:9000',
                      aws_access_key_id='minio-user',
                      aws_secret_access_key='myadmin123minio',
                      config=Config(signature_version='s3v4'),
                      verify=False  # Pour désactiver la vérification du certificat SSL
                      )

    # Le fichier source à télécharger, changez ce chemin si nécessaire
    source_file = "requirements.txt"

    # Le nom du bucket de destination et le nom de fichier sur le serveur S3
    bucket_name = "python-test-bucket"
    destination_file = "mon-fichier-test.txt"

    # Vérifiez si le bucket existe, sinon créez-le
    try:
        s3.head_bucket(Bucket=bucket_name)
        print("Bucket", bucket_name, "already exists")
    except s3.exceptions.NoSuchBucket:
        s3.create_bucket(Bucket=bucket_name)
        print("Created bucket", bucket_name)

    # Téléchargez le fichier en le renommant au passage
    try:
        s3.upload_file(source_file, bucket_name, destination_file)
        print(
            source_file, "successfully uploaded as object",
            destination_file, "to bucket", bucket_name,
        )
    except NoCredentialsError:
        print("Credentials not available")

if __name__ == "__main__":
    main()

