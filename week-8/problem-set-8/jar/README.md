# Cookie Jar

## Overview

This Python class simulates a cookie jar, allowing users to deposit and withdraw cookies while enforcing capacity limits. It provides a visual representation of the cookies using emojis and includes error handling for various scenarios.

## Features

- **Capacity Control**: Set a maximum capacity for the jar.
- **Deposit & Withdraw**: Add or remove cookies with checks for valid operations.
- **Visual Representation**: Displays the current cookies in the jar using emojis.

## How to Use

1. Include the `Jar` class in your Python project:

   ```python
   class Jar:
       def __init__(self, capacity=12):
           # Implementation here
   ```

2. Create an instance of the jar and use its methods:

   ```python
   jar = Jar()  # Create a cookie jar
   jar.deposit(5)  # Deposit cookies
   print(jar)  # Output: 🍪🍪🍪🍪🍪
   ```

3. Withdraw cookies and see the updated state:

   ```python
   jar.withdraw(2)  # Withdraw cookies
   print(jar)  # Output: 🍪🍪🍪
   ```

### Example

```python
jar = Jar()
jar.deposit(5)
print(jar)  # Output: 🍪🍪🍪🍪🍪

jar.withdraw(2)
print(jar)  # Output: 🍪🍪🍪
```

```python
jar.withdraw(10)  # Raises ValueError: Jar is empty
```

This will raise an error due to insufficient cookies in the jar.

## License

This project is licensed under the MIT License.