from game.framework import Vector2D


def test_sum_2_vectors():
    vector1 = Vector2D(2, 3)
    vector2 = Vector2D(4, 5)
    assert vector1 + vector2 == Vector2D(6, 8)


def test_vector_length_calculation():
    vector1 = Vector2D(3, 4)
    assert vector1.length == 5


def test_that_vector_loops_properly():
    vector1 = Vector2D(3, 4)
    size_vector = Vector2D(2, 2)
    expected_result = Vector2D(1, 0)
    result = vector1 % size_vector
    assert result == expected_result
