class CustomList(list):
    def __add__(self, value):
        if isinstance(value, list):
            self_len = len(self)
            val_len = len(value)
            if val_len <= self_len:
                res = [self[i] + value[i] if i < val_len else self[i]
                       for i in range(self_len)]
            else:
                res = [self[i] + value[i] if i < self_len else value[i]
                       for i in range(val_len)]
        elif isinstance(value, int):
            res = [x + value for x in self]
        else:
            return NotImplemented
        return CustomList(res)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, value):
        if isinstance(value, list):
            self_len = len(self)
            val_len = len(value)
            if val_len <= self_len:
                res = [self[i] - value[i] if i < val_len else self[i]
                       for i in range(self_len)]
            else:
                res = [self[i] - value[i] if i < self_len else -value[i]
                       for i in range(val_len)]
        elif isinstance(value, int):
            res = [x - value for x in self]
        else:
            return NotImplemented
        return CustomList(res)

    def __rsub__(self, value):
        if isinstance(value, list):
            self_len = len(self)
            val_len = len(value)
            if val_len <= self_len:
                res = [value[i] - self[i] if i < val_len else -self[i]
                       for i in range(self_len)]
            else:
                res = [value[i] - self[i] if i < self_len else value[i]
                       for i in range(val_len)]
        elif isinstance(value, int):
            res = [value - x for x in self]
        else:
            return NotImplemented
        return CustomList(res)

    def __str__(self):
        return f"{list(self)}, sum: {sum(self)}"

    def __eq__(self, value):
        return sum(self) == sum(value) if isinstance(value,
                                                     CustomList) else False

    def __ne__(self, value):
        return sum(self) != sum(value) if isinstance(value,
                                                     CustomList) else False

    def __gt__(self, value):
        return sum(self) > sum(value) if isinstance(value,
                                                    CustomList) else False

    def __ge__(self, value):
        return sum(self) >= sum(value) if isinstance(value,
                                                     CustomList) else False

    def __lt__(self, value):
        return sum(self) < sum(value) if isinstance(value,
                                                    CustomList) else False

    def __le__(self, value):
        return sum(self) <= sum(value) if isinstance(value,
                                                     CustomList) else False
