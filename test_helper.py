import datetime
import pytest
import random
import helper


def test_category():
    # Given: I have todos with different categories
    todos = [
        ("Kabelsalat auflösen", "Hausarbeit"),
        ("Wäsche machen", "Hausarbeit"),
        ("Trash Core-Album aufnehmen", "Kunst"),
        ("Französisch lernen", "Hausaufgaben"),
    ]

    # When: I add the items
    for todo in todos:
        month = random.randrange(1, 13)
        day = random.randrange(1, 29)
        helper.add(todo[0], date=f"2023-{month}-{day}", category=todo[1])

    # Then: They ought to have their categories
    for item in helper.items:
        categories = [todo[1] for todo in todos]
        assert item.category in categories


def test_description():
    # Given: I have todos with descriptions
    todos = [
        (
            "Zeitmaschine bauen",
            "Vergangenheit kompilieren, Gegenwart laufen lassen, Zukunft debuggen",
        ),
        (
            "AI-Nebenprojekt",
            "Eine unglaublich nervige AI trainieren, die den Benutzer nur veräppelt",
        ),
    ]

    # When: I add the items
    for todo in todos:
        helper.add(todo[0], description=todo[1])

    # Then: They should have descriptions
    for item in helper.items:
        assert item.description is not None


def test_sort():
    # Given: I have several to-dos with dates
    todos = [
        ("Universum debuggen", "2023-09-06"),
        ("Sinn des Lebens entdecken", "2023-09-01"),
        ("Superheld werden", "2023-10-25"),
        ("Netto null", "2050-01-01"),
    ]

    # When: I add the items
    for todo in todos:
        helper.add(todo[0], todo[1])

    # Then: They should be sorted by date
    for i in range(len(helper.items) - 1):
        assert helper.items[i].date <= helper.items[i + 1].date


def test_add():
    # Given: I want to add a to-do with a date
    text = "Lorem ipsum"
    date = "2023-09-02"

    # When: I add the item
    helper.add(text, date)

    # Then: The most recently added to-do should have a date
    item = helper.items[-1]
    assert isinstance(item.date, datetime.date)
