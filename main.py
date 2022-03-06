import utils.history_loader as hl
from utils.wyckoff_dot_drawer import Drawer, plot

if __name__ == '__main__':
    days = int(input("Enter number of days (e.g., 30, 35, 60): "))
    code = str(input("Enter stock code prefix with sz. or sh. (e.g., sz.000001): "))
    frequency = str(input("Enter frequency (d for day, 5, 15, 30, 60 for minutes): "))
    decimal_places = int(
        input(
            "Enter stock price decimal places (0 to keep none, 1 for one decimal place, 2 for 2 decimal places): "
        )
    )
    compression_threshold = int(input("Please enter the number of dots per trend (e.g., 1, 3, 5): "))

    data = hl.load_day_history(code, days, decimal_places, frequency)
    drawer = Drawer(
        data.get("open"),
        data.get("close"),
        data.get("high"),
        data.get("low"),
        decimal_places,
        compression_threshold
    )
    rst = drawer.get_dot_data()
    plot(code, rst)
