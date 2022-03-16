
from math import acos, sqrt, cos
import matplotlib.pyplot as plt

def FitzHughNagumo(x1_0, y1_0, x2_0, y2_0, x3_0, y3_0, k, dt, TF, eps):
    X1 = []
    Y1 = []
    X2 = []
    Y2 = []
    X3 = []
    Y3 = []

    
    OX_x = 10; OX_y = 0
    Fi1 = []
    Fi2 = []
    Fi3 = []
    Delta1 = []
    Delta2 = []

    T = []

    X1.append(x1_0)
    Y1.append(y1_0)
    X2.append(x2_0)
    Y2.append(y2_0)
    X3.append(x3_0)
    Y3.append(y3_0)

    t = 0
    T.append(0)

    fig = plt.figure("Plots X1(t), Y1(t), X2(t), Y2(t), X3(t), Y3(t)")

    ax_1 = fig.add_subplot(3, 2, 1)
    ax_1.set(title = 'x1(t)')

    ax_2 = fig.add_subplot(3, 2, 2)
    ax_2.set(title = 'y1(t)')

    ax_3 = fig.add_subplot(3, 2, 3)
    ax_3.set(title = 'x2(t)')

    ax_4 = fig.add_subplot(3, 2, 4)
    ax_4.set(title = 'y2(t)')

    ax_5 = fig.add_subplot(3, 2, 5)
    ax_5.set(title = 'x3(t)')

    ax_6 = fig.add_subplot(3, 2, 6)
    ax_6.set(title = 'y3(t)')

    while t <= TF:
        T.append(t)

        Q1_x1 = dt * funcX1(t, X1[-1], Y1[-1], X2[-1], Y2[-1], X3[-1], Y3[-1], k, eps)
        Q1_y1 = dt * funcY1(t, X1[-1], Y1[-1], X2[-1], Y2[-1], X3[-1], Y3[-1], k)
        Q1_x2 = dt * funcX2(t, X1[-1], Y1[-1], X2[-1], Y2[-1], X3[-1], Y3[-1], k, eps)
        Q1_y2 = dt * funcY2(t, X1[-1], Y1[-1], X2[-1], Y2[-1], X3[-1], Y3[-1], k)
        Q1_x3 = dt * funcX3(t, X1[-1], Y1[-1], X2[-1], Y2[-1], X3[-1], Y3[-1], k, eps)
        Q1_y3 = dt * funcY3(t, X1[-1], Y1[-1], X2[-1], Y2[-1], X3[-1], Y3[-1], k)

        Q2_x1 = dt * funcX1(t + dt / 2, X1[-1] + Q1_x1 / 2, Y1[-1] + Q1_y1 / 2, X2[-1] + Q1_x2 / 2, Y2[-1] + Q1_y2 / 2, X3[-1] + Q1_x3 / 2, Y3[-1] + Q1_y3 / 2, k, eps)
        Q2_y1 = dt * funcY1(t + dt / 2, X1[-1] + Q1_x1 / 2, Y1[-1] + Q1_y1 / 2, X2[-1] + Q1_x2 / 2, Y2[-1] + Q1_y2 / 2, X3[-1] + Q1_x3 / 2, Y3[-1] + Q1_y3 / 2, k)
        Q2_x2 = dt * funcX2(t + dt / 2, X1[-1] + Q1_x1 / 2, Y1[-1] + Q1_y1 / 2, X2[-1] + Q1_x2 / 2, Y2[-1] + Q1_y2 / 2, X3[-1] + Q1_x3 / 2, Y3[-1] + Q1_y3 / 2, k, eps)
        Q2_y2 = dt * funcY2(t + dt / 2, X1[-1] + Q1_x1 / 2, Y1[-1] + Q1_y1 / 2, X2[-1] + Q1_x2 / 2, Y2[-1] + Q1_y2 / 2, X3[-1] + Q1_x3 / 2, Y3[-1] + Q1_y3 / 2, k)
        Q2_x3 = dt * funcX3(t + dt / 2, X1[-1] + Q1_x1 / 2, Y1[-1] + Q1_y1 / 2, X2[-1] + Q1_x2 / 2, Y2[-1] + Q1_y2 / 2, X3[-1] + Q1_x3 / 2, Y3[-1] + Q1_y3 / 2, k, eps)
        Q2_y3 = dt * funcY3(t + dt / 2, X1[-1] + Q1_x1 / 2, Y1[-1] + Q1_y1 / 2, X2[-1] + Q1_x2 / 2, Y2[-1] + Q1_y2 / 2, X3[-1] + Q1_x3 / 2, Y3[-1] + Q1_y3 / 2, k)

        Q3_x1 = dt * funcX1(t + dt / 2, X1[-1] + Q2_x1 / 2, Y1[-1] + Q2_y1 / 2, X2[-1] + Q2_x2 / 2, Y2[-1] + Q2_y2 / 2, X3[-1] + Q2_x3 / 2, Y3[-1] + Q2_y3 / 2, k, eps)
        Q3_y1 = dt * funcY1(t + dt / 2, X1[-1] + Q2_x1 / 2, Y1[-1] + Q2_y1 / 2, X2[-1] + Q2_x2 / 2, Y2[-1] + Q2_y2 / 2, X3[-1] + Q2_x3 / 2, Y3[-1] + Q2_y3 / 2, k)
        Q3_x2 = dt * funcX2(t + dt / 2, X1[-1] + Q2_x1 / 2, Y1[-1] + Q2_y1 / 2, X2[-1] + Q2_x2 / 2, Y2[-1] + Q2_y2 / 2, X3[-1] + Q2_x3 / 2, Y3[-1] + Q2_y3 / 2, k, eps)
        Q3_y2 = dt * funcY2(t + dt / 2, X1[-1] + Q2_x1 / 2, Y1[-1] + Q2_y1 / 2, X2[-1] + Q2_x2 / 2, Y2[-1] + Q2_y2 / 2, X3[-1] + Q2_x3 / 2, Y3[-1] + Q2_y3 / 2, k)
        Q3_x3 = dt * funcX3(t + dt / 2, X1[-1] + Q2_x1 / 2, Y1[-1] + Q2_y1 / 2, X2[-1] + Q2_x2 / 2, Y2[-1] + Q2_y2 / 2, X3[-1] + Q2_x3 / 2, Y3[-1] + Q2_y3 / 2, k, eps)
        Q3_y3 = dt * funcY3(t + dt / 2, X1[-1] + Q2_x1 / 2, Y1[-1] + Q2_y1 / 2, X2[-1] + Q2_x2 / 2, Y2[-1] + Q2_y2 / 2, X3[-1] + Q2_x3 / 2, Y3[-1] + Q2_y3 / 2, k)

        Q4_x1 = dt * funcX1(t + dt, X1[-1] + Q3_x1, Y1[-1] + Q3_y1, X2[-1] + Q3_x2, Y2[-1] + Q3_y2, X3[-1] + Q3_x3, Y3[-1] + Q3_y3, k, eps)
        Q4_y1 = dt * funcY1(t + dt, X1[-1] + Q3_x1, Y1[-1] + Q3_y1, X2[-1] + Q3_x2, Y2[-1] + Q3_y2, X3[-1] + Q3_x3, Y3[-1] + Q3_y3, k)
        Q4_x2 = dt * funcX2(t + dt, X1[-1] + Q3_x1, Y1[-1] + Q3_y1, X2[-1] + Q3_x2, Y2[-1] + Q3_y2, X3[-1] + Q3_x3, Y3[-1] + Q3_y3, k, eps)
        Q4_y2 = dt * funcY2(t + dt, X1[-1] + Q3_x1, Y1[-1] + Q3_y1, X2[-1] + Q3_x2, Y2[-1] + Q3_y2, X3[-1] + Q3_x3, Y3[-1] + Q3_y3, k)
        Q4_x3 = dt * funcX3(t + dt, X1[-1] + Q3_x1, Y1[-1] + Q3_y1, X2[-1] + Q3_x2, Y2[-1] + Q3_y2, X3[-1] + Q3_x3, Y3[-1] + Q3_y3, k, eps)
        Q4_y3 = dt * funcY3(t + dt, X1[-1] + Q3_x1, Y1[-1] + Q3_y1, X2[-1] + Q3_x2, Y2[-1] + Q3_y2, X3[-1] + Q3_x3, Y3[-1] + Q3_y3, k)

        Y1.append(Y1[-1] + Q1_y1 / 6 + Q2_y1 / 3 + Q3_y1 / 3 + Q4_y1 / 6)
        X1.append(X1[-1] + Q1_x1 / 6 + Q2_x1 / 3 + Q3_x1 / 3 + Q4_x1 / 6)
        Y2.append(Y2[-1] + Q1_y2 / 6 + Q2_y2 / 3 + Q3_y2 / 3 + Q4_y2 / 6)
        X2.append(X2[-1] + Q1_x2 / 6 + Q2_x2 / 3 + Q3_x2 / 3 + Q4_x2 / 6)
        Y3.append(Y3[-1] + Q1_y3 / 6 + Q2_y3 / 3 + Q3_y3 / 3 + Q4_y3 / 6)
        X3.append(X3[-1] + Q1_x3 / 6 + Q2_x3 / 3 + Q3_x3 / 3 + Q4_x3 / 6)

        Fi1.append(acos(cos((X1[-1] * OX_x + Y1[-1] * OX_y) / (sqrt(X1[-1] * X1[-1] + Y1[-1] * Y1[-1]) + 10))))
        Fi2.append(acos(cos((X2[-1] * OX_x + Y2[-1] * OX_y) / (sqrt(X2[-1] * X2[-1] + Y2[-1] * Y2[-1]) + 10))))
        Fi3.append(acos(cos((X3[-1] * OX_x + Y3[-1] * OX_y) / (sqrt(X3[-1] * X3[-1] + Y3[-1] * Y3[-1]) + 10))))

        Delta1.append(Fi2[-1] - Fi1[-1])
        Delta2.append(Fi3[-1] - Fi1[-1])

        t = t + dt

    t = 0 
    while t <= 150:
        del T[0]
        del X1[0]; del Y1[0]
        del X2[0]; del Y2[0]
        del X3[0]; del Y3[0]
        del Fi1[0]; del Fi2[0]; del Fi3[0]
        del Delta1[0]; del Delta2[0]

        t = t + dt

    ax_1.plot(T, X1)
    ax_2.plot(T, Y2)
    ax_3.plot(T, X2)
    ax_4.plot(T, Y2)
    ax_5.plot(T, X3)
    ax_6.plot(T, Y3)

    plt.figure("FitzHugh-Nagumo")
    plt.plot(X1, Y1, label = 'Y1(X1)')
    plt.plot(X2, Y2, label = 'Y2(X2)')
    plt.plot(X3, Y3, label = 'Y3(X3)')
    plt.xlabel("X1, X2, X3")
    plt.ylabel("Y2, Y2, Y3")
    plt.legend()

    plt.figure("Delta1, Delta2")
    plt.plot(Delta1, Delta2)
    plt.xlabel("Delta1")
    plt.ylabel("Delta2")
    plt.show()

    #File = open("Logs.txt", 'w')

    # подстановка в x'
    # File.write('Система: ' + '\n' + '\n'
    #             + 'eps * x`1 = x1 - 1/3 * x1^3 + y1 + k * (x2 + x3 - 2 * x1)' + '\n'
    #             + 'y`1 = -x1' + '\n'
    #             + 'eps * x`2 = x2 - 1/3 * x2^3 + y2 + k * (x1 + x3 - 2 * x2)' + '\n'
    #             + 'y`2 = -x2' + '\n'
    #             + 'eps * x`3 = x3 - 1/3 * x3^3 + y3 + k * (x2 + x1 - 2 * x3)' + '\n'
    #             + 'y`3 = -x3' + '\n' + '\n')

    # подстановка в y'
    # File.write('Система: ' + '\n' + '\n'
    #             + 'eps * x`1 = x1 - 1/3 * x1^3 + y1' + '\n'
    #             + 'y`1 = -x1 + k * (y2 + y3 - 2 * y1)' + '\n'
    #             + 'eps * x`2 = x2 - 1/3 * x2^3 + y2' + '\n'
    #             + 'y`2 = -x2 + k * (y1 + y3 - 2 * y2)' + '\n'
    #             + 'eps * x`3 = x3 - 1/3 * x3^3 + y3' + '\n'
    #             + 'y`3 = -x3 + k * (y2 + y1 - 2 * y3)' + '\n' + '\n')
    # File.write('Начальные условия: X1_0 = ' + str(x1_0) + ', Y1_0 = ' + str(y1_0) + ', X2_0 = ' + str(x2_0) + ', Y2_0 = ' + str(y2_0) + ', X3_0 = ' + str(x3_0) + ', Y3_0 = ' + str(y3_0) + ', k = ' + str(k) + ', dt = ' + str(dt) + ', TF = ' + str(TF) + ', eps = ' + str(eps) + '\n' + '\n')
    # for i in range(0, len(T) - 1):
    #     #Вывод без округления 
    #     File.write('t = ' + str(T[i]) + ', (X1, Y1) = (' + str(X1[i]) + ',' + str(Y1[i]) + ')' + ', (X2, Y2) = (' + str(X2[i]) + ',' + str(Y2[i]) + ')' + ', (X3, Y3) = (' + str(X3[i]) + ',' + str(Y3[i]) + ')' + 
    #                 ', Fi1 = ' + str(Fi1[i]) + ', Fi2 = ' + str(Fi2[i]) + ', Fi3 = ' + str(Fi3[i]) + ', Delta1 = ' + str(Delta1[i]) + ', Delta2 = ' + str(Delta2[i]) + '\n')
    #     #Вывод с округлением 
    #     #File.write('t = ' + str('%.3f' % T[i]) + ', (X1, Y1) = (' + str('%.3f' % X1[i]) + ',' + str('%.3f' % Y1[i]) + ')' + ', (X2, Y2) = (' + str('%.3f' % X2[i]) + ',' + str('%.3f' % Y2[i]) + ')' + ', (X3, Y3) = (' + str('%.3f' % X3[i]) + ',' + str('%.3f' % Y3[i]) + ')' + 
    #     #            ', Fi1 = ' + str('%.3f' % Fi1[i]) + ', Fi2 = ' + str('%.3f' % Fi2[i]) + ', Fi3 = ' + str('%.3f' % Fi3[i]) + ', Delta1 = ' + str('%.3f' % Delta1[i]) + ', Delta2 = ' + str('%.3f' % Delta2[i]) + '\n')
    # File.close()
    return

def funcX1(t, x1, y1, x2, y2, x3, y3, k, eps):
    #return (x1 - (1 / 3) * x1 ** 3 + y1 + k * (x2 + x3 - 2 * x1)) / eps # подстановка в x'
    return x1 - (1 / 3) * (x1 ** 3) + y1

def funcY1(t, x1, y1, x2, y2, x3, y3, k):
    #return -x3
    return -x1 + k * (y2 + y3 - 2 * y1)

def funcX2(t, x1, y1, x2, y2, x3, y3, k, eps):
    #return (x2 - (1 / 3) * x2 ** 3 + y2 + k * (x1 + x3 - 2 * x2)) / eps # подстановка в x'
    return x2 - (1 / 3) * (x2 ** 3) + y2

def funcY2(t, x1, y1, x2, y2, x3, y3, k):
    #return -x2
    return -x2 + k * (y1 + y3 - 2 * y2)
 
def funcX3(t, x1, y1, x2, y2, x3, y3, k, eps):
    #return (x3 - (1 / 3) * x3 ** 3 + y3 + k * (x2 + x1 - 2 * x3)) / eps # подстановка в x'
    return x3 - (1 / 3) * (x3 ** 3) + y3

def funcY3(t, x1, y1, x2, y2, x3, y3, k):
    #return -x3
    return -x3 + k * (y2 + y1 - 2 * y3) # подстановка в y'

def main():
    k = float(input("Введите значение коэффициента k: "))
    eps = 0.1
    x1_0 = 0
    y1_0 = 5
    x2_0 = 5
    y2_0 = 10
    x3_0 = 5
    y3_0 = 5
    dt = 0.01 
    TF = 250
    FitzHughNagumo(x1_0, y1_0, x2_0, y2_0, x3_0, y3_0, k, dt, TF, eps)

if __name__ == "__main__":
    main()