from re import match


class InvalidAmountError(Exception):
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f"Недопустимое значение {self.amount} рублей"


class InsufficientFundsError(Exception):
    def __str__(self):
        return "На Вашем счете недостаточно средств"


# Класс банковский счет
# Атрибуты класса: текущее количество денег на счете (account),
# Файлы: в одном из которых хранится баланс (account_f), в другом хранятся операции (log)
# Методы класса: пополнить счет (replenish), снять деньги со счета (withdraw), проверить баланс (check),
# вывести последние n операций в консоль (transactions)
class BankAccount:
    # Конструктор класса
    def __init__(self, account_file: str = "balance.txt", log_file: str = "operations.txt"):
        self.account_f = account_file
        try:
            with open(self.account_f, "r") as ac_f:
                try:
                    balance = float(ac_f.read().split("=")[1])
                # Если файл открыт, но его не получилось прочитать, завершаем работу программы
                except ValueError:
                    print("Ошибка, структура данных в файле повреждена")
                    exit(1)

                # Если баланс отрицательный, создаем исключение
                if balance < 0:
                    self.account = 0
                    raise InvalidAmountError(balance)
                self.account = balance
            self.log_f = log_file
        # Если файл не открылся, завершаем работу программы
        except FileNotFoundError:
            print("Ошибка, файл с балансом не найден")
            exit(1)

    def replenish(self, amount: float):
        try:
            if amount <= 0:
                raise InvalidAmountError(amount)
            self.account += amount
            with open(self.account_f, "w") as ac_f:
                ac_f.write("balance=" + str(self.account))
            print(f"Вы пополнили счет на {amount} рублей, на счете {self.account} рублей")
            with open(self.log_f, "a") as log_f:
                log_f.write(f"Счет пополнен на {amount} рублей\n")
        except InvalidAmountError as error:
            print(error)

    def withdraw(self, amount: float):
        try:
            if amount <= 0:
                raise InvalidAmountError(amount)
            if self.account < amount:
                raise InsufficientFundsError
            self.account -= amount
            with open(self.account_f, "w") as ac_f:
                ac_f.write("balance=" + str(self.account))
            print(f"Вы сняли со счета {amount} рублей, на счете {self.account} рублей")
            with open(self.log_f, "a") as log_f:
                log_f.write(f"Со счета снято {amount} рублей\n")
        except Exception as error:
            print(error)

    def transactions(self, operations: int):
        try:
            with open(self.log_f, "r") as log_f:
                # Читаем все строки файла
                lines = log_f.readlines()
                # Выводим последние operations строк файла
                last_five_lines = lines[-operations:]
                for line in last_five_lines:
                    print(line.strip())
        except FileNotFoundError:
            print("Ошибка, файл с операциями не найден")

    def check(self):
        print(f"На счете {self.account} рублей")
        with open(self.log_f, "a") as log_f:
            log_f.write(f"Пользователь проверил баланс. На счете {self.account} рублей\n")


if __name__ == "__main__":
    YELLOW = '\033[93m'
    RESET = '\033[0m'
    account_f = input("Введите название файла, в котором будет сохранен баланс: ")
    if not account_f:
        account_f = "balance.txt"
        with open(account_f, "w") as file:
            print(f"Вы не выбрали файл, в котором сохранен баланс. По умолчанию будет создан файл {YELLOW}balance.txt{RESET}. "
                  "Баланс по умолчанию равен 0.")
            file.write("balance=0")
    log = input("Введите название файла, в котором будут сохранены операции: ")
    if not log:
        log = "log.txt"
        with open(log, "w") as file:
            print(f"Вы не выбрали файл, в котором сохранены операции. По умолчанию будет создан файл {YELLOW}log.txt{RESET}.")
    bank = BankAccount(account_f, log)
    help_arr = [f"1. Чтобы пополнить счет, напишите {YELLOW}+{RESET} и необходимую сумму.",
                f"2. Чтобы снять со счета, напишите {YELLOW}-{RESET} и необходимую сумму.",
                f"3. Чтобы посмотреть последние операции, напишите {YELLOW}l{RESET}.",
                f"4. Чтобы посмотреть баланс, напишите {YELLOW}c{RESET}.",
                f"5. Чтобы вызвать справку напишите {YELLOW}h{RESET}.",
                f"6. Чтобы выйти, напишите {YELLOW}q{RESET}."]
    for h in help_arr:
        print(h)
    user_input = input("Введите требуемую операцию: ")
    while user_input != "q":
        match user_input:
            # Пополнение счета
            case "+":
                money_str = input("Введите сумму, на которую хотите пополнить счет: ")
                counter = 3
                while counter != 0:
                    if match(r'^\d+\.?\d*$', money_str):
                        break
                    match counter:
                        case 1:
                            print("Некорректный ввод. У вас осталась 1 попытка.\n"
                                  "Пожалуйста, введите сумму еще раз: ", end="")
                        case 2 | 3 | 4:
                            print(f"Некорректный ввод. У вас осталось {counter} попытки.\n"
                                  f"Пожалуйста, введите сумму еще раз: ", end="")
                        case _:
                            print(f"Некорректный ввод. У вас осталось {counter} попыток.\n"
                                  f"Пожалуйста, введите сумму еще раз: ", end="")
                    money_str = input()
                    counter -= 1
                if counter == 0:
                    print("Вы исчерпали все попытки. Возврат в меню")
                    user_input = input("Введите требуемую операцию: ")
                    continue
                bank.replenish(float(money_str))
                user_input = input("Введите требуемую операцию: ")
            # Снятие денег со счета
            case "-":
                money_str = input("Введите сумму, которую хотите снять со счета: ")
                counter = 3
                while counter != 0:
                    if match(r'^\d+\.?\d*$', money_str):
                        break
                    match counter:
                        case 1:
                            print("Некорректный ввод. У вас осталась 1 попытка.\n"
                                  "Пожалуйста, введите сумму еще раз: ", end="")
                        case 2 | 3 | 4:
                            print(f"Некорректный ввод. У вас осталось {counter} попытки.\n"
                                  f"Пожалуйста, введите сумму еще раз: ", end="")
                        case _:
                            print(f"Некорректный ввод. У вас осталось {counter} попыток.\n"
                                  f"Пожалуйста, введите сумму еще раз: ", end="")
                    money_str = input()
                    counter -= 1
                if counter == 0:
                    print("Вы исчерпали все попытки. Возврат в меню")
                    user_input = input("Введите требуемую операцию: ")
                    continue
                bank.withdraw(float(money_str))
                user_input = input("Введите требуемую операцию: ")
            # Проверка баланса
            case "c":
                bank.check()
                user_input = input("Введите требуемую операцию: ")
            # Вызов справки
            case "h":
                for h in help_arr:
                    print(h)
                user_input = input("Введите требуемую операцию: ")
            # Просмотр операций
            case "l":
                num_of_ops = int(input("Введите число операций, которые хотите просмотреть. "
                                       "Чтобы посмотреть все операции, напишите 0: "))
                bank.transactions(num_of_ops)
                user_input = input("Введите требуемую операцию: ")
            # Выход из приложения
            case "q":
                print("До свидания!")
                break
            # Если операция не распознана, попадаем сюда
            case _:
                user_input = input("Ошибка, операция не распознана. Введите поддерживаемую операцию: ")
    print('До свидания!')
