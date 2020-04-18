import matplotlib.pyplot as plt
from numpy import sqrt, pi, exp, linspace


def f(x, m, s):
    return (1.0/(sqrt(2 * pi) * s)) * exp(-0.5*((x - m) / s) ** 2)


m = 0
s_min = 0.2
s_max = 2
x = linspace(m - 3 * s_max, 1000)
s_values = linspace(s_max, s_min, 30)
max_f = f(m, m, s_min)

fig = plt.figure()
y = f(x, m, s_max)
plt.axis([x[0], x[-1], -0.1, max_f])
lines = plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f')

# def init():
#    lines[0].set_data([], [])  # empty plot
##   return lines


# def frame(args):
#    frame_no, s, x, lines = args
##   y = f(x, m, s)
#    lines[0].set_data(x, y)
#    return lines


# anim = animation.FuncAnimation(
#    fig, frame, all_args, interval=150, init_func=init, blit=True)
counter = 0
for s in s_values:
    y = f(x, m, s)
    lines[0].set_ydata(y)
    plt.legend(["s={:.2f}".format(s)])
    plt.draw()
    plt.savefig('tmp_{:0>4}.png'.format(counter))
    counter += 1
# anim.save('movie1.mp4', fps=5)  # movie in MP4 format
