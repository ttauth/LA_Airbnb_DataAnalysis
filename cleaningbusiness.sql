select host_id, host_url, host_name, COUNT(*) AS num_dirty_reviews from reviews
inner join listings on reviews.listing_id = listings.id
where comments like "%dirty%"
group by host_id, host_url, host_name order by num_dirty_reviews desc;