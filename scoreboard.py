from turtle import Turtle
ALIGNEMENT = "center"
FONT = ("Arial",24,"normal")
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-20,270)
        self.color("white")
        self.score = 0
        with open("/home/carlos/Bureau/100 days of python/Day 20/data.txt", 'r') as file:
            self.high_score = file.read() 
            self.high_score = int(self.high_score)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"score:{self.score} High Score:{self.high_score}",align=ALIGNEMENT, font= FONT) 
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        with open("/home/carlos/Bureau/100 days of python/Day 20/data.txt", "w") as file:
            if self.score > self.high_score:
                self.high_score = self.score
                
            file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
""" 
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGNEMENT, font= FONT)
        """