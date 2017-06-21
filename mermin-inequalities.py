'''
A test of the mermin inequalities on the IBM Q
written by Marcus Edwards on May 8, 2017
updated by Gareth Sharpe on June 19, 2017
'''

from IBMQuantumExperience import IBMQuantumExperience 
from protocols import *

API_TOKEN = 'a0f9090f4b9b0a7f86cb31848730654bb4dbc35aab364a7d728162c96b264752d413b88daea7303c87f12e0a719345119c0f8a880a27d73b998887664a989fce'

def test_api_auth_token():
    '''
    Authentication with Quantum Experience Platform
    '''
    api = IBMQuantumExperience.IBMQuantumExperience(API_TOKEN)
    credential = api._check_credentials()

    return credential

def connect():
    '''
    Attempt to connect to the Quantum Experience Platform
    ''' 
    connection_success = test_api_auth_token()

    if(connection_success == True):
        print("API authentication success.")
    else:
        print("API authentication failure.")
        exit()

def parity_check(i):
    i = i - ((i >> 1) & 0x55555555)
    i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
    i = (((i + (i >> 4)) & 0x0F0F0F0F) * 0x01010101) >> 24
    return int(i % 2)

def print_results(exp, basis):
    '''
    Print the distribution of measured results from the given experiment
    '''
    print("---------------------")
    print("RESULTS: " + basis.upper())
    print("---------------------")
    states = "State       | "
    probabilities = "Probability | "
    expected = 0
    for i in range(len(exp['result']['measure']['labels'])):
        state = exp['result']['measure']['labels'][i]
        probability = exp['result']['measure']['values'][i]
        outcome = int(state, 2)
        
        # parity check
        parity = parity_check(outcome)
        
        if parity:
            expected -= probability
        else:   
            expected += probability

        states += str(state) + " | " 
        probabilities += "{:.3f}".format(probability) + " | "
        
    print(states)
    print(probabilities)
    print("<" + basis.upper() + "> = ", "{:.3f}".format(expected))
    return expected

def test_3Q_sim():
    
    connect() #connect to IBM Q
    print("Mermin's inequality test.")
    
    exp, basis = mermin_test_sim(1000, 'xxx')
    print_results(exp, basis) 
    exp, basis = mermin_test_sim(1000, 'xyy')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1000, 'yxy')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1000, 'yyx')
    print_results(exp, basis)
    
def test_3Q_comp():
    
    connect() #connect to IBM Q
    print("Mermin's inequality test.")
    
    exp, basis = mermin_test_comp(1000, 'xxx')
    print_results(exp, basis) 
    exp, basis = mermin_test_comp(1000, 'xyy')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1000, 'yxy')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1000, 'yyx')
    print_results(exp, basis)

def test_4Q_sim():
    
    connect() #connect to IBM Q
    print("Mermin's inequality test.")
    
    exp, basis = mermin_test_sim(1000, 'xxxx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1000, 'xxyy')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1000, 'xyxy')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1000, 'xyyx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1000, 'yxxy')
    print_results(exp, basis)    
    exp, basis = mermin_test_sim(1000, 'yxyx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1000, 'yyxx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1000, 'yyyy')
    print_results(exp, basis)

def test_5Q_sim():
    
    connect() #connect to IBM Q
    print("Mermin's inequality test.")
    
    exp, basis = mermin_test_sim(1000, 'xxxxx')
    print_results(exp, basis)    
    exp, basis = mermin_test_sim(1000, 'xxxyy')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1000, 'xxyxy')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1000, 'xxyyx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1000, 'xyxxy')
    print_results(exp, basis)    
    exp, basis = mermin_test_sim(1000, 'xyxyx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1000, 'xyyxx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1000, 'xyyyy')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1000, 'yxxxy')
    print_results(exp, basis)    
    exp, basis = mermin_test_sim(1000, 'yxxyx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1000, 'yxyxx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1000, 'yxyyy')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1000, 'yyxxx')
    print_results(exp, basis)   
    exp, basis = mermin_test_sim(1000, 'yyxyy')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1000, 'yyyxy')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1000, 'yyyyx')
    print_results(exp, basis)

test_3Q_sim()
# test_4Q_sim()
# test_5Q_sim()

# test_3Q_comp()
