# TP1

### Etape 0:

```cmd
ssh-keygen -t ed25519 -C "commentaire" -f cle
Generating public/private ed25519 key pair.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in cle
Your public key has been saved in cle.pub
The key fingerprint is:
SHA256:s4tvvOGqIza6l9IwLu8t9ODcd+zafEojnDCjX+xN1qA commentaire
```
### Fichier config :

```cmd
test@202-13:~/.ssh$ cat config 
Host registry.iutbeziers.fr
	User git
	PasswordAuthentication no
	IdentityFile ~/.ssh/cle
	ForwardX11 no
	ForwardAgent no	
```
![Alt_text](../images/1.1.png)

# TP2
**diiference entre fetch et pull, robas et merge**
## Creation de branche

```cmd
test@202-13:~/Bureau/karma_analysis$ git switch -c doc/contrib_Lucas
Basculement sur la nouvelle branche 'doc/contrib_Lucas'
git push -u origin doc/contrib_Lucas
```
![Alt_text](../images/1.2.png)

![Alt_text](../images/1.3.png)

## Etape 2:
![Alt_text](../images/1.4.png)

![Alt_text](../images/1.5.png)

![Alt_text](../images/1.6.png)

![Alt_text](../images/1.7.png)

![Alt_text](../images/1.8.png)

![Alt_text](../images/1.9.png)

![Alt_text](../images/1.10.png)

![Alt_text](../images/1.11.png)

## Etape 3:
![Alt_text](../images/1.12.png)

![Alt_text](../images/1.13.png)

![Alt_text](../images/1.14.png)

## Etape 4:

## Etape 5:
![Alt_text](../images/1.15.png)

![Alt_text](../images/1.16.png)

## Etape 6: Utilisation de docstrings
![Alt_text](../images/1.17.png)

![Alt_text](../images/1.18.png)

## Etape 7: Generation automatique de la documentation
![Alt_text](../images/1.21.png)

![Alt_text](../images/1.20.png)

![Alt_text](../images/1.19.png)

```yaml
#image: python:3
stages:
  - deploy

deploy:
  stage: deploy
  script:
    - whoami
    - pwd
    - pip install numpy matplotlib scipy lxml sphinx sphinx-rtd-theme myst-parser --break-system-packages
    - cd docs
    - sphinx-build -b html source ./build/html
    - cp -R /home/gitlab-runner/builds/GwQay9zmB/0/cloud2024/group1/karma_analysis /tmp/monbuild/

  artifacts:
    paths:
      - docs
  only:
    - develop1
```

# TP3 - Evaluer et amelliorer 
## Etape 0:

## Etape 1:
![Alt_text](../images/1.23.png)

![Alt_text](../images/1.24.png)

## Etape 2: Typage en Python
```cmd
mypy --ignore-missing-imports src/karma_analysis.py
```
![Alt_text](../images/1.25.png)

```cmd
 mypy --html-report type-coverage karma_analysis.py --ignore-missing-imports
```
![Alt_text](../images/1.26.png)

![Alt_text](../images/1.27.png)

```cmd
coverage run ../src/karma_analysis.py data1
coverage report -m
```
![Alt_text](../images/1.28.png)

![Alt_text](../images/1.29.png)

## Etape 3: Analyse de Qualité du code avec pylint et SonarQube
```cmd
pylint src/karma_analysis.py
```
![Alt_text](../images/1.30.png)

![Alt_text](../images/1.31.png)

```cmd
java -jar /opt/sonar-scanner/lib/sonar-scanner-cli-4.2.0.1873.jar \
  -Dsonar.projectKey=lucaju13 \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.token=sqp_5e7634eae4309889b853ce8e3d9e25cf01380fb8

```
![Alt_text](../images/1.32.png)

![Alt_text](../images/1.33.png)
