import requests
import os
import time

API_KEY = os.environ.get("PHANTOM_API_KEY")
ENDPOINT = f"https://a.phantomjscloud.com/single/browser/v2/{API_KEY}/"

payload = {
    "url": "https://greenbanan33.github.io/Automatizacion-Prueba/",
    "renderType": "plainText",
    "requestSettings": {
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    },
    "scripts": {
        "domReady": [
            "document.querySelector('iframe, a, ins')?.click();"
        ]
    }
}

TOTAL_REPETICIONES = 10

print(f"Iniciando bucle en PhantomJS Cloud ({TOTAL_REPETICIONES} ejecuciones)...")

for i in range(TOTAL_REPETICIONES):
    try:
        response = requests.post(ENDPOINT, json=payload)
        if response.status_code == 200:
            print(f"Ejecución #{i + 1} exitosa.")
        else:
            print(f"Ejecución #{i + 1} falló: {response.status_code}")
    except Exception as e:
        print(f"Error en ejecución #{i + 1}: {e}")
    
    time.sleep(2)

print("Bucle finalizado.")
