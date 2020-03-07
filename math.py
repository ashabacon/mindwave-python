import threading
import random
from tkinter import *
import time
player_ans = ""
correct_ans = 0
score = 0
time_remaining = 100
count = 0

def gui():
    print("gui running")
    window = Tk()

    window.title("Math is Stress Free")

    window.geometry('850x800')

    lbl = Label(window, text="2+1")

    lbl.grid(column=0, row=0)
    
    score_lbl = Label(window, text="score: 0")

    score_lbl.grid(column=2, row=3)

    timer_lbl = Label(window, text="time: 100")

    timer_lbl.grid(column=2, row=6)
        
    stress_lbl = Label(window, text="score: 0")

    stress_lbl.grid(column=6, row=6)
    
    stress_lbl.configure(text= "")
    
    txt = Entry(window,width=10)

    txt.grid(column=1, row=0)
    
    txt.focus()
    

    def clicked():
        global player_ans

        player_ans = int(txt.get())
        global score
        
        if player_ans == correct_ans:
            
            score += 1
        else:
            
            score -= 1
        disp_sc = "score" + str(score)
        score_lbl.configure(text= disp_sc)
        get_new_prob()
        txt.delete(0, 'end')
      
        
    def get_new_prob():
        type_math = random.randint(1,3) #4 if division
        global correct_ans  
        num_1 = random.randint(1,20)
        num_2 = random.randint(1,10)
        if type_math == 1:
            operation = '+'
            correct_ans = num_1 + num_2
        if type_math == 2:
            operation = '-'
            correct_ans = num_1 - num_2
        if type_math == 3:
            operation = 'x'
            correct_ans = num_1 * num_2
        
#       if type_math = 4:
#           operation = '/'n
#           ans = num_1 / num_2

        prob = str(num_1) + str(operation) + str(num_2)

        lbl.configure(text= prob)
    get_new_prob()

    btn = Button(window, text="Submit", command=clicked)

    btn.grid(column=2, row=0)
    
    timer_lbl.configure(text= "time left:" + str(time_remaining))
    
    def start_timer_in():
        def timink():
            print("timer_control running")
            global time_remaining
            
            while time_remaining > 0:
                global count
                time.sleep(1)
                time_remaining -= 1
                timer_lbl.configure(text= "time left:" + str(time_remaining))
                count += 1
                print(count)
                if count == 5:
                    count = 0
                    #get data from BCI
                    #going to proxy it as a random number here
                    med_measure = random.randint(1,100)
                    if med_measure >= 75:
                        #gain 2 sec
                        time_remaining += 2
                        stress_lbl.configure(text= "Un-Stressed! +2 seconds!")
                    elif med_measure <= 25:
                        #lose 2 sec
                        time_remaining -= 2
                        stress_lbl.configure(text= "Stressed! -2 seconds!")
                    else:
                        stress_lbl.configure(text= "Normal stress, no bonus or penalty")
                elif count == 3:
                    stress_lbl.configure(text= "")
                    
        
        t = threading.Thread(target=timink)
        t.start()
        
    
    window.after(10, start_timer_in) 
    window.mainloop()
    
gui()