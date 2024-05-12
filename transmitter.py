from encodedTypeEnum import EncodedTypeEnum
from encoder import encoder


class Transmitter:
    def __init__(self, encoded_type, simulation=False):
        self.simulation = simulation
        self.data = None
        self.receiver = None
        self.encoded_type = encoded_type
        self.timeout = 1
        self.number_of_retransmission = 0

    def init_receiver(self, receiver):
        self.receiver = receiver

    def send(self, data):
        self.__print_message("sending data...")
        self.data = data

        encoded_data = self.__add_control_bits()

        #TODO send data to channel
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
            self.__print_message("resending data...")
            self.number_of_retransmission += 1
            if self.number_of_retransmission < 100:
                self.send(self.data)
            else:
                self.__print_message("Data lost")
        else:
            self.__print_message("Data accepted")

    def __print_message(self, message):
        if self.simulation:
            print(message)
