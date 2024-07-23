import os

banco = {
    'dbname': os.getenv('POSTGRES_DB'),
    'user': os.getenv('POSTGRES_USER'),
    'host': os.getenv('POSTGRES_HOST'),
    'port': os.getenv('POSTGRES_PORT'),
    'password': os.getenv('POSTGRES_PASSWORD'),
}
credentialBorker = {
    'user': os.getenv('BROKER_USER'),
    'password': os.getenv('BROKER_PASSWORD'),
    'broker_host': os.getenv('BROKER_HOST'),
}
