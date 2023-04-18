from consts import CREDIT
from account import Account


class BillingSystem:
    """
    Represents a billing system that performs transactions and tracks account balances.

    Attributes:
    processor (Processor): The black box processor.
    accounts (dict): A dictionary mapping transaction IDs to Account objects.

    Methods:
    perform_advance(dst_bank_account, amount): Performs an advance payment on a bank account and creates a new Account object for tracking the outstanding balance (for each credit).
    update_report(): Generates a report of the payment status of all transactions.
    perform_debits(): Performs debit transactions on all unfully paid outstanding balances.
    """

    def _init_(self, processor):
        self.processor = processor
        self.accounts = {}

    def perform_advance(self, dst_bank_account, amount):
        """
        Performs an advance payment on a bank account and creates a new Account object for tracking the outstanding balance.

        Args:
        dst_bank_account (str): The destination bank account to make the payment to.
        amount (float): The amount to be paid.

        Returns:
        str: The ID of the transaction if successful, otherwise an empty string.
        """
        transaction_id = self.processor.perform_transaction(
            '', dst_bank_account, amount, CREDIT)
        if transaction_id is not None and transaction_id != '':
            self.accounts[transaction_id] = Account(dst_bank_account, amount)
        return transaction_id

    def update_report(self):
        """
        Updates the report of the payment status of all outstanding balances.

        Returns:
        str: The payment report, listing the transaction ID and payment status for each outstanding balance.
        """
        report = self.processor.download_report
        for transaction_id, account in self.accounts.items():
            if not account.is_paid_off():
                report += f"{transaction_id}, fail\n"
            else:
                report += f"{transaction_id}, success\n"
        return report

    def perform_debits(self):
        for account in self.accounts.values():
            account.perform_debit(self.processor)
        self.update_report
