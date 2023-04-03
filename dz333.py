result = []

def divider(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Invalid types for divider()")
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        if a < b:
            raise ValueError("a must be greater than or equal to b.")
        if b > 100:
            raise IndexError("b must be less than or equal to 100.")
    except (TypeError, ZeroDivisionError, ValueError, IndexError) as e:
        print(f"Exception raised: {type(e).__name__}")
        return None
    return a/b

data = {10: 2, 2: 5, "123": 4, 18: 0, (): 15, 8: 4}
for key in data:
    res = divider(key, data.get(key))
    if res is not None:
        result.append(res)

print(result)
