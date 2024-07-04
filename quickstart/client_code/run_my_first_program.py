from nada_dsl import *

def nada_main():
    # Define parties
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")
    party4 = Party(name="Party4")
    
    # Define secret inputs
    a = SecretInteger(Input(name="A", party=party1))
    b = SecretInteger(Input(name="B", party=party2))
    c = SecretInteger(Input(name="C", party=party3))
    
    # Perform computations
    sum_result = a + b + c
    product_result = a * b * c
    difference_result = a - b - c
    
    # Define outputs
    output_sum = Output(sum_result, "sum_output", party4)
    output_product = Output(product_result, "product_output", party4)
    output_difference = Output(difference_result, "difference_output", party4)
    
    print("Outputs have been generated successfully.")

    return [output_sum, output_product, output_difference]
