from abc import ABCMeta, abstractmethod
from contextlib import contextmanager

# tag::qubit_interface[]
class Qubit(metaclass=ABCMeta):
    @abstractmethod
    def h(self): pass

    @abstractmethod
    def x(self): pass  

    @abstractmethod
    def ry(self, angle : float): pass      # <1>     

    @abstractmethod
    def measure(self) -> bool: pass

    @abstractmethod
    def reset(self): pass
# end::qubit_interface[]

# tag::device_interface[]
class QuantumDevice(metaclass=ABCMeta):
    @abstractmethod
    def allocate_qubit(self) -> Qubit:           
        pass

    @abstractmethod
    def deallocate_qubit(self, qubit : Qubit):   
        pass

    @contextmanager
    def using_qubit(self):                       
        qubit = self.allocate_qubit()
        try:
            yield qubit
        finally:
            qubit.reset()                        
            self.deallocate_qubit(qubit)
# end::device_interface[]
