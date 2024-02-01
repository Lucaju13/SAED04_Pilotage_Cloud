# Gitlab dans tous ces états
## Comment contribuer à un projet ?
### Termes liés à Git:

**1. Feature "branching":**

**2. Pull request ou merge request:**

**3. Cherry picking:**

**4. merge et rebase:**

## Installation de Gitlab soit sous forme d’un container Docker, soit sur une machine virtuelle.
### Installation
[Source](https://github.com/sameersbn/docker-gitlab)
```cmd
docker pull sameersbn/gitlab:16.8.1
```

```cmd
root@debian:/home/debian# docker pull sameersbn/gitlab:16.8.1
16.8.1: Pulling from sameersbn/gitlab
521f275cc58b: Pull complete 
4540f875af57: Pull complete 
785e0c38a959: Pull complete 
ee1c9058318e: Pull complete 
357ad71158a4: Pull complete 
a7287c58934f: Pull complete 
7d3e58b4de17: Pull complete 
c1dae7ce0e53: Pull complete 
Digest: sha256:37eae09ed72578f6e57e8f949c2c7a6fd8b5422a4902b330d44df7879c3f619d
Status: Downloaded newer image for sameersbn/gitlab:16.8.1
docker.io/sameersbn/gitlab:16.8.1
```
**Etape 2:**
Docker compose, pour l'initializer plus rapidement:

```cmd
wget https://raw.githubusercontent.com/sameersbn/docker-gitlab/master/docker-compose.yml
```
ensuite:

```cmd
docker-compose up
```
![Alt_text](../images/49.png)

J'ai du faire unblock du port 10080 sur firefox pour pouvoir acceder au Gitlab server:
J'ai tabe sur la barre d'URL: about:config, ensuite j'ai cherché: "network.security.ports.banned.override" et j'ai ajouté le port 10080.

![Alt_text](../images/48.png)

**Résultat:**
![Alt_text](../images/50.png)

*Credentials:*
**user:root** 
**Pass: Lucaju@13** 
