# 상위% 구하기
SELECT ID,
       (CASE
        WHEN CEIL(PERCENT_RANK() OVER (ORDER BY SIZE_OF_COLONY DESC)*100) <= 25 THEN 'CRITICAL'
        WHEN CEIL(PERCENT_RANK() OVER (ORDER BY SIZE_OF_COLONY DESC)*100) <= 50 THEN 'HIGH'
        WHEN CEIL(PERCENT_RANK() OVER (ORDER BY SIZE_OF_COLONY DESC)*100) <= 75 THEN 'MEDIUM'
        ELSE 'LOW' END) AS COLONY_NAME
FROM ECOLI_DATA
ORDER BY ID

# 반올림 ROUND
# 올림 CEIL
# 내림 FLOOR
# 값의% = (SIZE_OF_COLONY / (SELECT SUM(SIZE_OF_COLONY) FROM ECOLI_DATA))*100