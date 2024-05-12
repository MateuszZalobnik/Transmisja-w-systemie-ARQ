from encodedtypeenum import EncodedTypeEnum
from encoder import encoder


class Receiver:
    def __init__(self, encoded_type_enum):
        self.transmitter = None
        self.encoded_type_enum = encoded_type_enum

    def init_transmitter(self, transmitter):
        self.transmitter = transmitter
        pass

    def receive(self, data):
        # sprawdzenie czy bity kontrolne są poprawne
        is_error_detected = self.__are_control_bits_correct(data)
        # odpowiedź do nadajnika
        self.__response(is_error_detected)
        pass

    def __are_control_bits_correct(self, data):
        if self.encoded_type_enum == EncodedTypeEnum.PARITY:
            # sprawdzenie czy bit parzystości zgadza się z uzyskanymi danymi
            data_without_parity = data[:-1]
            parity_bit = data[-1]

            encoded_data = encoder.encode_with_parity(data_without_parity)
            parity_bit_calculated = encoded_data[-1]

            return parity_bit_calculated != parity_bit

        elif self.encoded_type_enum == EncodedTypeEnum.CRC8:
            # sprawdzenie czy 8 bitów CRC zgadza się z uzyskanymi danymi
            data_without_crc = data[:-8]
            crc = data[-8:]

            encoded_data = encoder.encode_with_crc8(data_without_crc)
            crc_calculated = encoded_data[-8:]

            return crc_calculated != crc
        elif self.encoded_type_enum == EncodedTypeEnum.CRC16:
            # sprawdzenie czy 16 bitów CRC zgadza się z uzyskanymi danymi
            data_without_crc = data[:-16]
            crc = data[-16:]

            encoded_data = encoder.encode_with_crc16(data_without_crc)
            crc_calculated = encoded_data[-16:]

            return crc_calculated != crc
        elif self.encoded_type_enum == EncodedTypeEnum.CRC32:
            # sprawdzenie czy 32 bity CRC zgadzają się z uzyskanymi danymi
            data_without_crc = data[:-32]
            crc = data[-32:]

            encoded_data = encoder.encode_with_crc32(data_without_crc)
            crc_calculated = encoded_data[-32:]

            return crc_calculated != crc

    def __response(self, is_error_detected):
        # odpowiedź do nadajnika
        self.transmitter.response(is_error_detected)
