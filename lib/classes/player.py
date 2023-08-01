class Player:

    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []
        Player.all.append(self)

    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, value):
        if 2 < len(value) < 16 and isinstance(value, str):
            print("in setter")
            self._username = value
        else:
            raise Exception("the username in the setter exception")
        
    def results(self, new_result=None):
        from classes.result import Result
        if new_result and isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results
    
    def games_played(self, new_game=None):
        from classes.game import Game
        if new_game and isinstance(new_game, Game):
            self._games_played.append(new_game)
        return self._games_played
        
    
    def played_game(self, game):
        return game in self._games_played
    
    def num_times_played(self, game):
        return len([result for result in self._results if result.game == game])
    
    @classmethod
    def highest_scored(cls, game):
        if cls.all:
            max_player = None
            max_score = 0
            for play in cls.all:
                if game.average_score(play) > max_score:
                    max_player = play
                    max_score = game.average_score(play)
                return max_player
            else:
                return None
        
