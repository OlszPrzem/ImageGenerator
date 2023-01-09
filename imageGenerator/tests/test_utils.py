import os
import numpy as np

from imageGenerator import utils

def test_create_save_folder_exist() -> None:
    name_folder = "__test"
    path_test_folder = utils.create_save_folder(
        name_folder_to_save_img=name_folder)
    assert os.path.exists(path_test_folder)
    os.rmdir(path_test_folder)



# def test_create_save_folder_correct_path() -> None:

#     name_folder = "test"
#     destination_path = os.path.dirname(os.path(__file__)
#     path_test_folder = utils.create_save_folder(
#         name_folder_to_save_img=name_folder)

#     print("aaa")
#     print(path_test_folder)

#     assert os.path.exists(path_test_folder)

#     os.rmdir(path_test_folder)

def test_save_img1() -> None:
    test_img = np.zeros((300,300,3), dtype=np.uint8)
    path_folder_to_save_frame = os.path.dirname(os.path.abspath(__file__))
    name_file = "__test.png"
    path_to_check = os.path.join(path_folder_to_save_frame, name_file)

    utils.save_img(test_img, path_folder_to_save_frame, name_file)

    assert  os.path.exists(path_to_check)
    os.remove(path_to_check)
    
