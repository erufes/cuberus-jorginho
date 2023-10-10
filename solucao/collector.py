import json
from rubik.cube     import Cube
from rubik.solve        import Solver

from classes.cor        import getCorCubo

if __name__ == '__main__':
    c = Cube(getCorCubo())
    print(c)
    solver = Solver(c)
    solver.solve()
    
    #trocar o nome do .json para o nome desejado;
    with open ("solucao.txt", "w") as file:
        file.write(json.dumps(solver.moves))
        file.close()