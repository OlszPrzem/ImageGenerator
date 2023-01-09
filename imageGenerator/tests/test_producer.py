import numpy as np
from queue import Queue
import time

from imageGenerator import producer


global_test_frame = np.zeros((400,500,3), dtype = np.uint8)

def __generate_test_frames() -> np.ndarray:
    return global_test_frame


def test_producer_is_alive() -> None:
    test_queue_A = Queue()
    test_producer = producer.Producer(
        source_method = __generate_test_frames,
        queue_A = test_queue_A,
        )

    test_producer.start()
    assert test_producer.is_alive()
    test_producer.stop()


def test_producer_update_queue() -> None:
    test_queue_A = Queue()
    test_producer = producer.Producer(
        source_method = __generate_test_frames,
        queue_A = test_queue_A,
        )

    test_producer.start()
    test_frame = test_queue_A.get(timeout=1)
    assert (test_frame == global_test_frame).all()
    test_producer.stop()


def test_producer_stop() -> None:
    test_queue_A = Queue()
    test_producer = producer.Producer(
        source_method = __generate_test_frames,
        queue_A = test_queue_A,
        )

    test_producer.start()
    test_producer.stop()

    time.sleep(2*test_producer._time_update_queue_A)
    assert not test_producer.is_alive()
