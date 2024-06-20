SELECT 
    l.id, 
    l.listing_url, 
    l.name, 
    365 - l.availability_365 AS booked_out_365,
    CAST(REPLACE(l.price, '$', '') AS UNSIGNED) AS price_clean,
    CAST(REPLACE(l.price, '$', '') AS UNSIGNED) * (365 - l.availability_365) AS proj_rev_365
FROM 
    listings l
WHERE 
    l.availability_365 < 365 
ORDER BY 
    proj_rev_365 DESC 
LIMIT 20;
