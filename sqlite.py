def create_connection():
	print(1)
	con = sqlite3.connect(r'C:\CP\baza.db')

	cur = con.cursor()

	cur.execute('CREATE TABLE IF NOT EXISTS core_fes(Name TEXT,'
	                                               'Age INTEGER,'
	                                               'Marital_status TEXT,'
	                                               'Work_status TEXT,'
	                                               'War_status TEXT,'
	                                               'Awards_status TEXT'
	                                               'Seniority TEXT)')


	cur.execute('INSERT INTO core_fes VALUES("?, ?, ?, ?, ?, ?, ?")', data)

	cur.commit()

create_connection()