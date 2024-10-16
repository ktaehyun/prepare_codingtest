SELECT COUNT(FISH_TYPE) AS FISH_COUNT, MAX(LENGTH) AS MAX_LENGTH, FISH_TYPE
FROM (SELECT
     (CASE WHEN LENGTH IS NULL THEN 10
      ELSE LENGTH END) AS LENGTH, FISH_TYPE
      FROM FISH_INFO) AS FISH
GROUP BY FISH_TYPE
HAVING AVG(LENGTH) >= 33
ORDER BY FISH_TYPE;