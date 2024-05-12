# from dahuffman import HuffmanCodec

class DataGenerator:
    @staticmethod
    def generate_bits_from_text(text):
        binary_string = ''.join(format(ord(char), '08b') for char in text)
        return [int(bit) for bit in binary_string]