from nada_dsl import *

def nada_main():

    party1 = Party(name="NumStore")

    party2 = Party(name="Player")

    num_target = SecretInteger(Input(name="my_int1", party=party1))

    player_guess = SecretInteger(Input(name="my_int2", party=party2))

    is_same_num = num_target == player_guess

    return [Output(is_same_num, "is_same_num", party=party2)]



