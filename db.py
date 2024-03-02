import MySQLdb

class Database:

	host = "localhost"
	user = "root"
	passwd = ""
	db = "firstwms"

	def __init__(self):
		self.connection = MySQLdb.connect( host = self.host,
									user = self.user,
									passwd = self.passwd,
								      db = self.db )
	def updateT(self,quantity, item):
		self.cursor = self.connection.cursor()
		q = "update products set product_quantity = product_quantity - '%d' where product_name = '%s'"% (quantity, item)
		self.cursor.execute(q)
		self.cursor.close()
		self.connection.commit()
		self.connection.close()
	def selectT(self,item):
		self.cursor = self.connection.cursor()
		q2 = "select price from products where product_name = '%s'"% (item)
		self.cursor.execute(q2)
		pr = self.cursor.fetchone()
		prc  = int(pr[0])
		#print("PRICE VALUE: ",prc)
		self.cursor.close()
		self.connection.commit()
		self.connection.close()
		return prc
	def selectShf(self,item):
		self.cursor = self.connection.cursor()
		q3 = "select shelf_num from products where product_name =    '%s'"% (item)
		self.cursor.execute(q3)
		sh = self.cursor.fetchone()
		shf  = int(sh[0])
		#print("PRICE VALUE: ",prc)
		self.cursor.close()
		self.connection.commit()
		self.connection.close()
		return shf
