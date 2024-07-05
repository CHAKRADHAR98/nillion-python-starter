from nada_dsl import *

def nada_main():

    party2 = Party(name="Party2")

    secret_int1 = SecretInteger(Input(name="secret_int1", party=party2))

    secret_int2 = SecretInteger(Input(name="secret_int2", party=party2))

    result_int = secret_int1 - secret_int2

    return [Output(result_int, "result_output", party2)]
