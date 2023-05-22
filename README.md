# Flower shop - My E-Florist

**Ecommerce in Django**

The following functionality was implemented:

- User registration. Inherited from AbstractBaseUser
- Adding an item to the cart and/or favorites to authorized users
- Adding an item to the cart and/or favorites to unauthorized users using Django Session
- Discount system
- Product characteristics
- Setting up a personal account
- Product reviews
- Product rating
- Sending order information by email
- Product search

## Settings

Clone the project

```bash
https://github.com/victrmontero/My_E-Florist.git
```

Create a virtual environment

```
python3 -m venv venv
```

Activate the virtual environment:

```
source ./venv/bin/activate
```

If using windows

```
venv\Scripts\activate
```

Installing dependancies

```bash
pip install -r requirements.txt
```

**Create .env file and specify your keys to these variables:**

- SECRET_KEY
- DEBUG
- POSTGRES_DB
- POSTGRES_USER
- POSTGRES_PASSWORD
- POSTGRES_HOST
- POSTGRES_PORT
- EMAIL_HOST_USER
- EMAIL_HOST_PASSWORD

Launch Docker

```bash
docker-compose up --build
```

Create super user

```bash
docker-compose exec web python3 manage.py createsuperuser
```

Install the extension pg_trgm

```
docker-compose exec db bash
```

```
psql -U <postgres_user>
```

```
CREATE EXTENSION pg_trgm;
```
