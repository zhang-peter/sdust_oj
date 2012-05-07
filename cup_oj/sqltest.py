from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://root:123@localhost/mytest',echo=True,encoding='utf8')
# engine.execute("SELECT * FROM Description D LIMIT 0,1000").scalar()
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
class Test(Base):
	__tablename__ = 'Test'

	id = Column(Integer,Sequence('user_id_seq'),primary_key=True)
	name = Column(String(50))
	fullname = Column(String(50))
	password = Column(String(50))
	
	def __init__(self,name,fullname,password):
		self.name = name
		self.fullname = fullname
		self.password = password
	
	def __repr__(self):
		return "<Test('%d','%s','%s','%s')>" % (self.id,self.name,self.fullname,self.password)


Base.metadata.create_all(engine)
#ed_user = Test('ed','Ed Jones','edpassword')

#session.add(ed_user)

our_user = session.query(Test).filter_by(name='ed').limit(5)
#print our_user[3].__repr__
#print our_user.count()
for user in our_user:
	print user.__repr__()

#ed_user.password = 'f8s7ccs'
#session.dirty

"""
session.add_all([
	Test('wendy','Wendy Williams','foobar'),
	Test('mary','Mary Contrary','xxg527'),
	Test('fred','Fred Flinstone','blah')])
"""
#test1 = Test('wendy','Wendy Williams','foobar')
#test2 = Test('mary','Mary Contrary','xxg527')
#session.new
#session.commit()


