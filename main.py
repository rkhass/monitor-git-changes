"""Main script which monitors git status."""
import os
from typing import List

import telegram_send
from dotenv import load_dotenv
from git import Repo

load_dotenv(".env")


def get_changed_files(repo: Repo) -> List[str]:
    """Returns list of changed files."""
    return [item.a_path for item in repo.index.diff(None)]


def get_untracked_files(repo: Repo) -> List[str]:
    """Returns list of untracked files."""
    return repo.untracked_files


def format_text_to_print(lst1: List[str], lst2: List[str]) -> str:
    """Prepares readable report."""
    text = ""
    if len(lst2) > 0:
        text += "Files to commit:\n"
        text += format_bullet_list(lst1) + "\n"

    if len(lst2) > 0:
        text += "Untracked files:\n"
        text += format_bullet_list(lst2)

    if len(text) == 0:
        text += "Well done!"
    return text


def format_bullet_list(lst: List[str]) -> str:
    """Converts list of items to bullet list in text format."""
    text = ""
    for item in lst:
        text += f" - {item}\n"
    return text


if __name__ == "__main__":
    try:
        repo_paths = os.getenv("PATH_TO_REPO").replace(" ", "").split(",")
        for repo_path in repo_paths:
            repo = Repo(path=repo_path)

            changed_files = get_changed_files(repo)
            untracked_files = get_untracked_files(repo)
            report_text = format_text_to_print(lst1=changed_files, lst2=untracked_files)
            telegram_send.send(messages=[report_text])
    except Exception as e:
        telegram_send.send(messages=["Something went wrong...", "Error", str(e)])
