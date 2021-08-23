import numpy as np

def calculate(list_digits):

    if not len(list_digits) == 9:
        raise ValueError("List must contain nine numbers.")
    
    else:
        converted = np.array(list_digits)
        new = converted.reshape(3,3)

        calculations = {
            'mean': [np.mean(new, axis = 0).tolist(), np.mean(new, axis = 1).tolist(), np.mean(new)],
            'variance': [np.var(new, axis = 0).tolist(), np.var(new, axis = 1).tolist(), np.var(new)],
            'standard deviation': [np.std(new, axis = 0).tolist(), np.std(new, axis = 1).tolist(), np.std(new)],
            'max': [np.max(new, axis = 0).tolist(), np.max(new, axis = 1).tolist(), np.max(new)],
            'min': [np.min(new, axis = 0).tolist(), np.min(new, axis = 1).tolist(), np.min(new)],
            'sum': [np.sum(new, axis = 0).tolist(), np.sum(new, axis = 1).tolist(), np.sum(new)]
          }

    return calculations
