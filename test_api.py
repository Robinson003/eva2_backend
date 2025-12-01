import os
import django
from django.test import Client

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

client = Client()

endpoints = [
    '/api/',
    '/api/clientes/',
    '/api/productos/',
    '/api/ventas/',
    '/api/detalleventas/',
]

print("Verifying API endpoints...")
for endpoint in endpoints:
    response = client.get(endpoint)
    print(f"{endpoint}: {response.status_code}")
    if response.status_code != 200:
        print(f"Error accessing {endpoint}")
