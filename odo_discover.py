
from odo import odo, resource, discover
# import numpy as np

# x = np.ones((5, 6), dtype='f4')
# print(discover(x))
# dshape("5 * 6 * float32")


# 
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




------------------
historical
-----------------
var * {
  cust_id: int64,
  customer_no: ?string,
  mobile: ?string,
  identity_type: ?string,
  customer_age: int64,
  gender: ?string,
  account_no: ?string,
  account_age_in_days: date,
  account_age_in_seconds: date,
  regis_year: ?string,
  regis_month: ?string,
  regis_weekday: ?string,
  tot_bal_duration: int64,
  max_bal_duration: int64,
  min_bal_duration: int64,
  avg_bal_duration: float64,
  total_weighted_bal: float64,
  avg_weighted_bal: float64,
  tot_num_deposit: int64,
  total_deposit_amt: float64,
  max_deposit_amt: float64,
  min_deposit_amt: float64,
  avg_deposit_amt: float64,
  tot_num_withdrawal: int64,
  total_withdrawal_amt: float64,
  min_withdrawal_amt: float64,
  max_withdrawal_amt: float64,
  avg_withdrawal_amt: float64,
  avg_deposit_amount_per_day: float64,
  avg_num_deposit_per_day: float64,
  avg_withdrawal_amount_per_day: float64,
  avg_num_withdrawal_per_day: float64,
  last_deposit_amount: float64,
  last_withdrawal_amount: float64,
  time_since_last_deposit: int64,
  time_since_last_withdrawal: int64,
  balance: float64,
  weighted_bal: float64
  }
  """

