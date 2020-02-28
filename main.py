# coding: utf-8
import tushare as ts
import matplotlib.pyplot as plt
import matplotlib.dates as dat
import numpy
import math
# to remove warn
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

TOKEN = 'dbe457b7700aee993af8075d00ffedf4ea4471024eb556f2153d92d5'

# 股指代码
STOCK_LIST = [
    # 主要股指
    "sh",  # 上证综指
    "sz",  # 深证成指
    # "zxb",  # 中小板指
    # "cyb",  # 创业板指
    # 细分指数
    # "sz50",  # 上证50
    "hs300",  # 沪深300
    "000905",  # 中证500
]
START_DATE = "2019-01-01"


def main():
    print("tushare version:%s" % ts.__version__)
    ts.set_token(TOKEN)
    pro = ts.pro_api()
    col = 2
    row = math.ceil(len(STOCK_LIST) / float(col))
    for i, stock in enumerate(STOCK_LIST):
        df = ts.get_hist_data(stock, start=START_DATE)
        df.sort_index()
        xs = []
        for d in df.index:
            trans_date = dat.strpdate2num("%Y-%m-%d")(d)
            xs.append(trans_date)
        average = numpy.mean(df["close"])
        plt.subplot(row, col, i + 1)
        plt.title(stock)
        plt.plot_date(xs, df["close"], "r-")
        plt.axhline(y=average, color="b")

    plt.gcf().autofmt_xdate()
    plt.show()


if __name__ == '__main__':
    main()
