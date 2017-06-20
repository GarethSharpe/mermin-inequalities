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
        print("API auth success.")
    else:
        print("API auth failure.")
        exit()

def print_results(exp):
    '''
    Print the distribution of measured results from the given experiment
    '''
    print("---------------------")
    print("RESULTS")
    print("---------------------")
    states = "State       | "
    probabilities = "Probability | "
    expected = 0
    for i in range(len(exp['result']['measure']['labels'])):
        state = exp['result']['measure']['labels'][i]
        probability = exp['result']['measure']['values'][i]
        expected += int(state, 2) * probability
        states += str(state) + " | "
        probabilities += "{:.3f}".format(probability) + " | "
        
    print(states)
    print(probabilities)
    print("Expected Value: ", "{:.3f}".format(expected))
    return expected

    
connect() #connect to IBM Q

print("Mermin's inequality test.")

exp = mermin_test_sim(1000, 'xxxxx') #teleport with 1000 trials in the XXXXX basis
expected1 = print_results(exp) #print results
exp = mermin_test_sim(1000, 'xxxyy') #teleport with 1000 trials in the XXXYY basis
expected2 = print_results(exp) #print results
exp = mermin_test_sim(1000, 'xyyyy') #teleport with 1000 trials in the XYYYY basis
expected3 = print_results(exp) #print results
overall = (expected1 * -1) + (expected2 * 10) - (expected3 * 5)
print("-<xxxxx> + 10<xxxyy> - 5<xyyyy = <M5exp> = ", overall)