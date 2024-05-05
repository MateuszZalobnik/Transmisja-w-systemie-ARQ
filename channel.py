import komm


class channel:
    def __init__(self, error_probability):
        self.error_probability = error_probability
        pass

    def generate_errors_with_bsc(self, data):
        bsc = komm.BinarySymmetricChannel(self.error_probability)
        return bsc(data)

    def generate_random_errors(self, data):
        # wprowadź błędy losowe z prawdopodobieństwem error_probability
        pass

    def generate_burst_errors(self, data):
        # wprowadź błędy skupione z prawdopodobieństwem error_probability
        pass

    def generate_impulse_errors(self, data):
        # wprowadź błędy impulsowe z prawdopodobieństwem error_probability
        pass


