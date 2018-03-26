from src.app import app
import src.config as AppConfig
app.run('localhost', 4995, AppConfig.DEBUG)