import os
from github import Github


def create_issue(title, body, labels=None):

    token = os.getenv("GITHUB_TOKEN")

    repo_name = os.getenv("GITHUB_REPOSITORY")

    g = Github(token)

    repo = g.get_repo(repo_name)

    repo.create_issue(
        title=title,
        body=body,
        labels=labels or []
    )


if __name__ == "__main__":

    body = """
### Lausunnon analyysi

Tämä on automaattisesti luotu issue tekoälyagentilta.
"""

    create_issue(
        "Lausuntopyyntö: Laki 380/2023",
        body,
        labels=["lausunto"]
    )
