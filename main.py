"""
Program prepared due to recrutation task.

Application have two workers, in two seperate threads. 
First of them - "Producer" has to use source method to generate images and put to queue_A. 
Second worker - "Consumer" has to download images from queue_A, change them size and apply 
median filter, to the end put new processed image to queue_B.
Main function of the program has to download images from queue_B and save them in 
directory "processed".

"""

from queue import Queue
import datetime

import imageGenerator as ig # Special prepared for this task package imageGenerator


class MainProgram:
    '''
    Main class of program. 

    Attributes:
    -----------
    queue_A : queue.Queue
        Queue with new frames. Frame from queue_A is download by get() method.

    queue_B : queue.Queue
        Queue for processed frames. New images are added to queue_B via
        put() method.

    num_frames_to_generate : int
        Number of images that should generated and save in folder.

    base_name_saved_imgs : str
        Part of the name of images, that is generated for each new run program.

    path_folder_to_save_img : str
        Patch of a folder where new generated images will be save.

    source : Callable
        Method for generate new images by Producer.

    producer : Producer
        Instance of class Producer, object resposible for generate new frames and 
        put them to queue_A.

    Consumer : Consumer
        Instance of class Consumer. Main aim that object is download frame from
        queue_A, resize that frame, apply median filter on that frame and put
        processed frame to queue_B.

    Methods:
    --------
    main_loop
        Start thread responsible for resize and filter frame.

    generate_name
        Method for generate name of img to save

        Arguments:
        - ```num_actual_saved_img``` : int - numer actual img to save


        Return:
        - ```name_file``` : str - generated name of file with 
        extension *.png, for atctual image number.


    Examples 
    --------
    >>> if __name__ == "__main__":
    >>>     task = MainProgram()
    >>>     task.main_loop()
    
    '''

    def __init__(self) -> None:
        '''
        Constructor

        Parameters:
        -----------
        None
        
        '''

        self.queue_A = Queue()
        self.queue_B = Queue()
        self.num_frames_to_generate = 100 

        _now = datetime.datetime.now()
        self.base_name_saved_imgs = _now.strftime("%Y%m%d_%H%M%S") # create unique part name of images for every run program

        self.path_folder_to_save_img = ig.create_save_folder(
            name_folder_to_save_img="processed"
            )
    
        self.source = ig.Source((1024, 768, 3))

        self.producer = ig.Producer(
            self.source.get_data, 
            queue_A = self.queue_A, 
            )

        self.consumer = ig.Consumer(
            queue_A = self.queue_A,
            queue_B = self.queue_B
        )


    def main_loop(self) -> None:
        ''' Main loop of program '''
        
        run_program = True
        num_actual_saved_img = 0

        # run loops producer and consumer
        self.producer.start()
        self.consumer.start()

        # main loop of program
        while run_program:

            if not self.queue_B.empty():
                frame = self.queue_B.get()

                name_img = self.generate_name(num_actual_saved_img)
                ig.save_img(
                    frame, 
                    path_folder_to_save_frame = self.path_folder_to_save_img,
                    file_name = name_img
                    )

                num_actual_saved_img +=1

                if num_actual_saved_img >= self.num_frames_to_generate:
                    run_program = False

        # stop loops producer and consumer
        self.producer.stop()
        self.consumer.stop()

    def generate_name(self, num_actual_saved_img: int) -> str:
        '''
        Method to generate new file  name to save, with extension *.png .
        
        Parameters:
        -----------
        num_actual_saved_img : int
            Number of actual saving photo.


        Returns:
        --------
        generated_name : str
            Generated name for image.

        '''

        return "{}_{}.png".format(
            self.base_name_saved_imgs, 
            num_actual_saved_img,
            )
        

if __name__ == "__main__":
    task = MainProgram()
    task.main_loop()
