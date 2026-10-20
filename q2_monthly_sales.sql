-- Monthly Sales Trends.

SELECT strftime('%Y-%m', o.OrderDate) AS Month,
       CONCAT('$', ROUND(SUM(od.UnitPrice * od.Quantity * (1 - od.Discount)), 2)) AS Revenue
FROM Orders o
JOIN OrderDetails od ON o.OrderID = od.OrderID
GROUP BY Month
ORDER BY Month;
