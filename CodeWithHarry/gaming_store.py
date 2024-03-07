class Gamingstore:
    def __init__(self):
        self.total_games = 0
        self.games = {}
    def show_games(self):
        print("Games: ")
        for game,category in self.games.items():
            print("-", game ,"(category: ", category,")")
    def add_game(self,game,category):
        self.games[game] = category
        self.total_games += 1
    def get_total_games(self):
        return self.total_games

#Create an Object
gamingstore = Gamingstore()

#Show initial number of Games avalible in store
print("Initial number of games avalible in store are: ", Gamingstore().get_total_games())

#add New games
while True:
    print("Note: Enter 'exit' to quit and get the total info (or)")
    print("Enter a game name: ")
    game = input()
    if game == 'exit':
        break
    else:
        print("Enter the category of the game: ")
        category = input()
        Gamingstore().add_game(game,category)

#Show the total number of games avalible in the store
print("Total number of games in store: ",Gamingstore().get_total_games())

#print total games
Gamingstore().show_games()

