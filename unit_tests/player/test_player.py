from game.framework import Vector


def test_that_2_element_vector_has_len_2():
    vector = Vector([2, 3])
    assert len(vector) == 2


def test_sum_2_vectors():
    vector1 = Vector([2, 3])
    vector2 = Vector([4, 5])
    assert vector1 + vector2 == Vector([6, 8])


def test_vector_length_calculation():
    vector1 = Vector([3, 4])
    assert vector1.length == 5


def test_that_vector_loops_properly():
    vector1 = Vector([3, 4])
    size_vector = Vector([2, 2])
    expected_result = Vector([1, 0])
    result = vector1 % size_vector
    assert result == expected_result
