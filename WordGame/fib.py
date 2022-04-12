
def fibo(value = 10):
    series = [0, 1]
    i = 2
    while len(series) < value:
        next = series[i - 2] + series[i - 1]
        series.append(next)
        i +=1
    print(series)
    
fibo(12)
        
        
        