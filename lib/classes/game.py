class Game:
    def __init__(self, title):
        self.title = title
        self._results = []
        self._players = []
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if value and isinstance(value, str) and not hasattr(self, "title"):
            print("in setter")
            self._title = value
        else:
            raise Exception("the title in the setter exception")

        
    def results(self, new_result=None):
        from classes.result import Result
        if new_result and isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results
    
    
    def players(self, new_player=None):
        from classes.player import Player
        if new_player and isinstance(new_player, Player):
            self._players.append(new_player)
        return self._players
    
    def average_score(self, player):
        total = 0
        s = [result.score for result in self._results if result.player == player]
        if s:
            total = sum(s) / len(s)
        return total