import unittest
 
def fibonacci(number):
    fibonacci_numbers= [0, 1]
    total = 1
    print("number" + str(number))
    for index in range(2, number+1):
        total = fibonacci_numbers[-2] + fibonacci_numbers[-1]
        fibonacci_numbers.append(total)  
        print("fibonacci_numbers " + str(fibonacci))  
        print("total " + str(total))           
    return total


if __name__ == '__main__':
    unittest.main()
    