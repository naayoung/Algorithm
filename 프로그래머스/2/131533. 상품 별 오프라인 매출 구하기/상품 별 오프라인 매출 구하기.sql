-- 코드를 입력하세요
SELECT PR.PRODUCT_CODE, SUM(PR.PRICE * OFFSALE.SALES_AMOUNT) AS SALES
FROM PRODUCT PR
    JOIN OFFLINE_SALE OFFSALE
    ON PR.PRODUCT_ID = OFFSALE.PRODUCT_ID
GROUP BY PR.PRODUCT_CODE
ORDER BY SALES DESC, PR.PRODUCT_CODE ASC

