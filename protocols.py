'''
Quantum Protocols
written by Marcus Edwards on May 8, 2017
written by Gareth Sharpe on June 19-21, 2017
'''

from IBMQuantumExperience import IBMQuantumExperience
API_TOKEN = 'a0f9090f4b9b0a7f86cb31848730654bb4dbc35aab364a7d728162c96b264752d413b88daea7303c87f12e0a719345119c0f8a880a27d73b998887664a989fce'

def mermin_test_sim(shots, basis):
    
    api = IBMQuantumExperience.IBMQuantumExperience(API_TOKEN)
    device = 'simulator'
    n = len(basis)
    
    i = 0
    if n == 5:
        #Experiment registers and setup
        qasm = """IBMQASM 2.0;include "qelib1.inc";qreg q[5];creg c[5];h q[1];cx q[1],q[2];h q[1];h q[4];cx q[4],q[2];h q[3];h q[4];cx q[3],q[2];h q[0];h q[3];cx q[0],q[2];h q[0];h q[2];"""
    elif n == 4:
        i = 1
        qasm = """IBMQASM 2.0;include "qelib1.inc";qreg q[5];creg c[5];h q[1];x q[2];h q[3];h q[4];cx q[1],q[2];cx q[3],q[2];cx q[4],q[2];h q[1];h q[2];h q[3];h q[4];"""
    else:
        qasm = """IBMQASM 2.0;include "qelib1.inc";qreg q[5];creg c[5];h q[0];h q[1];x q[2];cx q[1],q[2];cx q[0],q[2];h q[0];h q[1];h q[2];"""
        
    for term in basis:
        if term == 'Y' or term == 'y':
            qasm += "sdg q[" + str(i) + "];"
        i += 1;
    
    if n == 5:
        qasm += "h q[0];h q[1];h q[2];h q[3];h q[4];measure q[0] -> c[0];measure q[1] -> c[1];measure q[2] -> c[2];measure q[3] -> c[3];measure q[4] -> c[4];"
    elif n == 4:
        qasm += "h q[1];h q[2];h q[3];h q[4];measure q[1] -> c[1];measure q[2] -> c[2];measure q[3] -> c[3];measure q[4] -> c[4];"
    else:
        qasm += "h q[0];h q[1];h q[2];measure q[0] -> c[0];measure q[1] -> c[1];measure q[2] -> c[2];"
        
    exp = api.run_experiment(qasm, device, shots)

    return exp, basis

def mermin_test_comp(shots, basis):
    
    api = IBMQuantumExperience.IBMQuantumExperience(API_TOKEN)
    device = 'ibmqx2'
    n = len(basis)
    
    i = 0
    if n == 5:
        #Experiment registers and setup
        qasm = """IBMQASM 2.0;include "qelib1.inc";qreg q[5];creg c[5];h q[1];cx q[1],q[2];h q[1];h q[4];cx q[4],q[2];h q[3];h q[4];cx q[3],q[2];h q[0];h q[3];cx q[0],q[2];h q[0];h q[2];"""
    elif n == 4:
        i = 1
        qasm = """IBMQASM 2.0;include "qelib1.inc";qreg q[5];creg c[5];h q[1];x q[2];h q[3];h q[4];cx q[1],q[2];cx q[3],q[2];cx q[4],q[2];h q[1];h q[2];h q[3];h q[4];"""
    else:
        qasm = """IBMQASM 2.0;include "qelib1.inc";qreg q[5];creg c[5];h q[0];h q[1];x q[2];cx q[1],q[2];cx q[0],q[2];h q[0];h q[1];h q[2];"""
        
    for term in basis:
        if term == 'Y' or term == 'y':
            qasm += "sdg q[" + str(i) + "];"
        i += 1;
    
    if n == 5:
        qasm += "h q[0];h q[1];h q[2];h q[3];h q[4];measure q[0] -> c[0];measure q[1] -> c[1];measure q[2] -> c[2];measure q[3] -> c[3];measure q[4] -> c[4];"
    elif n == 4:
        qasm += "h q[1];h q[2];h q[3];h q[4];measure q[1] -> c[1];measure q[2] -> c[2];measure q[3] -> c[3];measure q[4] -> c[4];"
    else:
        qasm += "h q[0];h q[1];h q[2];measure q[0] -> c[0];measure q[1] -> c[1];measure q[2] -> c[2];"
        
    exp = api.run_experiment(qasm, device, shots)

    return exp, basis

