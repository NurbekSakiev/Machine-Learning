import numpy as np


class Filter:

    moving_average_array = np.array([])      # Array containing the moving average

    def __init__(self):
        """ Initializer. """

        self.mov_aver_array = np.array([])

    def moving_average(self, val, size=5):
        # Calculates the moving average of the input value.
        

        # initializing the static array
        if len(self.mov_aver_array) == 0:
            self.mov_aver_array = np.full(size, val)

        self.mov_aver_array = np.append(self.mov_aver_array, val)
        window = np.ones(size) / float(size)

        # delete old data if array size is greater than window size
        if len(self.mov_aver_array) > size:
            self.mov_aver_array = np.delete(self.mov_aver_array, 0)

        filtered_values = np.convolve(self.mov_aver_array, window, mode='valid')

        return filtered_values[-1]

    def reset_moving_average(self):
        """ Resets the moving average filter. """

        self.mov_aver_array = np.array([])