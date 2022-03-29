import pytest
from unittest import TestCase
from BankAccount import *


class TestBankAccount(TestCase):
    ''' /////////////////////////////////////////////////////////////////////////////////////////////////////////////
         ------------    Chequing Account:  ------------------
                         Free transaction: 3
	                    Charge for each additional transaction: $2.00
	                    No interest
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    Test case 1:
        	Transaction 1: deposit $5000
        	Transaction 2: withdraw $2000
        	Transaction 3: deposit $1000
    Expected Results:
        balance = $4000.00
        Charge Fees  = 0.00

    ///////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

    def test_case1(self):
        chequing_account = ChequingAccount()
        # transactions
        chequing_account.depositAmt(5000.00)
        chequing_account.withdrawAmt(2000.00)
        chequing_account.depositAmt(1000.00)
        # verify output
        self.assertEqual(chequing_account.getBalance(), 4000.0)
        self.assertEqual(chequing_account.chargeFees(), 0.0)

    ''' /////////////////////////////////////////////////////////////////////////////////////////////////////////////
      Test case 2: 
        	Transaction 1: deposit $5000
        	Transaction 2: withdraw $2000
        	Transaction 3: deposit $1000
        	Transaction 4: deposit $200
        	Transaction 5: deposit $300
        	Transaction 6: withdraw $400
        	Transaction 7: withdraw $ 50

    Expected Results: 
        balance = $4042.0
        Charge Fees  = 8.0
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

    def test_case2(self):
        chequing_account = ChequingAccount()
        # transactions
        chequing_account.depositAmt(5000.00)
        chequing_account.withdrawAmt(2000.00)
        chequing_account.depositAmt(1000.00)
        chequing_account.depositAmt(200.00)
        chequing_account.depositAmt(300.00)
        chequing_account.withdrawAmt(400.00)
        chequing_account.withdrawAmt(50.00)
        # verify output
        self.assertEqual(chequing_account.getBalance(), 4042.0)
        self.assertEqual(chequing_account.chargeFees(), 8.0)

    ''' /////////////////////////////////////////////////////////////////////////////////////////////////////////////
             ------------    Savings Account:  ------------------
                     Interest rate: 0.03
                    No fees for transactions
                    Get interest for the balance amount
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////// '''

    ''' 

    Test case 3:  
        	Interest rate: 3%
        	Transaction 1: deposit $500
        	Transaction 2: withdraw $200
        	Transaction 3: deposit $100
        	Transaction 4: deposit $600
    Expected Results:	    	    
        Balance = $1030.00

           //////////////////////////////////////////////////////////////////////////////////////////////////////////// '''

    def test_case3(self):
        savings_account = SavingsAccount()
        # transactions
        savings_account.depositAmt(500.00)
        savings_account.withdrawAmt(200.00)
        savings_account.depositAmt(100.00)
        savings_account.depositAmt(600.00)

        # add interest to the balance
        savings_account.addInterest()

        # verify output
        self.assertEqual(savings_account.getBalance(), 1030.0)

    '''  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
     Test case 4:  
            	Interest rate: 4%
            	Transaction 1: deposit $3000
            	Transaction 2: withdraw $1000
            	Transaction 3: deposit $2000

        Expected Results:	    	    
            Balance = $4200.00

               ////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

    def test_case4(self):
        savings_account = SavingsAccount()
        # set interest rate to 5%
        savings_account.changeInterest(5)
        # transactions
        savings_account.depositAmt(3000.00)
        savings_account.withdrawAmt(1000.00)
        savings_account.depositAmt(2000.00)

        # add interest to the balance
        savings_account.addInterest()

        # verify output
        self.assertEqual(savings_account.getBalance(), 4200.0)


