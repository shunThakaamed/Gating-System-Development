# your-repo/src/gating_system/core.py

class GatingSystem:
    def __init__(self):
        self.gates = {}

    def add_gate(self, gate_id, status=False):
        self.gates[gate_id] = status

    def remove_gate(self, gate_id):
        if gate_id in self.gates:
            del self.gates[gate_id]

    def open_gate(self, gate_id):
        if gate_id in self.gates:
            self.gates[gate_id] = True

    def close_gate(self, gate_id):
        if gate_id in self.gates:
            self.gates[gate_id] = False

    def is_gate_open(self, gate_id):
        return self.gates.get(gate_id, False)
