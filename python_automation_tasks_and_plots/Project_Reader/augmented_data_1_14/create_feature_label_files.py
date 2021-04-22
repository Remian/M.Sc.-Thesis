import os
import numpy as np
from numpy import save
from numpy import load

"""
    aug first index ---> 0
    aug last index ---> 1259

    sub_15 first index ---> 1260
    sub_15 last index ---> 1304

    feature_matrix shape ---> 1305,124,62

"""


def get_aug_feature():

    return load("augmented_1_14_feature_matrix_music.npy")

def get_aug_label():

    return load("augmented_1_14_label_vector_music.npy")

def get_sub_feature():

    return load("sub_15_feature_matrix_music.npy")

def get_sub_label():

    return load("sub_15_label_vector_music.npy")

def get_feature():

    f_aug = get_aug_feature()
    f_sub = get_sub_feature()


    f_aug_list = f_aug.tolist()
    f_sub_list = f_sub.tolist()

    for each_feature in f_sub_list:
        f_aug_list.append(each_feature)

    f_np = np.array(f_aug_list)

    #print(f_np.shape)
    #(1305, 124, 62)
    #print(f_np[1260])
    # print(f_aug.shape)
    # (1260, 124, 62)
    # last index 1259
    #print(f_sub[0])

    return f_np

def get_label():

    l_aug = get_aug_label()
    l_sub = get_sub_label()

    l_aug_list = l_aug.tolist()
    l_sub_list = l_sub.tolist()

    for each_label in l_sub_list:
        l_aug_list.append(each_label)

    l_np = np.array(l_aug_list)

    #print(l_np)
    #print(l_np.shape)
    #print(l_sub[0])
    #print(l_np[1260])

    return l_np

def save_feature_label():

    f_np = get_feature()
    l_np = get_label()

    print(f_np.shape)
    print(l_np.shape)

    save("hybrid_aug_feature_music.npy", f_np)
    save("hybrid_aug_label_music.npy", l_np)

save_feature_label()




