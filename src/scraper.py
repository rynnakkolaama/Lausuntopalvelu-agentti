import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_lausunto_page():
    """Hakee lausuntopalvelu.fi-sivun"""
    url = "https://www.lausuntopalvelu.fi/FI"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'utf-8'
        return response.text
    except Exception as e:
        print(f"Virhe sivun lataamisessa: {e}")
        return None

def parse_lausunnot(html_content):
    """Jäsentää HTML:n ja etsii lausuntopyynnöt"""
    if not html_content:
        return []
    
    soup = BeautifulSoup(html_content, 'html.parser')
    lausunnot = []
    
    # Etsii lausuntopyynnöt sivulta
    # Huomio: rakenne voi vaihdella, tämä on template
    items = soup.find_all('div', class_=['lausunto-item', 'request-item'])
    
    for item in items:
        try:
            title = item.find('h3') or item.find('h2')
            link = item.find('a')
            
            if title and link:
                lausunnot.append({
                    'title': title.get_text(strip=True),
                    'url': link.get('href'),
                    'content': item.get_text(strip=True),
                    'timestamp': datetime.now().isoformat()
                })
        except Exception as e:
            print(f"Virhe lausunnon jäsentelyssä: {e}")
            continue
    
    return lausunnot

if __name__ == "__main__":
    html = fetch_lausunto_page()
    lausunnot = parse_lausunnot(html)
    print(f"Löydettiin {len(lausunnot)} lausuntopyyntöä")
