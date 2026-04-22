# Project Setup

Follow these steps to set up your local development environment for this Django project.

## Step 1: Clone the Repository

Clone the project repository to your local machine:

```bash
git clone https://github.com/BagzzDev/class-project-2-backend.git
cd class-project-2-backend
```

## Step 2: Set Up Virtual Environment

### On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

## Step 3: Install Required Packages

Install all project dependecis from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Step 4: Set Up Environment Variables

copy the `.env.example` file to create your own `.env` file.

```bash
cp .env.example .env
```

On Windows, use:

```bash
copy .env.example .env
```

Then generate a new secret key for your local development:

```bash
python -c "from django.core.management.utils import get_random_secret_key;
print(get_random_secret_key())"
```

Copy the generated key and paste it into your .env file.

> [!IMPORTANT]
> Remember to create your database in order fill out the PostgreSQL environment variables inside the `.env` file.

```
SECRET_KEY=your-generated-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# PostgreSQL Database Configuration
DB_ENGINE=django.db.backends.postgresql
DB_NAME=your-database-name
DB_USER=your-database-user
DB_PASSWORD=your-database-password
DB_HOST=localhost
DB_PORT=5432
```

Replace the values with the following:

- **SECRET_KEY :** The key you generated
- **DB_NAME :** The database name
- **DB_USER :** The user for the database (e.g., postgres)
- **DB_PASSWORD:** The password set for that user

Everything else needs to stay the same.

## Step 5: Check Database Connection

Verify that Django can connect to your PostgreSQL database:

```bash
python manage.py check
```

**Expected output:**

```
System check identified no issues (0 silenced).
```

If you see any errors, double-check your `.env` file and database credentials.

## Step 6: Run Database Migrations

Once the connection check passes, initialize your database with Django's migration files:

```bash
python manage.py migrate
```

## Step 7: Create a Superuser Account

Create an admin account to access Django's admin panel:

```bash
python manage.py createsuperuser
```
