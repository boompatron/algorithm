select member_id, member_name, gender, date_format(date_of_birth, '%Y-%m-%d')
from member_profile
where month(date_of_birth) = '3' and gender = 'W' and tlno is not null














# SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') as DATE_OF_BIRTH
# FROM MEMBER_PROFILE
# WHERE MONTH(DATE_OF_BIRTH) = 3
#     and GENDER = 'W'
#     and TLNO is not null
# ORDER BY MEMBER_ID