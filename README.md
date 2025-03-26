# Uploadly
Prijenos i dohvat datoteka putem lozinke.

## Preduvjeti
- Instaliran Python (verzija na kojoj je rađen projekt jest `3.11.5`)
- Instaliran Postgresql (verzija na kojoj je rađen projekt jest `17`)

## Koraci za lokalno pokretanje
- Kreiraj virtualno okruženje:
```py -3 -m venv .venv```

- Aktiviraj virtualno okruženje:
```.venv\Scripts\activate```

- Instaliranje potrebnih paketa:
```pip install -r requirements.txt```

- Kreirati bazu u Postgresu te izraditi .env datoteku po uzoru na .env.example (ne zaboraviti urediti podatke, npr. za spajanje na bazu podataka - `DATABASE_URL`)

- Napravite migracije:
```
flask db init
flask db migrate -m "Initial migration"
flask db upgrade (za slučaj promjene na modelima)
```

- Pokrenite server:
```python run.py```

Uploadly će biti dostupan na localhostu.

## Moguća poboljšanja
- Postaviti limit na veličinu prenesene datoteke, te vremenski limit za dohvat datoteke.
- Napisati testove kako bismo bili uvjereni da naš program radi ono za što je namijenjen.
- Dockerizirati program kako na lokalnoj mašini drugog programera ili produkcijskim
okolinama ne bismo morali instalirati Python, Postgresql globalno, te pojednostavljivanje samog pokretanja.
- Urediti dizajn aplikacije da odgovara standardu klijenta.
- Uvesti VueJS kao ruter i za dohvat template-ova, a Flask prebaciti u API.