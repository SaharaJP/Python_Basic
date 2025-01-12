class Date:
    def __init__(self, day: int = 0, month: int = 0, year: int = 0) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        return 'День: {day}\tМесяц: {month}\tГод: {year}'.format(
            day=self.day, month=self.month, year = self.year
        )

    @classmethod
    def is_date_valid(cls, date: str) -> bool:
        day, month, year = map(int, date.split('-'))
        return 0 < day <= 31 and 0 < month <= 12 and 0 < year <= 9999

    @classmethod
    def from_string(cls, date: str):
        day, month, year = map(int, date.split('-'))
        date_obj = cls(day, month, year)
        return date_obj


my_date = Date.from_string('10-12-2077')
print(my_date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))

