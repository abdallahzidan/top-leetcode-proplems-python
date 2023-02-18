def calculate_square(number):
    if number==0:
        return 0
    else:
        digit = number%10
        return digit*digit +calculate_square(number//10)
    
def is_helper(n):
    p1= n
    p2= calculate_square(n)
    while p1 !=p2:
        p1= calculate_square(p1)
        p2= calculate_square(calculate_square(p2))
        if p1==1 or p2==1:
            return True
    return False

