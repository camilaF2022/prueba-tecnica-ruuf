# def calculate_panels(base: float, height: float, a: float, b: float) -> int:
#     if base <= 0 or height <= 0:
#         return 0

#     if not ((base >= a and height >= b) or (base >= b and height >= a)):
#         return 0

#     contador_1 = 0
#     if height >= b: 
#         new_base_1 = base * (1 - b / height)   # equivalente a base - 2x
#         cantidad_1 = int(new_base_1 // a)
#         contador_1 += cantidad_1

#         if cantidad_1 > 0 and (height - b) > 0:
#             contador_1 += calculate_panels(new_base_1, height - b, a, b)

#     contador_2 = 0
#     if height >= a:
#         new_base_2 = base * (1 - a / height)
#         cantidad_2 = int(new_base_2 // b)
#         contador_2 += cantidad_2

#         if cantidad_2 > 0 and (height - a) > 0:
#             contador_2 += calculate_panels(new_base_2, height - a, a, b)

#     return max(contador_1, contador_2)

def fill_layer(base: float, height: float, a: float, b: float) -> int:
     # Validations
    if height < a:
        return 0
    x = (base * a) / (2 * height)
    new_base = base - 2 * x
    # Calculate how many rectangles fit in this layer
    count = int(new_base // b)
    if count <= 0:
        return 0

    remaining_h = height - a
    if remaining_h <= 0:
        return count

    return count + calculate_panels(new_base, remaining_h, a, b)


def calculate_panels(base: float, height: float, a: float, b: float) -> int:
    ## Validations
    if base <= 0 or height <= 0:
        return 0

    count_1 = fill_layer(base, height, a, b)

    count_2 = fill_layer(base, height, b, a)

    return max(count_1, count_2)

print(calculate_panels(50, 300, 20, 5))