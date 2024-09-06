from qiskit import QuantumCircuit, transpile, QuantumRegister
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, plot_state_city
import qiskit.quantum_info as qi

import numpy as np

def prepare_bb84(bit, basis, idx, qc):
    if basis == 0:
        if bit == 0:
            standard(qc, idx)
        else:
            standard_flip(qc, idx)
    else:
        if bit == 0:
            diagonal(qc, idx)
        else:
            diagonal_flip(qc, idx)
    return qc

def standard(qc, idx):
    return qc

def standard_flip(qc, idx):
    qc.x(idx)
    return qc

def diagonal(qc, idx):
    qc.h(idx)
    return qc

def diagonal_flip(qc, idx):
    qc.x(idx)
    qc.h(idx)
    return qc

def bit_basis_to_bb84(bit, basis):
    if (bit, basis) == (0, 0):
        return "0"
    elif (bit, basis) == (1, 0):
        return "1"
    elif (bit, basis) == (0, 1):
        return "+"
    elif (bit, basis) == (1, 1):
        return "-"
    else:
        raise ValueError("Invalid bit and basis")
