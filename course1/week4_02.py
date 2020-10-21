class Value:
    def __init__(self):
        self.value = None

    def __set__(self, instance, value):
        self.value = (1 - instance.commission) * value

    def __get__(self, instance, owner):
        return self.value


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission


if __name__ == '__main__':
    new_account = Account(0.1)
    new_account.amount = 100
    assert new_account.amount == 90
