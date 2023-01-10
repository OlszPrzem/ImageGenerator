''' Test for Source class '''

import numpy as np

from imageGenerator.source import Source


def test_get_data_shape_result() -> None:
    ''' Test for check correct shape of generated frames '''

    end_shape = (300,300,3)
    source = Source((300,300,3))
    data = source.get_data()
    assert (data.shape == end_shape)


def test_get_data_range_result() -> None:
    ''' Test for check range of value in generated frames '''

    source = Source((300,300,3))
    data = source.get_data()
    min_value = np.amin(data)
    max_value = np.amax(data)
    assert ((min_value >= 0) & (max_value <= 255))


def test_get_data_random_result() -> None:
    ''' Test for check if all values in frame are not the same '''

    source = Source((300,300,3))
    data = source.get_data()
    assert not np.all(data == data[0])
