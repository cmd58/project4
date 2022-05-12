"""This tests the transaction record"""
import logging

from app import db
from app.db.models import User, Transactions
#from faker import Faker

"""This tests adding new transaction"""


def test_adding_transaction():
    log = logging.getLogger("myApp")
    user = User('keith@webizly.com', 'testtest')
    db.session.add(user)
    user = User.query.filter_by(email='keith@webizly.com').first()
    log.info(user)
    #assers correct user is retrieved
    assert user.email == 'keith@webizly.com'
    #getting related record ready for insert
    user.transactions= [Transactions("test","smap"),Transactions("test2","te")]
    #commit to save transactions
    db.session.commit()
    assert db.session.query(Transactions).count() == 2
    transaction1 = Transactions.query.filter_by(title='test').first()
    assert transaction1.type == "test"
    #changing the title of the transaction
    transaction1.title = "BigTransaction"
    #saving the new title of the transaction
    db.session.commit()
    transaction2 = Transactions.query.filter_by(title='BigTransaction').first()
    assert transaction2.title == "BigTransaction"
    #checking cascade delete
    db.session.delete(user)
    assert db.session.query(User).count() == 0
    assert db.session.query(Transactions).count() == 0