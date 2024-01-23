-- 코드를 입력하세요
SELECT B.TITLE, B.BOARD_ID, R.REPLY_ID, R.WRITER_ID, R.CONTENTS, date_format(R.CREATED_DATE, '%Y-%m-%d') AS CREATED_DATE
FROM USED_GOODS_REPLY R JOIN USED_GOODS_BOARD B ON (R.BOARD_ID = B.BOARD_ID)
WHERE date_format(B.CREATED_DATE, '%Y-%m-%d') BETWEEN '2022-10-01' AND '2022-10-31'
ORDER BY date_format(R.CREATED_DATE, '%Y-%m-%d'), B.TITLE