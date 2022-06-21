import tkinter as tk

cnv = tk.Canvas(height = 300, width = 300, background = 'mediumturquoise')
cnv.pack()

x, y = 0, 0

for i in range(0, 300, 100):
    for j in range(0, 300, 100):
        cnv.create_rectangle(x, y, x + 100, y + 100)

        x += 100
        
    x = 0
    y += 100

radius_x, radius_y = [50, 150, 250], [50, 150, 250]

lines_player_1, lines_player_2 = [], []

def player_1():
    global n
    
    shortest_x = []
    shortest_y = []

    for i in range(3):
        shortest_x.append(abs(radius_x[i] - a))
        shortest_y.append(abs(radius_y[i] - b))

    centered_x = radius_x[shortest_x.index(min(shortest_x))]
    centered_y = radius_y[shortest_y.index(min(shortest_y))]

    if [centered_x, centered_y] not in lines_player_2 and [centered_x, centered_y] not in lines_player_1:
        lines_player_1.append([centered_x, centered_y])
        
        n += 1

        cnv.create_oval(centered_x - 50, centered_y - 50, centered_x + 50, centered_y + 50, fill = 'red', outline = 'cyan', tags = 'kruh')

def player_2():
    global n

    shortest_x = []
    shortest_y = []

    for i in range(3):
        shortest_x.append(abs(radius_x[i] - a))
        shortest_y.append(abs(radius_y[i] - b))

    centered_x = radius_x[shortest_x.index(min(shortest_x))]
    centered_y = radius_y[shortest_y.index(min(shortest_y))]

    if [centered_x, centered_y] not in lines_player_1 and [centered_x, centered_y] not in lines_player_2:
        lines_player_2.append([centered_x, centered_y])

        n += 1

        cnv.create_rectangle(centered_x - 50, centered_y - 50, centered_x + 50, centered_y + 50, fill = 'blue', outline = 'cyan', tags = 'stvorec')

n = 2
winner = False

def draw(pos):
    global a, b, n, lines_player_1, lines_player_2, winner

    a, b = pos.x, pos.y

    if n > 10 or winner == True:

        cnv.delete('stvorec')
        cnv.delete('kruh')
        cnv.delete('crossline')

        lines_player_1, lines_player_2 = [], []
        n = 1
        winner = False

    if n >= 2 and n < 11:
        if n % 2 == 0:
            player_1()

        #PLAYER_1 CROSSLINES

            if [50, 50] in lines_player_1:
                if [150, 50] in lines_player_1 and [250, 50] in lines_player_1:
                    cnv.create_line(25, 50, 275, 50, fill = 'white', width = 5, tags = 'crossline')

                elif [150, 150] in lines_player_1 and [250, 250] in lines_player_1:
                    cnv.create_line(25, 25, 275, 275, fill = 'white', width = 5, tags = 'crossline')

                elif [50, 150] in lines_player_1 and [50, 250] in lines_player_1:
                    cnv.create_line(50, 25, 50, 275, fill = 'white', width = 5, tags = 'crossline')

            if [50, 150] in lines_player_1 and [150, 150] in lines_player_1 and [250, 150] in lines_player_1:
                cnv.create_line(25, 150, 275, 150, fill = 'white', width = 5, tags = 'crossline')

            if [50, 250] in lines_player_1:
                if [150, 250] in lines_player_1 and [250, 250] in lines_player_1:
                    cnv.create_line(25, 250, 275, 250, fill = 'white', width = 5, tags = 'crossline')

                elif [150, 150] in lines_player_1 and [250, 50] in lines_player_1:
                    cnv.create_line(25, 275, 275, 25, fill = 'white', width = 5, tags = 'crossline')

            if [150, 50] in lines_player_1 and [150, 150] in lines_player_1 and [150, 250] in lines_player_1:
                cnv.create_line(150, 25, 150, 275, fill = 'white', width = 5, tags = 'crossline')
            
            if [250, 50] in lines_player_1 and [250, 150] in lines_player_1 and [250, 250] in lines_player_1:
                cnv.create_line(250, 25, 250, 275, fill = 'white', width = 5, tags = 'crossline')

        #PLAYER_1 WIN CONDITIONS

            if [50, 50] in lines_player_1:
                if [150, 50] in lines_player_1 and [250, 50] in lines_player_1:
                    winner = True

                elif [150, 150] in lines_player_1 and [250, 250] in lines_player_1:
                    winner = True

                elif [50, 150] in lines_player_1 and [50, 250] in lines_player_1:
                    winner = True

            if [50, 150] in lines_player_1 and [150, 150] in lines_player_1 and [250, 150] in lines_player_1:
                winner = True

            if [50, 250] in lines_player_1:
                if [150, 250] in lines_player_1 and [250, 250] in lines_player_1:
                    winner = True

                elif [150, 150] in lines_player_1 and [250, 50] in lines_player_1:
                    winner = True

            if [150, 50] in lines_player_1 and [150, 150] in lines_player_1 and [150, 250] in lines_player_1:
                winner = True
            
            if [250, 50] in lines_player_1 and [250, 150] in lines_player_1 and [250, 250] in lines_player_1:
                winner = True

        if n % 2 == 1:
            player_2()

        #PLAYER_2 CROSSLINES

            if [50, 50] in lines_player_2:
                if [150, 50] in lines_player_2 and [250, 50] in lines_player_2:
                    cnv.create_line(25, 50, 275, 50, fill = 'white', width = 5, tags = 'crossline')

                elif [150, 150] in lines_player_2 and [250, 250] in lines_player_2:
                    cnv.create_line(25, 25, 275, 275, fill = 'white', width = 5, tags = 'crossline')

                elif [50, 150] in lines_player_2 and [50, 250] in lines_player_2:
                    cnv.create_line(50, 25, 50, 275, fill = 'white', width = 5, tags = 'crossline')

            if [50, 150] in lines_player_2 and [150, 150] in lines_player_2 and [250, 150] in lines_player_2:
                cnv.create_line(25, 150, 275, 150, fill = 'white', width = 5, tags = 'crossline')

            if [50, 250] in lines_player_2:
                if [150, 250] in lines_player_2 and [250, 250] in lines_player_2:
                    cnv.create_line(25, 250, 275, 250, fill = 'white', width = 5, tags = 'crossline')

                elif [150, 150] in lines_player_2 and [250, 50] in lines_player_2:
                    cnv.create_line(25, 275, 275, 25, fill = 'white', width = 5, tags = 'crossline')

            if [150, 50] in lines_player_2 and [150, 150] in lines_player_2 and [150, 250] in lines_player_2:
                cnv.create_line(150, 25, 150, 275, fill = 'white', width = 5, tags = 'crossline')
            
            if [250, 50] in lines_player_2 and [250, 150] in lines_player_2 and [250, 250] in lines_player_2:
                cnv.create_line(250, 25, 250, 275, fill = 'white', width = 5, tags = 'crossline')

        #PLAYER_2 WIN CONDITIONS

            if [50, 50] in lines_player_2:
                if [150, 50] in lines_player_2 and [250, 50] in lines_player_2:
                    winner = True

                elif [150, 150] in lines_player_2 and [250, 250] in lines_player_2:
                    winner = True

                elif [50, 150] in lines_player_2 and [50, 250] in lines_player_2:
                    winner = True

            if [50, 150] in lines_player_2 and [150, 150] in lines_player_2 and [250, 150] in lines_player_2:
                winner = True

            if [50, 250] in lines_player_2:
                if [150, 250] in lines_player_2 and [250, 250] in lines_player_2:
                    winner = True

                elif [150, 150] in lines_player_2 and [250, 50] in lines_player_2:
                    winner = True

            if [150, 50] in lines_player_2 and [150, 150] in lines_player_2 and [150, 250] in lines_player_2:
                winner = True
            
            if [250, 50] in lines_player_2 and [250, 150] in lines_player_2 and [250, 250] in lines_player_2:
                winner = True
    
    else:
        n += 1

cnv.bind('<Button-1>', draw)

cnv.mainloop()