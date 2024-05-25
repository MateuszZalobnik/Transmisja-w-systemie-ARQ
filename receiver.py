from encodedTypeEnum import EncodedTypeEnum
from encoder import Encoder


class Receiver:
    def __init__(self, encoded_type_enum, simulation=False):
        self.simulation = simulation
        self.data = None
        self.transmitter = None
        self.encoded_type_enum = encoded_type_enum

    def init_transmitter(self, transmitter):
        self.transmitter = transmitter
        pass

    def receive(self, sent_data):
        self.__print_message("receiving data...")

        # podział danych na dane i bity kontrolne
        data, control_bits = self.__split_data_and_control_bits(sent_data)

        # sprawdzenie czy bity kontrolne są poprawne
        is_error_detected = self.__are_control_bits_correct(data, control_bits)

        # zapisanie danych do porównania z pierwotnymi danymi
        if not is_error_detected:
            self.data = data

        # odpowiedź do nadajnika
        self.__response(is_error_detected)
        pass

    def __split_data_and_control_bits(self, data):
        if self.encoded_type_enum == EncodedTypeEnum.PARITY:
            return data[:-1], data[-1]
        elif self.encoded_type_enum == EncodedTypeEnum.CRC8:
            return data[:-8], data[-8:]
        elif self.encoded_type_enum == EncodedTypeEnum.CRC16:
            return data[:-16], data[-16:]
        elif self.encoded_type_enum == EncodedTypeEnum.CRC32:
            return data[:-32], data[-32:]

    def __are_control_bits_correct(self, data, control_bits):
        if self.encoded_type_enum == EncodedTypeEnum.PARITY:
            # sprawdzenie czy bit parzystości zgadza się z uzyskanymi danymi
            encoded_data = Encoder.encode_with_parity(data)
            parity_bit_calculated = encoded_data[-1]
            return parity_bit_calculated != control_bits

        elif self.encoded_type_enum == EncodedTypeEnum.CRC8:
            # sprawdzenie czy 8 bitów CRC zgadza się z uzyskanymi danymi
            encoded_data = Encoder.encode_with_crc8(data)
            crc_calculated = encoded_data[-8:]
            return crc_calculated != control_bits

        elif self.encoded_type_enum == EncodedTypeEnum.CRC16:
            # sprawdzenie czy 16 bitów CRC zgadza się z uzyskanymi danymi
            encoded_data = Encoder.encode_with_crc16(data)
            crc_calculated = encoded_data[-16:]
            return crc_calculated != control_bits

        elif self.encoded_type_enum == EncodedTypeEnum.CRC32:
            # sprawdzenie czy 32 bity CRC zgadzają się z uzyskanymi danymi
            encoded_data = Encoder.encode_with_crc32(data)
            crc_calculated = encoded_data[-32:]
            return crc_calculated != control_bits

    def __response(self, is_error_detected):
        # odpowiedź do nadajnika
        self.transmitter.response(is_error_detected)

    def __print_message(self, message):
        if self.simulation:
            print(message)
        pass
