import json
import numpy as np

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (np.integer, np.int64, np.int32)):
            return int(obj)
        if isinstance(obj, (np.floating, np.float64, np.float32)):
            return float(obj)
        if isinstance(obj, np.bool_):
            return bool(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, complex):
            return {'re': obj.real, 'im': obj.imag}
        return super().default(obj)

def save_json(data, path):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2, cls=NumpyEncoder)
