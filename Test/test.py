import math
from matplotlib import pyplot

class Transducer():

    def __init__(self, x, y, t_array):
        self.x = x
        self.y = y
        self.t_array = t_array
        self.signal = len(self.t_array)*[0]

class Receiver(Transducer):

     def __init__(self, x, y, t_array):
         super().__init__(x, y, t_array)

class Emitter(Transducer):

     def __init__(self, x, y, t_array):
         super().__init__(x, y, t_array)

     def generate_signal(self, f_c, n_cycles, amplitude):
         if not isinstance(f_c,float):
             raise TypeError('f_c should be float')
         if not isinstance(n_cycles,int):
             raise TypeError('n_cycle should be int')
         if not isinstance(amplitude,float):
             raise TypeError('amplitude should be float')
         interval = self.t_array[1] - self.t_array[0]
         Signal_Point = int(n_cycles / (f_c * interval))
         signal = []
         for t in self.t_array:
             if 0 <= t <= Signal_Point * interval:
                 signal.append(amplitude * math.sin(2 * math.pi * f_c * t))
             else:
                signal.append(0.0)

         self.signal = signal

         return signal



t_delta = 0.1e-6
t_N = 800
t_array = [t_i * t_delta for t_i in range(t_N)]

receiver_positions = [[receiver_x / 1000.0, 0.04] for receiver_x in range(-40, 41, 2)]
emitters = [Emitter(0, 0, t_array)]
signal = emitters[0].generate_signal(1e6, 5, 1.0)

fig, axs = pyplot.subplots(1)
axs.plot(t_array, signal)
axs.set_xlabel('time (seconds)')
axs.set_ylabel('amplitude')