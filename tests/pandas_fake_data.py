"""
Helper Module for generating fake data during tests
"""

import pandas as pd
from random import randint, random
from faker import Faker
from typing import Callable, Any, List

def generate_iterable_fake_data(faker_function: Callable[[], Any], num_rows: int = 100) -> List[Any]:
    return [faker_function() for _ in range(num_rows)]

def generate_fake_pandas_dataframe(num_rows: int = 100) -> pd.DataFrame:
    factory = Faker()
    df = pd.DataFrame()
    df["integer"] = generate_iterable_fake_data(faker_function=lambda: randint(1, 100), num_rows=num_rows)
    df["float"] = generate_iterable_fake_data(faker_function=lambda: 100*random(), num_rows=num_rows)
    df["email"] = generate_iterable_fake_data(faker_function=factory.email, num_rows=num_rows)
    df["name"] = generate_iterable_fake_data(faker_function=factory.name, num_rows=num_rows)
    df["address"] = generate_iterable_fake_data(faker_function=factory.address, num_rows=num_rows)
    df["country"] = generate_iterable_fake_data(faker_function=factory.country, num_rows=num_rows)
    df["text"] = generate_iterable_fake_data(faker_function=factory.text, num_rows=num_rows)

    return df
