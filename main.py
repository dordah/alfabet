from processor import Processor  # MOCK
from billing_system import BillingSystem
import schedule
import time

processor = Processor()

billing_system = BillingSystem(processor)


def perform_advance(dst_bank_account, amount):
    """
    Performs an advance payment on a bank account through the billing system and prints the transaction ID.

    Args:
    dst_bank_account (str): The destination bank account to make the payment to.
    amount (float): The amount to be paid.
    """
    transaction_id = billing_system.perform_advance(dst_bank_account, amount)

    print(f"Transaction ID: {transaction_id}")


schedule.every().week.do(billing_system.perform_debits)

# Tests
# perform_advance('account_1', 1000000)
# perform_advance('account_2', 2000000)

# Schedule the perform_debits function to run once a week
while True:
    schedule.run_pending()
    time.sleep(1)
