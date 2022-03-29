
from datetime import datetime

''' //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
               ----- Parent class :  BankAccount -------
                     • Private attributes: balance 
                     • Methods: depositAmt(), withdrawAmt(), getBalance 
                     
////////////////////////////////////////////////////////////////////////////////////////////////////////////////// '''
class BankAccount:
    # constructor
    def __init__(self):
        self.__balance = 0.0

    def depositAmt(self,amount:float):
        assert amount >0, "The amount to be deposited must be greater than 0"
        self.__balance += amount

    def withdrawAmt(self,amount:float):
        assert amount > 0, "The amount to be withdrawn must be greater than 0"
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print(f'You don\'t have sufficient balance in your account')

    # getter method to get balance
    def getBalance(self):
        return self.__balance

''' //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
               ----- Sub class:  ChequingAccount -------
                     • provides 3 free transactions per month
                     • additional transactions are charged a small fee ($2.00).
                     • any balance does not provide interest
////////////////////////////////////////////////////////////////////////////////////////////////////////////////// '''
class ChequingAccount(BankAccount):
    # Constants values -------
    transactions_limit = 3
    additional_transaction_fee = 2.0

    # Constructor
    def __init__(self):
        # call super class
        super().__init__()
        self.__transactionCnt = 0

    ''' //////////////////////////////////////////////////////////////////////////////////////////////////////////////
           -- overrides  depositAmt() method to add service if applicable 
           -- If service fee applies to a transaction, the fees amount will be reduced from the balance immediately
           -- service charge is applied to the account by calling withdrawAmt() in super class 
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////// '''
    def depositAmt(self,amount:float):
        super().depositAmt(amount)
        self.__transactionCnt += 1
        if self.__transactionCnt > ChequingAccount.transactions_limit:
            super().withdrawAmt(ChequingAccount.additional_transaction_fee)  # service fees (if applicable)

    ''' //////////////////////////////////////////////////////////////////////////////////////////////////////////////
       -- overrides  withdrawAmt() method to add service if applicable
       -- If service fee applies to a transaction, the fees amount will be reduced from the balance immediately
       -- service charge is applied to the account by calling withdrawAmt() in super class 
    /////////////////////////////////////////////////////////////////////////////////////////////////////////////// '''
    def withdrawAmt(self, amount):
        super().withdrawAmt(amount)
        self.__transactionCnt += 1
        if self.__transactionCnt > ChequingAccount.transactions_limit:
            super().withdrawAmt(ChequingAccount.additional_transaction_fee)  # service fees (if applicable )

    ''' //////////////////////////////////////////////////////////////////////////////////////////////////////////////
          -- chargeFees() calculates total service was charged in the account in a certain period 
          -- total service charge : serviceCharge should not be applied to the account again since service fees
          -- are applied to the account on transaction basis 
    /////////////////////////////////////////////////////////////////////////////////////////////////////////////// '''
    def chargeFees(self):
        if self.__transactionCnt > ChequingAccount.transactions_limit:
            return  (self.__transactionCnt -3) * ChequingAccount.additional_transaction_fee
        else:
            return 0.0


''' //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
               ----- Sub class:  SavingsAccount: -------
               • earns interest (3%) on a monthly basis
////////////////////////////////////////////////////////////////////////////////////////////////////////////////// '''

class SavingsAccount(BankAccount):
    ''' //////////////////////////////////////////////////////////////////////////////////////////////////////////////
                       ----- Constructor ------
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////// '''
    def __init__(self):
        super().__init__()
        self.__interestRate = 3

    ''' //////////////////////////////////////////////////////////////////////////////////////////////////////////////
                       ----- setter method to change interest rate ------
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////// '''
    def  changeInterest(self, new_interestRate):
        self.__interestRate = new_interestRate

    ''' //////////////////////////////////////////////////////////////////////////////////////////////////////////////
                           ----- calculate interest
                           --- deposit that interest amount to the account 
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////// '''
    def addInterest(self):
        interestAmt = (super().getBalance() * self.__interestRate) / 100
        super().depositAmt(interestAmt)

''' //////////////////////////////////////////////////////////////////////////////////////////////////////////////
                           ----- The End ------ 
////////////////////////////////////////////////////////////////////////////////////////////////////////////// '''


