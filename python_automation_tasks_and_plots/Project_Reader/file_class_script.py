import numpy as np
import pandas as pd

class File_Class():

    def __init__(self, file_name, dir_loc):
        self.file_name = file_name
        self.dir_loc = dir_loc
        self.file_loc = self.dir_loc + self.file_name

        self.data = self.read_file()

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
