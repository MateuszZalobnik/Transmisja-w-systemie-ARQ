import komm
import random
from channelTypeEnum import ChannelTypeEnum

class Channel:
    def __init__(self, error_probability, channel_type, p_good_to_bad=0.01, p_bad_to_good=0.1):
        self.error_probability = error_probability
        self.channel_type = channel_type
        self.state = 'good'
        self.p_good_to_bad = p_good_to_bad # p-odobieństwo przejścia z dobrego do złego stanu w modelu Gilberta-Elliota
        self.p_bad_to_good = p_bad_to_good

    def generate_errors(self, data):
        if(self.channel_type == ChannelTypeEnum.Random):
            return self.__generate_random_errors(data)
        elif(self.channel_type == ChannelTypeEnum.Burst):
            return self.__generate_burst_errors(data)

    def __generate_errors_with_bsc(self, data):
        bsc = komm.BinarySymmetricChannel(self.error_probability)
        return bsc(data)
    def __generate_random_errors(self, data):
        # błędy losowe z prawdopodobieństwem error_probability
        # random.random() zwraca liczbe z przedzialu (0, 1)
        # "zamiana" bitów, gdy ta liczba jest mniejsza niz error_probability
        return [bit if random.random() > self.error_probability else 1 - bit for bit in data]

    def __generate_burst_errors(self, data):
        # kanal/model Gilberta-Elliota, bledy skupione
        # gdy stan jest "dobry" - jezeli wylosowana liczba z przedzialu (0,1) bedzie mniejsza
        # od liczby p_good_to_bad to przechodzimy do zlego stanu
        # jezeli zostajemy w dobrym stanie to error_prob pozostaje niskie
        error_data = []
        for bit in data:
            if self.state == 'good':
                if random.random() < self.p_good_to_bad:
                    self.state = 'bad'
                error_prob = 0.0
            else:
                if random.random() < self.p_bad_to_good:
                    self.state = 'good'
                error_prob = 0.5

            # dodanie bitu do error_data, odwracajac go z p-o error_prob
            error_data.append(bit if random.random() > error_prob else 1 - bit)
        return error_data


