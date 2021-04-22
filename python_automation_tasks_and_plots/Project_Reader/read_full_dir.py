import os
import numpy as np
import pandas as pd


def read_file_matrix(file_location_local):

    data_frame_local = pd.read_csv(file_location_local)
    data_frame_header_local = list(data_frame_local)

    data_frame_header_local.pop(0)
    #removed frequency header

    data_matrix_local = np.array([])

    for header_name in data_frame_header_local:
        channel_vector = np.array(data_frame_local[header_name])
        channel_matrix = channel_vector.reshape(-1,1)

        if header_name is data_frame_header_local[0]:
            data_matrix_local = channel_matrix

        else:
            data_matrix_local = np.concatenate((data_matrix_local, channel_matrix), axis=1)

    #transpose the matrix as each row will now represent one channel

    #return np.transpose(data_matrix_local)
    return data_matrix_local




def read_dir_matrix(dir_location_local, label_value_local):

    parent_directory_local = os.getcwd()
    os.chdir(dir_location_local)

    file_list_local = os.listdir()
    print(file_list_local)

    dir_data_list_local = []

    for file in file_list_local:
        file_data_matrix_local = read_file_matrix(file)

        dir_data_list_local.append(file_data_matrix_local)

    dir_data_np_array_local = np.array(dir_data_list_local)
    label_np_vector_local = np.full((len(file_list_local)),label_value_local)

    os.chdir(parent_directory_local)

    return dir_data_np_array_local, label_np_vector_local















#testing codes, starts--->


'''neg_data_matrix, neg_label_vector = read_dir_matrix("/home/abrar/Desktop/music_dir/Neg", 1)
neu_data_matrix, neu_label_vector = read_dir_matrix("/home/abrar/Desktop/music_dir/Neu", 2)

feature_matrix = np.concatenate((neg_data_matrix,neu_data_matrix))
label_vector = np.concatenate((neg_label_vector,neu_label_vector))

print(feature_matrix.shape)
print(label_vector.shape)


data_matrix_1 = read_file_matrix("/home/abrar/Desktop/music_dir/Neg/7-3-15neg_music.csv")
data_matrix_2 = feature_matrix[223]

print(np.array_equal(data_matrix_1,data_matrix_2))
print(label_vector[223])

data_matrix_3 = read_file_matrix("/home/abrar/Desktop/music_dir/Neu/11-1-8neu_music.csv")
data_matrix_4 = feature_matrix[449]

print(np.array_equal(data_matrix_3,data_matrix_4))
print(label_vector[449])'''









'''neg_data_matrix, neg_label_vector = read_dir_matrix("/home/abrar/Desktop/music_dir/Neg", 1)

print(neg_data_matrix.shape)
print(type(neg_data_matrix))

print(neg_label_vector.shape)
print(type(neg_label_vector))

data_matrix_1 = read_file_matrix("/home/abrar/Desktop/music_dir/Neg/2-2-7neg_music.csv")
data_matrix_2 = neg_data_matrix[3]

print(np.array_equal(data_matrix_1,data_matrix_2))

#test_numpy = np.full((5), 1)
#print(test_numpy)
#print(test_numpy.shape)'''


'''

file_loc = "/home/abrar/Desktop/music_dir/Neg/6-1-12neg_music.csv"
dir_loc = "/home/abrar/Desktop/music_dir/Neg"

data_matrix_1 = read_file_matrix(file_loc)

os.chdir(dir_loc)
list_files = os.listdir()
print(len(list_files))
print(list_files)

data_matrix_2 = read_file_matrix(list_files[0])

print(np.array_equal(data_matrix_1,data_matrix_2))


feature_matrix = []
feature_matrix.append(data_matrix_1)
feature_matrix.append(data_matrix_2)
#print(feature_matrix)

print("..................\n............\nnp feature\n.......")
feature_matrix_np = np.array(feature_matrix)
print(feature_matrix_np)
print(feature_matrix_np.shape)
print(np.amax(data_matrix_1))
print(np.amax(data_matrix_2))
print(np.amax(feature_matrix_np))

print("..................\n............\nnp labels\n.......")
label_list_1 = []
label_list_1.append(1)
label_list_1.append(1)

label_list_1_np = np.array(label_list_1)

print(label_list_1_np)
print(label_list_1_np.shape)

label_list_2 = []
label_list_2.append(2)
label_list_2.append(2)

label_list_2_np = np.array(label_list_2)

print(label_list_2_np)
print(label_list_2_np.shape)

label_list_np = np.concatenate((label_list_1_np,label_list_2_np), axis=0)
print(label_list_np)
print(label_list_np.shape)
'''
