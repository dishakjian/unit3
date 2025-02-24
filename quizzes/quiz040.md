## Code/SQL Queries
```.sql
SELECT *
FROM transactions
ORDER BY amount DESC
LIMIT 1


SELECT account_id,
       SUM(CASE WHEN transaction_type = 'deposit' THEN amount ELSE -amount END) AS balance
FROM transactions
GROUP BY account_id

SELECT *
FROM customers c
JOIN accounts a ON c.customer_id = a.customer_id
JOIN transactions t ON a.account_id = t.account_id
WHERE t.amount = (SELECT MAX(amount) FROM transactions);

SELECT 'Bancruptcy was of amount: ' || MAX(amount) || ' from customer: ' || c.first_name, c.last_name
FROM transactions t
JOIN accounts a ON t.account_id = a.account_id
JOIN customers c ON a.customer_id = c.customer_id;

SELECT t.transaction_id, t.transaction_type, t.amount, t.date, t.account_id, c.first_name, c.last_name
FROM transactions t
JOIN accounts a ON t.account_id = a.account_id
JOIN customers c ON a.customer_id = c.customer_id
WHERE t.transaction_type = 'withdraw'

SELECT *
FROM transactions
WHERE transaction_type = 'withdraw'
ORDER BY amount DESC
LIMIT 10;
SELECT account_id, COUNT(*) AS num_large_withdrawals
FROM transactions
WHERE transaction_type = 'withdraw' AND amount >= 400
GROUP BY account_id
HAVING COUNT(*) > 1;

SELECT * FROM transactions
SELECT a.account_id, a.balance, c.first_name, c.last_name
FROM accounts a
JOIN customers c ON a.customer_id = c.customer_id
WHERE a.balance < 0

SELECT a.account_id, c.first_name, c.last_name, SUM(t.amount) AS total_withdrawals
FROM transactions t
JOIN accounts a ON t.account_id = a.account_id
JOIN customers c ON a.customer_id = c.customer_id
WHERE t.transaction_type = 'withdraw'
GROUP BY a.account_id, c.first_name, c.last_name
ORDER BY total_withdrawals DESC
LIMIT 1;


```

No accounts were found with negative balances, the largest transactions were deposits, and based on this information, the person with the largest withdrawal of 900 was Jane Doe
![image](https://github.com/user-attachments/assets/1620c585-5109-4d34-a243-7f5b0a1b39e0)


## UML Diagram

![image](https://github.com/user-attachments/assets/d063af15-22a0-4cf6-abb0-7ab1453a0585)

