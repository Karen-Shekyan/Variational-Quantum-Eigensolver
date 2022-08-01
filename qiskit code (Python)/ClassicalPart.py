#commands needed:
    #pip install qiskit-nature
    #pip install numpy

import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import Aer
from qiskit.algorithms.optimizers import COBYLA
from qiskit.algorithms import VQE
from qiskit_nature.algorithms import (GroundStateEigensolver,
                                      NumPyMinimumEigensolverFactory)
from qiskit_nature.drivers import Molecule
from qiskit_nature.drivers.second_quantization import (
    ElectronicStructureMoleculeDriver, ElectronicStructureDriverType)
from qiskit_nature.transformers.second_quantization.electronic import FreezeCoreTransformer
from qiskit_nature.problems.second_quantization import ElectronicStructureProblem
from qiskit_nature.converters.second_quantization import QubitConverter
from qiskit_nature.mappers.second_quantization import ParityMapper
import numpy as np
from qiskit_nature.circuit.library import UCCSD, HartreeFock
from qiskit.circuit.library import EfficientSU2
from qiskit.algorithms.optimizers import COBYLA, SPSA, SLSQP
from qiskit.opflow import TwoQubitReduction
from qiskit import BasicAer, Aer
from qiskit.utils import QuantumInstance
from qiskit.utils.mitigation import CompleteMeasFitter
from qiskit.providers.aer.noise import NoiseModel


np.random.seed(999999)
p0 = np.random.random()
target_distr = {0: p0, 1: 1-p0}
backend = Aer.get_backend("aer_simulator")

##################################################################################################
#                     FUNCTIONS TO BE USED HERE. THE REST ARE HELPER METHODS                     #
##################################################################################################

#Input:
    #params - numpy array containing parameters to be optimized
#Output:
    #returns a numpy array containing optimized parameters
def optimizeParams(objective_function, params=np.array([])):
    optimizer = COBYLA(maxiter=500, tol=0.0001)
    result = optimizer.minimize(fun=objective_function, x0=params)
    return result.x

#Input:
    #electrons - number of electrons in simulated molecule
    #orbitals - number of orbitals in simulated molecule. This is also the size of the
    #quantum register initialized
    #circuit - quantum circuit in which the Hartree-Fock state will be initialized
#Outcome:
    #creates a quantum register in the Hartree-Fock state and adds it to the circuit
def getHartreeFockState(electrons, orbitals, circuit):
    register = QuantumRegister(orbitals)
    circuit.add_register(register)
    for i in range(electrons):
        circuit.x(register[i])
    return

##################################################################################################
#                     FUNCTIONS TO BE USED HERE. THE REST ARE HELPER METHODS                     #
##################################################################################################

# def get_var_form(params):
#     qr = QuantumRegister(1, name="q")
#     cr = ClassicalRegister(1, name='c')
#     qc = QuantumCircuit(qr, cr)
#     qc.u(params[0], params[1], params[2], qr[0])
#     qc.measure(qr, cr[0])
#     return qc


# def counts_to_distr(counts):
#     """Convert Qiskit result counts to dict with integers as
#     keys, and pseudo-probabilities as values."""
#     n_shots = sum(counts.values())
#     return {int(k, 2): v/n_shots for k, v in counts.items()}


# def objective_function(params):
#     """Compares the output distribution of our circuit with
#     parameters `params` to the target distribution."""
#     # Create circuit instance with paramters and simulate it
#     qc = get_var_form(params)
#     result = backend.run(qc).result()
#     # Get the counts for each measured state, and convert
#     # those counts into a probability dict
#     output_distr = counts_to_distr(result.get_counts())
#     # Calculate the cost as the distance between the output
#     # distribution and the target distribution
#     cost = sum(
#         abs(target_distr.get(i, 0) - output_distr.get(i, 0))
#         for i in range(2**qc.num_qubits)
#     )
#     return cost



#DEBUG CODE BELOW
# circuit = QuantumCircuit()
# getHartreeFockState(2, 4, circuit)
# print(circuit)
# print(optimizeParams(np.random.rand(3)))
# print(type(optimizeParams(np.random.rand(3))))