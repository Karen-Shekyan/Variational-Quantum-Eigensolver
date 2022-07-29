from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute
from qiskit import Aer
import numpy as np


#function to change bool String to integer
def boolStringToInt(array):
    integer = 0
    for i in range(0, len(array)):
        if (array[i] == "1"):
            integer += 2^i
    return integer

#Measeurement algorithm for energy
def measureExpectationValue(array, standardError, circuit):
    totalH = 0.00
    counter = 0

    #simulation of measurement results
    measurement = ClassicalRegister(len(array))
    circuit.measure(input, measurement)
    simulator = Aer.get_backend('aer_simulator')

    #runs 1/standard error squared times for standard error given
    simulation = execute(circuit, simulator, shots=(1/standardError)^2)
    mresult = simulation.result()
    counts = mresult.get_counts(circuit)
    for(measured_state, count) in counts.items():
        counter += count
        intM = boolStringToInt(measured_state)
        totalH += intM * count
    #Find expectationValue for given set of Pauli Strings for energies
    expectationValue = totalH / counter
    return expectationValue



def VQE(numberOfQubits, theta, standardError):

    #theta is an initial angle
    #epsilon is target standard error 
    register = QuantumRegister(numberOfQubits)
    circuit = QuantumCircuit(register)
    

    #This b should be true until optimizer reaches some value
    b = False
    while (b):
        thetaH = {}
        for i in range(numberOfQubits^4):
            #dictionary to store theta and expectation energy values
            totalH = 0.00
            numberOfIterations = 0

            #prepare state function of theta[i]
            for qubit in register:
                circuit.rx(theta, qubit)
                circuit.ry(theta, qubit)

            #entangled anzatz states preparation
            for k in range(len(register) - 1):
                circuit.cx(register[k], register[k+1])
            
            #measurement and pauli strings rotation

        #Expectation value for pauli strings???
        expectationValue = measureExpectationValue(PauliStrings, standardError)
        thetaH[theta] = expectationValue
        #find newtheta from optimizer
    return thetaH
