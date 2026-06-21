from src.game_tree import sample_tree
from src.minimax import minimax
from src.alpha_beta import alpha_beta


def test_minimax():

    resultado = minimax(sample_tree(), False)

    assert resultado == 5



def test_alpha_beta():

    resultado = alpha_beta(sample_tree(), maximizing=False)

    assert resultado == 5