from abc import ABC, abstractmethod

class Estrategia(ABC):
    @abstractmethod
    def ejecutar(self,)