from encodedtypeenum import EncodedTypeEnum
from receiver import Receiver
from transmitter import Transmitter

data = [1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1]

transmitter_with_parity = Transmitter(EncodedTypeEnum.PARITY, data)
receiver_with_parity = Receiver(EncodedTypeEnum.PARITY)

transmitter_with_parity.init_receiver(receiver_with_parity)
receiver_with_parity.init_transmitter(transmitter_with_parity)

transmitter_with_parity.send()
