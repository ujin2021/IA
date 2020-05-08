def sum_of_digit_square(args):
    args_abs = abs(args) #== args and args or abs(args)
    print("args and args or abs(args)", args and args or abs(args))
    return sum(list(map(lambda v:int(v)**2, list(str(args_abs)))))

print(sum_of_digit_square(789))