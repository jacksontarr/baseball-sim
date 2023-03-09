class Team:
    __slots__ = {"id", "loc", "nickname", "wins", "losses", "gp"}

    def __init__(self, id, loc, nickname):
        self.id = id
        self.loc = loc
        self.nickname = nickname
        self.wins = 0
        self.losses = 0
        self.gp = 0

    def get_id(self):
        return self.id
    
    def get_loc(self):
        return self.loc
    
    def get_nickname(self):
        return self.nickname
    
    def get_wins(self):
        return self.wins
    
    def get_losses(self):
        return self.losses
    
    def get_gp(self):
        return self.gp
    
    def win(self):
        self.wins += 1
        self.gp += 1

    def lose(self):
        self.losses += 1
        self.gp += 1

    def win_pct(self):
        return round(float(self.wins) / float(self.gp), 3)

class Player:
    __slots__ = {"id", "contact", "power", "eye"}

    def __init__(self, id, contact, power, eye):
        self.id = id
        self.contact = contact
        self.power = power
        self.eye = eye

def main():
    phillies = Team(21, "Philadelphia", "Phillies")
    for _ in range(100):
        phillies.win()
    
    for _ in range(62):
        phillies.lose()

    print(phillies.win_pct())

if __name__ == "__main__":
    main()