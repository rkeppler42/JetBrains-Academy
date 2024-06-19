/*
Task 1:

Objectives:
    - Identify printers in your inventory that are priced over $200;
    - Find the model number, type, and price of the Printer. The order of the columns matters.
*/

SELECT
    model,
    type,
    price
FROM
    Printer
WHERE
    price > 200;
