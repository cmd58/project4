"""click test"""
#import logging
import os

from click.testing import CliRunner

from app.cli import create_database

runner = CliRunner()

#def test_create_logs():
    #"""logs"""
    #response = runner.invoke(create_logs)
    # assert response.exit_code == 0
    # root = os.path.dirname(os.path.abspath(__file__))
    # logdir = os.path.join(root, '../logs')
    # response = os.path.exists(logdir)
    # assert response is True


def test_create_database():
    """creating db test"""
    response = runner.invoke(create_database)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    dbdir = os.path.join(root, '../database')
    # make a directory if it doesn't exist
    assert os.path.exists(dbdir) is True