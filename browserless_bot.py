import requests
import time

url = "https://production-sfo.browserless.io/chrome/bql?token=2VTyl6jEXx4Mr0L56772103aff586496d00f0e905bda30315&proxy=residential&proxySticky=true&proxyCountry=us&humanlike=true"
headers = {"Content-Type": "application/json"}

query = """
mutation {
  newPage {
    id
  }
  viewport(width: 1366, height: 768) {
    width
    height
    time
  }
  goto(url: "https://greenbanan33.github.io/Automatizacion-Prueba/") {
    status
  }
  click(selector: "iframe, a, ins") {
    selector
    time
    x
    y
  }
  closePage
}
"""

data = {"query": query, "variables": {}}

for i in range(1, 101):
    print(f"Ejecución #{i} (Página nueva)")
    try:
        response = requests.post(url, json=data, headers=headers, timeout=30)
        print(f"Respuesta #{i}: {response.status_code}")
    except Exception as e:
        print(f"Error en la ejecución #{i}: {e}")
    time.sleep(1)
