from pybricks.parameters import Stop
import time

class Sensor():
    # Construtor
    def __init__(self, motor):
        self.motor = motor
        self.angle = 0
        
    # Funções da clase
    def _movCentro(self):
        self._movOrigem()
        self.motor.run_angle(1000, 360, Stop.HOLD, True)
        self.angle = 360
        
    def _movOrigem(self):
        
        if(self.angle == 65):
            self.motor.run_angle(1000, -65, Stop.HOLD, True)
        elif(self.angle == 360):
            self.motor.run_angle(1000, -360, Stop.HOLD, True)
        self.angle = 0  

        
    # Set
    def set_TimerLeituraCentro(self, time=0):
        self.timer_leitura_centro = time
        
    def set_movimenta(self):
        # Move até o centro do cubo
        self._movCentro()
        time.sleep(self.timer_leitura_centro) # aguada tempo de leitura

        # Retorna estado inicial
        self._movOrigem()
        
        