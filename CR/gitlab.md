# Gitlab dans tous ces états
## Comment contribuer à un projet ?
### Termes liés à Git:

**1. Feature "branching":**

Il s'agit d'une pratique dans Git où vous créez une nouvelle branche (branch) pour travailler sur une nouvelle fonctionnalité (feature) isolément du code principal. Cela permet de développer et tester la fonctionnalité sans affecter la branche principale du projet.

**2. Pull request ou merge request:**

Une pull request (PR) ou une merge request (MR) est une demande faite par un contributeur à un projet pour fusionner les changements qu'il a effectués dans une branche avec la branche principale du projet. Les autres membres de l'équipe peuvent examiner les modifications, donner leur avis et, éventuellement, approuver la fusion.

**3. Cherry picking:**

Cette opération permet de sélectionner des commits spécifiques d'une branche et de les appliquer à une autre. Cela peut être utile lorsque vous souhaitez appliquer uniquement certains changements d'une branche à une autre, sans fusionner l'ensemble de la branche.

**4. merge et rebase:**

**Merge (fusionner):** C'est le processus d'intégration des modifications d'une branche dans une autre. Lorsqu'une branche est fusionnée, les modifications apportées à cette branche sont combinées avec la branche cible.

**Rebase (rebaser):** C'est une autre façon d'intégrer les changements d'une branche à une autre. Plutôt que de fusionner les changements, le rebase repositionne les modifications de la branche courante au sommet de la branche cible, créant une séquence linéaire et épurée de l'historique des commits. Cela peut rendre l'historique des commits plus propre, mais il est important de l'utiliser avec prudence car il modifie l'historique existant.


## I - Installation de Gitlab soit sous forme d’un container Docker, soit sur une machine virtuelle.
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

**User: root** 

**Pass: Lucaju@13** 

![Alt_text](../images/51.png)

## II - Utilisation de glab
####  Installation et paramétrage de glab
**1 - Installez glab sur une machine.**

```cmd
docker pull gitlab/glab
```
![Alt_text](../images/53.png)

**2. Activation la complétion automatique pour glab.**

Ajout de lignes suivantes dans mon fichier ~/.bashrc
```cmd
if [ -f /usr/share/bash-completion/completions/git ]; then
    . /usr/share/bash-completion/completions/git
elif [ -f /etc/bash_completion.d/git ]; then
    . /etc/bash_completion.d/git
fi
```
ensuite j'ai redemmaré:
```cmd
source ~/.bashrc
```

**test:**
![Alt_text](../images/52.png)

**3. Création un token sur votre compte gitlab.**

