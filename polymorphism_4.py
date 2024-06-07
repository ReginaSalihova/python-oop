class MinStat:
    def __init__(self):
        self.nums = []

    def add_number(self, value):
        self.nums.append(value)

    def result(self):
        if not self.nums:
            return None
        return min(self.nums)


class MaxStat:
    def __init__(self):
        self.nums = []

    def add_number(self, value):
        self.nums.append(value)

    def result(self):
        if not self.nums:
            return None
        return max(self.nums)


class AverageStat:
    def __init__(self):
        self.nums = []

    def add_number(self, value):
        self.nums.append(value)

    def result(self):
        if not self.nums:
            return None
        return sum(self.nums) / len(self.nums)


values = [1, 0, 0]

mins = MinStat()
maxs = MaxStat()
average = AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)

print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))