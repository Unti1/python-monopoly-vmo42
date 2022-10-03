class Map:
    def __init__(self):
        self.__SessionID: str = ""
        self.__CurrentUsersList: dict = {}
        self.__MapImagePath: str = ""
        self.__MapStructure = [
            "-----------",
            "-         -",
            "-         -",
            "-         -",
            "-         -",
            "-         -",
            "-         -",
            "-         -",
            "-         -",
            "-         -",
            "-----------",
        ]

    def set_MapImagePath(self, value: str):
        self.__MapImagePath = value

    def set_CurrentUsersList(self, value: dict):
        self.__CurrentUsersList = value

    def set_SessionID(self, value: str):
        self.__SessionID = value

    @ property
    def get_MapImagePath(self):
        return (self.__MapImagePath)

    @ property
    def get_CurrentUsersList(self):
        return (self.__CurrentUsersList)

    @ property
    def get_SessionID(self):
        return (self.__SessionID)
        
    @ property
    def get_MapStructure(self):
        return (self.__MapStructure)
