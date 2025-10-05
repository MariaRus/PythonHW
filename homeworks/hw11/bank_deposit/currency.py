class CurrencyConverter:
    def __init__(self):
        self.exchange_rates = {
            'USD': {'BYN': 3.2677, 'EUR': 0.9518},
            'EUR': {'BYN': 3.399, 'USD': 1.0506},
            'BYN': {'USD': 0.3063, 'EUR': 0.2942},
        }

    def convert(self, from_currency, amount, to_currency='BYN'):
        if from_currency not in self.exchange_rates:
            raise ValueError(f"Unsupported currency: {from_currency}")

        if to_currency not in self.exchange_rates[from_currency]:
            raise ValueError(f"Unsupported currency: {to_currency}")

        converted_amount = amount * self.exchange_rates[from_currency][to_currency]
        return round(converted_amount, 2), to_currency
