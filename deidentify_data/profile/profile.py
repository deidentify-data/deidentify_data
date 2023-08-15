from pydantic import BaseModel


class NumericProfile(BaseModel):
    n: int
    mean: float
    n1_variance: float   # n-1 times the variance
