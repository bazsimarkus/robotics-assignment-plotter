import math

import matplotlib.pyplot as plt
import numpy as np
from csv import reader

# read csv file as a list of lists
from matplotlib import ticker

with open('proj3.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Pass reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)

print(len(list_of_rows))

q0 = []
q1 = []
q2 = []

qd0 = []
qd1 = []
qd2 = []

tau0 = []
tau1 = []
tau2 = []

x0 = []
x1 = []
x2 = []

xd0 = []
xd1 = []
xd2 = []

counter = 0

for row in list_of_rows:
    q0.append(float(row[1]))
    q1.append(float(row[2]))
    q2.append(float(row[3]))
    qd0.append(float(row[7]))
    qd1.append(float(row[8]))
    qd2.append(float(row[9]))
    tau0.append(float(row[10]))
    tau1.append(float(row[11]))
    tau2.append(float(row[12]))
    x0.append(float(row[13]))
    x1.append(float(row[14]))
    x2.append(float(row[15]))
    xd0.append(float(row[19]))
    xd1.append(float(row[20]))
    xd2.append(float(row[21]))

desired_angle_velocity = []
desired_angle = []
t_var = []
beta = []
beta_velocity = []

deg = 57.2958

x_below_zero = False;
y_below_zero = True;
offset = 0
offsets = []


for x in range(len(list_of_rows)):
    xd0[x] = xd0[x] - 0.6
    xd1[x] = xd1[x] - 0.35

    beta.append(math.atan(xd1[x] / xd0[x]))

for x in range(len(list_of_rows)):
    if x_below_zero is False and xd0[x] < 0:
        x_below_zero = True
        offset = offset + abs(beta[x] - beta[x-1])

    if x_below_zero is True and xd0[x] > 0:
        x_below_zero = False
        offset = offset + abs(beta[x] - beta[x-1])

    if y_below_zero is False and xd1[x] < 0:
        y_below_zero = True

    if y_below_zero is True and xd1[x] > 0:
        y_below_zero = False

    offsets.append(offset)
    print(offset)

for x in range(len(list_of_rows)):
    beta[x] = (beta[x] + offsets[x])*deg

for x in range(len(list_of_rows)):
    if x > 0:
        beta_velocity.append(beta[x] - beta[x-1])
    else:
        beta_velocity.append(0)


last_notzero_value = beta_velocity[0]

for x in range(len(list_of_rows)):
    if beta_velocity[x] < 0.001:
        beta_velocity[x] = last_notzero_value
    else:
        last_notzero_value = beta_velocity[x]



times = range(len(list_of_rows))

fig, ax = plt.subplots()
ax.plot(times, beta_velocity, 'b', label="angle velocity")
#ax.plot(times, x0, 'g', label="x")
#ax.plot(times, x1, 'r', label="y")

plt.legend(loc="upper left")

ax.set(xlabel='time [steps]', ylabel='angle velocity [degree/step]')
# ax.set(xlabel='time [step]', ylabel='torque [Nm]', title='Proj2 torque vs. time')

ax.grid()

# fig.savefig("test.png")
plt.show()
