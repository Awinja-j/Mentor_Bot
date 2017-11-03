from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app import create_app
from app.models.models import db

app = create_app('default')

manager = Manager(app)
migrate = Migrate(app, db)


manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
