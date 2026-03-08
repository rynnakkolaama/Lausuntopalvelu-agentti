from anthropic import Anthropic
import os

def analyze_lausunto(title, content, url):
    """Analysoi lausuntopyynnön Claude API:lla"""
    
    api_key = os.getenv("CLAUDE_API_KEY")
    client = Anthropic()
    
    prompt = f"""
Analysoi seuraava lausuntopyyntö ja määritä, liittyykö se lakiin 380/2023 
(työvoimapalveluiden järjestämislaki).

Otsikko: {title}

Sisältö: {content}

URL: {url}

Vastaa seuraavassa muodossa:
1. Liittyytkö lakiin 380/2023? (KYLLÄ/EI/MAHDOLLISESTI)
2. Perustelu (1-2 lausetta)
3. Relevantit kohdat (jos löytyy)

Ole tarkka ja ammattimainen analyysissa.
"""
    
    try:
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=500,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return message.content[0].text
    except Exception as e:
        return f"Analyysivirhe: {str(e)}"

if __name__ == "__main__":
    # Testaus
    result = analyze_lausunto(
        "Testiotsikko",
        "Testisisältö",
        "https://example.com"
    )
    print(result)
