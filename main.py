from matplotlib import ticker
import numpy as np
from channel import Channel
from dataGenerator import DataGenerator
from encodedTypeEnum import EncodedTypeEnum
from channelTypeEnum import ChannelTypeEnum
from receiver import Receiver
from transmitter import Transmitter
import matplotlib.pyplot as plt


def simulate(encoded_type, channel_type):
    channel = Channel(0.7, channel_type)
    # inicjalizacja nadajnika i odbiornika
    transmitter = Transmitter(encoded_type, channel)
    receiver = Receiver(encoded_type)

    transmitter.init_receiver(receiver)
    receiver.init_transmitter(transmitter)

    # liczba badanych próbek
    iterations = 100
    total_number_of_retransmissions = 0
    total_number_of_accepted_data = 0
    number_of_data_lost = 0
    total_number_of_incorrect_data = 0
    total_number_of_correct_data = 0

    for i in range(iterations):
        transmitter.send(data)

        if transmitter.data_lost:
            number_of_data_lost += 1
        else:
            total_number_of_accepted_data += 1
            total_number_of_retransmissions += transmitter.number_of_retransmission
            if receiver.data != transmitter.data:
                total_number_of_incorrect_data += 1
            else:
                total_number_of_correct_data += 1

        # reset nadajnika i odbiornika
        transmitter.number_of_retransmission = 0
        transmitter.number_of_data_lost = 0
        transmitter.data_lost = False
        transmitter.data = None
        receiver.data = None

    average_number_of_retransmissions = 0
    if total_number_of_accepted_data != 0:
        average_number_of_retransmissions = total_number_of_retransmissions / total_number_of_accepted_data

    return [average_number_of_retransmissions, total_number_of_correct_data, total_number_of_incorrect_data, number_of_data_lost]


def print_plots(result_parity, result_crc8, result_crc16, result_crc32):
    coorection_codes = ("Parity bit", "CRC8", "CRC16", "CRC32")

    plot_data = {
        'liczba poprawnych wysłań': np.array([result_parity[1], result_crc8[1], result_crc16[1], result_crc32[1]]),
        'liczba nie wykrytych błędnych wysłań': np.array(
            [result_parity[2], result_crc8[2], result_crc16[2], result_crc32[2]]),
        'liczba utraconych wysłań': np.array([result_parity[3], result_crc8[3], result_crc16[3], result_crc32[3]]),
    }

    width = 0.5

    fig, ax = plt.subplots()
    bottom = np.zeros(len(coorection_codes))

    for boolean, item in plot_data.items():
        p = ax.bar(coorection_codes, item, width, label=boolean, bottom=bottom)
        bottom += item

    ax.set_title('Porównanie skuteczności kodów korekcyjnych dla 100 wysłań')
    ax.legend(loc="upper right")

    plt.show()

    fig, ax = plt.subplots()
    counts = [result_parity[0], result_crc8[0], result_crc16[0], result_crc32[0]]

    ax.bar(coorection_codes, counts)
    ax.set_ylabel('n')
    ax.set_title('Średnia liczba retransmisji w zależności od kodu detekcyjnego')

    plt.show()




# data = DataGenerator.generate_bits_from_text("Hello, World!")
data = DataGenerator.generate_bits_from_text("Hello, World!")

result_parity = simulate(EncodedTypeEnum.PARITY, ChannelTypeEnum.BSC)
result_crc8 = simulate(EncodedTypeEnum.CRC8, ChannelTypeEnum.BSC)
result_crc16 = simulate(EncodedTypeEnum.CRC16, ChannelTypeEnum.BSC)
result_crc32 = simulate(EncodedTypeEnum.CRC32, ChannelTypeEnum.BSC)

print_plots(result_parity, result_crc8, result_crc16, result_crc32)


result_parity = simulate(EncodedTypeEnum.PARITY, ChannelTypeEnum.Random)
result_crc8 = simulate(EncodedTypeEnum.CRC8, ChannelTypeEnum.Random)
result_crc16 = simulate(EncodedTypeEnum.CRC16, ChannelTypeEnum.Random)
result_crc32 = simulate(EncodedTypeEnum.CRC32, ChannelTypeEnum.Random)

print_plots(result_parity, result_crc8, result_crc16, result_crc32)


result_parity = simulate(EncodedTypeEnum.PARITY, ChannelTypeEnum.Burst)
result_crc8 = simulate(EncodedTypeEnum.CRC8, ChannelTypeEnum.Burst)
result_crc16 = simulate(EncodedTypeEnum.CRC16, ChannelTypeEnum.Burst)
result_crc32 = simulate(EncodedTypeEnum.CRC32, ChannelTypeEnum.Burst)

print_plots(result_parity, result_crc8, result_crc16, result_crc32)