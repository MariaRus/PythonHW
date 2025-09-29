class Deposit:
    def __init__(self, start_balance, years):
        self.start_balance = start_balance
        self.years = years
        self.interest_rate = 0.10  # 10% годовых
        self.months = years * 12

    def calculate_final_amount(self):
        # Формула для расчета с капитализацией процентов
        final_amount = self.start_balance * ((1 + self.interest_rate / 12) ** self.months)
        return round(final_amount, 2)


class Bank:
    def __init__(self):
        self.clients = {}
        self.deposits = {}

    def register_client(self, client_id, name):
        if client_id not in self.clients:
            self.clients[client_id] = name
            return True
        return False

    def open_deposit_account(self, client_id, start_balance, years):
        if client_id in self.clients:
            self.deposits[client_id] = Deposit(start_balance, years)
            return True
        return False

    def calc_interest_rate(self, client_id):
        if client_id in self.deposits:
            return self.deposits[client_id].calculate_final_amount()
        return False

    def close_deposit(self, client_id):
        if client_id in self.deposits:
            final_amount = self.deposits[client_id].calculate_final_amount()
            del self.deposits[client_id]
            return final_amount
        return False
