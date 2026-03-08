import os
from anthropic import Anthropic


def analyze_lausunto(text):

    api_key = os.getenv("ANTHROPIC_API_KEY")

    client = Anthropic(api_key=api_key)

    prompt = f"""
Analysoi seuraava lausuntopyyntö ja tee siitä tiivis yhteenveto.

Lausunto:
{text}

Vastaa:
- pääaihe
- keskeiset muutokset
- vaikutukset
"""

    message = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=500,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return message.content[0].text


if __name__ == "__main__":

    sample_text = """
Laki 380/2023 koskee digitaalisten palveluiden saavutettavuutta
ja velvoittaa viranomaisia parantamaan verkkopalveluiden
käytettävyyttä.
"""

    result = analyze_lausunto(sample_text)

    print(result)
