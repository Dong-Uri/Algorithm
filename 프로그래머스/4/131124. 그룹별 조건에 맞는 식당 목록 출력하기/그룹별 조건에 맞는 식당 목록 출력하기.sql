-- 코드를 입력하세요
SELECT P.MEMBER_NAME, R.REVIEW_TEXT, date_format(R.REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM MEMBER_PROFILE P JOIN REST_REVIEW R ON (P.MEMBER_ID = R.MEMBER_ID)
WHERE P.MEMBER_ID IN    (SELECT MEMBER_ID FROM REST_REVIEW
                        GROUP BY MEMBER_ID
                        HAVING count(*) =   (SELECT count(*)
                                            FROM REST_REVIEW
                                            GROUP BY MEMBER_ID
                                            ORDER BY count(*) desc limit 1))
ORDER BY R.REVIEW_DATE, R.REVIEW_TEXT