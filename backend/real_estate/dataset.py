from dataclasses import dataclass
@dataclass
class Dataset(object):
    context: str
    fname: str
    housing: object

    @property
    def context(self) -> str: return self._context
    @context.setter
    def context(self, context): self._context = context
    @property
    def fname(self) -> str: return self._fname
    @fname.setter
    def fname(self, fname): self._fname = fname
    @property
    def housing(self) -> object: return self._housing
    @housing.setter
    def housing(self, housing): self._housing = housing
