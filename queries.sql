-- 1. SELECT / WHERE: All in-stock books with rating >= 4
SELECT title, price_inr, rating FROM books WHERE in_stock = 1 AND rating >= 4;

-- 2. ORDER BY / LIMIT: Top 5 most expensive books in INR
SELECT title, price_inr FROM books ORDER BY price_inr DESC LIMIT 5;

-- 3. DISTINCT: All distinct star ratings in stock
SELECT DISTINCT rating FROM books WHERE in_stock = 1;

-- 4. BETWEEN / IN: Books priced between 2000 and 4000 INR with ratings 3 or 5
SELECT title, price_inr, rating FROM books WHERE (price_inr BETWEEN 2000.0 AND 4000.0) AND rating IN (3, 5);

-- 5. JOIN: List books with their category name
SELECT b.title, c.category_name, b.price_inr, b.rating 
FROM books b 
JOIN categories c ON b.category_id = c.category_id 
ORDER BY c.category_name, b.price_inr DESC;
