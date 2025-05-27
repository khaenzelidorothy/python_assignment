class Account:
    def __init__(self,name):
        self.name = name
        self.balance = 0
        self.deposit = []
        self.transaction = []
        self.withdrawal = []
        self.new_account =[]
        self.min_balance = 50
        self.loan = 0

# Depodesit: method to deposit funds, store the deposit and return a message with the new balance to the customer. It should only accept positive amounts.
    def depositing(self,amount):
        if amount <=0:
            return "cannot be deposited"
        if amount > 0:
            self.deposit.append(amount)
        for i in self.deposit:
            self.balance += i
        return f"Confirmed you have received {amount}, new balance is {self.balance}"

# Withdraw: method to withdraw funds, store the withdrawal and return a message with the new balance to the customer. An account cannot be overdrawn.
    def withdrawals(self,withdraw_amount):
        if withdraw_amount <= 0:
            return "Put a reasonable amount"
        if self.balance < withdraw_amount:
            return"The amount you have is not enough"
        if self.balance >= withdraw_amount:
            self.withdrawal.append(withdraw_amount)
            self.balance -= withdraw_amount
            self.transaction.append(f"You have withdrawn {withdraw_amount}")
            return f"Your new balance is {self.balance}"

# Get Balance: Method to calculate an account balance from deposits and withdrawals.
    def get_balance(self):
        total = 0
        for i in self.deposit:
            total+= i 
        sum = 0
        for i in self.withdrawal:
            sum += i
        self.balance = total - sum
        return f"Dear {self.name}, your balance is {self.balance}"


# Transfer Funds: Method to transfer funds from one account to an instance of another account.
    def transfer_funds(self,transfer_amount):
        if transfer_amount<=0:
            return "The amount cannot be transferred"
        if transfer_amount < self.balance:
            self.new_account.append(transfer_amount)
            self.balance -= transfer_amount
            self.transaction.append(f"You have transferred {transfer_amount}")
        return f"Dear {self.name} the amount you've transferred is {transfer_amount} and your balance is {self.balance}"

# Request Loan: Method to request a loan amount.

    def request_loan(self,loan_amount):
        loan_limit = 2000
        if loan_amount > loan_limit:
            return f"Amount cannot be loaned"
        else:
            self.loan += loan_amount
            self.balance += loan_amount
        return f"Your loan is {self.loan}"

# Repay Loan: Method to repay a loan with a given amount.
    def repay_loan(self,repay_amount):
        if repay_amount > 0:
            self.loan -= repay_amount
            self.balance -= repay_amount
        return f"Dear {self.name} you have repaid {repay_amount} and your loan debt is {self.loan}"

# View Account Details: Method to display the account owner's details and current balance.
    def account_details(self):
        return f"{self.name} your account balance is {self.balance} and your loan is {self.loan}"

# Change Account Owner: Method to update the account owner's name.
    def change_details(self,newOwner):
        self.name = newOwner
        return f"The new owner of the account is {self.name}"
# Account Statement: Method to generate a statement of all transactions in an account. (Print using a for loop).
    def transaction_history(self):
        print("Transaction history")
        for i in self.deposit:
            print(f"Deposit:{i}")
        for withdraw in self.withdrawal:
            print(f"Withdrawal:{withdraw}")

# Interest Calculation: Method to calculate and apply an interest to the balance. Use 5% interest. 
    def calc_interest(self):
        interest_calc = self.balance*0.05
        self.balance += interest_calc
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