import numpy as np

class Source:
    '''
    A class for generate new image frames by get_data method

    Attributes:
    -----------
    _source_shape : touple
        Touple with values of shape generated frames.

    Methods:
    --------
    get_data
        Method generate new image with random values. 
        It is RGB noise.

        Attributes:
        - ``` None ```

        Return:
        - ``` frame ``` : generated frame (``np.ndarray``)


    Example 
    --------
    >>> source = Source((300,300,3))
    >>>
    >>> frame = source.get_data()
    >>>
    >>> cv2.imshow("test", frame)
    >>> cv2.waitKey(0)
    
    '''

    def __init__(self, source_shape: tuple) -> None:
        '''
        Constructor class for generate frames method

        Parameters:
        -----------
        source_shape : touple
            Touple with shape for generate frames
        '''

        self._source_shape: tuple = source_shape


    def get_data(self) -> np.ndarray:
        '''
        Method for generate new frame
        
        Parameters:
        -----------
        None

        Return:
        -------
        frame : np.ndarray
            Generated frame with random RGB values.
        '''
        
        rows, cols, channels = self._source_shape
        return np.random.randint(
            256,
            size = rows * cols * channels,
            dtype = np.uint8,
        ).reshape(self._source_shape)

