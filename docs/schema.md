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
- user_tier → [Silver, Gold, Platinum]
- currency → [INR, USD, EUR, MXN]
- amount_local → amount in original currency
- fx_rate → conversion rate to INR
- amount_inr → total value in INR (local * rate)
- fee_charged → calculated based on Tier
- city → location of transaction
- timestamp → date and time

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