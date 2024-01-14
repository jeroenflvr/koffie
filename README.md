# koffie
differentiequotiënt

## Intro

We gebruiken python, en dan voornamelijk deze techonologiën:

- [Jupyter Notebook (JupyterLab)](https://jupyter.org/)
- [Pandas](https://pandas.pydata.org/) 
- [Matplotlib](https://matplotlib.org/)


Python is een vrij 'makkelijke' programmeertaal zodat we ons kunnen concentreren op 
het eigenlijke doel: koffie.

## Setup

1) zorg dat je [python](https://www.python.org/) hebt 
2) installeer een nieuwe virtual environment: [https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html)
3) installeer jupyterlab, pandas en matplotlib:
```bash
pip install -r requirements.txt
```

of dit:
```bash
pip install jupyterlab matplotlib pandas
```

4) voer het volgende ook nog uit
```bash
jupyter lab build --dev-build=False --minimize=False
```

## start jupyter lab
Starten doe je gewoon met 'jupyter-lab' vanuit je python venv.
Dit zal tevens jouw browser openen en verbinen met jouw jupyterlab sessie.


De Jupyter Notebook ziet er zo uit: [koffie.ipynb](./koffie.ipynb)