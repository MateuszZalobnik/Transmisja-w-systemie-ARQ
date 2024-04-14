from transmitter import transmitter


class receiver:
    def __init__(self, transmitter):
        self.transmitter = transmitter
        # ...
        pass

    def receive(self, data):
        is_error_detected = self.__check_control_bits(data)
        self.__response(is_error_detected)
        pass

    def __check_control_bits(self, data):
        pass

    def __response(self, is_error_detected):
        if is_error_detected:
            self.transmitter.response(True)
        else:
            self.transmitter.response(False)
        pass

