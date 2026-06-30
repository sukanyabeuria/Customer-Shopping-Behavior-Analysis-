COPY customer_shopping(
    customer_id,
    age,
    gender,
    category,
    purchase_amount_usd,
    payment_method,
    location,
    review_rating
)
FROM 'customer_shopping_behavior.csv'
DELIMITER ','
CSV HEADER;