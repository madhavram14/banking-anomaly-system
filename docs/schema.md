USERS

- user_id → unique id for each user
- home_city → where the user lives
- account_type → savings or checking


ACCOUNTS

- account_id → unique account number
- user_id → which user owns this
- account_type → savings or checking
- balance → money in account
- status → active or inactive


TRANSACTIONS

- txn_id → unique transaction id
- account_id → which account is used
- txn_type → debit or credit
- amount → money value
- timestamp → date and time
- channel → UPI / ATM / POS / NETBANKING
- city → where transaction happened
- device_id → which device used
- status → success or failed


-----------------------------------

NORMAL BEHAVIOR

Savings account:
- small transactions (₹100–₹2000)
- mostly daytime
- same city
- same device

Checking account:
- bigger transactions (₹1000–₹10000)
- more frequent


-----------------------------------

SUSPICIOUS BEHAVIOR

- very high amount
- too many transactions quickly
- transaction at night (2 AM – 5 AM)
- different city
- new device