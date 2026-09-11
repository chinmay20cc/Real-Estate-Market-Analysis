CREATE DATABASE real_estate;


SHOW DATABASES;


USE real_estate;


USE real_estate;

DROP TABLE IF EXISTS properties;

CREATE TABLE properties (
    property_id INT PRIMARY KEY,
    area_sqft DECIMAL(10,2),
    bedrooms INT,
    build_year INT,
    city VARCHAR(50),
    street_type VARCHAR(50),
    furnishing VARCHAR(30),
    property_type VARCHAR(30),
    has_pool VARCHAR(5),
    price DECIMAL(15,2),
    is_price_outlier VARCHAR(5),
    price_per_sqft DECIMAL(10,2),
    property_age INT,
    area_bucket VARCHAR(20),
    is_luxury VARCHAR(5)
);
SHOW TABLES;
DESCRIBE properties;












