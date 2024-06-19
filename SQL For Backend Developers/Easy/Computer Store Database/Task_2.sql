/*
Task 2:

Objectives:
    - Obtain a list of manufacturers (maker) that produce laptops with a hard disk (hd) space of at least 1000 GB, along with the speed (speed), the price (price), and the model (model) of those laptops;
    - Find the maker and model of the laptop from the table Product, and the hd, speed, and price from the table Laptop. Order output first by hd, then by descending order speed, and then by price.
*/

SELECT
  Product.maker,
  Product.model,
  Laptop.hd,
  Laptop.speed,
  Laptop.price
FROM
  Product
INNER JOIN
  Laptop
  ON Product.model = Laptop.model
WHERE
  Laptop.hd >= 1000
ORDER BY
  Laptop.hd,
  Laptop.speed DESC,
  Laptop.price;
