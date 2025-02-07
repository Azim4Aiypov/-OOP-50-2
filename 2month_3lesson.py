

from abc import ABC, abstractmethod
import random


class OTPSrvice(ABC):
    @abstractmethod
    def sms_send():