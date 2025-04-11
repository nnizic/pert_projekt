# PERT Project API

Ovo je backend aplikacija za upravljanje projektima i zadacima pomoću FastAPI frameworka. Aplikacija uključuje izgradnju grafa ovisnosti zadataka, kao i izvođenje PERT analize.

## 📁 Struktura projekta

```
pert_project/
└── server/
    ├── main.py             # Ulazna točka aplikacije
    ├── models.py           # SQLAlchemy modeli
    ├── schemas.py          # Pydantic sheme
    ├── database.py         # DB konekcija i session
    ├── routers/            # API rute (projekti, zadaci)
    │   ├── __init__.py
    │   ├── projects.py
    │   └── tasks.py
    └── services/           # PERT logika
        ├── __init__.py
        └── perth_graph.py
```

## 🚀 Pokretanje aplikacije

1. Instaliraj potrebne pakete:

```bash
pip install fastapi uvicorn sqlalchemy
```

2. Pokreni aplikaciju iz korijenskog direktorija `pert_project`:

```bash
uvicorn server.main:app --reload
```

📌 `--reload` omogućuje automatski restart pri izmjeni koda (korisno za razvoj).

3. Otvori preglednik i idi na:

```
http://127.0.0.1:8000
```

Za dokumentaciju API-ja (automatski generiranu):

```
http://127.0.0.1:8000/docs
```

## ✅ Napomena

Ako dobiješ grešku `ModuleNotFoundError: No module named 'server'`, provjeri da si u **korijenskom direktoriju projekta** (`pert_project/`) kad pokrećeš `uvicorn`.

---

PERT Project API - Frontend

Frontend za aplikaciju koristi Vue.js framework uz Vite build alat, dok se podaci o projektima i zadacima dohvaćaju putem REST API-ja razvijenog u FastAPI.
📁 Struktura frontend projekta

```
pert_frontend/
├── index.html # Glavna HTML datoteka
├── vite.config.js # Konfiguracija za Vite build alat
├── src/
│ ├── main.js # Ulazna točka Vue aplikacije
│ ├── App.vue # Glavna komponenta Vue aplikacije
│ ├── api.js # Axios instanca + API pozivi
│ ├── router/ # Konfiguracija Vue Routera
│ └── views/
│ ├── ProjectList.vue # Komponenta za prikaz projekata
│ └── PertGraph.vue # Komponenta za prikaz PERT grafa

```

🚀 Pokretanje frontenda

Instaliraj potrebne pakete:

    npm install

Pokreni frontend aplikaciju:

    npm run dev

Aplikacija će biti dostupna na:

```

http://localhost:5173

```

## 📬 Kontakt

Autor: Neven Nižić  
Fakultet: FIPU  
Kolegij: RITR
