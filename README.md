Voglio creare un progetto django + vue.js da zero.  
Il backend è in django e deve fornire le API per gestire gli elementi, mentre vue.js gestisce la grafica.  
Il progetto è un sistema di lezioni online.  
Esistono gli insegnanti che creano le lezioni (pagine html) e possono indicare quanti studenti possono partecipare.  
Gli studenti vedono tutte le lezioni disponibili e si iscrivono.  
Per il momento non creiamo autenticazione di alcun tipo.  
Creiamo un superadmin che possa generare dei dati da zero  

```bash

# Creare e attivare un ambiente virtuale
python3 -m venv venv
source venv/bin/activate  # Su Windows usa `venv\Scripts\activate`

# Installare Django, Django REST Framework, CORS su Django per permettere le richieste dal frontend
pip install django djangorestframework django-cors-headers

# Creare un nuovo progetto Django
django-admin startproject backend

cd backend
git init

# Creare una nuova applicazione per gestire le lezioni
python manage.py startapp lessons

# Esegui le migrazioni per creare le tabelle nel database
python manage.py makemigrations
python manage.py migrate

# Creazione del Superadmin
python manage.py createsuperuser


# Usa Vue CLI per creare un nuovo progetto
npm install -g @vue/cli
vue create frontend

# Installa Axios
cd frontend
npm install axios


# Avviare Django
python manage.py runserver

# Avviare Vue.js
npm run serve

```

- [x] BACKEND : http://127.0.0.1:8000/api/
- [x] FRONTEND: http://127.0.0.1:8080/

Ho dovuto aggiungere `CORS_ALLOW_ALL_ORIGINS = True` per evitare gli errori CORS (va bene per debug ma non in prod)