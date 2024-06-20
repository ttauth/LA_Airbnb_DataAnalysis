select id, listing_url, name, 30 - availability_30 AS booked_out_30,
CAST(replace(Price,'$','') as unsigned) as price_clean,
CAST(replace(Price,'$','') as unsigned)*(30 - availability_30) as proj_rev_30
FROM listings ORDER By proj_rev_30 DESC LIMIT 20;
