from pybricks.parameters import Stop

class Braco():
    # Construtor
    def __init__(self, motor):
        self.motor = motor
        self.sentido = 1
        
    # Funções da clase
    def _segurarCubo(self):                                    #seria a posição inicial do braço, usa-se pra quando for girar ou segurar o cubo;
        self.motor.run_angle(1000, 100, Stop.HOLD, True)

    def _girarCubo(self):                                      #no caso, ele faz esse movimento antes da leitura e isso acontece 4 vezes, exceto na quinta vez que ele faz esse movimento 2 vezes direto;
        self.motor.run_angle(1000, 140, Stop.HOLD, True)            #para encaixar no cubo;
        self.motor.run_angle(1000, -140, Stop.HOLD, True)           #para puxar o cubo, ou seja, fazendo ele girar;

    def _voltarPosicaoOriginal(self):                          #volta para a posição original antes de segurar o cubo;
        self.motor.run_angle(1000, -100, Stop.HOLD, True)
        
    # Set
    def set_sentido(self, sentido=1):
        self.sentido = sentido
        
    def set_movimenta(self):
        if self.sentido == 1:
            self._segurarCubo()
            self._girarCubo()
            self._voltarPosicaoOriginal()