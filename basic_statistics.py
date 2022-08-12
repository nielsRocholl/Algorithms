from data import basic_statistics_data as data

"""
Returns the mean of a list of numbers
"""


def get_mean(input_list):
    return sum(input_list) / len(input_list)


"""
Returns the median of a list of numbers
"""


def get_median(input_list):
    n = len(input_list)
    index = n // 2
    # if length even
    if n % 2 == 0:
        return sum(sorted(input_list)[index - 1:index + 1]) / 2
    # if length odd
    else:
        return sorted(input_list)[index]


"""
Returns the mode of a list of numbers
"""


def get_mode(input_list):
    mode = {}
    for i in input_list:
        if i in mode:
            mode[i] += 1
        else:
            mode[i] = 1
    return max(mode, key=mode.get)


"""
Returns the sample variance of a list of numbers
"""


def get_sample_variance(input_list):
    mean = get_mean(input_list)
    n = len(input_list)
    return sum([pow(i - mean, 2) / (n - 1) for i in input_list])


"""
Returns the confidence interval of a list of numbers
"""


def get_confidence_interval(input_list):
    z = 1.96
    n = len(input_list)
    sd = get_sample_variance(input_list) ** 0.5
    se = sd / (n ** 0.5)
    mean = get_mean(input_list)
    return [mean - (z * se), mean + (z * se)]


"""
Return a dictionary of statistics for a list of numbers. Statistics include:
mean, median, mode, sample variance, sample standard deviation, mean confidence interval.
"""


def get_statistics(input_list):
    stats = {
        "mean": sum(input_list) / len(input_list),
        "median": get_median(input_list),
        "mode": get_mode(input_list),
        "sample_variance": get_sample_variance(input_list),
        "sample_standard_deviation": get_sample_variance(input_list) ** 0.5,
        "mean_confidence_interval": [
            get_mean(input_list) - 1.96 * get_sample_variance(input_list) ** 0.5 / (len(input_list) ** 0.5),
            get_mean(input_list) + 1.96 * get_sample_variance(input_list) ** 0.5 / (len(input_list) ** 0.5)],
    }
    return stats


result = get_statistics(data['list'])
print(f'{result == data["expected"]}\n{result}')
