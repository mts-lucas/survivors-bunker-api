#!/usr/bin/env bash
# exit on error
set -o errexit

# Instalação das dependências usando pip
pip install -r requirements.txt

# Comandos de gerenciamento do Django
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py init_admin
python manage.py init_users
python manage.py init_monsters
python manage.py init_survivors