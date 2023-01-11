import os
import cv2
import numpy as np

def create_save_folder(name_folder_to_save_img: str = "processed") -> str:
    '''
    A function that creates a folder for saving new images with the variable name 
    "name_folder_to_save_img". If the folder has already created before, in the 
    execution folder of the main script, then the function does nothing. If the 
    folder with this name does not exist, then it creates a new folder with 
    the specified name. 

    Parameters
    ----------
    name_folder_to_save_img : str
        The name of the folder to be created.

    Returns
    -------
    _path_folder_to_save_img : str
        Path to the folder with name of variable "name_folder_to_save_img"

    '''
    
    _path_parent_folder = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    _path_folder_to_save_img = os.path.join(
        _path_parent_folder, name_folder_to_save_img)

    if not os.path.exists(_path_folder_to_save_img):
        os.mkdir(_path_folder_to_save_img)
        
    return _path_folder_to_save_img


def save_img(frame: np.ndarray, path_folder_to_save_frame: str, file_name: str) -> None:
    '''
    Function that saves an image to a file.

    Parameters
    ----------
    frame : np.ndarray
        Numpy array representing the image(RGB). 
        Values in the image range from 0 to 255.

    path_folder_to_save_frame : str
        Path to the folder where to save the image.

    file_name : str
        Name of the image to be saved. The name is to include the save extension. 

    Returns
    -------
    None
    '''
    
    path_save = os.path.join(path_folder_to_save_frame, file_name)
    cv2.imwrite(path_save,frame)
