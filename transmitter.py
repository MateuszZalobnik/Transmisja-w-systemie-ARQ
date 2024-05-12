from encodedtypeenum import EncodedTypeEnum
from encoder import encoder


class Transmitter:
    def __init__(self, encoded_type, data):
        self.encoded_type = encoded_type
        self.receiver = None
        self.timeout = 1
        self.resend_count = 0
        self.data = data

    def init_receiver(self, receiver):
        self.receiver = receiver

    def send(self):
        encoded_data = self.__add_control_bits()
        # self.channel.send(encoded_data)
        self.receiver.receive(encoded_data)

    def __add_control_bits(self):
        if self.encoded_type == EncodedTypeEnum.PARITY:
            return encoder.encode_with_parity(self.data)
        elif self.encoded_type == EncodedTypeEnum.CRC8:
            return encoder.encode_with_crc8(self.data)
        elif self.encoded_type == EncodedTypeEnum.CRC16:
            return encoder.encode_with_crc16(self.data)
        elif self.encoded_type == EncodedTypeEnum.CRC32:
            return encoder.encode_with_crc32(self.data)

    def response(self, should_resend):
        if should_resend:
            self.resend_count += 1
            self.send()

    def __start_timer(self):
        pass
