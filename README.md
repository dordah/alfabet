# high-level overview of the flow:

1. The customer requests a perform_advance function with their destination bank account and the requested amount.
2. The system credits the customer's account with the requested amount and creates a new Account instance.
3. The Account instance keeps track of the outstanding balance and the repayment plan.
   Every week, the system debits the customer's account with the amount/12 and updates the repayment plan accordingly (array of 12 equal payments).
   If a debit transaction is successful, the Account class will reduce the remaining amount and pop out the payment from the repayment_plan.
   If a debit transaction fails, the Account class will do nothing (the rest of the flow will try to recharge the amount again one week after. This way, the debit transaction will be postponed to a week after the last payment, since all the amount are equal).
   The customer can check the status of their account at any time by downloading a report using the download_report function from the processor.

The BillingSystem class encapsulates the logic for perform_advance, perform_debits and update_report. It keeps track of all customer accounts using a dictionary, where the keys are the transaction IDs and the values are Account instances.

To run the system, we need to schedule the perform_debits function to run once a week. This can be done using a scheduler library like schedule.

This code will schedule the perform_debits function to run once a week. The while loop at the end will keep the program running indefinitely, allowing the scheduler to run the perform_debits function on a weekly basis.
