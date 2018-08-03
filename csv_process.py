from odo import odo, dshape

sh = """
var * {
  cust_id: int64,
  customer_no: ?string,
  mobile: ?string,
  identity_type: ?string,
  customer_age: int64,
  gender: ?string,
  account_no: ?string,
  account_age_in_days: ?string,
  account_age_in_seconds: ?string,
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

ds = dshape(sh)


odo('hist3.csv', 'postgresql://pry:pass@localhost/sfl_fid_nig_demo::historical', dshape=ds)  # Load CSVs to Postgres

# odo('transactions.csv', 'postgresql://pry:pass@localhost/sfl_fid_nig_demo::transactions')  # Load CSVs to Postgres


# export DATABASE_URL='postgres://postgres:west1234@localhost/westcape'
# 'postgres://pry:pp@localhost/flask_demo_auth'



