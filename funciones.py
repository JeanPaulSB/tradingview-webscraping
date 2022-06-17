###################ALGORITMO DE PUNTAJES DE EXITO
def succes_score(l):
    c=0
    x=0
    #c=c+4 --> c+=4
    #c=c-4 --> c-=4
    c = c + ((l[0]**2)*2/25)-(8*l[0])+(200)#rsi
    c = c +(l[1]**2)/50 - 2*l[1] +100#IMI
    c = c + ((-abs(l[2])**2)/800)+50#SQZMOM
    c = c + -l[3]/2+50 #ADX
    c = c -5*(abs(l[4]-l[5]))+ 100 #HISTOGRAMA Y SIGNAL
    c = c -(abs(l[0]-l[6])) + 50 #rsi y based
    c = c + ((-abs(l[7])**2)/200)+50#MACD
    m = (1/(l[8]-l[9]))
    a = (m*l[10]) - l[9]*m
    c = c + (a**2)*400 - (400*a)+100#FIBONACCI, H(1), G(0)

    if l[0] <= 30:
        x = x + 2
    if l[0] >= 70:
        x = x - 2
    ##########################IMI
    if l[1] <= 20:
        x = x + 1
    if l[1] >= 80:
        x = x - 1
    ##############SQZMOM
    if l[2] >= 0:
        x = x - 1
    if l[2] < 0:
        x = x + 1
    #############histograma y signal
    if l[5]-l[4] >= 0 :
        x = x + 1
    else:
        x = x - 1
    ##############DIFERENCIAL DE RSI
    if l[6]-l[0] >= 0:
        x = x + 1
    else:
        x = x - 1
    #############MACD
    if l[7] >= 0:
        x = x + 1
    if l[7] < 0:
        x = x - 1
    ###########FIBONACCI
    if (1/(l[8]-l[9])*l[10]) + l[9]<= 0.236:
        x = x + 1
    if (1/(l[8]-l[9])*l[10]) + l[9] > 0.7:
        x = x - 1
    if x >= 5:
        print("FUERTE SUGERENCIA COMPRA")
    if x <= -5:
        print("FUERTE SUGERENCIA DE VENTA")

    return (c/600)*100


