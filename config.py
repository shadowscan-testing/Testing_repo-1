DEBUG = True
SECRET_KEY = "django-insecure-fake-secret-key"

DATABASE = {
    "ENGINE": "django.db.backends.postgresql",
    "NAME": "prod_db",
    "USER": "postgres",
    "PASSWORD": "Postgres@123",
    "HOST": "127.0.0.1",
    "PORT": "5432"
}

AWS_ACCESS_KEY = "FAKEAWSACCESSKEY"
AWS_SECRET_KEY = "FAKEAWSSECRETKEY"

ALLOWED_HOSTS = ["*"]
