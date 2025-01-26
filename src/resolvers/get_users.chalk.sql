-- resolves: User
-- source: sqlite
select 
  id,
  last_name,
  first_name,
  stock,
  num_shares,
  purchase_price,
  total_investment,
  desired_roi
from
  user_stocks;
