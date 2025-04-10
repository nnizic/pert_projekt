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

## 📬 Kontakt

Autor: Neven Nižić  
Fakultet: FIPU  
Kolegij: RITR
