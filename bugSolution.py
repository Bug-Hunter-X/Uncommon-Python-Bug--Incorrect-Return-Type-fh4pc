def function(x):
    try:
        return int(x + 1)
    except (TypeError, ValueError):
        return None  # Or raise a more specific exception

result = function(5)
print(result)

result = function("5")
print(result)