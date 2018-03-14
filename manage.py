import os

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from api import app, db
from api.config import app_config
from api.todo import models

config_name = os.environ.get('APP_SETTINGS', 'development')
app.config.from_object(app_config.get(config_name))

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()