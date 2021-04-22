from read_full_dir import read_dir_matrix
import pandas as pd
import numpy as np
from numpy import load

"""
dir_location = "/home/abrar/Desktop/transformed_seed_extracted/welch_dir_extracted_channels/Pos/"

label_value = 2

welc_array, welc_label = read_dir_matrix(dir_location, label_value)

print(welc_label[0:20])
print(welc_array.shape)
"""
loc_local = "/home/abrar/PycharmProjects/tfLearner_v4/model_80_genuine_100_pca/"
label_train_local = load(loc_local + "music_nn_label_train.npy")

print(label_train_local)





























"""sub_1_test = one_file("1-1-3neg_music.csv",
                      "/home/abrar/Desktop/transformed_seed_extracted/music/Subject 1/Neg/")


print(sub_1_test.file_loc)
print(sub_1_test.dir_loc)
print(sub_1_test.file_name)
"""

"""file_loc = "/home/abrar/Desktop/transformed_seed_extracted/music/Subject 1/Neg/1-1-3neg_music.csv"

data_frame_local = pd.read_csv(file_loc)

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
print(data_matrix_local.shape)
print(data_matrix_local[4,0:15])"""

"""
print(data_matrix_local.shape)
print(data_matrix_local[4,0:15])


(5, 128)
[0.0201686 0.0201833 0.0202979 0.0204952 0.0207324 0.0209482 0.0210775
 0.0210741 0.0209318 0.0206948 0.0204502 0.0203115 0.020404  0.0208612
 0.0218375]


"""