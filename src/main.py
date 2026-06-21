from src.game_tree import sample_tree
from src.minimax import minimax
from src.alpha_beta import alpha_beta


arbol = sample_tree()


print(
"Minimax:",
minimax(arbol)
)


print(
"Alpha Beta:",
alpha_beta(arbol)
)