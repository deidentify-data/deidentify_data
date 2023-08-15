def pool_mean(profile_1, profile_2):
    """
    Given two NumericProfiles, finds the pooled mean
    """
    mean = (profile_1.n * profile_1.mean + profile_2.n * profile_2.mean) / (
        profile_1.n + profile_2.n
    )
    return mean


def sum_squares(profile):
    """
    Given a profile, finds the total sum of squares of the dataset
    """
    return profile.n1_variance + profile.n * profile.mean**2


def pool_n1_variance(profile_1, profile_2):
    """
    Given two profiles, finds the pooled n1_variance
    """
    pooled_mean = pool_mean(profile_1, profile_2)
    n = profile_1.n + profile_2.n
    return sum_squares(profile_1) + sum_squares(profile_2) - n * (pooled_mean) ** 2
