from pybricks.parameters import Stop

class Base():
    
    # Construtor
    def __init__(self, motor, ev3):
        self.motor = motor
        self.ev3 = ev3
        self.qtd = 1
        
    # Funções da clase
    def ajeitadinha(self):
        self.motor.run_angle(2000, 15 * self.qtd, Stop.HOLD, True)
        self.motor.run_angle(2000, -15 * self.qtd, Stop.HOLD, True)
        self.motor.run_angle(2000, 15 * self.qtd, Stop.HOLD, True)
        self.motor.run_angle(2000, -15 * self.qtd, Stop.HOLD, True)
        self.motor.run_angle(2000, 15 * self.qtd, Stop.HOLD, True)
        self.motor.run_angle(2000, -15 * self.qtd, Stop.HOLD, True)
        
    def _movEsquerda(self, preso=False):
        if preso == False:
            self.motor.run_angle(1000, -270 * self.qtd, Stop.HOLD, True)
        else:
            self.motor.run_angle(1000, -270 * self.qtd, Stop.HOLD, True)
            

    def _movDireita(self, preso=False):
        if preso == False:
            self.motor.run_angle(1000, 270 * self.qtd, Stop.HOLD, True)
        else:
            self.motor.run_angle(1000, 270 * self.qtd, Stop.HOLD, True)
        
    # Set
    def set_qtdMovimentos(self, qtd=1):
        self.qtd = qtd
        
    def set_Direcao(self, direcao='d'):
        self.direcao = direcao
        
    def set_movimenta(self):
        if self.direcao == 'e': 
            self._movEsquerda()
        else:
            if self.direcao == 'd':
                self._movDireita()