import shutil
import os



def copy_paste_dir(source_directory_location_local, target_directory_location_local):

    parent_directory_location_local = os.getcwd()
    os.chdir(source_directory_location_local)

    file_list_local = os.listdir()
    print(file_list_local)

    for each_file in file_list_local:

        shutil.copy2(each_file, target_directory_location_local)

    os.chdir(parent_directory_location_local)


def trasfer_subject(subject_directory_location_local, target_parent_directory_local):

    parent_directory_location_local = os.getcwd()
    os.chdir(subject_directory_location_local)

    list_directory_names = os.listdir()

    for directory_name in list_directory_names:

        source_directory_location_local = subject_directory_location_local + \
                                          directory_name + \
                                          "/"

        target_directory_location_local = target_parent_directory_local + \
                                          directory_name+ \
                                          "/"

        copy_paste_dir(source_directory_location_local, target_directory_location_local)

    os.chdir(parent_directory_location_local)


def make_whole_dataset(source_parent_directory_local, target_parent_directory_local):

    parent_directory_location_local = os.getcwd()
    os.chdir(source_parent_directory_local)

    list_subject_names = os.listdir()

    for subject in list_subject_names:
        subject_directory_location_local = source_parent_directory_local+\
                                           subject+"/"
        #print junk start
        print("Transfering from : ")
        print(subject_directory_location_local)
        print("Transfering to : ")
        print(target_parent_directory_local)
        print("...............")
        # print junk end

        trasfer_subject(subject_directory_location_local, target_parent_directory_local)

    os.chdir(parent_directory_location_local)

    # print junk start
    print("File Transfer completed")
    print("...............")
    print("...............")
    # print junk end





def main():

    #music make
    source_parent_directory_music = "/home/abrar/Desktop/transformed_seed_extracted/music/"
    target_parent_directory_music = "/home/abrar/Desktop/transformed_seed_extracted/music_dir_extracted_channels/"

    make_whole_dataset(source_parent_directory_music, target_parent_directory_music)

    #welch make
    source_parent_directory_welch = "/home/abrar/Desktop/transformed_seed_extracted/welch/"
    target_parent_directory_welch = "/home/abrar/Desktop/transformed_seed_extracted/welch_dir_extracted_channels/"
    make_whole_dataset(source_parent_directory_welch, target_parent_directory_welch)

def main_2():
    # music_augmented make
    source_parent_directory_music = "/home/abrar/Desktop/transformed_Seed/music_7/"
    target_parent_directory_music = "/home/abrar/Desktop/music_7_dir/"

    make_whole_dataset(source_parent_directory_music, target_parent_directory_music)
#main()

main_2()




"""
src_file = "/home/abrar/Desktop/transformed_seed_extracted/music/Subject 1/Neg/1-1-3neg_music.csv"

target_dir_neg = "/home/abrar/Desktop/transformed_seed_extracted/music_dir_extracted_channels/Neg"
target_dir_neu = "/home/abrar/Desktop/transformed_seed_extracted/music_dir_extracted_channels/Neu"
target_dir_pos = "/home/abrar/Desktop/transformed_seed_extracted/music_dir_extracted_channels/Pos"
"""




"""

{'/home/abrar/Desktop/transformed_seed_extracted/music/Subject 1/Pos/': 
'/home/abrar/Desktop/transformed_seed_extracted/music_dir_extracted_channels/Pos/', 

'/home/abrar/Desktop/transformed_seed_extracted/music/Subject 1/Neu/': 
'/home/abrar/Desktop/transformed_seed_extracted/music_dir_extracted_channels/Neu/', 

'/home/abrar/Desktop/transformed_seed_extracted/music/Subject 1/Neg/': 
'/home/abrar/Desktop/transformed_seed_extracted/music_dir_extracted_channels/Neg/'}

"""

"""
    source_dir = "/home/abrar/Desktop/transformed_seed_extracted/music/Subject 1/Neg/"
    target_dir_neg = "/home/abrar/Desktop/transformed_seed_extracted/music_dir_extracted_channels/Neg"

    current_dir = os.getcwd()
    print(current_dir)

    copy_paste_dir(source_dir, target_dir_neg)

    current_dir = os.getcwd()
    print(current_dir)
"""

"""
    subject_directory_location = "/home/abrar/Desktop/transformed_seed_extracted/music/Subject 1/"
    target_parent_directory = "/home/abrar/Desktop/transformed_seed_extracted/music_dir_extracted_channels/"
    copy_paste_subject(subject_directory_location, target_parent_directory)
"""

