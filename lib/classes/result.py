class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        
        player.results(self)
        player.games_played(game)
        game.result(self)
        game.players(player)
        Result.all.append(self)
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        if 1 <= value <= 5000 and isinstance(value, int):
            print("in setter")
            self._score = value
        else:
            raise Exception("the score in the setter exception")
    
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, value):
        from classes.player import Player
        if isinstance(value, Player):
            print("in setter")
            self._player = value
        else:
            raise Exception("the player(result) in the setter exception")
    
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, value):
        from classes.game import Game
        if isinstance(value, Game):
            print("in setter")
            self._game = value
        else:
            raise Exception("the game(result) in the setter exception")
    
