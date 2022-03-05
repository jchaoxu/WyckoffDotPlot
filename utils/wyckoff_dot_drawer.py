import datetime
import math
import matplotlib.pyplot as plt
from enum import Enum


class Trend(Enum):
    Unknown = 0
    increasing = 1
    decreasing = 2


class Movement:
    def __init__(self, moves: list[float], trend: Trend):
        self._moves = moves
        self._trend = trend

    def get_moves(self):
        return self._moves

    def get_size(self):
        return len(self._moves)

    def is_increasing(self):
        return self._trend == Trend.increasing

    def is_decreasing(self):
        return self._trend == Trend.decreasing


def get_single_day_movement(open_p: float, close_p: float, high_p: float, low_p: float, precision: int):
    coefficient = math.pow(10, precision)
    rst = []
    for i in range(int(open_p * coefficient), int(high_p * coefficient + 1), 1):
        rst.append(float(float(i) / float(coefficient)))

    for i in range(int(high_p * coefficient) - 1, int(low_p * coefficient - 1), -1):
        rst.append(float(float(i) / float(coefficient)))

    for i in range(int(low_p * coefficient) + 1, int(close_p * coefficient + 1), 1):
        rst.append(float(float(i) / float(coefficient)))

    return rst


def concat_single_day_movement(movements: list[list[float]], precision) -> list[float]:
    result = []

    tmp = []
    for i in range(0, len(movements)):
        if i == 0:
            tmp.extend(movements[i])
        else:
            transition = concat_day_end_start(movements[i - 1][len(movements[i - 1]) - 1], movements[i][0], precision)
            tmp.extend(transition)
            tmp.extend(movements[i])

    for i in range(len(tmp)):
        if i > 0:
            if tmp[i] == tmp[i - 1]:
                continue
        result.append(tmp[i])

    return result


def concat_day_end_start(end, start, precision) -> list[float]:
    rst = []
    coefficient = math.pow(10, precision)

    step = 1
    if end == start:
        return rst

    if end > start:
        step = -1

    for i in range(int(end * coefficient + step), int(start * coefficient), step):
        rst.append(float(float(i) / float(coefficient)))

    return rst


def separate_trend(movements: list[float]) -> list[Movement]:
    tmp = []
    result = []
    current_trend: Trend = Trend.Unknown
    for i in range(0, len(movements)):
        if i == 1:
            if movements[i] > movements[i - 1]:
                current_trend = Trend.increasing
            else:
                current_trend = Trend.decreasing
        elif i > 1:
            if is_inverted_trend(movements[i - 1], movements[i], current_trend):
                result.append(Movement(tmp, current_trend))
                tmp = []
                if current_trend == Trend.increasing:
                    current_trend = Trend.decreasing
                else:
                    current_trend = Trend.increasing
        tmp.append(movements[i])

    if len(tmp) > 0:
        result.append(Movement(tmp, current_trend))

    return result


def is_inverted_trend(prev: float, curr: float, trend: Trend) -> bool:
    if curr > prev and trend == Trend.decreasing:
        return True

    if curr < prev and trend == Trend.increasing:
        return True

    return False


def plot(title, rst: list[Movement]):
    plt.figure(figsize=(max(len(rst) / 2, 64), 32))
    plt.title(title)
    for i in range(len(rst)):
        plt.scatter(
            [i] * rst[i].get_size(),
            rst[i].get_moves(),
            color="green" if rst[i].is_decreasing() else "red")
    plt.savefig(f".\\rst\\result_{title}_{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.png")
    print("Plot saved successfully. See result folder.")


class Drawer:
    def __init__(self, open_p, close_p, high_p, low_p, precision):
        self._open_p = open_p
        self._close_p = close_p
        self._high_p = high_p
        self._low_p = low_p
        self._size = len(self._open_p)
        self._precision = precision

    def get_single_dot(self) -> list[Movement]:
        movements = []
        for i in range(0, self._size):
            movements.append(
                get_single_day_movement(
                    self._open_p.get(i),
                    self._close_p.get(i),
                    self._high_p.get(i),
                    self._low_p.get(i),
                    self._precision
                )
            )

        # Concat days data
        concat_movement = concat_single_day_movement(movements, self._precision)

        # Separate data by trend (increasing / decreasing)
        trend_separated_movement = separate_trend(concat_movement)
        return trend_separated_movement
