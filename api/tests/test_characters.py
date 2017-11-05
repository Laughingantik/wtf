# pylint: disable=missing-docstring,invalid-name
from mock import patch, Mock
from api.characters import Character


def test_character_defaults():
    character = Character()
    assert character.name is None
    assert character.level == 1
    assert character.exp == 0
    assert character.health == 1
    assert character.health_max == 1


def test_character_construction():
    character = Character(
        name='foobar',
        level=23,
        exp=123,
        health=42,
        health_max=100
    )
    assert character.name == 'foobar'
    assert character.level == 23
    assert character.exp == 123
    assert character.health == 42
    assert character.health_max == 100


def test_character_setters():
    character = Character()
    character.name = 'foobar'
    assert character.name == 'foobar'
    character.level = 23
    assert character.level == 23
    character.exp = 123
    assert character.exp == 123
    character.health = 42
    assert character.health == 42
    character.health_max = 100
    assert character.health_max == 100
