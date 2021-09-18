
import pytest

from . import poke_api


# Test get prokemon with capital letter
def test_capital_letter_pokemon():
    poke = poke_api.Pokemon()
    poke = poke.get_pokemon("charmandeR")
    assert "not found" in poke
