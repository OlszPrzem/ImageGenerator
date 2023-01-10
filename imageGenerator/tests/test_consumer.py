''' Tests for Consumer object '''

import numpy as np
from queue import Queue
import time

from imageGenerator.consumer import Consumer

start_img = np.zeros((300, 300, 3), dtype = np.uint8)
end_img = np.zeros((150, 150, 3), dtype = np.uint8)

def test_Consumer_resize_RGB1() -> None:
    ''' Test resize method on RGB image '''

    proceed_img = Consumer._resize(start_img, 2)
    assert (end_img==proceed_img).all()


def test_Consumer_resize_GRAY1() -> None:
    ''' Test resize method on GRAY image '''

    start_img = np.zeros((300, 300, 1), dtype = np.uint8)
    end_img = np.zeros((100, 100, 1), dtype = np.uint8)

    proceed_img = Consumer._resize(start_img, 3)
    assert (end_img==proceed_img).all()


def test_Consumer_create() -> None:
    ''' Test check corect create Consumer and alive main thread '''

    test_queue_A = Queue()
    test_queue_B = Queue()

    test_consumer = Consumer(
        queue_A = test_queue_A,
        queue_B = test_queue_B
    )

    test_consumer.start()

    assert test_consumer.is_alive()
    test_consumer.stop()


def test_Consumer_stop() -> None:
    ''' Test check correct stop Consumer main thread '''
    
    test_queue_A = Queue()
    test_queue_B = Queue()

    test_consumer = Consumer(
        queue_A = test_queue_A,
        queue_B = test_queue_B
    )

    test_consumer.start()
    test_consumer.stop()
    time.sleep(0.1)

    assert not test_consumer.is_alive()


def test_Consumer_put_get() -> None:
    ''' 
    Test check correct work of main loop Consumer, by put new 
    frame to queue_A and recieved processed frame from queue_B
    '''

    test_queue_A = Queue()
    test_queue_B = Queue()

    test_consumer = Consumer(
        queue_A = test_queue_A,
        queue_B = test_queue_B
    )

    test_consumer.start()
    test_queue_A.put(start_img)
    time.sleep(0.1)
    result_frame = test_queue_B.get(timeout=1)

    assert (result_frame == end_img).all()
    test_consumer.stop()

