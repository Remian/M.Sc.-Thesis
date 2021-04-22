import os
import numpy as np
import pandas as pd
from read_full_dir import read_dir_matrix
from numpy import save
from numpy import load
import tensorflow as tf



def get_feature_label_matrix(data_set_dir_location_local, class_label_dict_local):


    dataset_feature_matrix_local, dataset_label_vector_local, number_of_label_local = \
        read_data_set_matrix(data_set_dir_location_local, class_label_dict_local)

    feature_matrix_local = get_float_32_feature_matrix(dataset_feature_matrix_local)
    label_matrix_local = get_label_matrix(dataset_label_vector_local, number_of_label_local)

    return feature_matrix_local, label_matrix_local, dataset_label_vector_local



def read_data_set_matrix(data_set_dir_location_local, class_label_dict_local):

    parent_directory_local = os.getcwd()

    class_location_list_local, label_value_list_local, number_of_label_local = \
        get_location_label_list(data_set_dir_location_local, class_label_dict_local)

    for index_local in range(len(class_location_list_local)):

        class_feature_matrix_local, class_label_vector = read_dir_matrix(class_location_list_local[index_local],
                                            label_value_list_local[index_local])

        if index_local == 0:
            dataset_feature_matrix_local = class_feature_matrix_local
            dataset_label_vector_local = class_label_vector

        else:
            dataset_feature_matrix_local = np.concatenate((dataset_feature_matrix_local, class_feature_matrix_local))
            dataset_label_vector_local = np.concatenate((dataset_label_vector_local, class_label_vector))

    os.chdir(parent_directory_local)

    return dataset_feature_matrix_local, dataset_label_vector_local, number_of_label_local

def get_float_32_feature_matrix(dataset_feature_matrix_local):

    dataset_feature_matrix_float_32_local = np.float32(dataset_feature_matrix_local)

    return dataset_feature_matrix_float_32_local

def get_label_matrix(label_vector_local, number_of_labels):

    with tf.Session() as sesh:
        label_matrix_local = sesh.run(tf.one_hot(label_vector_local, number_of_labels))

    return label_matrix_local



def get_location_label_list(dir_location_local, label_dict_local):

    label_values_list_local = []
    locations_list_local = []

    for k,v in label_dict_local.items():

        locations_list_local.append(dir_location_local+k)
        label_values_list_local.append(v)

    return locations_list_local, label_values_list_local, len(label_values_list_local)


def run_test():
    #data_set_dir_location = "/home/abrar/Desktop/transformed_seed_extracted/music_dir_extracted_channels/"
    data_set_dir_location = "/home/abrar/Desktop/trasformed_seed_augmented/music_dir_augmented_1_14/"
    class_label_dict = {"Neg": 0, "Neu": 1, "Pos": 2}

    feature_matrix, label_matrix, label_vector = get_feature_label_matrix(data_set_dir_location, class_label_dict)

    print(os.getcwd())
    """
    save('temp_test_feature_matrix_music.npy', feature_matrix)
    save('temp_test_label_matrix_music.npy', label_matrix)
    save('temp_test_label_vector_music.npy', label_vector)
    """
    save('augmented_data_1_14/augmented_1_14_feature_matrix_music.npy', feature_matrix)
    save('augmented_data_1_14/augmented_1_14_label_matrix_music.npy', label_matrix)
    save('augmented_data_1_14/augmented_1_14_label_vector_music.npy', label_vector)

    

    print(feature_matrix.shape)
    print(type(feature_matrix[1,1,1]))


    print(label_matrix)
    print(label_matrix.shape)
    print(type(label_matrix))


def run_test_v2():
    data_set_dir_location = "/home/abrar/Desktop/trasformed_seed_augmented/music_dir_real_15/"
    class_label_dict = {"Neg": 0, "Neu": 1, "Pos": 2}

    feature_matrix, label_matrix, label_vector = get_feature_label_matrix(data_set_dir_location, class_label_dict)

    print(os.getcwd())

    save('augmented_data_1_14/sub_15_feature_matrix_music.npy', feature_matrix)
    save('augmented_data_1_14/sub_15_label_matrix_music.npy', label_matrix)
    save('augmented_data_1_14/sub_15_label_vector_music.npy', label_vector)



    print(feature_matrix.shape)
    print(type(feature_matrix[1, 1, 1]))

    print(label_matrix)
    print(label_matrix.shape)
    print(type(label_matrix))


def run_music_7():
    data_set_dir_location = "/home/abrar/Desktop/music_7_dir/"
    class_label_dict = {"Neg": 0, "Neu": 1, "Pos": 2}

    feature_matrix, label_matrix, label_vector = get_feature_label_matrix(data_set_dir_location, class_label_dict)

    print(os.getcwd())

    save('music_7_data/7_feature_matrix_music.npy', feature_matrix)
    save('music_7_data/7_label_matrix_music.npy', label_matrix)
    save('music_7_data/7_label_vector_music.npy', label_vector)


    print(feature_matrix.shape)
    print(type(feature_matrix[1, 1, 1]))

    print(label_matrix)
    print(label_matrix.shape)
    print(type(label_matrix))


#run_test()
#run_test_v2()
run_music_7()


