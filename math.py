#python code

stress = 0;
score = 0;
start = time.time()
time_value = 100;
while time.time() - start < time_value:
    give_math_problems

def give_math_problems:
    type_math = rand(1,3): #4 if division
    if type_math = 1:
        operation = '+'
    if type_math = 2:
        operation = '-'
    if type_math = 3:
        operation = 'x'
#    if type_math = 4:
#        operation = '/'n

    num_1 = rand (1,20);
    num_2 = rand (1,10);

    print (num_1, operation, num_2);
    (switch) #case depends on value of operation
      case 1: ans = num_1 + num_2;
      case 2: ans = num_1 - num_2;
      case 3: ans = num_1 * num_3;

    user_ans = input(num_1, operation, num_2, "=" :\n");

    if user_ans == ans: #might be type issues here but I think python handles it correctly?
      score += 1;
    else:
      score -= 1;


#more updatey timer taken from stack overflow:
#import signal
#def timeout_handler(signal, frame):
#    raise Exception('Time is up!')
#signal.signal(signal.SIGALRM, timeout_handler)
#signal.alarm.timeout(60) #60 is their value, ours would be 100
#try:
#    while lives > 0 # we dont have live so i think we would just put give_math_problems
        # stuff
#except:
    # print score

#https://www.google.com/search?rlz=1C5CHFA_enUS817US817&biw=1440&bih=766&ei=GQpUXr2vK5De-gTL2rKwBQ&q=python+timer+in+background+display&oq=python+timer+in+background+display&gs_l=psy-ab.3..33i22i29i30.956.2109..2268...0.2..0.101.671.7j1......0....1..gws-wiz.......0i71j0i22i30.G2fUARunSKE&ved=0ahUKEwj9n_u43ernAhUQr54KHUutDFYQ4dUDCAs&uact=5#kpvalbx=_rgtUXsjDBZjy-gT8mqXQBQ19
#that video link might be helpful
