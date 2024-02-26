# Traitement de logs Suricata en utilisant nushell

## Etape 0: Pré-Requis

### Installation nushell sur linux

```cmd
sudo apt-get update
sudo apt-get install rustc cargo
export PATH="$HOME/.cargo/bin:$PATH"
```

Pour verifier l'installation du cargo: ```cargo version ```

```cmd
test@202-13:~$ cargo version 
cargo 1.65.0
```

Ensuite j'ai lancé la commande:

```cmd
cargo install nu
```

## Etape 1: Analyse de Logs
