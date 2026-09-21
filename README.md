# Gaming For All (GFA)

Gaming For All est un projet personnel en cours de création.

L'objectif est de construire progressivement une application permettant à tous les joueurs d'organiser facilement des sessions de jeu entre amis, tout en découvrant chaque brique d'une application et de son exploitation SRE.

## Étape actuelle

Cette première version est volontairement minimale. Elle contient uniquement une petite API créée en Python avec FastAPI.

Elle permet de comprendre :

- ce qu'est une API ;
- comment démarrer un serveur local ;
- comment créer une route ;
- comment vérifier que l'application fonctionne avec `/health`.

Docker, PostgreSQL, Redis et Kubernetes seront ajoutés plus tard, une étape à la fois.

## Contenu du dépôt

- `main.py` : le code de l'API ;
- `requirements.txt` : les bibliothèques Python nécessaires ;
- `.gitignore` : les fichiers locaux que Git ne doit pas publier.

## Lancer l'API

### 1. Créer un environnement Python

```bash
python -m venv .venv
```

Sous Windows :

```bash
.venv\Scripts\activate
```

Sous macOS ou Linux :

```bash
source .venv/bin/activate
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 3. Démarrer le serveur

```bash
uvicorn main:app --reload
```

## Tester l'API

Une fois le serveur lancé :

- accueil : <http://127.0.0.1:8000/> ;
- état de l'API : <http://127.0.0.1:8000/health> ;
- documentation interactive : <http://127.0.0.1:8000/docs>.

La route `/health` doit renvoyer :

```json
{
  "status": "ok"
}
```

## Prochaine étape

La prochaine étape consistera à ajouter une première véritable fonctionnalité métier, avant d'introduire une base de données.
