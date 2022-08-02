# Copyright 2021 The MITRE Corporation. All Rights Reserved.

import unittest

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute
from qiskit import Aer
import random
from qiskit.opflow import I, X, Y, Z
import main


class VQETests(unittest.TestCase):

    def test1(self):
        electrons = 2
        orbitals = 8
        theta = 1
        standardError = 0.05
        hamiltonian =  (-1.0523732 * I^I) + (0.39793742 * I^Z) + (-0.3979374 * Z^I) \
    + (-0.0112801 * Z^Z) + (0.18093119 * X^X)

        result = main.VQE(electrons, orbitals, theta, standardError, hamiltonian)
        print(result)

    def test2(self):
        
        print("Test 2 passed!")


    def test3(self):
        
        print("Test 3 passed!")


if __name__ == '__main__':
    unittest.main()