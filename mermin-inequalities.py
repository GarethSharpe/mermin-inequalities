'''
A test of the mermin inequalities on the IBM Q
written by Marcus Edwards on May 8, 2017
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
    print("state     probability")
    for i in range(len(exp['result']['measure']['labels'])):
        print("{0}       {1}".format(exp['result']['measure']['labels'][i],exp['result']['measure']['values'][i]))    

    return

    
connect() #connect to IBM Q

print("Mermin's inequality test.")
exp = mermin_test_comp(1000) #teleport with 1000 trials

print_results(exp) #print results
