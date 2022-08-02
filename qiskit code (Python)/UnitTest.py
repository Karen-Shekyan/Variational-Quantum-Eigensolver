# Copyright 2021 The MITRE Corporation. All Rights Reserved.

import unittest

# from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
# from qiskit import execute
# from qiskit import Aer
# import random
# import pennylane
import testing
from qiskit.opflow import I, X, Y, Z
import main
import numpy as np


class VQETests(unittest.TestCase):

    def test1(self):
        if testing.boolStringToInt("1000") != 1:
            {
            self.fail(f"You were suppose to measure a 3 but you got 1")
            }
        print("Test 1 passed!")
        electrons = 2
        orbitals = 8

        thetaArray = np.array([])
        for i in range(orbitals*2):
            thetaArray = np.append(thetaArray, [1])

        # print(thetaArray)
        standardError = 0.5
        hamiltonian =  (-1.0523732 * I^I) + (0.39793742 * I^Z) + (-0.3979374 * Z^I) \
    + (-0.0112801 * Z^Z) + (0.18093119 * X^X)

        result = main.VQE(electrons, orbitals, standardError, thetaArray, hamiltonian)
        print("\n")
        print(result)

    def test2(self):
        
        # print("Test 2 passed!")
        return


    def test3(self):
        
        # print("Test 3 passed!")
        return


if __name__ == '__main__':
    unittest.main()