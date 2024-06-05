import requests
from bs4 import BeautifulSoup

# URL del sitio web
url = "https://sports.caliente.mx/es_MX/EE.UU-MLS"

# Realizar la solicitud HTTP al sitio web
response = requests.get(url)

# Comprobar si la solicitud fue exitosa
if response.status_code == 200:
    # Analizar el contenido HTML de la página
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Buscar los contenedores que contienen la información de los partidos de la MLS
    match_containers = soup.find_all('tr', class_='mkt_content')
    
    if not match_containers:
        print("No se encontraron partidos de la MLS. Verifica los selectores.")
    else:
        # Recorrer los contenedores de partidos encontrados
        for container in match_containers:
            # Encontrar los nombres de los equipos y los momios
            teams = container.find_all('span', class_='seln-name')
            odds = container.find_all('span', class_='price dec')
            
            if len(teams) == 2 and len(odds) == 3:
                team1 = teams[0].text.strip()
                team2 = teams[1].text.strip()
                odd1 = odds[0].text.strip()
                draw = odds[1].text.strip()
                odd2 = odds[2].text.strip()
                
                # Imprimir la información en el formato deseado
                print(f"{team1}: {odd1}")
                print(f"Empate: {draw}")
                print(f"{team2}: {odd2}")
                print()
else:
    print(f"Error al acceder a la página: {response.status_code}")
