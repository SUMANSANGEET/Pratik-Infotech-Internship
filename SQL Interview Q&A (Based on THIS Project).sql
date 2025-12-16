-- SQL Interview Q&A (Based on THIS Project)
-- Q1️⃣ How did you calculate engagement rate?
SELECT 
  (likes + comments + shares) * 100.0 / reach AS engagement_rate
FROM social_media;

-- Q2️⃣ Which platform has highest engagement?
SELECT platform,
AVG((likes+comments+shares)*100.0/reach) AS avg_engagement
FROM social_media
GROUP BY platform
ORDER BY avg_engagement DESC;

-- Q3️⃣ How do you find top-performing posts?
SELECT *
FROM social_media
ORDER BY (likes+comments+shares)*100.0/reach DESC
LIMIT 10;
