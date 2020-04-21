
from models.database import Database

class ProgramManager:
    def __init__(self):
        self.db = Database("localhost", "root", "")

    def launch(self):
        self.db.drop()
        self.db.create()


prog = ProgramManager()
prog.launch()