#commands needed:
    #pip install pennylane --upgrade
    #pip install pennylane-qiskit
from pennylane import numpy as np
import pennylane as qml
from qiskit import QuantumRegister


#Input:
    #symbols - array of atomic symbols corresponding to the molecule being studied
    #coordinates - np.array() containing a list of coordinates as specified by
    #qml.qchem.molecular_hamiltonian() documentation
#Output:
    #Hamiltonian of the molecule
def getHamiltonian (symbols, coordinates):
    H, qubits = qml.qchem.molecular_hamiltonian(symbols, coordinates)
    return (H, qubits)


#Input: 
    #circuit - quantum circuit being used
    #electrons - number of electrons in the molecule
    #orbitals - number if spin orbitals. Also the size of the register initialized
#Outcome:
    #Initializes a quantum register in the Hartree-Fock state and adds it to the circuit
def getHartreeFockState (circuit, electrons, orbitals):
    HFState = qml.qchem.hf_state(electrons, orbitals)
    register = QuantumRegister(orbitals)
    circuit.add(register)

    for i in range(len(HFState)):
        if (HFState[i] == 1):
            circuit.x(register[i])