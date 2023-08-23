from pydantic import BaseModel, Field
from abc import ABC, abstractmethod
from deidentify_data.profile.base_profile import BaseProfile


class Analysis(BaseModel):
    fields: list[BaseProfile] = Field(description="list of profiles for the various fields")


class BaseAnalyzer(BaseModel, ABC):
    """
    Abstract BaseAnalyzer template
    """

    # TODO need to come up with some standard arguments for this guy
    @classmethod
    @abstractmethod
    def analyze(cls, *args, **kwargs) -> Analysis:
        pass


class BaseTabularAnalyzer(BaseAnalyzer):

    @abstractmethod
    @staticmethod
    def analyze_column() -> BaseProfile:

    @classmethod
    def analyze(cls, *args, **kwargs) -> Analysis:


    # TODO need to come up with some standard arguments for this guy
    @abc.abstractmethod
    @classmethod
    def analyze_field(cls, *args, **kwargs) -> BaseProfile:
        pass



