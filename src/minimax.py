def minimax(node, maximizing=True):

    if isinstance(node, int):
        return node


    valores=[]

    for hijo in node:
        valores.append(
            minimax(hijo, not maximizing)
        )


    if maximizing:
        return max(valores)
    else:
        return min(valores)