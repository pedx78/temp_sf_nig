
from odo import odo, resource, discover

# csv = resource('customer_type.csv')
csv = resource('transactions.csv')

# discover(csv)
print(discover(csv))


"""
var * {
  customer_index: int64,
  customer_no: int64,
  mobile: int64,
  identity_type: ?string,
  customer_age: int64,
  gender: ?string,
  account_no: int64,
  account_age_in_days: float64,
  account_age_in_seconds: int64,
  regis_year: int64,
  regis_month: ?string,
  regis_weekday: ?string,
  tot_bal_duration: int64,
  max_bal_duration: int64,
  min_bal_duration: int64,
  avg_bal_duration: int64,
  total_weighted_bal: int64,
  avg_weighted_bal: int64,
  tot_num_deposit: int64,
  total_deposit_amt: int64,
  max_deposit_amt: int64,
  min_deposit_amt: int64,
  avg_deposit_amt: int64,
  tot_num_withdrawal: int64,
  total_withdrawal_amt: int64,
  min_withdrawal_amt: int64,
  max_withdrawal_amt: int64,
  avg_withdrawal_amt: int64,
  avg_deposit_amount_per_day: float64,
  avg_num_deposit_per_day: float64,
  avg_withdrawal_amount_per_day: int64,
  avg_num_withdrawal_per_day: int64,
  last_deposit_amount: int64,
  last_withdrawal_amount: int64,
  time_since_last_deposit: int64,
  time_since_last_withdrawal: int64,
  balance: int64,
  weighted_bal: int64,
  regis_date: ?string,
  customer_type: ?string
  }


  """

