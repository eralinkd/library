import re
from pathlib import Path
import os

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_books():
    """
    Returns a list of all names of library books.
    """
    BASE_DIR = Path(__file__).resolve().parent.parent
    filepath = os.path.join(BASE_DIR, "media")
    files = os.listdir(filepath)
    return list(sorted(files))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None
