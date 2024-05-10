class encoder:
    """
    Klasa dodająca bity kontrolne
    """
    @staticmethod
    def encode_with_crc8(data):
        """
        Metoda wywołująca dodanie 8 bitów CRC, dla wielomianu CRC x^8+x^7+x^6+x^4+x^2+1
        """
        # Utwórz obiekt CRC z określonymi parametrami
        return encoder.encode_with_crc(data, [1, 1, 1, 0, 1, 0, 1, 0, 1])

    @staticmethod
    def encode_with_crc16(data):
        """
        Metoda wywołująca dodanie 16 bitów CRC, dla wielomianu CRC x^16+x^15+x^11+x^9+x^8+x^7+x^5+x^4+x^2+x^1+1
        """
        # Utwórz obiekt CRC z określonymi parametrami
        return encoder.encode_with_crc(
            data, [1, 1, 0, 0, 0, 1, 0, 1, 1,
                   1, 0, 1, 1, 0, 1, 1, 1])

    @staticmethod
    def encode_with_crc32(data):
        """
        Metoda wywołująca dodanie 32 bitów CRC,
        dla wielomianu CRC x^32+x^26+x^23+x^22+x^16+x^12+x^11+x^10+x^8+x^7+x^5+x^4+x^2+x^1+1
        """
        # Utwórz obiekt CRC z określonymi parametrami
        return encoder.encode_with_crc(
            data, [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1,
                   0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1])

    @staticmethod
    def __encode_with_crc(data, divisor):
        """
        Metoda dodająca bity kontrolne CRC na końcu danych, zależnie od podanego wielomianu CRC
        """
        datatemp = data.copy()
        datatemp_length = len(datatemp)
        datatemp += [0 for i in range(len(divisor) - 1)]
        for i in range(datatemp_length):
            if datatemp[i] == 0:
                continue
            for j, val in enumerate(divisor):
                datatemp[i + j] = datatemp[i + j] ^ val
        data = data + datatemp[datatemp_length:]
        return data

    @staticmethod
    def encode_with_parity(data):
        """
        Metoda dodająca bit parzystości na końcu danych
        """
        sum = 0
        for bit in data:
            sum += bit
        sum = sum % 2
        data = data + [sum]
        return data
