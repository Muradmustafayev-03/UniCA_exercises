def dog_to_human_age(age):
    """
    Converts a dog's age to human age.
    First 2 years as 10.5 and each additional year counts as 4
    :param age: dog age in years
    :return: human age in years
    """
    if age < 0:
        raise ValueError("Cannot convert negative age")

    if age <= 2:
        return age * 10.5
    else:
        return 21 + (age - 2) * 4


def test_dog_to_human_age():
    assert dog_to_human_age(1) == 10.5
    assert dog_to_human_age(2) == 21
    assert dog_to_human_age(3) == 25
    assert dog_to_human_age(4) == 29
    assert dog_to_human_age(5) == 33
    assert dog_to_human_age(6) == 37
    assert dog_to_human_age(7) == 41

    assert dog_to_human_age(0) == 0

    try:
        dog_to_human_age(-1)
        raise AssertitionError('No error raised')
    except ValueError:
        pass

    print("All tests passed")


test_dog_to_human_age()
