
from app.controller.controller import Controller


class ProgramManager:
    """
    Responsability: application process
    """
    def __init__(self):
        self.controller = Controller()

    def run(self):
        """
        launches and ensures the correct process of the program
        """
        self.controller.welcome()
        self.controller.db_management_menu_process()
        self.controller.find_or_display_substitute_process()
