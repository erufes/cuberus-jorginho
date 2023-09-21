import random
import time
import json
from rubik import solve
from rubik.cube import Cube
from rubik.solve import Solver
from rubik.optimize import optimize_moves

def resolveCubo (strCubo):
    c = Cube(strCubo)
    solver = Solver(c)
    solver.solve()
    print(solver.moves)
    #trocar o nome do .json para o nome desejado;
    with open ("cubos/movimentos_cuboConfigEx1.json", "w") as file:
        file.write(json.dumps(solver.moves))
        file.close()
#cubo resolvido: YYYYYYYYYOOOBBBRRRGGGOOOBBBRRRGGGOOOBBBRRRGGGWWWWWWWWW;