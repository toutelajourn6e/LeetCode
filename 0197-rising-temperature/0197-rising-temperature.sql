select W1.id
from Weather W1, Weather W2
where W1.temperature > W2.temperature and W1.recordDate = date_add(W2.recordDate, interval 1 Day)