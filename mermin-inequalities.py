'''
A test of the mermin inequalities on the IBM Q
created by Marcus Edwards on May 8, 2017
written by Gareth Sharpe on June 19-23, 2017
finalized by Gareth Sharpe on June 23, 2017
adapted for ibmqx4 by Marcus Edwards on November 9, 2017

@author: Gareth Sharpe
@author: Marcus Edwards
'''

from IBMQuantumExperience import IBMQuantumExperience 
from protocols import *
from math import fabs

API_TOKEN = 'a0f9090f4b9b0a7f86cb31848730654bb4dbc35aab364a7d728162c96b264752d413b88daea7303c87f12e0a719345119c0f8a880a27d73b998887664a989fce'

def test_api_auth_token():
    '''
    Authentication with Quantum Experience Platform
    '''
    api = IBMQuantumExperience(API_TOKEN)
    credential = api.check_credentials()

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
    print()
    return expected

def mermin_3Q_sim():
    
    connect() #connect to IBM Q
    print("Mermin's inequality test.\n")
    
    exp, basis = mermin_test_sim(1024, 'xyy')
    expected_xyy = print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'xxx')
    expected_xxx = print_results(exp, basis) 

    
    expected = (expected_xyy * 3) - expected_xxx
    print("<M3>exp = " + str(expected))
    
def mermin_3Q_comp():
    
    connect() #connect to IBM Q
    print("Mermin's inequality test.\n")
    
    exp, basis = mermin_test_comp(8192, 'xyy')
    expected_xyy = print_results(exp, basis)
    exp, basis = mermin_test_comp(8192, 'xxx')
    expected_xxx = print_results(exp, basis) 
    
    expected = (expected_xyy * 3) - expected_xxx
    print("<M3>exp = " + str(expected))

def mermin_4Q_sim():
    
    connect() #connect to IBM Q
    print("Mermin's inequality test.\n")
    
    exp, basis = mermin_test_sim(1024, 'yyyy')
    expected_yyyy = print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'xyyy')
    expected_xyyy = print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'xxyy')
    expected_xxyy = print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'yxxx')
    expected_yxxx = print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'xxxx')
    expected_xxxx = print_results(exp, basis)

    expected = -expected_yyyy + (4 * expected_xyyy) + (6 * expected_xxyy) - (4 * expected_yxxx) - expected_xxxx
    print("<M4>exp = " + str(expected))
    
def mermin_4Q_comp():
    
    connect() #connect to IBM Q
    print("Mermin's inequality test.\n")
    
    exp, basis = mermin_test_comp(8192, 'yyyy')
    expected_yyyy = print_results(exp, basis)
    exp, basis = mermin_test_comp(8192, 'xyyy')
    expected_xyyy = print_results(exp, basis)
    exp, basis = mermin_test_comp(8192, 'xxyy')
    expected_xxyy = print_results(exp, basis)
    exp, basis = mermin_test_comp(8192, 'yxxx')
    expected_yxxx = print_results(exp, basis)
    exp, basis = mermin_test_comp(8192, 'xxxx')
    expected_xxxx = print_results(exp, basis)

    expected = -expected_yyyy + (4 * expected_xyyy) + (6 * expected_xxyy) - (4 * expected_yxxx) - expected_xxxx
    print("<M4>exp = " + str(expected))

def mermin_5Q_sim():
    
    connect() #connect to IBM Q
    print("Mermin's inequality test.\n")
    
    exp, basis = mermin_test_sim(1024, 'xxxxx')
    expected_yyyyy = print_results(exp, basis)    
    exp, basis = mermin_test_sim(1024, 'xxxyy')
    expected_xxyyy = print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'yyyyx')
    expected_xxxxy = print_results(exp, basis)

    expected = -expected_yyyyy + (10 * expected_xxyyy) - (5 * expected_xxxxy)
    print("<M5>exp = " + str(fabs(expected)))
    
def mermin_5Q_comp():
    
    connect() #connect to IBM Q
    print("Mermin's inequality test.\n")
    
    exp, basis = mermin_test_comp(8192, 'xxxxx')
    expected_yyyyy = print_results(exp, basis)    
    exp, basis = mermin_test_comp(8192, 'yyxxx')
    expected_xxyyy = print_results(exp, basis)
    exp, basis = mermin_test_comp(8192, 'yyyyx')
    expected_xxxxy = print_results(exp, basis)

    expected = -expected_yyyyy + (10 * expected_xxyyy) - (5 * expected_xxxxy)
    print("<M5>exp = " + str(fabs(expected)))
    
def test_3Q_sim():
    exp, basis = mermin_test_sim(1024, 'xxx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'xxy')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'xyx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'xyy')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'yxx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'yxy')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'yyx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'yyy')
    print_results(exp, basis)
    
def test_3Q_comp():
    exp, basis = mermin_test_comp(1024, 'xxx')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'xxy')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'xyx')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'xyy')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'yxx')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'yxy')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'yyx')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'yyy')
    print_results(exp, basis)

def test_4Q_sim():
    exp, basis = mermin_test_sim(1024, 'xxxx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'xxxy')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'xxyx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'xxyy')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'xyxx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'xyxy')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'xyyx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'xyyy')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'yxxx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'yxxy')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'yxyx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'yxyy')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'yyxx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'yyxy')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'yyyx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'yyyy')
    print_results(exp, basis)

def test_4Q_comp():
    exp, basis = mermin_test_comp(1024, 'xxxx')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'xxxy')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'xxyx')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'xxyy')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'xyxx')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'xyxy')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'xyyx')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'xyyy')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'yxxx')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'yxxy')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'yxyx')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'yxyy')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'yyxx')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'yyxy')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'yyyx')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'yyyy')
    print_results(exp, basis)
    
def test_5Q_sim():
    exp, basis = mermin_test_sim(1024, 'xxxxx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'xxxxy')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'xxxyx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'xxxyy')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'xxyxx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'xxyxy')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'xxyyx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'xxyyy')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'xyxxx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'xyxxy')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'xyxyx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'xyxyy')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'xyyxx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'xyyxy')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'xyyyx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'xyyyy')
    print_results(exp, basis) 
    exp, basis = mermin_test_sim(1024, 'yxxxx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'yxxxy')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'yxxyx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'yxxyy')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'yxyxx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'yxyxy')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'yxyyx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'yxyyy')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'yyxxx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'yyxxy')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'yyxyx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'yyxyy')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'yyyxx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'yyyxy')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'yyyyx')
    print_results(exp, basis)
    exp, basis = mermin_test_sim(1024, 'yyyyy')
    print_results(exp, basis)
    
def test_5Q_comp():
    exp, basis = mermin_test_comp(1024, 'xxxxx')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'xxxxy')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'xxxyx')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'xxxyy')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'xxyxx')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'xxyxy')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'xxyyx')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'xxyyy')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'xyxxx')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'xyxxy')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'xyxyx')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'xyxyy')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'xyyxx')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'xyyxy')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'xyyyx')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'xyyyy')
    print_results(exp, basis) 
    exp, basis = mermin_test_comp(1024, 'yxxxx')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'yxxxy')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'yxxyx')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'yxxyy')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'yxyxx')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'yxyxy')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'yxyyx')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'yxyyy')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'yyxxx')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'yyxxy')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'yyxyx')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'yyxyy')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'yyyxx')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'yyyxy')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'yyyyx')
    print_results(exp, basis)
    exp, basis = mermin_test_comp(1024, 'yyyyy')
    print_results(exp, basis)
    
''' Simulated Mermin Inequalities '''    
mermin_3Q_sim()
# mermin_4Q_sim()
# mermin_5Q_sim()

''' Computed Mermin Inequalities '''    
# mermin_3Q_comp()
# mermin_4Q_comp()
# mermin_5Q_comp()

''' Testing '''
# test_3Q_sim()
# test_4Q_sim()
# test_5Q_sim()
# test_3Q_comp()
# test_4Q_comp()
# test_5Q_comp()
