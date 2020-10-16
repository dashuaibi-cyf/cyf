import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t)

def g(t):
    return np.exp(t)

def h(t):
    return np.exp(0*t)

def x(t):
    return np.sin(t+1)
def n(t):
    return np.exp(0.05*t)*np.sin(t)
def s(t):
    return np.exp(0.05*-t)*np.sin(t)

t1 = np.arange(-5.0, 5.0, 0.1)
t2 = np.arange(-5.0, 5.0, 0.1)
t3 = np.arange(-1000,1000,1)

plt.figure(2)           
plt.subplot(221)      

plt.plot(t1, f(t1), '-b',label='X(t)=e^-t')
plt.plot(t2, g(t2), '-r',label='X(t)=e^t')
plt.plot(t2, h(t2), 'g-',label='X(t)=e^0=1')
plt.legend(loc='best')
plt.xlim((-5, 5))
plt.ylim((-1,10))
plt.xlabel('t/s')
plt.ylabel('X(t)')
ax = plt.gca()                                            
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')         
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')          
ax.spines['bottom'].set_position(('data', 0))   
ax.spines['left'].set_position(('data', 0))
plt.title("e^-t,e^t,e^0=1")

plt.subplot(222)      

ax = plt.gca()

plt.plot(t2, x(t2), 'r-')

plt.xlim((-5, 5))
plt.ylim((-2, 2))

plt.xlabel('t/s')
plt.ylabel('X(t)')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')        
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')          
ax.spines['bottom'].set_position(('data', 0))   
ax.spines['left'].set_position(('data', 0))
plt.title("sin(x+1)")

plt.subplot(223)      

ax = plt.gca()
plt.plot(t3, n(t3), 'g-')

plt.xlim((-10, 100))
plt.ylim((-50, 50))

plt.xlabel('t/s')
plt.ylabel('X(t)')
#设置坐标轴刻度
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')          # 指定下边的边作为 x 轴   指定左边的边为 y 轴
ax.spines['bottom'].set_position(('data', 0))   #指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))
plt.title("e^(-0.05t)*sin(X)")



plt.subplot(224)      # 2 rows, 1 column, 2ndplot

ax = plt.gca()
plt.plot(t3, s(t3), 'g-')
#设置坐标轴范围
plt.xlim((-100, 10))
plt.ylim((-50, 50))
#设置坐标轴名称
plt.xlabel('t/s')
plt.ylabel('X(t)')
#设置坐标轴刻度
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')          # 指定下边的边作为 x 轴   指定左边的边为 y 轴
ax.spines['bottom'].set_position(('data', 0))   #指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))
plt.title("e^(-0.05t)*sin(X)")
plt.show()
