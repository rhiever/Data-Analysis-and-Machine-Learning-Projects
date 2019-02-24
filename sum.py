

'''
    state: list(balls = 0, runs = 0, fours = 0, sixes = 0, extras = 0, out = FALSE)
    valid outcome: {'0','1','2','4','6',"wide","Noball","out"}
'''

def oneBall(state,outcome):
    if outcome=='0':
        state[0] +=1

    elif outcome=='1':
        state[0] +=1
        state[1] +=1

    elif outcome=='2':
        state[0] += 1
        state[1] += 2

    elif outcome=='4':
        state[0] += 1
        state[1] += 4
        state[2] +=1

    elif outcome=='6':
        state[0] += 1
        state[1] += 6
        state[3] +=1

    elif outcome=="Wide":
        state[4] +=1

    elif outcome=="Noball":
        state[4] +=1

    elif outcome=="out":
        state[0] +=1
        state[5] +=1

t=int(input())
l=[0]*6
for i in range(t):
    outcome=input()
    oneBall(l,outcome)
print(l)
