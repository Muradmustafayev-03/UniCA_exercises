def calculate_mean(distribution: dict) -> float:
    """
    Calculates the mean of a distribution
    :param distribution: dictionary of form {value: probability}
    :return: the mean of the distribution
    """
    return sum([val * prob for val, prob in distribution.items()]) / sum(distribution.values())


def calculate_variance(distribution: dict) -> float:
    """
    Calculates the variance of a distribution
    :param distribution: dictionary of form {value: probability}
    :return: the variance of the distribution
    """
    mean = calculate_mean(distribution)
    return sum([prob * (val - mean) ** 2 for val, prob in distribution.items()]) / sum(distribution.values())


X = {
    1: 0.2,
    2: 0.3,
    3: 0.4,
    4: 0.1
}

print(f'The mean of the distribution is {calculate_mean(X):.2f}')
print(f'The variance of the distribution is {calculate_variance(X):.2f}')
