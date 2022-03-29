# OOP-Python: Class, Object, Inheritance 

# Problem Statment: This is an assignment problem for CP1890 of Winter 2022 at CNA
   
<p>We have been tasked with creating a program to run an ATM. In this iteration of development, 
we are only concerned with creating the following functionality related to bank accounts:
Specifically, we will have two types of accounts:
<ol> 
  <li>Chequing account: 
    <ul> 
        <li> provides 3 free transactions per month  </li>
        <li> additional transactions are charged a small fee ($2.00). </li> 
        <li> any balance does not provide interest </li> 
     </ul> 
  </li> 
    
  <li>Savings account:
    <ul>         
        <li> earns interest (3%) on a monthly basis (note: we do not need to worry about 
timing here, we will just create an ability for the program to add interest)  </li>        
     </ul>   
  </li> 
</ol>   

Both types of accounts share some common functionality:
<ul> 
    <li> Should contain an attribute balance </li>
    <li> Should have a constructor that creates a new bank account with a zero balance. </li>
    <li> Contains a depositAmt method that accepts an amount to be deposited in the account </li>
    <li> Contains a withdrawAmt method that accepts an amount to withdraw from the account </li>
    <li> Contains a getBalance method that returns the current balance in the account. </li>

</ul>   

</p>

In addition: 
<p> 
ChequingAccount:

<ul> 
    <li> Should contain a attribute transactionCnt (to keep track of transactions) </li>
    <li> Should override the depositAmt and withdrawAmt methods in order to increment the 
transaction count. </li>
    <li> Contains a chargeFees method that will charge the transaction fee (if any) to the account 
for any transactions beyond the free transactions (assume that transfers or balance checks 
are free) </li>

</ul>   

SavingsAccount:
<ul> 
<li> Should contain an attribute interestRate that holds the interest rate defined. (note that 
3% is equivalent to 0.03) </li>
<li> Contains a changeInterest method that can be used to adjust the interest rate. </li>
<li> Contains an addInterest method that adds the interest, as specified, to the account 
balance. To calculate the interest for the amount in the account you can use this formula: 
interestAmt = balance * interestRate / 100.00 </li>
</ul>
</p> 
