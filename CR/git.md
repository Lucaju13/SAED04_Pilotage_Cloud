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

