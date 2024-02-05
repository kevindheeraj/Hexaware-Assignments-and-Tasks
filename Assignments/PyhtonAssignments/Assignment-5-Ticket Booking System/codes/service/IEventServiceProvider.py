from abc import *


class IEventServiceProvider(ABC):

    @abstractmethod
    def create_event(self):
        pass

    @abstractmethod
    def getEventDetails(self):
        pass

    @abstractmethod
    def getAvailableNoOfTickets(self):
        pass
