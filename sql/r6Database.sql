CREATE DATABASE R6Marketplace;
USE R6Marketplace;

CREATE TABLE items
(
	item_id varchar(255) NOT NULL,
    item_name varchar(255) NOT NULL,
    item_type varchar(255) NOT NULL,
    item_pic_url TEXT NOT NULL,
	PRIMARY KEY (item_id)
);

CREATE TABLE prices
(
	item_id varchar(255) NOT NULL,
	sale_id INT AUTO_INCREMENT PRIMARY KEY,
    sold_at DATETIME NOT NULL,
    price INT NOT NULL,
    UNIQUE (item_id, sold_at)
);
