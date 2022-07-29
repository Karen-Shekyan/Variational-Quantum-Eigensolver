# Tests for Lab 12: Deutsch-Jozsa Algorithm
# Copyright 2021 The MITRE Corporation. All Rights Reserved.

import unittest

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute
from qiskit import Aer
import random
import pennylane
import testing

class VQETests(unittest.TestCase):

    def test1(self):
        if testing.boolStringToInt("1000") != 1:
            {
            self.fail(f"You were suppose to measure a 3 but you got 1")
            }
        print("Test 1 passed!")


    def test2(self):
        
        print("Test 2 passed!")


    def test3(self):
        
        print("Test 3 passed!")


if __name__ == '__main__':
    unittest.main()