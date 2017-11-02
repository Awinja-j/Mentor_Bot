import os
import inspect
import sys
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db

app = create_app('default')

manager = Manager(app)
migrate = Migrate(app, db)


manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
