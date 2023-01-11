import threading
import time
import cv2
import numpy as np
from queue import Queue


class Consumer(threading.Thread):
    '''
    A class for modify image frames by resize and median filter. 

    Attributes:
    -----------
    queue_A : queue.Queue
        Queue with new frames. Frame from queue_A is download by get() method.

    queue_B : queue.Queue
        Queue for processed frames. New images are adding to queue_B by put() method.

    _active_thread : bool
        The value specifying the condition for the main loop of the class.

    _resize_coef : int
        Photo resize factor. (Default = 2)

    _median_kernel : int
        Value of kernel for median filer. (Default = 5)


    Methods:
    --------
    start
        Start thread responsible for resize and filter frame.

    stop
        Stop thread changing frame.


    Examples 
    --------
    >>> my_queue_A = Queue()
    >>> my_queue_B = Queue()
    >>>
    >>> consumer = Consumer(
    >>>     queue_A = my_queue_A
    >>>     queue_B = my_queue_B
    >>>     )
    >>>
    >>> consumer.start()
    >>>
    >>> while True:
    >>>     frame = np.zeros((300,300,3), dtype = np.uint8)
    >>>     my_queue_A.put(frame)
    >>>
    >>>     # main program
    >>>
    >>>     new_frame = my_queue_B.get()  # modified image, reduced and with median filter
    >>> consumer.stop()
    
    '''

    def __init__(self, queue_A: Queue, queue_B: Queue) -> None:
        '''
        A class for modifying image frames by resize and median filter. 

        Parameters:
        -----------
        queue_A : queue.Queue
            Queue with new frames. Frame from queue_A is download by get() method.

        queue_B : queue.Queue
            Queue for processed frames. New images are adding to queue_B by put() method.


        '''
        super().__init__()
        self.queue_A = queue_A
        self.queue_B = queue_B

        self._active_thread = False
        self._resize_coef = 2
        self._median_kernel = 5


    def start(self) -> None:
        ''' 
        Method for start main loop of class

        Parameters
        ----------
        None

        Returns
        -------
        None
                
        '''
        self._active_thread = True
        super().start()


    def stop(self) -> None:
        ''' 
        Method for stop main loop of class
        
        Parameters
        ----------
        None

        Returns
        -------
        None
        
        '''
        self._active_thread = False


    def run(self) -> None:
        ''' 
        Main function of class.

        Method work in the loop, depends on _active_thread value and wait for new image from queue_A. 
        If queue_A is not empty, the first element is taken. Frame is resized and apply median filter. New frame is put on queue_B.
        
        '''
        while self._active_thread:
            if not self.queue_A.empty():
                frame = self.queue_A.get()
                frame = self._resize(
                    img = frame, 
                    coeficiant_resize = self._resize_coef
                    )
                frame = self._median_filter(
                    img = frame,
                    kernel = self._median_kernel)

                self.queue_B.put(frame)                


    @staticmethod
    def _median_filter(img: np.ndarray, kernel: int = 5) -> np.ndarray:
        ''' 
        Median filter for frame
        
        Parameters
        ----------
        img : np.ndarray
            Frame to apply median filter.
        
        kernel : int
            Value of kernel for median filter.

        Returns
        -------
        img : np.ndarray
            Frame with median filter
        
        '''
        return cv2.medianBlur(img, kernel)
    
    
    @staticmethod
    def _resize(img: np.ndarray, coeficiant_resize: int = 2) -> np.ndarray:
        ''' 
        Resize method for frame
        
        Parameters
        ----------
        img : np.ndarray
            Frame to resize.

        coeficiant_resize : int
            Coeficiant how many times frame should be resize. 

        Returns
        -------
        img : np.ndarray
            Resized image.
        
        '''
        return cv2.resize(
            img, 
            (int(img.shape[0]/coeficiant_resize),
            int(img.shape[1]/coeficiant_resize))
        )
