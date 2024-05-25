from matplotlib import ticker

from channel import Channel
from dataGenerator import DataGenerator
from encodedTypeEnum import EncodedTypeEnum
from channelTypeEnum import ChannelTypeEnum
from receiver import Receiver
from transmitter import Transmitter
import matplotlib.pyplot as plt


def simulate(transmitter, receiver):
    # inicjalizacja nadajnika i odbiornika
    transmitter.init_receiver(receiver)
    receiver.init_transmitter(transmitter)

    # liczba badanych próbek
    iterations = 100
    number_of_retransmissions = 0
    number_of_incorrect_data = 0
    for i in range(iterations):
        transmitter.send(data)
        number_of_retransmissions += transmitter.number_of_retransmission

        if receiver.data != transmitter.data:
            number_of_incorrect_data += 1

        # reset nadajnika i odbiornika
        transmitter.number_of_retransmission = 0
        transmitter.data = None
        receiver.data = None

    average_number_of_retransmissions = number_of_retransmissions / iterations
    average_number_of_incorrect_data = number_of_incorrect_data / iterations
    return [average_number_of_retransmissions, average_number_of_incorrect_data]

data = DataGenerator.generate_bits_from_text("Hello, World!")
# data = DataGenerator.generate_bits_from_text("H")

channel = Channel(0.03, ChannelTypeEnum.Random)

# bit parzystości
# stworzenie nadajnika i odbiornika
transmitter_with_parity = Transmitter(EncodedTypeEnum.PARITY, channel)
receiver_with_parity = Receiver(EncodedTypeEnum.PARITY)

# CRC 8
# stworzenie nadajnika i odbiornika
transmitter_crc8 = Transmitter(EncodedTypeEnum.CRC8, channel)
receiver_crc8 = Receiver(EncodedTypeEnum.CRC8)

# CRC 16
# stworzenie nadajnika i odbiornika
transmitter_crc16 = Transmitter(EncodedTypeEnum.CRC16, channel)
receiver_crc16 = Receiver(EncodedTypeEnum.CRC16)

# CRC 32
# stworzenie nadajnika i odbiornika
transmitter_crc32 = Transmitter(EncodedTypeEnum.CRC32, channel)
receiver_crc32 = Receiver(EncodedTypeEnum.CRC32)

result_parity = simulate(transmitter_with_parity, receiver_with_parity)
result_crc8 = simulate(transmitter_crc8, receiver_crc8)
result_crc16 = simulate(transmitter_crc16, receiver_crc16)
result_crc32 = simulate(transmitter_crc32, receiver_crc32)

plt.figure(figsize=(8, 6))

coorection_codes = ("Parity bit", "CRC8", "CRC16", "CRC32")

# Dane dla pierwszego wykresu
plot_data = [result_parity[1], result_crc8[1], result_crc16[1], result_crc32[1]]
plt.bar(coorection_codes, plot_data)
plt.ylabel('% zaakceptowanych złych danych')
plt.title('Średnia procent zaakceptowanych złych danych w zależności od kodu detekcyjnego')

# Formatowanie etykiet osi Y jako procenty
plt.gca().yaxis.set_major_formatter(ticker.PercentFormatter(1.0))
plt.show()


# Dane dla drugiego wykresu
plot_data = [result_parity[0], result_crc8[0], result_crc16[0], result_crc32[0]]
plt.bar(coorection_codes, plot_data)
plt.ylabel('liczba retransmisji')
plt.title('Średnia liczba retransmisji w zależności od kodu detekcyjnego')
plt.show()
