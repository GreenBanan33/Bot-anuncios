import subprocess
import sys
import time

# Forzar la instalación de Chromium al iniciar el script en Render
try:
    print("Instalando navegador Chromium...")
    subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"], check=True)
except Exception as e:
    print(f"Error al instalar Chromium: {e}")

from playwright.sync_api import sync_playwright

def ejecutar_bot():
    print("Iniciando bot...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        url = "https://greenbanan33.github.io/Automatizacion-Prueba/"
        
        for i in range(1000):
            try:
                print(f"Ejecución #{i + 1}")
                page.goto(url, wait_until="networkidle")

                with context.expect_page(timeout=5000) as nueva_pestana_info:
                    page.click("iframe, a, ins, button")

                nueva_pestana = nueva_pestana_info.value
                nueva_pestana.close()
            except Exception:
                pass

            time.sleep(0.5)

        browser.close()

if __name__ == "__main__":
    ejecutar_bot()
