import matplotlib.pyplot as plt
import numpy as np
from csv import reader

# read csv file as a list of lists
from matplotlib import ticker

with open('proj2_medium.csv', 'r') as read_obj:
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

xd0 = []
xd1 = []
xd2 = []

e0 = []
e1 = []
e2 = []

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

for i in range(len(list_of_rows)):
    e0.append(x0[i] - xd0[i])
    e1.append(x1[i] - xd1[i])
    e2.append(x2[i] - xd2[i])


times = range(len(list_of_rows))

fig, ax = plt.subplots()
ax.plot(times, e0, 'b', label="err_x")
ax.plot(times, e1, 'g', label="err_y")
ax.plot(times, e2, 'r', label="err_alpha")
#ax.plot(times, xd0, 'b--', label="xd0")
#ax.plot(times, xd1, 'g--', label="xd1")
#ax.plot(times, xd2, 'r--', label="xd2")

plt.legend(loc="upper right")

ax.set(xlabel='time [step]', ylabel='value [number]', title='Proj2 error medium')
#ax.set(xlabel='time [step]', ylabel='torque [Nm]', title='Proj2 torque vs. time')

ax.grid()

# fig.savefig("test.png")
plt.show()
