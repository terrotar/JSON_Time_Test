
import pytest

import time

from . import poke_api


# Test get prokemon with capital letter
def test_capital_letter_pokemon():
    start = time.time()
    poke = poke_api.Pokemon()
    poke = poke.get_pokemon("charmandeR")
    end = time.time()
    print(int((end-start) % 60))
    assert "not found" in poke


# Test get prokemon with invalid input
def test_invalid_input__pokemon():
    start = time.time()
    poke = poke_api.Pokemon()
    poke = poke.get_pokemon("teste02")
    end = time.time()
    print(int((end-start) % 60))
    assert "not found" in poke
