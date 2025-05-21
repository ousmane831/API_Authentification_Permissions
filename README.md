# 🔐 API Authentification & Permissions - Django REST Framework

Ce projet est une API RESTful construite avec **Django** et **Django REST Framework (DRF)**.  
Elle gère des tâches personnelles avec un système d'**authentification par token** et des **permissions basées sur les utilisateurs**.

---

## 📁 Fonctionnalités

- 🔐 Authentification par **Token (TokenAuthentication)**
- 👥 Gestion des utilisateurs (lecture seule)
- ✅ CRUD complet pour les tâches (`Task`)
- 🔒 Permissions personnalisées : seuls les propriétaires peuvent modifier leurs tâches

---

## 🧱 Technologies utilisées

- Python 3.x
- Django
- Django REST Framework
- SQLite (par défaut)

---

## 🛠️ Installation

```bash
# Cloner le projet
git clone https://https://github.com/ousmane831/API_Authentification_Permissions.git
cd api-auth-permissions

# Créer un environnement virtuel
python -m venv env
source env/bin/activate   # macOS/Linux
env\Scripts\activate      # Windows

# Installer les dépendances
pip install -r requirements.txt

# Appliquer les migrations
python manage.py migrate

# Créer un superutilisateur
python manage.py createsuperuser

# Démarrer le serveur
python manage.py runserver
