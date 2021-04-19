def check_simple(num):
    nums = [num/i for i in range(1, num+1)]
    x = 0
    for i in nums:
        y = str(i)
        if y[y.find('.'):] == '.0':
            x += 1

    return True if x == 2 else False

def simple_nums(args):
    x,y = args
    x,y = int(x), int(y)
    x = bin(x).replace('0b', '')
    y = bin(y).replace('0b', '')
    return int(x+y, 2), check_simple(int(x+y, 2))

while True:
    print(simple_nums(input().split()))
    
