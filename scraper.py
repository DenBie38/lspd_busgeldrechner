import requests
from bs4 import BeautifulSoup
import json

# URL der Seite, von der du die Daten abrufen möchtest
url = 'https://gta5grand.com/forum/threads/947959/'

response = requests.get(url)

# Wenn die Seite erfolgreich geladen wurde
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Beispiel: Alle Bußgelder extrahieren (passt die Selektoren an, je nachdem, wie die Daten strukturiert sind)
    violations = []

    # Dies ist ein Platzhalter für das Scraping - Passe den Code an, um die relevanten Daten zu extrahieren
    # Zum Beispiel: Wenn die Verstöße in <li> oder <div> Tags enthalten sind, musst du die richtigen Selektoren verwenden
    violation_elements = soup.find_all('div', class_='post-text')  # Beispiel

    for element in violation_elements:
        # Dies muss angepasst werden, um die richtigen Strafen und Verstöße zu extrahieren
        violation_text = element.get_text().strip()
        if violation_text:  # Stelle sicher, dass es nicht leer ist
            violations.append({
                "violation": violation_text.split(":")[0],  # Verstoßname (passen)
                "fine": int(violation_text.split(":")[1].strip().replace('$', '').replace(' ', ''))  # Strafe (passen)
            })

    # Speichern der Daten in einer JSON-Datei
    with open('violations.json', 'w') as file:
        json.dump(violations, file, ensure_ascii=False, indent=4)
else:
    print("Fehler beim Abrufen der Seite!")
