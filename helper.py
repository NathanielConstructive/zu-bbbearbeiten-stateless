from dataclasses import dataclass
import datetime

# Globale Liste für To-Do-Items
items = []


@dataclass
class Item:
    text: str
    date: datetime.date
    isCompleted: bool = False


def add(text, date_str):
    """
    Fügt ein neues To-Do hinzu und sortiert die Liste nach Datum.
    """
    # Text verarbeiten (B --> Bbb)
    text = text.replace('b', 'bbb').replace('B', 'Bbb')

    # Datum parsen
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()

    # Item erstellen und hinzufügen
    items.append(Item(text, date))

    # Liste nach Datum sortieren
    items.sort(key=lambda x: x.date)


def get_all():
    """
    Gibt alle To-Do-Items zurück.
    """
    return items


def get(index):
    """
    Gibt ein bestimmtes To-Do anhand seines Indexes zurück.
    """
    return items[index]


def update(index):
    """
    Aktualisiert den Status eines To-Do-Items (Completed/Not Completed).
    """
    items[index].isCompleted = not items[index].isCompleted
