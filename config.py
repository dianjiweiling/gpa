import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
	SECRET_KEY = 'hard to guess string'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True

	@staticmethod
	def init_app(app):
		pass


class DevelopmentConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
		'default': DevelopmentConfig
}