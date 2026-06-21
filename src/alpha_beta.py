def alpha_beta(node, alpha=-999, beta=999, maximizing=True):

    if isinstance(node,int):
        return node


    if maximizing:

        valor=-999

        for hijo in node:

            valor=max(
                valor,
                alpha_beta(hijo,alpha,beta,False)
            )

            alpha=max(alpha,valor)

            if beta <= alpha:
                break

        return valor


    else:

        valor=999

        for hijo in node:

            valor=min(
                valor,
                alpha_beta(hijo,alpha,beta,True)
            )

            beta=min(beta,valor)


            if beta <= alpha:
                break

        return valor