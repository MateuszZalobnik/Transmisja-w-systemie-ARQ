from enum import Enum


class EncodedTypeEnum(Enum):
    CRC8 = 1
    CRC16 = 2
    CRC32 = 3
    PARITY = 4