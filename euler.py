import numpy as np
import matplotlib.pyplot as plt


def euler_method(xmax, h):
    x = np.arange(1, xmax + h, h)
    y = [1]  # Valoarea inițială y(1) = 1
    for i in range(1, len(x)):
        y.append(y[i-1] + h * (2 * x[i-1] * y[i-1]))
    return x, y

xmax = 3.0 # x(max) = 3.0
h = 0.05 # h = 0.05
x_euler, y_euler = euler_method(xmax, h)


# Calcularea soluției exacte
x_exact = np.arange(1, xmax + h, h)
y_exact = np.exp(x_exact ** 2 - 1)

# Afișarea graficului
plt.plot(x_exact, y_exact, label='Exact Solution')
plt.plot(x_euler, y_euler, label='Euler Method')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Approximation using Euler Method')
plt.show()

def runge_kutta_method(xmax, h):
    x = np.arange(1, xmax + h, h)
    y = [1]  # Valoarea inițială y(1) = 1
    for i in range(1, len(x)):
        k1 = h * (2 * x[i-1] * y[i-1])
        k2 = h * (2 * (x[i-1] + h/2) * (y[i-1] + k1/2))
        k3 = h * (2 * (x[i-1] + h/2) * (y[i-1] + k2/2))
        k4 = h * (2 * (x[i-1] + h) * (y[i-1] + k3))
        y.append(y[i-1] + (k1 + 2*k2 + 2*k3 + k4) / 6)
    return x, y

x_rk4, y_rk4 = runge_kutta_method(xmax, h)


# Afișarea graficului
plt.plot(x_exact, y_exact, label='Exact Solution')
plt.plot(x_rk4, y_rk4, label='Runge-Kutta Method')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Approximation using Runge-Kutta Method')
plt.show()

#Compararea metodelor

    
#Grafic Comparare    
plt.plot(x_exact, y_exact, label='Exact Solution')
plt.plot(x_euler, y_euler, label='Euler Method')
plt.plot(x_rk4, y_rk4, label='Runge-Kutta Method')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Comparison of Approximation Methods')
plt.show()

#Calculare erori si afisare in consola 

error_euler = np.abs(np.array(y_euler) - np.array(y_exact))
error_rk4 = np.abs(np.array(y_rk4) - np.array(y_exact))

print("Valorile pentru metoda lui Euler:")
for i in range(len(x_euler)):
    print("x = {:.1f}, y_aprox_euler = {:.6f}, y_exact = {:.6f}, eroare_abs_euler = {:.6f}".format(x_euler[i], y_euler[i], y_exact[i], error_euler[i]))
print()

print("Valorile pentru metoda Runge-Kutta de ordinul patru:")
for i in range(len(x_rk4)):
    print("x = {:.1f}, y_aprox_rk4 = {:.6f}, y_exact = {:.6f}, eroare_abs_rk4 = {:.6f}".format(x_rk4[i], y_rk4[i], y_exact[i], error_rk4[i]))


print("Comparația soluției exacte și soluțiilor aproximate:")
for i in range(len(x_exact)):
    print("x = {:.1f}, y_exact = {:.6f}, y_aprox_euler = {:.6f}, eroare_euler = {:.6f}, y_aprox_rk4 = {:.6f}, eroare_rk4 = {:.6f}".format( x_exact[i], y_exact[i], y_euler[i], error_euler[i], y_rk4[i], error_rk4[i]))
