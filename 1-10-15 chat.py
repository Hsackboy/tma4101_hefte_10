import numpy as np
import matplotlib.pyplot as plt

# Function f(x_n, y_n)
def f_value(x_n, y_n):
    return x_n + y_n - np.log(np.abs(x_n)) - np.log(np.abs(y_n))

# Partial derivatives for symplectic Euler
def f_x(x_n):
    return 1 - 1/x_n

def f_y(y_n):
    return 1 - 1/y_n

# Symplectic Euler method implementation
def symplectic_euler(x0, y0, dt, steps):
    x_vals = [x0]
    y_vals = [y0]
    f_vals = [f_value(x0, y0)]  # Store the function values of f(x, y) over time

    x_n = x0
    y_n = y0

    for _ in range(steps):
        # Update momentum y_n first
        y_n = y_n + dt * f_x(x_n)
        
        # Then update position x_n with new y_n
        x_n = x_n + dt * f_y(y_n)
        
        # Store the new values
        x_vals.append(x_n)
        y_vals.append(y_n)
        f_vals.append(f_value(x_n, y_n))  # Calculate and store f(x_n, y_n)

    return np.array(x_vals), np.array(y_vals), np.array(f_vals)

# Initial conditions
x0 = 2
y0 = 2.0
dt = 0.01
steps = 1000

# Solve the system using Symplectic Euler
x_vals, y_vals, f_vals = symplectic_euler(x0, y0, dt, steps)

# Time array
t_vals = np.linspace(0, dt * steps, steps + 1)

# Plot f(x_n, y_n) over time
plt.plot(t_vals, f_vals, label="f(x_n, y_n) over time")
plt.xlabel('Time')
plt.ylabel('f(x_n, y_n)')
plt.title('f(x_n, y_n) vs Time using Symplectic Euler')
plt.legend()
plt.grid(True)
plt.show()
