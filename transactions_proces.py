from odo import odo, dshape

sh = """
var * {
  transaction_index: int64,
  transaction_id: ?string,
  transaction_type: ?string,
  status: ?string,
  payer_name: ?string,
  account_no: ?string,
  currency: ?string,
  amount: float64,
  date: ?datetime,
  customer_no: ?string,
  mtn_transaction_no: ?string,
  fbl_transaction_no: ?string
  }
  """

ds = dshape(sh)


odo('transactions3.csv', 'postgresql://pry:pass@localhost/sfl_demo_nigeria::transactions', dshape=ds)  # Load CSVs to Postgres






