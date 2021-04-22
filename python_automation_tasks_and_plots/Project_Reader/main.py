import numpy as np
import pandas as pd
import os

from file_class_script import File_Class
from file_class_extended_script import File_Class_Extended

file_extended = File_Class_Extended("1-1-3neg_music.csv",
                      "/home/abrar/Desktop/transformed_seed_extracted/music/Subject 1/Neg/")

file_basic = File_Class("1-1-3neg_music.csv",
                      "/home/abrar/Desktop/transformed_seed_extracted/music/Subject 1/Neg/")


print(file_extended.data_shape)
print(file_basic.get_shape())

print(file_basic.data[0,0:15])
print(file_extended.data[0,0:15])
















"""
class one_file():

    def __init__(self, file_name, dir_loc):
        self.file_name = file_name
        self.dir_loc = dir_loc
        self.file_loc = self.dir_loc + self.file_name

        self.data = self.read_file()
        self.data_shape = self.get_shape()

        self.data_header = self.get_header()
        self.freq_series = self.get_freq_series()


    def read_file(self):

        data_frame_local = pd.read_csv(self.file_loc)

        data_frame_header_local = list(data_frame_local)

        data_frame_header_local.pop(0)

        data_matrix_local = np.array([])

        for header_name in data_frame_header_local:
            channel_vector = np.array(data_frame_local[header_name])
            channel_matrix = channel_vector.reshape(-1, 1)

            if header_name is data_frame_header_local[0]:
                data_matrix_local = channel_matrix

            else:
                data_matrix_local = np.concatenate((data_matrix_local, channel_matrix), axis=1)

        data_matrix_local = np.transpose(data_matrix_local)

        return data_matrix_local

    def get_shape(self):

        return self.data.shape

    def get_header(self):

        data_frame_local = pd.read_csv(self.file_loc)

        return list(data_frame_local)

    def get_freq_series(self):

        data_frame_local = pd.read_csv(self.file_loc)

        freq_vector = np.array(data_frame_local[self.data_header[0]])

        return freq_vector.reshape(-1, 1)





"""








