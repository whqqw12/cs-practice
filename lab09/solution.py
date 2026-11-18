import numpy as np 

def make_hours() -> list[int]:
    arr = np.arange(0,22,3)
    return arr.tolist()
def vector_report(values: list[float]) -> dict:
    arr = np.asanyarray(values,dtype = float)
    return {
        "third" : floar(arr[2]),
        "last" : float(arr[-1]),
        "middle" : arr[2:6].tolist(),
        "every_second" : arr[::2].tolist(),
        "reversed" : arr[::-1].tolist()
    }
