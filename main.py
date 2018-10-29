import datetime
import tushare as ts

TOKEN = 'dbe457b7700aee993af8075d00ffedf4ea4471024eb556f2153d92d5'
STOCK_POOL = ['002174.SZ', '002517.SZ', '002555.SZ', '002624.SZ']


def main():
	print(ts.__version__)
	ts.set_token(TOKEN)
	pro = ts.pro_api()

	stocks = pro.stock_basic(exchange_id='', is_hs='', fields='symbol,name,list_date,list_status')
	print stocks

	now = datetime.datetime.now()
	start_dt = now - datetime.timedelta(days=91)
	start_dt = start_dt.strftime('%Y%m%d')
	end_dt = now - datetime.timedelta(days=1)
	end_dt = end_dt.strftime('%Y%m%d')
	print('from ' + start_dt + ' to ' + end_dt)

	total = len(STOCK_POOL)
	for i in range(len(STOCK_POOL)):
		try:
			df = pro.daily(ts_code=STOCK_POOL[i], start_date=start_dt, end_date=end_dt)
			print('The stock: (' + str(i + 1) + ' / ' + str(total) + ') Code: ' + str(STOCK_POOL[i]))
			print(df)
		except Exception as e:
			print(STOCK_POOL[i] + ': ' + str(e))
			continue
	print('All Finished!')


if __name__ == '__main__':
	main()
