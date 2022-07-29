"""Main script which monitors git status."""
import os
from typing import List

import telegram
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


def send_text_to_chat(text: str) -> None:
    """Sends text to the chat.

    :param text: input text
    """
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    bot = telegram.Bot(os.getenv("TELEGRAM_TOKEN"))

    for pos in range(0, len(text), 4096):
        bot.send_message(
            chat_id, text[pos : pos + 4096], parse_mode=telegram.ParseMode.HTML
        )


def get_location_title() -> str:
    """Returns location title."""
    name = os.getenv("LOCATION_NAME")
    if name != "":
        name = f"<b>Location: {name}</b>\n"
    return name


def get_repo_name(repo: Repo):
    """Returns formatted repo name."""
    name = repo.working_dir.split("/")[-1]
    repo_name_fmt = f"<b>Repo:</b> {name}\n\n"
    return repo_name_fmt


if __name__ == "__main__":
    try:
        repo_paths = os.getenv("REPOS_TO_MONITOR").replace(" ", "").split(",")
        for repo_path in repo_paths:
            repo = Repo(path=repo_path)
            repo_name = get_repo_name(repo)

            changed_files = get_changed_files(repo)
            untracked_files = get_untracked_files(repo)

            header = get_location_title() + get_repo_name(repo)
            report_text = format_text_to_print(lst1=changed_files, lst2=untracked_files)
            send_text_to_chat(text=header + report_text)
    except Exception as e:
        send_text_to_chat(text=f"Something went wrong...\n Error\n {e}")
