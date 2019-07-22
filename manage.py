from flask_script import Manager

from app.app import app

manager = Manager(app)


@manager.option('-p', '--port', dest='port', default=app.config["FLASK_PORT"])
@manager.option('-h', '--host', dest='host', default=app.config["FLASK_HOST"])
@manager.option('-d', '--debug', dest='debug', default=False)
def runserver(host, port, debug):
    app.run(host=host, port=port, debug=True)


if __name__ == '__main__':
    manager.run()
