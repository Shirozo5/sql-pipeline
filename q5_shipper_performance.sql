-- Shipper Usage and average delivery time

SELECT s.CompanyName AS Shipper,
       COUNT(o.OrderID) AS 'Orders Shipped',
       ROUND(AVG(julianday(o.ShippedDate) - julianday(o.OrderDate)), 1) AS Avg_Delivery_Days
FROM Orders o
JOIN Shippers s ON o.ShipperID = s.ShipperID
WHERE o.ShippedDate IS NOT NULL
GROUP BY s.CompanyName
ORDER BY 'Orders Shipped' DESC;