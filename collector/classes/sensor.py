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
        self.motor.run_angle(500, 130, Stop.HOLD, True)
        self.angle = 130   
    def _movAresta(self):
        self.angle = 65  
         
        if(self.angle == 0):
            self.motor.run_angle(500, 65, Stop.HOLD, True)
        elif(self.angle == 130):
            self.motor.run_angle(500, -65, Stop.HOLD, True)
        
    def _movOrigem(self):
        self.angle = 0  
        
        if(self.angle == 65):
            self.motor.run_angle(500, -65, Stop.HOLD, True)
        elif(self.angle == 130):
            self.motor.run_angle(500, -130, Stop.HOLD, True)

        
    # Set
    def set_TimerLeituraCentro(self, time):
        self.timer_leitura_centro = time
    def set_TimerLeituraAresta(self, time):
        self.timer_leitura_aresta = time
        
    def set_movimenta(self):
        # Move até o centro do cubo
        self._movCentro()
        time.sleep(self.timer_leitura_centro) # aguada tempo de leitura
        
        # Move até a aresta do cubo
        self._movAresta()
        time.sleep(self.timer_leitura_aresta)# aguada tempo de leitura
        
        # Retorna estado inicial
        self._movCentro
        
        