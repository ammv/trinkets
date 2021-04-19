from time import sleep

s = int(input())
 
table = {1: [1,0,0,1],
            2: [1,0,0,1],
            3: [1,1,0,2],
            4: [2,1,1,4],
            5: [4,2,1,7],
            6: [6,2,1,9],
            7: [9,4,2,15],
            8: [15,6,4,25],
}
 
for i in range(len(table)+1, s+1):
    value = [
        table[i-1][3],
        table[i-2][0],
        table[i-1][1],
    ]
    value.append(sum(value))
    table[i] = value
            
