--Best selling products by revenue and quantity sold
SELECT c.CategoryName AS 'Category Name',
       p.ProductName AS 'Product Name',
       SUM(od.Quantity) AS 'Quantity Sold',
       ROUND(SUM(od.UnitPrice * od.Quantity * (1 - od.Discount)), 2) AS Revenue
FROM Products p
JOIN Categories c ON p.CategoryID = c.CategoryID
JOIN OrderDetails od ON p.ProductID = od.ProductID
GROUP BY c.CategoryName, p.ProductName
ORDER BY Revenue DESC
LIMIT 15;