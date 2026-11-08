from abc import ABC, abstractmethod

class Notifier(ABC):

    @abstractmethod
    def send_notification(self,message):
        pass
    def notify(self,message):
        ...