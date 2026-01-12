from typing import List, Tuple, Dict
import json


# def calculate_panels(panel_width: int, panel_height: int, 
#                     roof_width: int, roof_height: int) -> int:
#     #One side first
#     count_1 = 0
#     count_2 = 0
#     if (roof_width >= panel_width and roof_height >= panel_width) or (roof_width >= panel_height and roof_height >= panel_height):
#         #Calculate the amount of panels that fit 
#         panels_1 = roof_width // panel_width
#         panels_2 = roof_height // panel_height
#         # Calculate the remainders that are left
#         remainder_1 = roof_width % panel_width
#         remainder_2 = roof_height % panel_height

#         count_1 += panels_1 * panels_2
#         # Check if there is any remainder to fit more panels
#         if not(panels_1 == 0 or panels_2 == 0):
#             if remainder_1 >= remainder_2:
#                 count_1 += calculate_panels(panel_width, panel_height, roof_height, remainder_1)
#             else:
#                 count_1 += calculate_panels(panel_width, panel_height, roof_width, remainder_2)
#         # The other side
#         panels_3 = roof_width // panel_height
#         panels_4 = roof_height // panel_width
#         remainder_3 = roof_width % panel_height
#         remainder_4 = roof_height % panel_width
#         count_2 += panels_3 * panels_4
#         if not(panels_3 == 0 or panels_4 == 0):
#             if remainder_3 >= remainder_4:
#                 count_2 += calculate_panels(panel_width, panel_height, roof_height, remainder_3)
#             else:
#                 count_2 += calculate_panels(panel_width, panel_height, roof_width, remainder_4)
#     return max(count_1, count_2)

def calculate_panels(panel_width: int, panel_height: int, 
                    roof_width: int, roof_height: int) -> int:
    if not (
        (panel_width <= roof_width and panel_height <= roof_height) or
        (panel_width <= roof_height and panel_height <= roof_width)
    ):
        return 0

    count_1 = fill_layer(
        roof_width, roof_height, panel_width, panel_height
    )

    count_2 = fill_layer(
        roof_width, roof_height, panel_height, panel_width
    )

    return max(count_1, count_2)

def fill_layer(roof_width: int, roof_height: int, panel_w: int, panel_h: int) -> int:
    panels_1 = roof_width // panel_w
    panels_2 = roof_height // panel_h
    remainder_1 = roof_width % panel_w
    remainder_2 = roof_height % panel_h

    count = panels_1 * panels_2
    if panels_1 > 0 and panels_2 > 0:
        if remainder_1 >= remainder_2:
            count += calculate_panels(panel_w, panel_h, roof_height, remainder_1)
        else:
            count += calculate_panels(panel_w, panel_h, roof_width, remainder_2)

    return count


def run_tests() -> None:
    with open('test_cases.json', 'r') as f:
        data = json.load(f)
        test_cases: List[Dict[str, int]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "expected": test["expected"]
            }
            for test in data["testCases"]
        ]
    
    print("Corriendo tests:")
    print("-------------------")
    
    for i, test in enumerate(test_cases, 1):
        result = calculate_panels(
            test["panel_w"], test["panel_h"], 
            test["roof_w"], test["roof_h"]
        )
        passed = result == test["expected"]
        
        print(f"Test {i}:")
        print(f"  Panels: {test['panel_w']}x{test['panel_h']}, "
              f"Roof: {test['roof_w']}x{test['roof_h']}")
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")


def main() -> None:
    print("🐕 Wuuf wuuf wuuf 🐕")
    print("================================\n")
    
    run_tests()


if __name__ == "__main__":
    main()