#!/user/bin/python
# -*-coding:Utf-8 *-

# TIC TACE TOE GAME #
# CREATED BY HATIM AKA MARSECHELON 03/08/2015 #


import Tkinter
from tkMessageBox import *

class Application(Tkinter.Tk):

    def __init__(self):
        Tkinter.Tk.__init__(self)

        # Definition du Canvas
        self.App = Tkinter.Canvas(self , width = 300 , height = 300 , bg = 'white')
        self.App.pack(padx = 5 , pady = 5)
        self.recommencer()
        self.App.bind('<Button-1>',self.click_analyzer)
        self.buttReplay = Tkinter.Button(self , text = "Repaly" , command = self.recommencer)
        self.buttReplay.pack(side = 'left' , padx = 5)
        self.buttQuit = Tkinter.Button(self , text = "Exit" , command = self.destroy)
        self.buttQuit.pack(side = 'right' , padx = 5)
        self.labelScore = Tkinter.Label(self , text = " Player1 : {0} : {1} : Player2 ".format(self.scorePlayer1,self.scorePlayer2))
        self.labelScore.pack(pady = 1)



    def tracerPlateau(self):
        self.App.create_line(105 , 10 , 105 , 290 , width = 10)
        self.App.create_line(205 , 10 , 205 , 290 ,width = 10)
        self.App.create_line(10 , 105 , 290 ,105 , width = 10)
        self.App.create_line(10 , 205 , 290 , 205 ,width = 10)




    def recommencer(self):
        self.game_table = [[0,0,0],[0,0,0],[0,0,0]]
        self.scorePlayer1 = 0   #  Cercle rouge , commence en premierr
        self.scorePlayer2 = 0   #  Croix bleue , the second 1 .
        self.tour = 1
        self.winner = 3         # no winner until now        self.title('Tic Tac Toe !!!')
        self.App.delete(Tkinter.ALL)
        self.labelScore = Tkinter.Label(self , text = " Player1 : {0} : {1} : Player2 ".format(self.scorePlayer1,self.scorePlayer2))
        self.tracerPlateau()

    def tracer_Cercle(self , x , y):

        self.App.create_oval(x - 35 , y - 35 , x + 35 , y + 35 , outline = 'red' , width = 5)


    def tracer_Croix(self , x , y):
        self.App.create_line(x - 35 , y - 35 , x + 35 , y + 35 , width = 5 , fill = 'blue' )
        self.App.create_line(x - 35 , y + 35 , x + 35 , y - 35 , width = 5 , fill = 'blue' )


    def test_Win(self):

        if( self.game_table[0][0]==self.game_table[0][1]==self.game_table[0][2] !=0 ):
            if(self.tour == 1 ):
                self.winner = 2
                self.scorePlayer2 += 1
            else:
                self.winner = 1
                self.scorePlayer1 += 1
        if( self.game_table[1][0]==self.game_table[1][1]==self.game_table[1][2]!=0 ):
            if(self.tour == 1 ):
                self.winner = 2
            else:
                self.winner = 1
        if( self.game_table[2][0]==self.game_table[2][1]==self.game_table[2][2]!=0 ):
            if(self.tour == 1 ):
                self.winner = 2
            else:
                self.winner = 1

        if( self.game_table[0][0]==self.game_table[1][0]==self.game_table[2][0]!=0 ):
            if(self.tour == 1 ):
                self.winner = 2
            else:
                self.winner = 1
        if( self.game_table[0][1]==self.game_table[1][1]==self.game_table[2][1]!=0 ):
            if(self.tour == 1 ):
                self.winner = 2
            else:
                self.winner = 1
        if( self.game_table[0][2]==self.game_table[1][2]==self.game_table[2][2]!=0 ):
            if(self.tour == 1 ):
                self.winner = 2
            else:
                self.winner = 1

        if( self.game_table[0][0]==self.game_table[1][1]==self.game_table[2][2]!=0 ):
            if(self.tour == 1 ):
                self.winner = 2
            else:
                self.winner = 1
        if( self.game_table[0][2]==self.game_table[1][1]==self.game_table[2][0]!=0 ):
            if(self.tour == 1 ):
                self.winner = 2
            else:
                self.winner = 1



    def click_analyzer(self , event):

        print('x -> ',event.x, 'y - >',event.y)



        if(self.tour == 1):

            if( 5 <= event.x <= 105 and  3 <= event.y <= 100 and self.game_table[0][0] == 0):
                self.tracer_Cercle(50 , 50)
                self.game_table[0][0] = 1
                self.tour = 2
            if( 110 <= event.x <= 200 and  3 <= event.y <= 100 and self.game_table[0][1] == 0):
                self.tracer_Cercle(154 , 50)
                self.game_table[0][1] = 1
                self.tour = 2
            if( 210 <= event.x <= 300 and  3 <= event.y <= 100 and self.game_table[0][2] == 0):
                self.tracer_Cercle(255 , 50)
                self.game_table[0][2] = 1
                self.tour = 2

            if( 5 <= event.x <= 105 and  112 <= event.y <= 201 and self.game_table[1][0] == 0):
                self.tracer_Cercle(50 , 155)
                self.game_table[1][0] = 1
                self.tour = 2
            if( 110 <= event.x <= 200 and  112 <= event.y <= 201 and self.game_table[1][1] == 0):
                self.tracer_Cercle(154 , 155)
                self.game_table[1][1] = 1
                self.tour = 2
            if( 210 <= event.x <= 300 and  112 <= event.y <= 201 and self.game_table[1][2] == 0):
                self.tracer_Cercle(255 , 155)
                self.game_table[1][2] = 1
                self.tour = 2

            if( 5 <= event.x <= 105 and  212 <= event.y <= 301 and self.game_table[2][0] == 0):
                self.tracer_Cercle(50 , 255)
                self.game_table[2][0] = 1
                self.tour = 2
            if( 110 <= event.x <= 200 and  212 <= event.y <= 301 and self.game_table[2][1] == 0):
                self.tracer_Cercle(154 , 255)
                self.game_table[2][1] = 1
                self.tour = 2
            if( 210 <= event.x <= 300 and  212 <= event.y <= 301 and self.game_table[2][2] == 0):
                self.tracer_Cercle(255 , 255)
                self.game_table[2][2] = 1
                self.tour = 2



        elif(self.tour == 2):

            if( 5 <= event.x <= 105 and  3 <= event.y <= 100 and self.game_table[0][0] == 0):
                self.tracer_Croix(50 , 50)
                self.game_table[0][0] = 2
                self.tour = 1
            if( 110 <= event.x <= 200 and  3 <= event.y <= 100 and self.game_table[0][1] == 0):
                self.tracer_Croix(154 , 50)
                self.game_table[0][1] = 2
                self.tour = 1
            if( 210 <= event.x <= 300 and  3 <= event.y <= 100 and self.game_table[0][2] == 0):
                self.tracer_Croix(255 , 50)
                self.game_table[0][2] = 2
                self.tour = 1

            if( 5 <= event.x <= 105 and  112 <= event.y <= 201 and self.game_table[1][0] == 0):
                self.tracer_Croix(50 , 155)
                self.game_table[1][0] = 2
                self.tour = 1
            if( 110 <= event.x <= 200 and  112 <= event.y <= 201 and self.game_table[1][1] == 0):
                self.tracer_Croix(154 , 155)
                self.game_table[1][1] = 2
                self.tour = 1
            if( 210 <= event.x <= 300 and  112 <= event.y <= 201 and self.game_table[1][2] == 0):
                self.tracer_Croix(255 , 155)
                self.game_table[1][2] = 2
                self.tour = 1

            if( 5 <= event.x <= 105 and  212 <= event.y <= 301 and self.game_table[2][0] == 0):
                self.tracer_Croix(50 , 255)
                self.game_table[2][0] = 2
                self.tour = 1
            if( 110 <= event.x <= 200 and  212 <= event.y <= 301 and self.game_table[2][1] == 0):
                self.tracer_Croix(154 , 255)
                self.game_table[2][1] = 2
                self.tour = 1
            if( 210 <= event.x <= 300 and  212 <= event.y <= 301 and self.game_table[2][2] == 0):
                self.tracer_Croix(255 , 255)
                self.game_table[2][2] = 2
                self.tour = 1


        self.test_Win()
        if(self.winner == 1):
            self.scorePlayer1 += 1
            showinfo('Fin du jeu', "Player 1 Congrats ,u won !!!")
            self.recommencer()
        elif(self.winner == 2):
            self.scorePlayer2 += 1
            showinfo('Fin du jeu', "Player 2 Congrats , u won !!!")
            self.recommencer()


if __name__ == '__main__':
    fen = Application()
    fen.mainloop()
