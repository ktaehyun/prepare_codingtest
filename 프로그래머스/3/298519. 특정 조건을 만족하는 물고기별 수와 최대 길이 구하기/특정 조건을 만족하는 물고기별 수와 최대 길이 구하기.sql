SELECT COUNT(FISH_TYPE) FISH_COUNT, MAX(LENGTH) MAX_LENGTH, FISH_TYPE
FROM (SELECT (CASE
              WHEN LENGTH IS NULL THEN 10
              ELSE LENGTH END) LENGTH, FISH_TYPE
      FROM FISH_INFO) FISH
GROUP BY FISH_TYPE
HAVING AVG(LENGTH) >= 33
ORDER BY FISH_TYPE