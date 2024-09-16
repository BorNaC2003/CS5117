import numpy as np
import matplotlib.pyplot as plt

def x(t):
    return 9 * np.cos(200 * np.pi * t + 0.4 * np.pi)


t_start, t_end = -0.02, 0.02

t_continuous = np.linspace(t_start, t_end, 10000)
x_continuous = x(t_continuous)

Ts_values = [0.0075, 0.005, 0.0005]

fig, axs = plt.subplots(3, 1, figsize=(10, 15))
fig.suptitle('Sampled Sinusoidal Signal: x(t) = 9cos(200πt + 0.4π)')

for i, Ts in enumerate(Ts_values):
    t_sampled = np.arange(t_start, t_end + Ts, Ts)
    x_sampled = x(t_sampled)
    
    axs[i].plot(t_continuous, x_continuous, 'b-', label='Continuous')
    axs[i].stem(t_sampled, x_sampled, 'r', label='Sampled', linefmt='r-', markerfmt='ro', basefmt=' ')
    
    axs[i].set_xlim(t_start, t_end)
    axs[i].set_ylim(-10, 10)
    axs[i].set_xlabel('Time (s)')
    axs[i].set_ylabel('Amplitude')
    axs[i].set_title(f'Sampling Interval Ts = {Ts} s')
    axs[i].legend()
    axs[i].grid(True)

plt.tight_layout()
plt.savefig('sampled_sinusoidal_signal.png', dpi=300, bbox_inches='tight')
plt.show()