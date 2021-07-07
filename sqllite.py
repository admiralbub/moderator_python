import sqlite3 
class BD:
	def __init__(self):
		#self.id_user = id_user
		self.conn = sqlite3.connect('chat.db')
		self.cur = self.conn.cursor()




	def ban_users(self,id_user):
		result = self.cur.execute("SELECT * FROM Ban WHERE user_id=?", (id_user,)).fetchall()
		return bool(len(result))


	def new_ban_users(self,id_user,status=1):
		with self.conn:
			return self.cur.execute("INSERT INTO Ban (user_id,status) VALUES (?,?)",(id_user,status))
