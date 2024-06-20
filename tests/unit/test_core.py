# your-repo/tests/unit/test_core.py

import pytest
from src.gating_system.core import GatingSystem

def test_add_gate():
    gs = GatingSystem()
    gs.add_gate('gate1')
    assert 'gate1' in gs.gates

def test_remove_gate():
    gs = GatingSystem()
    gs.add_gate('gate1')
    gs.remove_gate('gate1')
    assert 'gate1' not in gs.gates

def test_open_gate():
    gs = GatingSystem()
    gs.add_gate('gate1')
    gs.open_gate('gate1')
    assert gs.is_gate_open('gate1')

def test_close_gate():
    gs = GatingSystem()
    gs.add_gate('gate1')
    gs.open_gate('gate1')
    gs.close_gate('gate1')
    assert not gs.is_gate_open('gate1')

def test_is_gate_open():
    gs = GatingSystem()
    gs.add_gate('gate1')
    assert not gs.is_gate_open('gate1')
    gs.open_gate('gate1')
    assert gs.is_gate_open('gate1')
