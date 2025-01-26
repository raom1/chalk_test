import requests
import ast
from pydantic import BaseModel

#from chalk.feature import before_all
from chalk import online
from chalk.features import features

#rt_stocks: RealTimeStocks = RealTimeStocks(BaseModel):
#	symbol: str
#	key: str

#@before_all
#def initialize():
#	with open('../no_push/finnub_key.txt') as f:
#		key = f.read()
#	rt_stocks.key = key

@features
class User:
	id: int
	last_name: str
	first_name: str
	stock: str
	num_shars: int
	purchase_price: float
	total_investment: float
	desired_roi: float

	profit: float


@online
async def get_user_current_profit(
	symbol: User.symbol,
	shares: User.num_shares,
	investment: User.investment) -> User.profit:
	with open('../no_push/finnhub_key.txt') as f:
        	key = f.read()
	r = requests.get('https://finnhub.io/api/v1/quote', params = {'symbol': symbol, 'token': key}
	curr_price = ast.literal_eval(r.text)['c']
	return (shares * curr_price) - investment
