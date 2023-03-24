select MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') AS DATE_OF_BIRTH
from MEMBER_PROFILE
where MONTH(date_of_birth) = 3
    and gender = 'W'
    and tlno is not null
order by member_id asc;