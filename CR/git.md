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

Le résultat de pylint indique qu'il y a quelques problèmes de style et de convention le code.

J'ai ajouté des docstrings, changé quelques noms de variables pour les rendre plus explicites, et j'ai corrigé quelques espaces en fin de ligne pour respecter les conventions PEP 8.
```cmd
(env) test@232-22:~/karma_analysis$ pylint src/karma_analysis.py
************* Module karma_analysis
src/karma_analysis.py:161:0: C0301: Line too long (106/100) (line-too-long)
src/karma_analysis.py:165:0: C0301: Line too long (106/100) (line-too-long)
src/karma_analysis.py:1:0: C0114: Missing module docstring (missing-module-docstring)
src/karma_analysis.py:20:13: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
src/karma_analysis.py:27:8: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/karma_analysis.py:26:4: W0612: Unused variable 'e' (unused-variable)
src/karma_analysis.py:95:4: W0632: Possible unbalanced tuple unpacking with sequence defined at line 1028 of scipy.optimize._minpack_py: left side has 2 labels, right side has 5 values (unbalanced-tuple-unpacking)
src/karma_analysis.py:151:4: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/karma_analysis.py:152:4: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/karma_analysis.py:153:4: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/karma_analysis.py:154:4: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
src/karma_analysis.py:186:8: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)

------------------------------------------------------------------
Your code has been rated at 8.38/10 (previous run: 7.43/10, +0.95)
```
```python3
import argparse
import json
import logging
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf

def parse_json_data(filename: str) -> dict:
    """
    This function takes one file as input and reorders json content to reindex the final dictionary.

    Parameters:
    filename (str): File path.

    Returns:
    dict: Dictionary reindexed according to the number of participants.
    """
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            # Sort the data by raclette consumption
            data = sorted(data, key=lambda x: x["raclette_consumption"])
            # Reshape the data to have one array per key
            data = {key: np.array([entry[key] for entry in data]) for key in data[0].keys()}
    except json.JSONDecodeError as e:
        logging.error(f"Json file '{filename}' format is not correct.")
        data = {}
    return data

def convert(k, f) -> float:
    """
    Convert data.

    Returns:
    float: Converted data.
    
    >>> convert(1, 1)
    0.01
    >>> convert(6, 4)
    0.24
    """
    prob = k * f / 100.0
    return prob

def linear(x, a, b) -> float:
    """
    Compute linear value from y = ax + b.

    Returns:
    float: y.

    >>> linear(4.8, 10, 5)
    53.0
    >>> linear(48, 1, 5)
    53
    """
    return a * x + b

def quadratic(x, a, b, c) -> float:
    """
    Compute quadratic value from y = ax^2 + bx + c.

    Returns:
    float: y.

    >>> quadratic(3, 5, -4, 0)
    33
    >>> quadratic(1, 5, -4, 0)
    1
    """
    return a * x**2 + b * x + c

def sinusoidal(x, a, b, c, d) -> float:
    """
    Compute sinusoidal value from y = a*sin(bx+c)+d.

    Returns:
    float: y.

    >>> sinusoidal(3, 5, -4, 0, 10)
    12.682864590002175
    >>> sinusoidal(1, 5, -4, 0, 10)
    13.784...
    """
    return a * np.sin(b * x + c) + d

def fit(data, func, p0=None) -> np.ndarray:
    """
    Fit data using the given function.

    Returns:
    np.ndarray: Fitted parameters.
    """
    params, _ = cf(func, data["raclette_consumption"], data["prob"], p0=p0)
    return params

def plot(data, params, func, name) -> None:
    """
    Plot the data and the fitted model.

    Returns:
    None
    """
    x = data["raclette_consumption"]
    x2 = np.linspace(x[0], x[-1], 100)

    model = func(x2, *params)

    plt.plot(x2, model, label=name, color="C1")
    plt.scatter(x, data["prob"], label="Data", color="C0")

    plt.xlabel("RC")
    plt.ylabel("RP")
    plt.title("Model")
    plt.legend()
    plt.show()

def compare_models(data) -> tuple:
    """
    Compare different models and return the best one.

    Returns:
    tuple: Best model information.
    """
    data["prob"] = convert(data["karma"], data["slug_factor"])

    param1 = fit(data, linear)
    param2 = fit(data, quadratic)
    param3 = fit(data, sinusoidal, p0=[10, 0.2, 0, 100])

    x = data["raclette_consumption"]
    prob = data["prob"]

    pred1 = linear(x, *param1)
    pred2 = quadratic(x, *param2)
    pred3 = sinusoidal(x, *param3)

    mse1 = np.mean((prob - pred1) ** 2)
    mse2 = np.mean((prob - pred2) ** 2)
    mse3 = np.mean((prob - pred3) ** 2)

    best_model = min(
        [
            (mse1, "Linear", param1, linear),
            (mse2, "Quadratic", param2, quadratic),
            (mse3, "Sinusoidal", param3, sinusoidal),
        ]
    )

    logging.info(f"Linear MSE: {mse1}")
    logging.info(f"Quadratic MSE: {mse2}")
    logging.info(f"Sinusoidal MSE: {mse3}")
    logging.info(f"Best model: {best_model[1]} with MSE {best_model[0]}")
    logging.info(best_model)

    return best_model

def main(argv=sys.argv[1:]) -> None:
    """
    Main function for analyzing the impact of raclette consumption on karma and reincarnation probability.
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description="Analyzing the impact of raclette consumption on karma and reincarnation probability."
    )
    parser.add_argument("data_file", type=str, help="Path to the JSON data file")

    args = parser.parse_args(argv)
    file = vars(args)

    try:
        # Path to the json data (simulation results)
        file_path = "../data/" + file["data_file"] + ".json"

        # Parse the json data into a reindexed dictionary
        data = parse_json_data(file_path)

        # Compare the models
        model = compare_models(data)

        # Plot the results
        plot(data, model[2], model[3], model[1])

    except FileNotFoundError:
        logging.error(
            f"File named '{file['data_file']}.json' does not exist in the data directory."
        )

if __name__ == "__main__":
    main()

```
## SonarQube installation et Utilisation:

commande:

```cmd
docker run -d --name sonarqube -p 9000:9000 -p 9092:9092 sonarqube
```

![Alt_text](../images/1.31.png)

```cmd
sonar-scanner \
  -Dsonar.projectKey=test \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.token=sqp_340945536f28534df2ee426dc44cc0b79a8e4ef2
```
![Alt_text](../images/1.33.png)

![Alt_text](../images/1.32.png)

*Petit changement de projet car j'ai changé de PC*

**Utilisation avancée du sonarcube:**

Remplacement des elements de ligne de comande en utilisant le fichier: sonar-project.properties

![Alt_text](../images/1.111.png)

Utilisation de ```sonar.python.coverage.reportPaths``` :

Geneation du fichier xml:

```cmd
(env) test@203-0:~/karma_analysis/data$ coverage xml
Wrote XML report to coverage.xml
(env) test@203-0:~/karma_analysis/data$ ls
coverage.xml  data1.json  data2.json
``
Dans le fichier:
```cmd
# Configure here general information about the environment, such as SonarQube server details
# No information about the specific project should appear here

# Default SonarQube server
sonar.host.url=http://localhost:9000

# Default source code encoding
sonar.sourceEncoding=UTF-8

# Project specific configuration
sonar.projectKey=test
sonar.sources=.
sonar.token=sqp_340945536f28534df2ee426dc44cc0b79a8e

#Utilisation de la fonction coverage
sonar.python.coverage.reportPaths=/home/test/karma_analysis/data/coverage.xml
```

## Etape 4:


