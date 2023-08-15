from deidentify_data.profile.profile import NumericProfile
from deidentify_data.numeric_utils import pool_mean, pool_n1_variance, sum_squares


def test_pool_mean():
    profile_1 = NumericProfile(n=10, mean=54.7, n1_variance=8490.1)
    profile_2 = NumericProfile(n=25, mean=60.36, n1_variance=21819.76)

    assert round(pool_mean(profile_1, profile_2) - 58.74285714285714, 7) == 0


def test_pool_mean_2():
    profile_1 = NumericProfile(n=10, mean=54.7, n1_variance=8490.1)
    profile_2 = NumericProfile(n=1, mean=15, n1_variance=0)

    assert round(pool_mean(profile_1, profile_2) - 51.09090909090909, 7) == 0


def test_pool_n1_variance():
    profile_1 = NumericProfile(n=10, mean=54.7, n1_variance=8490.1)
    profile_2 = NumericProfile(n=25, mean=60.36, n1_variance=21819.76)

    assert round(pool_n1_variance(profile_1, profile_2) - 30538.68571428572, 7) == 0


def test_pool_n1_variance_2():
    profile_1 = NumericProfile(n=10, mean=54.7, n1_variance=8490.1)
    profile_2 = NumericProfile(n=1, mean=15, n1_variance=0)

    assert round(pool_n1_variance(profile_1, profile_2) - 9922.909090909092, 7) == 0


def test_sum_squares():
    profile_1 = NumericProfile(n=10, mean=42.7, n1_variance=9008.1)

    assert round(sum_squares(profile_1) - 27241, 7) == 0
