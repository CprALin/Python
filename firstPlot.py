from matplotlib import pyplot as plt

plt.style.use('bmh')

dev_age_x= [25, 26, 27, 28, 29 ,30 ,32, 35] 

dev_salary_y = [38000, 39000, 46500, 47843, 51203, 54234, 60983, 70983]

plt.plot(dev_age_x, dev_salary_y, color='k', linestyle='--' ,marker='.', linewidth=3, label='All Devs')

py_dev_salary_y = [49029, 48763, 50342, 52392, 64321, 63421, 67832, 76433]

plt.plot(dev_age_x, py_dev_salary_y, color='b', marker='o', linewidth=3 , label= 'Python')

js_dev_salary_y = [23456, 26790, 30000, 34567, 36982, 38978, 40000, 45679]

plt.plot(dev_age_x, js_dev_salary_y, color='g',marker='.', linewidth=3, label='JavaScript')


plt.grid(True)
plt.tight_layout()

plt.title('Median Salary (usd) by age')
plt.xlabel('Ages')
plt.ylabel('Salary')

plt.legend()

#plt.savefig('plot.png')

plt.show()