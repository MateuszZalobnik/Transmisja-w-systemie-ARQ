from encoder import encoder
from receiver import receiver


class transmitter:
    def __init__(self):
        self.receiver = receiver(self)
        self.timeout = 1
        self.resend_count = 0
        pass

    def __send(self):
        # encoder.encode_with_crc(data)
        pass

    def __add_control_bits(self):
        pass

    def response(self, should_resend):
        pass

    def __start_timer(self):
        pass

