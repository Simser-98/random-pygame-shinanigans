
def clamp_f(value, min_value, max_value):
    return max(min(value, max_value), min_value)

def clamp_vector(vector, min_value, max_value):
    return clamp_f(vector[0], min_value[0], max_value[0]), clamp_f(vector[1], min_value[1], max_value[1])
