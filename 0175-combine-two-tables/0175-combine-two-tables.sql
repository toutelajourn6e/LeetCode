select P.firstname, P.lastname, A.city, A.state
from Person P
    left join Address A on P.personid = A.personid
