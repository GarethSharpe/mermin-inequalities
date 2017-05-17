'''
Quantum Protocols
written by Marcus Edwards on May 8, 2017
'''

from IBMQuantumExperience import IBMQuantumExperience
API_TOKEN = 'a0f9090f4b9b0a7f86cb31848730654bb4dbc35aab364a7d728162c96b264752d413b88daea7303c87f12e0a719345119c0f8a880a27d73b998887664a989fce'

def mermin_test(shots):
    '''
    Mermin's inequality test on the IBM Q.

    Open QASM:
    
        OPENQASM 2.0;
        include "qelib1.inc";
        
        qreg q[5];
        creg c[5];
        
        h q[1];
        cx q[1],q[2];
        h q[1];
        h q[4];
        cx q[4],q[2];
        h q[3];
        h q[4];
        cx q[3],q[2];
        h q[0];
        h q[3];
        cx q[0],q[2];
        h q[0];
        h q[2];
        sdg q[1];
        sdg q[4];
        h q[0];
        h q[1];
        h q[2];
        h q[3];
        h q[4];
        measure q[0] -> c[0];
        measure q[1] -> c[1];
        measure q[2] -> c[2];
        measure q[3] -> c[3];
        measure q[4] -> c[4];

        
        
    '''
    
    api = IBMQuantumExperience.IBMQuantumExperience(API_TOKEN)
    device = 'simulator'
    
    #Experiment registers and setup
    qasm = "IBMQASM 2.0;\n\ninclude \"qelib1.inc\";\nqreg q[5];\ncreg c[5];\nh q[1];\ncx q[1],q[2];\nh q[1];\nh q[4];\ncx q[4],q[2];\nh q[3];\nh q[4];\ncx q[3],q[2];\nh q[0];\nh q[3];\ncx q[0],q[2];\nh q[0];\nh q[2];\nsdg q[1];\nsdg q[4];\nh q[0];\nh q[1];\nh q[2];\nh q[3];\nh q[4];\nmeasure q[0] -> c[0];\nmeasure q[1] -> c[1];\nmeasure q[2] -> c[2];\nmeasure q[3] -> c[3];\nmeasure q[4] -> c[4];\n"
    exp = api.run_experiment(qasm, device, shots)

    return exp