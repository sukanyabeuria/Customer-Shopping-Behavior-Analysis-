-- ===========================================================
-- CUSTOMER SHOPPING BEHAVIOR ANALYSIS
-- SQL ANALYSIS QUERIES
-- ===========================================================

-- ===========================================================
-- 1. Total Customers
-- ===========================================================

SELECT COUNT(*) AS total_customers
FROM customer_shopping;

-- ===========================================================
-- 2. Total Revenue
-- ===========================================================

SELECT SUM(purchase_amount_usd) AS total_revenue
FROM customer_shopping;

-- ===========================================================
-- 3. Average Purchase Amount
-- ===========================================================

SELECT AVG(purchase_amount_usd) AS average_purchase
FROM customer_shopping;

-- ===========================================================
-- 4. Average Review Rating
-- ===========================================================

SELECT AVG(review_rating) AS average_rating
FROM customer_shopping;

-- ===========================================================
-- 5. Sales by Category
-- ===========================================================

SELECT
    category,
    SUM(purchase_amount_usd) AS total_sales
FROM customer_shopping
GROUP BY category
ORDER BY total_sales DESC;

-- ===========================================================
-- 6. Sales by Gender
-- ===========================================================

SELECT
    gender,
    SUM(purchase_amount_usd) AS total_sales
FROM customer_shopping
GROUP BY gender
ORDER BY total_sales DESC;

-- ===========================================================
-- 7. Sales by Payment Method
-- ===========================================================

SELECT
    payment_method,
    SUM(purchase_amount_usd) AS total_sales
FROM customer_shopping
GROUP BY payment_method
ORDER BY total_sales DESC;

-- ===========================================================
-- 8. Sales by Location
-- ===========================================================

SELECT
    location,
    SUM(purchase_amount_usd) AS total_sales
FROM customer_shopping
GROUP BY location
ORDER BY total_sales DESC;

-- ===========================================================
-- 9. Highest Purchase
-- ===========================================================

SELECT *
FROM customer_shopping
ORDER BY purchase_amount_usd DESC
LIMIT 1;

-- ===========================================================
-- 10. Top 10 Customers
-- ===========================================================

SELECT *
FROM customer_shopping
ORDER BY purchase_amount_usd DESC
LIMIT 10;

-- ===========================================================
-- 11. Lowest Purchase
-- ===========================================================

SELECT *
FROM customer_shopping
ORDER BY purchase_amount_usd ASC
LIMIT 1;

-- ===========================================================
-- 12. Customer Count by Gender
-- ===========================================================

SELECT
    gender,
    COUNT(*) AS total_customers
FROM customer_shopping
GROUP BY gender;

-- ===========================================================
-- 13. Customer Count by Category
-- ===========================================================

SELECT
    category,
    COUNT(*) AS total_customers
FROM customer_shopping
GROUP BY category;

-- ===========================================================
-- 14. Customer Count by Payment Method
-- ===========================================================

SELECT
    payment_method,
    COUNT(*) AS total_transactions
FROM customer_shopping
GROUP BY payment_method;

-- ===========================================================
-- 15. Age Group Analysis
-- ===========================================================

SELECT
CASE
    WHEN age < 25 THEN '18-24'
    WHEN age BETWEEN 25 AND 34 THEN '25-34'
    WHEN age BETWEEN 35 AND 44 THEN '35-44'
    WHEN age BETWEEN 45 AND 54 THEN '45-54'
    ELSE '55+'
END AS age_group,

AVG(purchase_amount_usd) AS average_purchase

FROM customer_shopping

GROUP BY age_group

ORDER BY average_purchase DESC;

-- ===========================================================
-- 16. Window Function (Ranking)
-- ===========================================================

SELECT
    customer_id,
    category,
    purchase_amount_usd,

RANK() OVER(
ORDER BY purchase_amount_usd DESC
) AS purchase_rank

FROM customer_shopping;

-- ===========================================================
-- 17. Dense Rank
-- ===========================================================

SELECT
    customer_id,
    category,
    purchase_amount_usd,

DENSE_RANK() OVER(
ORDER BY purchase_amount_usd DESC
) AS dense_rank

FROM customer_shopping;

-- ===========================================================
-- 18. Row Number
-- ===========================================================

SELECT
    customer_id,
    category,

ROW_NUMBER() OVER(
ORDER BY purchase_amount_usd DESC
) AS row_number

FROM customer_shopping;

-- ===========================================================
-- 19. Common Table Expression (CTE)
-- ===========================================================

WITH category_sales AS
(
SELECT

category,

SUM(purchase_amount_usd) AS total_sales

FROM customer_shopping

GROUP BY category
)

SELECT *

FROM category_sales

ORDER BY total_sales DESC;

-- ===========================================================
-- 20. Highest Spending Location
-- ===========================================================

SELECT
location,

SUM(purchase_amount_usd) AS total_sales

FROM customer_shopping

GROUP BY location

ORDER BY total_sales DESC;