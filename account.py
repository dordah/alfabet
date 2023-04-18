from consts import PAYMENT_PERIOD, DEBIT


class Account:
    """
    Represents a bank account that has an outstanding balance and a repayment plan.

    Attributes:
    dst_bank_account (str): The destination bank account that payments will be made to.
    outstanding_balance (float): The current amount owed on the account.
    repayment_plan (list): A list of equal payments that need to be made to pay off the outstanding balance.

    Methods:
    perform_debit(processor): Performs a debit transaction on the account using the provided payment processor.
    is_paid_off(): Checks whether the account has been fully cover the loan.
    """

    def _init_(self, dst_bank_account, amount):
        self.dst_bank_account = dst_bank_account
        self.outstanding_balance = amount
        self.repayment_plan = [amount/PAYMENT_PERIOD]*PAYMENT_PERIOD

    def perform_debit(self, processor):
        """
        Performs a debit transaction on the account using the provided payment processor.

        Args:
        processor (Processor): The payment processor to use for the transaction - black box.
        """
        amount_to_pay = self.repayment_plan[0]
        transaction_id = processor.perform_transaction(
            self.dst_bank_account, amount_to_pay, DEBIT)
        # Assumning successful transaction returns id and failed isn't
        if transaction_id is not None and transaction_id != '':
            self.outstanding_balance -= amount_to_pay
            self.repayment_plan.pop(0)

    def is_paid_off(self):
        return self.outstanding_balance == 0
