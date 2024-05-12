from matplotlib import ticker
from dataGenerator import DataGenerator
from encodedTypeEnum import EncodedTypeEnum
from receiver import Receiver
from transmitter import Transmitter
import matplotlib.pyplot as plt

data = DataGenerator.generate_bits_from_text("Hello, World!")

# stworzenie nadajnika i odbiornika
transmitter_with_parity = Transmitter(EncodedTypeEnum.PARITY)
receiver_with_parity = Receiver(EncodedTypeEnum.PARITY)

# inicjalizacja nadajnika i odbiornika
transmitter_with_parity.init_receiver(receiver_with_parity)
receiver_with_parity.init_transmitter(transmitter_with_parity)


number_of_retransmissions = 0
number_of_incorrect_data = 0
for i in range(100):
    transmitter_with_parity.send(data)
    number_of_retransmissions += transmitter_with_parity.number_of_retransmission

    if receiver_with_parity.data != transmitter_with_parity.data:
        number_of_incorrect_data += 1

    # reset nadajnika i odbiornika
    transmitter_with_parity.number_of_retransmission = 0
    transmitter_with_parity.data = None
    receiver_with_parity.data = None

average_number_of_retransmissions = number_of_retransmissions / 100
average_number_of_incorrect_data = number_of_incorrect_data / 100




plt.figure(figsize=(8, 6))

coorection_codes = ("Parity bit", "CRC8", "CRC16", "CRC32")

# Dane dla pierwszego wykresu
plot_data = [average_number_of_incorrect_data, 0.5, 0.3, 0.5]
plt.bar(coorection_codes, plot_data)
plt.ylabel('% zaakceptowanych złych danych')
plt.title('Średnia ilość zaakceptowanych złych danych w zależności od kodu korekcyjnego')

# Formatowanie etykiet osi Y jako procenty
plt.gca().yaxis.set_major_formatter(ticker.PercentFormatter(1.0))
plt.show()


# Dane dla drugiego wykresu
plot_data = [average_number_of_retransmissions, 100, 30, 55]
plt.bar(coorection_codes, plot_data)
plt.ylabel('ilość retransmisji')
plt.title('Średnia ilość retransmisji w zależności od kodu korekcyjnego')
plt.show()
