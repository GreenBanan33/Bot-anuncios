import time
from playwright.sync_api import sync_playwright

def ejecutar_bot():
    print("Iniciando bot...")
    with sync_playwright() as p:
        # Se ejecuta sin interfaz gráfica en el servidor (headless=True)
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        url = "https://greenbanan33.github.io/Automatizacion-Prueba/"
        
        for i in range(1000):
            try:
                print(f"Ejecución #{i + 1}")
                page.goto(url, wait_until="networkidle")

                # Espera a que al hacer clic se intente abrir la nueva pestaña
                with context.expect_page(timeout=5000) as nueva_pestana_info:
                    # Busca el elemento de anuncio o botón
                    page.click("iframe, a, ins, button")

                nueva_pestana = nueva_pestana_info.value
                nueva_pestana.close()
            except Exception as e:
                # Si falla o no se abre pestaña nueva, continúa el bucle
                pass

            time.sleep(0.5) # Espera medio segundo entre clics

        browser.close()

if __name__ == "__main__":
    ejecutar_bot()
