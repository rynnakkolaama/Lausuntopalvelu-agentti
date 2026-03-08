import os
from github import Github

def create_issue(title, body, labels=None):
    """Luo GitHub Issuen repositorioon"""
    
    github_token = os.getenv("GITHUB_TOKEN")
    if not github_token:
        raise ValueError("GITHUB_TOKEN ei asetettu")
    
    g = Github(github_token)
    repo = g.get_user().get_repo("lausunto-ai-agent")
    
    try:
        issue = repo.create_issue(
            title=title,
            body=body,
            labels=labels or []
        )
        print(f"Issue luotu: {issue.html_url}")
        return issue
    except Exception as e:
        print(f"Virhe Issuen luomisessa: {e}")
        return None

if __name__ == "__main__":
    body = """
## Lausuntopyyntö löydetty

Laki 380/2023 (työvoimapalveluiden järjestämislaki) liittyvä lausuntopyyntö.

- URL: https://example.com
- Analyysi: Tämä liittyy lakiin 380/2023
"""
    create_issue("Lausuntopyyntö: Laki 380/2023", body, labels=["380/2023"])
