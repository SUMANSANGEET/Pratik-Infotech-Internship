SELECT platform, AVG((likes+comments+shares)/reach)*100 AS engagement_rate
FROM social_media
GROUP BY platform;

SELECT post_type, AVG((likes+comments+shares)/reach)*100 AS engagement_rate
FROM social_media
GROUP BY post_type;