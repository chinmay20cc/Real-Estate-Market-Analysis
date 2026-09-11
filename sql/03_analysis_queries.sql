USE real_estate;

-- 1. Average, minimum and maximum property price
SELECT
    AVG(price) AS average_price,
    MIN(price) AS minimum_price,
    MAX(price) AS maximum_price
FROM properties;


-- 2. Top 10 most expensive properties
SELECT
    property_id,
    city,
    property_type,
    area_sqft,
    bedrooms,
    price
FROM properties
ORDER BY price DESC
LIMIT 10;


-- 3. Number of properties by city
SELECT
    city,
    COUNT(*) AS property_count
FROM properties
GROUP BY city
ORDER BY property_count DESC;


-- 4. Property type distribution
SELECT
    property_type,
    COUNT(*) AS property_count
FROM properties
GROUP BY property_type
ORDER BY property_count DESC;


-- 5. Average area by property type
SELECT
    property_type,
    AVG(area_sqft) AS average_area_sqft
FROM properties
GROUP BY property_type
ORDER BY average_area_sqft DESC;


-- 6. Top 10 properties by price per square foot
SELECT
    property_id,
    city,
    property_type,
    area_sqft,
    price,
    price_per_sqft
FROM properties
ORDER BY price_per_sqft DESC
LIMIT 10;


-- 7. Average price by city
SELECT
    city,
    COUNT(*) AS property_count,
    AVG(price) AS average_price
FROM properties
GROUP BY city
ORDER BY average_price DESC;


-- 8. City ranking by average price
SELECT
    city,
    AVG(price) AS average_price,
    RANK() OVER (ORDER BY AVG(price) DESC) AS price_rank
FROM properties
GROUP BY city
ORDER BY price_rank;


-- 9. Bedroom count and average price
SELECT
    bedrooms,
    COUNT(*) AS property_count,
    AVG(price) AS average_price
FROM properties
GROUP BY bedrooms
ORDER BY bedrooms;


-- 10. Average price by build year
SELECT
    build_year,
    COUNT(*) AS property_count,
    AVG(price) AS average_price
FROM properties
GROUP BY build_year
ORDER BY build_year;


-- 11. Luxury property analysis
SELECT
    COUNT(*) AS luxury_properties,
    AVG(price) AS average_luxury_price,
    MAX(price) AS highest_luxury_price
FROM properties
WHERE is_luxury = 'True';


-- 12. Luxury properties by city
SELECT
    city,
    COUNT(*) AS luxury_count,
    AVG(price) AS average_luxury_price
FROM properties
WHERE is_luxury = 'True'
GROUP BY city
ORDER BY luxury_count DESC;


-- 13. Average price per square foot by property type
SELECT
    property_type,
    AVG(price_per_sqft) AS average_price_per_sqft
FROM properties
GROUP BY property_type
ORDER BY average_price_per_sqft DESC;


-- 14. Furnishing impact on price
SELECT
    furnishing,
    COUNT(*) AS property_count,
    AVG(price) AS average_price
FROM properties
GROUP BY furnishing
ORDER BY average_price DESC;


-- 15. Pool impact on price
SELECT
    has_pool,
    COUNT(*) AS property_count,
    AVG(price) AS average_price
FROM properties
GROUP BY has_pool
ORDER BY average_price DESC;