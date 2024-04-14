import komm


class channel:
    @staticmethod
    def generate_errors_with_bsc(data, error_probability):
        bsc = komm.BinarySymmetricChannel(error_probability)
        return bsc(data)

    @staticmethod
    def generate_errors_with_gilbert_elliott(data, error_probability):
        pass