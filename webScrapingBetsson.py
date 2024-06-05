import requests
from bs4 import BeautifulSoup

# URL del sitio web
url = "https://www.betsson.mx/apuestas-deportivas/futbol/usa/eeuu-mls"

# Realizar la solicitud HTTP al sitio web
response = requests.get(url)

# Comprobar si la solicitud fue exitosa
if response.status_code == 200:
    # Analizar el contenido HTML de la página
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Buscar el contenedor que contiene las opciones de apuestas
    betting_options_container = soup.find('div', class_='obg-market-selection-group')
    
    # Verificar si se encontró el contenedor de opciones de apuestas
    if betting_options_container:
        # Buscar todas las opciones de apuestas dentro del contenedor
        betting_options = betting_options_container.find_all('div', class_='obg-outcome')
        
        # Verificar si se encontraron opciones de apuestas
        if betting_options:
            for option in betting_options:
                # Obtener el nombre del equipo
                team_name = option.find('span', class_='obg-outcome-name').text.strip()
                
                # Obtener el momio del equipo
                odds = option.find('span', class_='obg-outcome-odds').text.strip()
                
                # Imprimir la información del equipo y su momio
                print(f"{team_name}: {odds}")
        else:
            print("No se encontraron opciones de apuestas.")
    else:
        print("No se encontró el contenedor de opciones de apuestas.")
else:
    print(f"Error al acceder a la página: {response.status_code}")
