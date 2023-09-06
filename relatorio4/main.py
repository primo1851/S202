from ProductAnalyzer import ProductAnalyzer
from database import Database
from writeAJson import writeAJson
import dataset

sales_data = [dataset]

analyzer = ProductAnalyzer()

analyzer.bestSeller()
analyzer.bestConsumer()
analyzer.inStock()
analyzer.totalSales()
