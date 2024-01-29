# Le Stockage Objet MinIO
##  Implémentation d’un stockage objet:Minio
### Installation et Configuration de MinIO

#### Création d'un Utilisateur et d'un Groupe pour MinIO
```cmd
root@debian:~# groupadd -r minio-user
root@debian:~# useradd -r -g minio-user -s -d /home/minio-user /sbin/nologin minio-user
root@debian:~# useradd -r -g minio-user -d /home/minio-user -s /sbin/nologin minio-user
root@debian:~# mkdir /data
root@debian:~# chown minio-user:minio-user /data
root@debian:~# chmod 750 /data
```
#### Installation de MinIO via DEB
```cmd
root@debian:~# wget https://dl.min.io/server/minio/release/linux-amd64/minio.deb--2024-01-29 08:57:54--  https://dl.min.io/server/minio/release/linux-amd64/minio.deb
Résolution de dl.min.io (dl.min.io)… 178.128.69.202, 138.68.11.125
Connexion à dl.min.io (dl.min.io)|178.128.69.202|:443… connecté.
requête HTTP transmise, en attente de la réponse… 200 OK
Taille : 35683782 (34M) [application/vnd.debian.binary-package]
Sauvegarde en : « minio.deb »

minio.deb                    100%[===========================================>]  34,03M   816KB/s    ds 71s     

2024-01-29 08:59:05 (494 KB/s) — « minio.deb » sauvegardé [35683782/35683782]

root@debian:~#  dpkg -i minio.deb
Sélection du paquet minio précédemment désélectionné.
(Lecture de la base de données... 34127 fichiers et répertoires déjà installés.)
Préparation du dépaquetage de minio.deb ...
Dépaquetage de minio (20240129035632.0.0) ...
Paramétrage de minio (20240129035632.0.0) ...
```
#### Configuration des Variables d'Environnement
- Créez le fichier de configuration :
```cmd
nano /etc/default/minio

GNU nano 7.2                                                                          /etc/default/minio                                                                                    
MINIO_ACCESS_KEY=minio-user
MINIO_SECRET_KEY=myadmin123minio
MINIO_VOLUMES="/data"
```
- Ajout de permissions:
```cmd
mkdir /mnt/disk1 /mnt/disk2 /mnt/disk3 /mnt/disk4
chown minio-user:minio-user /mnt/disk1 /mnt/disk2 /mnt/disk3 /mnt/disk4

groupadd -r minio-user
useradd -M -r -g minio-user minio-user
chown minio-user:minio-user /mnt/disk1 /mnt/disk2 /mnt/disk3 /mnt/disk4

systemctl enable minio.service
sudo systemctl restart  minio.service
```
- Fonctionnement:
![Alt_text](../images/1.png)

![Alt_text](../images/2.png)

#### Génération des Certificats

