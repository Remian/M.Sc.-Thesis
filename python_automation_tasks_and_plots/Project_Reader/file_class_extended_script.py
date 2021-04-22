from file_class_script import File_Class
import numpy as np
import pandas as pd
import os


class File_Class_Extended(File_Class):

    def __init__(self, file_name, dir_loc):
        super().__init__(file_name, dir_loc)
        self.data_shape = self.get_shape()

        self.data_header = self.get_header()
        self.freq_series = self.get_freq_series()




    def get_header(self):

        data_frame_local = pd.read_csv(self.file_loc)

        return list(data_frame_local)

    def get_freq_series(self):

        data_frame_local = pd.read_csv(self.file_loc)

        freq_vector = np.array(data_frame_local[self.data_header[0]])

        return freq_vector.reshape(-1, 1)














