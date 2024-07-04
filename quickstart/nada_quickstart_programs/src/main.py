from nada_dsl import *

def nada_main():
    # Define parties
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")

    # Define secret inputs
    a = SecretInteger(Input(name="A", party=party1))
    b = SecretInteger(Input(name="B", party=party2))

    # Perform computation
    result = a + b

    # Define output
    output = Output(result, "sum_output", party=party3)

    return [output]
