result = 0
start = 1
end = 100

def compute():
#def compute(result, start, end):
    global result
    global start
    global end
    while start <= end:
        result += start
        start += 1
    print(result)

if __name__ == '__main__':
    compute()
#    compute(result, start, end)
