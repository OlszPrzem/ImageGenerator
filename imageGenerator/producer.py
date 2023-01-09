import threading
import time
import numpy as np
from queue import Queue
from typing import Callable

class Producer(threading.Thread):
    '''
    A class for generate new image frames by get_new_frame method and
    put new image to queue_A. 

    Attributes:
    -----------
    get_new_frame : Callable
        Method download new frame from source, 
        takes no arguments, but return frame:

        Arguments:
        None

        Return:
        - ``frame`` : generated frame (``np.ndarray``)

    _queue_A : queue.Queue
        Queue for new generate frames from get_new_frame method.

    num_generated_frames : int
        Actual number of generated frames.

    _time_update_queue_A: : float
        The period of time every which a new image is generated and
        put new frame to queue_A.

    _active_thread : bool
        The value specifying the condition for the main loop of the class.


    Methods:
    --------
    start
        Start thread responsible for generatenew frames and puts frames
        to queue_A.

    stop
        Stop thread changing frame.


    Example 
    --------
    >>> def return_img() -> np.ndarray:
    >>>     return np.zeros((300,300,3), dtype=np.uint8)
    >>>
    >>> my_queue_A = Queue()
    >>>
    >>> producer = Producer(
    >>>     source_method = return_img
    >>>     queue_a = my_queue_A
    >>>     )
    >>>
    >>> producer.start()
    >>>
    >>> while True:
    >>>     frame = my_queue_A.get()
    >>>
    >>>     # main program
    >>>
    >>>     cv2.imshow("Test", frame)
    >>>     cv2.waitKey(5)
    >>>
    >>> producer.stop()
    
    '''

    def __init__(
            self, 
            source_method: Callable[[], np.ndarray], 
            queue_A: Queue, 
            ) -> None:
        '''
        Constructor class for generate new image frames and put to queue_A. 

        Parameters:
        -----------
        source_method : Callable
            Method download new frame from source, 
            takes no arguments, but return frame:

            Arguments:
            - ``None``

            Return:
            - ``frame`` : generated frame (``np.ndarray``)

        queue_A : queue.Queue
            Queue for new generate image frames.

        '''
        super().__init__()

        self.get_new_frame: Callable[[], np.ndarray] = source_method
        self._queue_A: Queue = queue_A
        self.num_generated_frames: int = 0

        self._time_update_queue_A: float = 0.050 # s
        self._active_thread: bool = False


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

        New images are generate from get_new_frame method and put to queue_A every _time_update_queue_A seconds.
        '''
        while self._active_thread:
            self._update_queue()
            time.sleep(self._time_update_queue_A)


    def _update_queue(self) -> None:
        '''
        Method for call get_new_frame method and put result to queue_A.
        Increase num_generated_frames value for every frame.
        '''
        frame = self.get_new_frame()
        self._queue_A.put(frame)
        self.num_generated_frames += 1
