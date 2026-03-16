from typing import Union, Optional

Number = Union[int, float]


class Distance:
    def init(self, km: Number) -> None:
        self.km: Number = km

    @staticmethod
    def _get_km(value: Union["Distance", Number]) -> Optional[Number]:
        """Отримати значення km або None, якщо тип не підходить."""
        if isinstance(value, Distance):
            return value.km
        if isinstance(value, (int, float)):
            return value
        return None

    # ------- STRING REPRESENTATION -------

    def str(self) -> str:
        return f"Distance: {self.km} kilometers."

    def repr(self) -> str:
        return f"Distance(km={self.km})"

    # ------- ADDITION -------

    def add(self, other: Union["Distance", Number]) -> "Distance":
        km = self._get_km(other)
        if km is None:
            return NotImplemented
        return Distance(self.km + km)

    def iadd(self, other: Union["Distance", Number]) -> "Distance":
        km = self._get_km(other)
        if km is None:
            return NotImplemented
        self.km += km
        return self

    # ------- MULTIPLICATION -------

    def mul(self, other: Union["Distance", Number]) -> Optional["Distance"]:
        if isinstance(other, Distance):
            return None
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    # ------- TRUE DIVISION -------

    def truediv(
            self, other: Union["Distance", Number]
    ) -> Optional["Distance"]:
        if isinstance(other, Distance):
            return None
        if isinstance(other, (int, float)):
            result = round(self.km / other, 2)
            return Distance(result)
        return NotImplemented

    # ------- COMPARISON OPERATORS -------

    def lt(self, other: Union["Distance", Number]) -> bool:
        km = self._get_km(other)
        if km is None:
            return NotImplemented
        return self.km < km

    def gt(self, other: Union["Distance", Number]) -> bool:
        km = self._get_km(other)
        if km is None:
            return NotImplemented
        return self.km > km

    def eq(self, other: Union["Distance", Number]) -> bool:
        km = self._get_km(other)
        if km is None:
            return NotImplemented
        return self.km == km

    def le(self, other: Union["Distance", Number]) -> bool:
        km = self._get_km(other)
        if km is None:
            return NotImplemented
        return self.km <= km

    def ge(self, other: Union["Distance", Number]) -> bool:
        km = self._get_km(other)
        if km is None:
            return NotImplemented
        return self.km >= km
