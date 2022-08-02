#commands needed:
    #pip install pennylane --upgrade
    #pip install pennylane-qiskit
    #pip install qiskit-nature
    #pip install pyscf
    
from pennylane import numpy as np
import pennylane as qml
from qiskit import QuantumCircuit, QuantumRegister
from qiskit_nature.drivers import UnitsType, Molecule
from qiskit_nature.drivers.second_quantization import (
    ElectronicStructureDriverType,
    ElectronicStructureMoleculeDriver,
)
from qiskit_nature.problems.second_quantization import ElectronicStructureProblem
from qiskit_nature.converters.second_quantization import QubitConverter
from qiskit_nature.mappers.second_quantization import JordanWignerMapper, ParityMapper



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
    circuit.add_register(register)

    for i in range(len(HFState)):
        if (HFState[i] == 1):
            circuit.x(register[i])





#DEBUG CODE BELOW

# circuit = QuantumCircuit()
# getHartreeFockState(circuit, 2, 4)
# print(circuit)

# (x,y) = getHamiltonian(["H"], np.array([0.0, 0.0, 0.0]))
# print(x)
# print(y)
# print(x.coeffs)
# print(x.ops)

molecule = Molecule(geometry=["H", [0.0, 0.0, 0.0]], charge=0, multiplicity=1)
driver = ElectronicStructureMoleculeDriver(
    molecule, basis="sto3g", driver_type=ElectronicStructureDriverType.PYSCF
)
es_problem = ElectronicStructureProblem(driver)
second_q_op = es_problem.second_q_ops()
print(second_q_op[0])