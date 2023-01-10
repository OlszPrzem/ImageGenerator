''' Test for utils functions '''

import os
import numpy as np

from imageGenerator import utils

def test_create_save_folder_exist() -> None:
    ''' Test for check if function really create new folder '''
    
    name_folder = "__test"
    path_test_folder = utils.create_save_folder(
        name_folder_to_save_img=name_folder)
    assert os.path.exists(path_test_folder)
    os.rmdir(path_test_folder)


def test_save_img1() -> None:
    ''' Test if function save new image in correct path '''

    test_img = np.zeros((300,300,3), dtype=np.uint8)
    path_folder_to_save_frame = os.path.dirname(os.path.abspath(__file__))
    name_file = "__test.png"
    path_to_check = os.path.join(path_folder_to_save_frame, name_file)

    utils.save_img(test_img, path_folder_to_save_frame, name_file)

    assert  os.path.exists(path_to_check)
    os.remove(path_to_check)
    
