from datetime import datetime
class Transaction:
    def __init__(self,narration,amount,transaction_type):
        self.date_time = datetime.now()
        self.narration = narration
        self.amount = amount
        self.transaction_type = transaction_type

    def __str__(self):
        return f"{self.date_time} | {self.transaction_type} | {self.amount}"
class Account:
    def __init__(self,owner,account_number):
        self.__owner = owner
        self.__account_number = account_number
        self.__transaction = []
        self.__balance = 0
        self.__min_balance = 50
        self.__loan = 0
        self.__is_frozen = False

# Deposit: method to deposit funds, store the deposit and return a message with the new balance to the customer. It should only accept positive amounts.
    def depositing(self,amount):
        if amount <=0:
            return "cannot be deposited"
        if amount > 0:
            self.__transaction.append(Transaction("Deposit",amount,"CREDIT"))
            self.__balance+=amount
        return f"Confirmed you have received {amount}, new balance is {self.get_balance()}"

# Withdraw: method to withdraw funds, store the withdrawal and return a message with the new balance to the customer. An account cannot be overdrawn.
    def withdrawals(self,amount):
        if amount <= 0:
            return "Put a reasonable amount"
        if amount < self.__min_balance:
            return"The amount you have is not enough"
            self.__transaction.append(Transaction("Withdrawal",-amount,"DEBIT"))
            return f"Your new balance is {self.get_balance()}"

# Get Balance: Method to calculate an account balance from deposits and withdrawals.
    def get_balance(self):
            return sum(t.amount for t in self.__transaction)


# Transfer Funds: Method to transfer funds from one account to an instance of another account.
    def transfer_funds(self,amount,transfer_account):
        if amount<=0:
            return "The amount cannot be transferred"
        if self.get_balance() - amount < self.__min_balance:
            return "Insufficient amount"
            self.__transaction.append(Transaction(f"You have transferred {transfer_account.account_number}",-amount,"DEBIT"))
            self.__balance-=amount
        return f"Dear {self.__owner} the amount you've transferred is {amount} and your balance is {self.get_balance()}"

# Request Loan: Method to request a loan amount.

    def request_loan(self,amount):
        loan_limit = 2000
        if loan_amount > loan_limit:
            return f"Amount cannot be loaned"
        else:
            self.__loan += amount
            self.__transaction.append(Transaction("Loan granted",amount,"CREDIT"))
            self.__balance+=amount
        return f"Your loan is {self.__loan}"

# Repay Loan: Method to repay a loan with a given amount.
    def repay_loan(self,amount):
        if repay_amount > 0:
            self.__loan -= amount
            self.__transaction.append(Transaction("Loan repayment", -amount,"DEBIT"))
        return f"Dear {self.name} you have repaid {amount} and your loan debt is {self.__loan}"

# View Account Details: Method to display the account owner's details and current balance.
    def account_details(self):
        return f"{self.__owner} your account balance is {self.get_balance()} and your loan is {self.loan}"

# Change Account Owner: Method to update the account owner's name.
    def change_details(self,newOwner):
        self.__owner = newOwner
        return f"The new owner of the account is {self.name}"
# Account Statement: Method to generate a statement of all transactions in an account. (Print using a for loop).
    def transaction_history(self):
        for t in self.__transaction:
            print(t)

# Interest Calculation: Method to calculate and apply an interest to the balance. Use 5% interest. 
    def calc_interest(self):
        interest_calc = self.get_balance()*0.05
        self.__transaction.append(Transaction("Interest applied", interest, "CREDIT"))
        return f"Interest applied is {interest_calc}"

# Freeze/Unfreeze Account: Methods to freeze and unfreeze the account for security reasons.
    def freeze_account(self):
        self.frozen = True
        return f"Your account has been closed due to security reasons"

    def unfreeze_account(self):
        self.frozen = False
        return f"Your account has been unfrozen"


# Close Account: Method to close the account and set all balances to zero and empty all transactions
    def close_account(self):
        self.balance = 0
        self.deposit.clear()
        self.transaction.clear()
        self.withdrawal.clear()
        self.new_account.clear()
        self.min_balance = 0
        self.loan = 0


        