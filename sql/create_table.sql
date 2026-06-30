DROP TABLE IF EXISTS customer_shopping;

CREATE TABLE customer_shopping (
    customer_id INT,
    age INT,
    gender VARCHAR(20),
    category VARCHAR(100),
    purchase_amount_usd DECIMAL(10,2),
    payment_method VARCHAR(50),
    location VARCHAR(100),
    review_rating DECIMAL(3,1)
);