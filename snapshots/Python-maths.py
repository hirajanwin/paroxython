# ----------------------------------------------------------------------------------------
# ../Python/maths/3n+1.py
# ----------------------------------------------------------------------------------------
from typing import Tuple, List # import:typing:List, import:typing:Tuple, import_module:typing, import_name:List, import_name:Tuple
def n31(a: int) -> Tuple[List[int], int]: # function:n31 (-> +12), function_returning_something:n31 (-> +12), index
    if not isinstance(a, int): # call_argument:a, call_argument:int, function_call:isinstance, if (-> +1), if_test_id:a, if_test_id:int, if_test_id:isinstance, unary_operator:Not
        raise TypeError("Must be int, not {0}".format(type(a).__name__)) # call_argument:, call_argument:a, composition, function_call:TypeError, function_call:type, if_then_branch, literal:Str, method_call, method_call_name:format, raise:TypeError
    if a < 1: # comparison_operator:Lt, if (-> +1), if_test_id:a, int_literal, literal:Num
        raise ValueError("Given integer must be greater than 1, not {0}".format(a)) # call_argument:, call_argument:a, composition, function_call:ValueError, if_then_branch, literal:Str, method_call, method_call_name:format, raise:ValueError
    path = [a] # assignment, assignment_lhs_identifier:path, assignment_rhs_atom:a
    while a != 1: # comparison_operator:NotEq, evolve_state (-> +5), int_literal, literal:Num, while (-> +5)
        if a % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +3), if_test_id:a, int_literal, literal:Num, suggest_conditional_expression (-> +3)
            a = a // 2 # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:2, assignment_rhs_atom:a, binary_operator:FloorDiv, if_then_branch, int_literal, literal:Num, suggest_augmented_assignment, update_variable:a:2
        else:
            a = 3 * a + 1 # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:1, assignment_rhs_atom:3, assignment_rhs_atom:a, binary_operator:Add, binary_operator:Mult, if_else_branch, int_literal, literal:Num, suggest_constant_definition, update_variable:a:1, update_variable:a:3
        path += [a] # assignment_lhs_identifier:path, assignment_rhs_atom:a, augmented_assignment, update_variable:path:a
    return path, len(path) # call_argument:path, function_call:len, return
def test_n31(): # function:test_n31 (-> +113), function_returning_nothing:test_n31 (-> +113)
    assert n31(4) == ([4, 2, 1], 3) # assertion, call_argument:4, comparison_operator:Eq, function_call:n31, int_literal, literal:List, literal:Num, literal:Tuple, suggest_constant_definition
    assert n31(11) == ([11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], 15) # assertion, call_argument:11, comparison_operator:Eq, function_call:n31, int_literal, literal:List, literal:Num, literal:Tuple, suggest_constant_definition
    assert n31(31) == ( # assertion, call_argument:31, function_call:n31, int_literal, literal:Num, suggest_constant_definition
        [ # comparison_operator:Eq, literal:List, literal:Tuple
            31, # int_literal, literal:Num, suggest_constant_definition
            94, # int_literal, literal:Num, suggest_constant_definition
            47, # int_literal, literal:Num, suggest_constant_definition
            142, # int_literal, literal:Num, suggest_constant_definition
            71, # int_literal, literal:Num, suggest_constant_definition
            214, # int_literal, literal:Num, suggest_constant_definition
            107, # int_literal, literal:Num, suggest_constant_definition
            322, # int_literal, literal:Num, suggest_constant_definition
            161, # int_literal, literal:Num, suggest_constant_definition
            484, # int_literal, literal:Num, suggest_constant_definition
            242, # int_literal, literal:Num, suggest_constant_definition
            121, # int_literal, literal:Num, suggest_constant_definition
            364, # int_literal, literal:Num, suggest_constant_definition
            182, # int_literal, literal:Num, suggest_constant_definition
            91, # int_literal, literal:Num, suggest_constant_definition
            274, # int_literal, literal:Num, suggest_constant_definition
            137, # int_literal, literal:Num, suggest_constant_definition
            412, # int_literal, literal:Num, suggest_constant_definition
            206, # int_literal, literal:Num, suggest_constant_definition
            103, # int_literal, literal:Num, suggest_constant_definition
            310, # int_literal, literal:Num, suggest_constant_definition
            155, # int_literal, literal:Num, suggest_constant_definition
            466, # int_literal, literal:Num, suggest_constant_definition
            233, # int_literal, literal:Num, suggest_constant_definition
            700, # int_literal, literal:Num, suggest_constant_definition
            350, # int_literal, literal:Num, suggest_constant_definition
            175, # int_literal, literal:Num, suggest_constant_definition
            526, # int_literal, literal:Num, suggest_constant_definition
            263, # int_literal, literal:Num, suggest_constant_definition
            790, # int_literal, literal:Num, suggest_constant_definition
            395, # int_literal, literal:Num, suggest_constant_definition
            1186, # int_literal, literal:Num, suggest_constant_definition
            593, # int_literal, literal:Num, suggest_constant_definition
            1780, # int_literal, literal:Num, suggest_constant_definition
            890, # int_literal, literal:Num, suggest_constant_definition
            445, # int_literal, literal:Num, suggest_constant_definition
            1336, # int_literal, literal:Num, suggest_constant_definition
            668, # int_literal, literal:Num, suggest_constant_definition
            334, # int_literal, literal:Num, suggest_constant_definition
            167, # int_literal, literal:Num, suggest_constant_definition
            502, # int_literal, literal:Num, suggest_constant_definition
            251, # int_literal, literal:Num, suggest_constant_definition
            754, # int_literal, literal:Num, suggest_constant_definition
            377, # int_literal, literal:Num, suggest_constant_definition
            1132, # int_literal, literal:Num, suggest_constant_definition
            566, # int_literal, literal:Num, suggest_constant_definition
            283, # int_literal, literal:Num, suggest_constant_definition
            850, # int_literal, literal:Num, suggest_constant_definition
            425, # int_literal, literal:Num, suggest_constant_definition
            1276, # int_literal, literal:Num, suggest_constant_definition
            638, # int_literal, literal:Num, suggest_constant_definition
            319, # int_literal, literal:Num, suggest_constant_definition
            958, # int_literal, literal:Num, suggest_constant_definition
            479, # int_literal, literal:Num, suggest_constant_definition
            1438, # int_literal, literal:Num, suggest_constant_definition
            719, # int_literal, literal:Num, suggest_constant_definition
            2158, # int_literal, literal:Num, suggest_constant_definition
            1079, # int_literal, literal:Num, suggest_constant_definition
            3238, # int_literal, literal:Num, suggest_constant_definition
            1619, # int_literal, literal:Num, suggest_constant_definition
            4858, # int_literal, literal:Num, suggest_constant_definition
            2429, # int_literal, literal:Num, suggest_constant_definition
            7288, # int_literal, literal:Num, suggest_constant_definition
            3644, # int_literal, literal:Num, suggest_constant_definition
            1822, # int_literal, literal:Num, suggest_constant_definition
            911, # int_literal, literal:Num, suggest_constant_definition
            2734, # int_literal, literal:Num, suggest_constant_definition
            1367, # int_literal, literal:Num, suggest_constant_definition
            4102, # int_literal, literal:Num, suggest_constant_definition
            2051, # int_literal, literal:Num, suggest_constant_definition
            6154, # int_literal, literal:Num, suggest_constant_definition
            3077, # int_literal, literal:Num, suggest_constant_definition
            9232, # int_literal, literal:Num, suggest_constant_definition
            4616, # int_literal, literal:Num, suggest_constant_definition
            2308, # int_literal, literal:Num, suggest_constant_definition
            1154, # int_literal, literal:Num, suggest_constant_definition
            577, # int_literal, literal:Num, suggest_constant_definition
            1732, # int_literal, literal:Num, suggest_constant_definition
            866, # int_literal, literal:Num, suggest_constant_definition
            433, # int_literal, literal:Num, suggest_constant_definition
            1300, # int_literal, literal:Num, suggest_constant_definition
            650, # int_literal, literal:Num, suggest_constant_definition
            325, # int_literal, literal:Num, suggest_constant_definition
            976, # int_literal, literal:Num, suggest_constant_definition
            488, # int_literal, literal:Num, suggest_constant_definition
            244, # int_literal, literal:Num, suggest_constant_definition
            122, # int_literal, literal:Num, suggest_constant_definition
            61, # int_literal, literal:Num, suggest_constant_definition
            184, # int_literal, literal:Num, suggest_constant_definition
            92, # int_literal, literal:Num, suggest_constant_definition
            46, # int_literal, literal:Num, suggest_constant_definition
            23, # int_literal, literal:Num, suggest_constant_definition
            70, # int_literal, literal:Num, suggest_constant_definition
            35, # int_literal, literal:Num, suggest_constant_definition
            106, # int_literal, literal:Num, suggest_constant_definition
            53, # int_literal, literal:Num, suggest_constant_definition
            160, # int_literal, literal:Num, suggest_constant_definition
            80, # int_literal, literal:Num, suggest_constant_definition
            40, # int_literal, literal:Num, suggest_constant_definition
            20, # int_literal, literal:Num, suggest_constant_definition
            10, # int_literal, literal:Num, suggest_constant_definition
            5, # int_literal, literal:Num, suggest_constant_definition
            16, # int_literal, literal:Num, suggest_constant_definition
            8, # int_literal, literal:Num, suggest_constant_definition
            4, # int_literal, literal:Num, suggest_constant_definition
            2, # int_literal, literal:Num
            1, # int_literal, literal:Num
        ],
        107, # int_literal, literal:Num, suggest_constant_definition
    )

# ----------------------------------------------------------------------------------------
# ../Python/maths/abs.py
# ----------------------------------------------------------------------------------------
def abs_val(num): # function:abs_val (-> +1), function_returning_something:abs_val (-> +1)
    return -num if num < 0 else num # comparison_operator:Lt, conditional_expression, int_literal, literal:Num, return, unary_operator:USub
def test_abs_val(): # function:test_abs_val (-> +3), function_returning_nothing:test_abs_val (-> +3)
    assert 0 == abs_val(0) # assertion, call_argument:0, comparison_operator:Eq, function_call:abs_val, int_literal, literal:Num
    assert 34 == abs_val(34) # assertion, call_argument:34, comparison_operator:Eq, function_call:abs_val, int_literal, literal:Num, suggest_constant_definition
    assert 100000000000 == abs_val(-100000000000) # assertion, call_argument:-100000000000, comparison_operator:Eq, function_call:abs_val, int_literal, literal:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/abs_max.py
# ----------------------------------------------------------------------------------------
from typing import List # import:typing:List, import_module:typing, import_name:List
def abs_max(x: List[int]) -> int: # function:abs_max (-> +5), function_returning_something:abs_max (-> +5), index
    j = x[0] # assignment, assignment_lhs_identifier:j, assignment_rhs_atom:0, assignment_rhs_atom:x, index, int_literal, literal:Num
    for i in x: # find_best_element (-> +2), for:i (-> +2), for_each (-> +2)
        if abs(i) > abs(j): # call_argument:i, call_argument:j, comparison_operator:Gt, function_call:abs, if (-> +1), if_test_id:abs, if_test_id:i, if_test_id:j
            j = i # assignment, assignment_lhs_identifier:j, assignment_rhs_atom:i, if_then_branch
    return j # return:j
def abs_max_sort(x): # function:abs_max_sort (-> +1), function_returning_something:abs_max_sort (-> +1)
    return sorted(x, key=abs)[-1] # call_argument:x, function_call:sorted, index, int_literal, literal:Num, negative_index:-1, return
def main(): # function:main (-> +3), function_returning_nothing:main (-> +3)
    a = [1, 2, -11] # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:-11, assignment_rhs_atom:1, assignment_rhs_atom:2, int_literal, literal:List, literal:Num, suggest_constant_definition
    assert abs_max(a) == -11 # assertion, call_argument:a, comparison_operator:Eq, function_call:abs_max, int_literal, literal:Num, suggest_constant_definition
    assert abs_max_sort(a) == -11 # assertion, call_argument:a, comparison_operator:Eq, function_call:abs_max_sort, int_literal, literal:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/abs_min.py
# ----------------------------------------------------------------------------------------
from .abs import abs_val # import:abs:abs_val, import_module:abs, import_name:abs_val
def absMin(x): # function:absMin (-> +5), function_returning_something:absMin (-> +5)
    j = x[0] # assignment, assignment_lhs_identifier:j, assignment_rhs_atom:0, assignment_rhs_atom:x, index, int_literal, literal:Num
    for i in x: # find_best_element (-> +2), for:i (-> +2), for_each (-> +2)
        if abs_val(i) < abs_val(j): # call_argument:i, call_argument:j, comparison_operator:Lt, function_call:abs_val, if (-> +1), if_test_id:abs_val, if_test_id:i, if_test_id:j
            j = i # assignment, assignment_lhs_identifier:j, assignment_rhs_atom:i, if_then_branch
    return j # return:j
def main(): # function:main (-> +2), function_returning_nothing:main (-> +2)
    a = [-3, -1, 2, -11] # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:-1, assignment_rhs_atom:-11, assignment_rhs_atom:-3, assignment_rhs_atom:2, int_literal, literal:List, literal:Num, suggest_constant_definition
    print(absMin(a)) # call_argument:, call_argument:a, composition, function_call:absMin, function_call:print

# ----------------------------------------------------------------------------------------
# ../Python/maths/average_mean.py
# ----------------------------------------------------------------------------------------
def average(nums): # function:average (-> +1), function_returning_something:average (-> +1)
    return sum(nums) / len(nums) # binary_operator:Div, call_argument:nums, function_call:len, function_call:sum, return
def test_average(): # function:test_average (-> +3), function_returning_nothing:test_average (-> +3)
    assert 12.0 == average([3, 6, 9, 12, 15, 18, 21]) # assertion, call_argument:, comparison_operator:Eq, float_literal, function_call:average, int_literal, literal:List, literal:Num, suggest_constant_definition
    assert 20 == average([5, 10, 15, 20, 25, 30, 35]) # assertion, call_argument:, comparison_operator:Eq, function_call:average, int_literal, literal:List, literal:Num, suggest_constant_definition
    assert 4.5 == average([1, 2, 3, 4, 5, 6, 7, 8]) # assertion, call_argument:, comparison_operator:Eq, float_literal, function_call:average, int_literal, literal:List, literal:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/average_median.py
# ----------------------------------------------------------------------------------------
def median(nums): # function:median (-> +10), function_returning_something:median (-> +10)
    sorted_list = sorted(nums) # assignment, assignment_lhs_identifier:sorted_list, assignment_rhs_atom:nums, call_argument:nums, function_call:sorted
    med = None # assignment, assignment_lhs_identifier:med, assignment_rhs_atom:None, literal:None
    if len(sorted_list) % 2 == 0: # binary_operator:Mod, call_argument:sorted_list, comparison_operator:Eq, divisibility_test:2, function_call:len, if (-> +6), if_test_id:len, if_test_id:sorted_list, int_literal, literal:Num
        mid_index_1 = len(sorted_list) // 2 # assignment, assignment_lhs_identifier:mid_index_1, assignment_rhs_atom:2, assignment_rhs_atom:sorted_list, binary_operator:FloorDiv, call_argument:sorted_list, function_call:len, if_then_branch (-> +2), int_literal, literal:Num
        mid_index_2 = (len(sorted_list) // 2) - 1 # assignment, assignment_lhs_identifier:mid_index_2, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:sorted_list, binary_operator:FloorDiv, binary_operator:Sub, call_argument:sorted_list, function_call:len, int_literal, literal:Num
        med = (sorted_list[mid_index_1] + sorted_list[mid_index_2]) / float(2) # assignment, assignment_lhs_identifier:med, assignment_rhs_atom:2, assignment_rhs_atom:mid_index_1, assignment_rhs_atom:mid_index_2, assignment_rhs_atom:sorted_list, binary_operator:Add, binary_operator:Div, call_argument:2, function_call:float, index, int_literal, literal:Num
    else:
        mid_index = (len(sorted_list) - 1) // 2 # assignment, assignment_lhs_identifier:mid_index, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:sorted_list, binary_operator:FloorDiv, binary_operator:Sub, call_argument:sorted_list, function_call:len, if_else_branch (-> +1), int_literal, literal:Num
        med = sorted_list[mid_index] # assignment, assignment_lhs_identifier:med, assignment_rhs_atom:mid_index, assignment_rhs_atom:sorted_list, index
    return med # return:med
def main(): # function:main (-> +4), function_returning_nothing:main (-> +4)
    print("Odd number of numbers:") # call_argument:, function_call:print, literal:Str
    print(median([2, 4, 6, 8, 20, 50, 70])) # call_argument:, composition, function_call:median, function_call:print, int_literal, literal:List, literal:Num, suggest_constant_definition
    print("Even number of numbers:") # call_argument:, function_call:print, literal:Str
    print(median([2, 4, 6, 8, 20, 50])) # call_argument:, composition, function_call:median, function_call:print, int_literal, literal:List, literal:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/average_mode.py
# ----------------------------------------------------------------------------------------
import statistics # import:statistics, import_module:statistics
def mode(input_list): # function:mode (-> +7), function_returning_something:mode (-> +7)
    check_list = input_list.copy() # assignment, assignment_lhs_identifier:check_list, assignment_rhs_atom:input_list, method_call, method_call_name:copy
    result = list() # assignment, assignment_lhs_identifier:result, function_call:list
    for x in input_list: # accumulate_elements:result (-> +4), for:x (-> +4), for_each (-> +4)
        result.append(input_list.count(x)) # call_argument:, call_argument:x, composition, method_call, method_call_name:append, method_call_name:count, method_call_object:result, update_variable:result:, update_variable:result:x
        input_list.remove(x) # call_argument:x, method_call, method_call_name:remove, method_call_object:input_list
        y = max(result) # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:result, call_argument:result, function_call:max
        return check_list[result.index(y)] # call_argument:y, index, method_call, method_call_name:index, method_call_object:result, return

# ----------------------------------------------------------------------------------------
# ../Python/maths/basic_maths.py
# ----------------------------------------------------------------------------------------
import math # import:math, import_module:math
def prime_factors(n: int) -> list: # function:prime_factors (-> +11), function_returning_something:prime_factors (-> +11)
    pf = [] # assignment, assignment_lhs_identifier:pf, literal:List
    while n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, evolve_state (-> +2), int_literal, literal:Num, while (-> +2)
        pf.append(2) # call_argument:2, int_literal, literal:Num, method_call, method_call_name:append, method_call_object:pf, update_variable:pf:2
        n = int(n / 2) # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:2, assignment_rhs_atom:n, binary_operator:Div, call_argument:, function_call:int, int_literal, literal:Num, update_variable:n:2
    for i in range(3, int(math.sqrt(n)) + 1, 2): # accumulate_elements:n (-> +3), accumulate_elements:pf (-> +3), binary_operator:Add, call_argument:, call_argument:2, call_argument:3, call_argument:n, composition, for:i (-> +3), for_range:3:_:2 (-> +3), function_call:int, function_call:range, int_literal, literal:Num, method_call, method_call_name:sqrt, range:3:_:2, suggest_constant_definition
        while n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, evolve_state (-> +2), int_literal, literal:Num, while (-> +2)
            pf.append(i) # call_argument:i, method_call, method_call_name:append, method_call_object:pf, update_variable:pf:i
            n = int(n / i) # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:i, assignment_rhs_atom:n, binary_operator:Div, call_argument:, function_call:int, update_variable:n:i
    if n > 2: # comparison_operator:Gt, if (-> +1), if_test_id:n, int_literal, literal:Num
        pf.append(n) # call_argument:n, if_then_branch, method_call, method_call_name:append, method_call_object:pf, update_variable:pf:n
    return pf # return:pf
def number_of_divisors(n: int) -> int: # function:number_of_divisors (-> +13), function_returning_something:number_of_divisors (-> +13)
    div = 1 # assignment, assignment_lhs_identifier:div, assignment_rhs_atom:1, int_literal, literal:Num
    temp = 1 # assignment, assignment_lhs_identifier:temp, assignment_rhs_atom:1, int_literal, literal:Num
    while n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, evolve_state (-> +2), int_literal, literal:Num, while (-> +2)
        temp += 1 # assignment_lhs_identifier:temp, assignment_rhs_atom:1, augmented_assignment, int_literal, literal:Num, update_variable:temp:1
        n = int(n / 2) # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:2, assignment_rhs_atom:n, binary_operator:Div, call_argument:, function_call:int, int_literal, literal:Num, update_variable:n:2
    div *= temp # assignment_lhs_identifier:div, assignment_rhs_atom:temp, augmented_assignment, update_variable:div:temp
    for i in range(3, int(math.sqrt(n)) + 1, 2): # accumulate_elements:n (-> +5), binary_operator:Add, call_argument:, call_argument:2, call_argument:3, call_argument:n, composition, for:i (-> +5), for_range:3:_:2 (-> +5), function_call:int, function_call:range, int_literal, literal:Num, method_call, method_call_name:sqrt, range:3:_:2, suggest_constant_definition
        temp = 1 # assignment, assignment_lhs_identifier:temp, assignment_rhs_atom:1, int_literal, literal:Num
        while n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, int_literal, literal:Num, while (-> +2)
            temp += 1 # assignment_lhs_identifier:temp, assignment_rhs_atom:1, augmented_assignment, int_literal, literal:Num, update_variable:temp:1
            n = int(n / i) # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:i, assignment_rhs_atom:n, binary_operator:Div, call_argument:, function_call:int, update_variable:n:i
        div *= temp # assignment_lhs_identifier:div, assignment_rhs_atom:temp, augmented_assignment, update_variable:div:temp
    return div # return:div
def sum_of_divisors(n: int) -> int: # function:sum_of_divisors (-> +15), function_returning_something:sum_of_divisors (-> +15)
    s = 1 # assignment, assignment_lhs_identifier:s, assignment_rhs_atom:1, int_literal, literal:Num
    temp = 1 # assignment, assignment_lhs_identifier:temp, assignment_rhs_atom:1, int_literal, literal:Num
    while n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, evolve_state (-> +2), int_literal, literal:Num, while (-> +2)
        temp += 1 # assignment_lhs_identifier:temp, assignment_rhs_atom:1, augmented_assignment, int_literal, literal:Num, update_variable:temp:1
        n = int(n / 2) # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:2, assignment_rhs_atom:n, binary_operator:Div, call_argument:, function_call:int, int_literal, literal:Num, update_variable:n:2
    if temp > 1: # comparison_operator:Gt, if (-> +1), if_test_id:temp, int_literal, literal:Num
        s *= (2 ** temp - 1) / (2 - 1) # assignment_lhs_identifier:s, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:temp, augmented_assignment, binary_operator:Div, binary_operator:Pow, binary_operator:Sub, if_then_branch, int_literal, literal:Num, update_variable:s:1, update_variable:s:2, update_variable:s:temp
    for i in range(3, int(math.sqrt(n)) + 1, 2): # accumulate_elements:n (-> +6), accumulate_elements:s (-> +6), binary_operator:Add, call_argument:, call_argument:2, call_argument:3, call_argument:n, composition, for:i (-> +6), for_range:3:_:2 (-> +6), function_call:int, function_call:range, int_literal, literal:Num, method_call, method_call_name:sqrt, range:3:_:2, suggest_constant_definition
        temp = 1 # assignment, assignment_lhs_identifier:temp, assignment_rhs_atom:1, int_literal, literal:Num
        while n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, int_literal, literal:Num, while (-> +2)
            temp += 1 # assignment_lhs_identifier:temp, assignment_rhs_atom:1, augmented_assignment, int_literal, literal:Num, update_variable:temp:1
            n = int(n / i) # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:i, assignment_rhs_atom:n, binary_operator:Div, call_argument:, function_call:int, update_variable:n:i
        if temp > 1: # comparison_operator:Gt, if (-> +1), if_test_id:temp, int_literal, literal:Num
            s *= (i ** temp - 1) / (i - 1) # assignment_lhs_identifier:s, assignment_rhs_atom:1, assignment_rhs_atom:i, assignment_rhs_atom:temp, augmented_assignment, binary_operator:Div, binary_operator:Pow, binary_operator:Sub, if_then_branch, int_literal, literal:Num, update_variable:s:1, update_variable:s:i, update_variable:s:temp
    return int(s) # call_argument:s, function_call:int, function_tail_call:int, return
def euler_phi(n: int) -> int: # function:euler_phi (-> +4), function_returning_something:euler_phi (-> +4)
    s = n # assignment, assignment_lhs_identifier:s, assignment_rhs_atom:n
    for x in set(prime_factors(n)): # accumulate_elements:s (-> +1), call_argument:, call_argument:n, composition, for:x (-> +1), function_call:prime_factors, function_call:set
        s *= (x - 1) / x # assignment_lhs_identifier:s, assignment_rhs_atom:1, assignment_rhs_atom:x, augmented_assignment, binary_operator:Div, binary_operator:Sub, int_literal, literal:Num, update_variable:s:1, update_variable:s:x
    return int(s) # call_argument:s, function_call:int, function_tail_call:int, return

# ----------------------------------------------------------------------------------------
# ../Python/maths/binary_exponentiation.py
# ----------------------------------------------------------------------------------------
def binary_exponentiation(a, n): # body_recursive_function:binary_exponentiation (-> +7), function:binary_exponentiation (-> +7), function_returning_something:binary_exponentiation (-> +7), recursive_function:binary_exponentiation (-> +7)
    if n == 0: # comparison_operator:Eq, if (-> +6), if_test_id:n, int_literal, literal:Num
        return 1 # if_then_branch, int_literal, literal:Num, return:1
    elif n % 2 == 1: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +4), if_test_id:n, int_literal, literal:Num
        return binary_exponentiation(a, n - 1) * a # binary_operator:Mult, binary_operator:Sub, call_argument:, call_argument:a, function_call:binary_exponentiation, if_elif_branch, int_literal, literal:Num, return
    else:
        b = binary_exponentiation(a, n / 2) # assignment, assignment_lhs_identifier:b, assignment_rhs_atom:2, assignment_rhs_atom:a, assignment_rhs_atom:n, binary_operator:Div, call_argument:, call_argument:a, function_call:binary_exponentiation, if_else_branch (-> +1), int_literal, literal:Num
        return b * b # binary_operator:Mult, return

# ----------------------------------------------------------------------------------------
# ../Python/maths/binomial_coefficient.py
# ----------------------------------------------------------------------------------------
def binomial_coefficient(n, r): # function:binomial_coefficient (-> +8), function_returning_something:binomial_coefficient (-> +8)
    C = [0 for i in range(r + 1)] # assignment, assignment_lhs_identifier:C, assignment_rhs_atom:0, assignment_rhs_atom:1, assignment_rhs_atom:i, assignment_rhs_atom:r, binary_operator:Add, call_argument:, comprehension:List, comprehension_for_count:1, function_call:range, int_literal, literal:Num, range:_
    C[0] = 1 # assignment, assignment_lhs_identifier:C, assignment_rhs_atom:1, index, int_literal, literal:Num
    for i in range(1, n + 1): # binary_operator:Add, call_argument:, call_argument:1, for:i (-> +4), for_range:1:_ (-> +4), function_call:range, int_literal, literal:Num, range:1:_
        j = min(i, r) # assignment, assignment_lhs_identifier:j, assignment_rhs_atom:i, assignment_rhs_atom:r, call_argument:i, call_argument:r, function_call:min
        while j > 0: # comparison_operator:Gt, evolve_state (-> +2), int_literal, literal:Num, while (-> +2)
            C[j] += C[j - 1] # assignment_lhs_identifier:C, assignment_rhs_atom:1, assignment_rhs_atom:C, assignment_rhs_atom:j, augmented_assignment, binary_operator:Sub, index, index_arithmetic, int_literal, literal:Num, update_variable:C:1, update_variable:C:C, update_variable:C:j
            j -= 1 # assignment_lhs_identifier:j, assignment_rhs_atom:1, augmented_assignment, int_literal, literal:Num, update_variable:j:1
    return C[r] # index, return
print(binomial_coefficient(n=10, r=5)) # call_argument:, composition, function_call:binomial_coefficient, function_call:print, int_literal, literal:Num

# ----------------------------------------------------------------------------------------
# ../Python/maths/ceil.py
# ----------------------------------------------------------------------------------------
def ceil(x) -> int: # function:ceil (-> +2), function_returning_something:ceil (-> +2)
    return ( # return
        x if isinstance(x, int) or x - int(x) == 0 else int(x + 1) if x > 0 else int(x) # binary_operator:Add, binary_operator:Sub, boolean_operator:Or, call_argument:, call_argument:int, call_argument:x, comparison_operator:Eq, comparison_operator:Gt, conditional_expression, function_call:int, function_call:isinstance, int_literal, literal:Num
    )

# ----------------------------------------------------------------------------------------
# ../Python/maths/collatz_sequence.py
# ----------------------------------------------------------------------------------------
def collatz_sequence(n): # function:collatz_sequence (-> +8), function_returning_something:collatz_sequence (-> +8)
    sequence = [n] # assignment, assignment_lhs_identifier:sequence, assignment_rhs_atom:n
    while n != 1: # comparison_operator:NotEq, evolve_state (-> +5), int_literal, literal:Num, while (-> +5)
        if n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +3), if_test_id:n, int_literal, literal:Num
            n //= 2 # assignment_lhs_identifier:n, assignment_rhs_atom:2, augmented_assignment, if_then_branch, int_literal, literal:Num, update_variable:n:2
        else:
            n = 3 * n + 1 # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:1, assignment_rhs_atom:3, assignment_rhs_atom:n, binary_operator:Add, binary_operator:Mult, if_else_branch, int_literal, literal:Num, suggest_constant_definition, update_variable:n:1, update_variable:n:3
        sequence.append(n) # call_argument:n, method_call, method_call_name:append, method_call_object:sequence, update_variable:sequence:n
    return sequence # return:sequence
def main(): # function:main (-> +4), function_returning_nothing:main (-> +4)
    n = 43 # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:43, int_literal, literal:Num, suggest_constant_definition
    sequence = collatz_sequence(n) # assignment, assignment_lhs_identifier:sequence, assignment_rhs_atom:n, call_argument:n, function_call:collatz_sequence
    print(sequence) # call_argument:sequence, function_call:print
    print("collatz sequence from %d took %d steps." % (n, len(sequence))) # binary_operator:Mod, call_argument:, call_argument:sequence, composition, function_call:len, function_call:print, literal:Str

# ----------------------------------------------------------------------------------------
# ../Python/maths/explicit_euler.py
# ----------------------------------------------------------------------------------------
import numpy as np # import:numpy, import_module:numpy
def explicit_euler(ode_func, y0, x0, stepsize, x_end): # function:explicit_euler (-> +8), function_returning_something:explicit_euler (-> +8)
    N = int(np.ceil((x_end - x0) / stepsize)) # assignment, assignment_lhs_identifier:N, assignment_rhs_atom:np, assignment_rhs_atom:stepsize, assignment_rhs_atom:x0, assignment_rhs_atom:x_end, binary_operator:Div, binary_operator:Sub, call_argument:, composition, function_call:int, method_call, method_call_name:ceil
    y = np.zeros((N + 1,)) # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:1, assignment_rhs_atom:N, assignment_rhs_atom:np, binary_operator:Add, call_argument:, int_literal, literal:Num, method_call, method_call_name:zeros
    y[0] = y0 # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:y0, index, int_literal, literal:Num
    x = x0 # assignment, assignment_lhs_identifier:x, assignment_rhs_atom:x0
    for k in range(N): # accumulate_elements:y (-> +2), call_argument:N, for:k (-> +2), for_range:N (-> +2), function_call:range, range:N
        y[k + 1] = y[k] + stepsize * ode_func(x, y[k]) # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:k, assignment_rhs_atom:stepsize, assignment_rhs_atom:x, assignment_rhs_atom:y, binary_operator:Add, binary_operator:Mult, call_argument:, call_argument:x, function_call:ode_func, index, index_arithmetic, int_literal, literal:Num, update_variable:y:k, update_variable:y:stepsize, update_variable:y:x
        x += stepsize # assignment_lhs_identifier:x, assignment_rhs_atom:stepsize, augmented_assignment, update_variable:x:stepsize
    return y # return:y

# ----------------------------------------------------------------------------------------
# ../Python/maths/extended_euclidean_algorithm.py
# ----------------------------------------------------------------------------------------
import sys # import:sys, import_module:sys
def extended_euclidean_algorithm(m, n): # function:extended_euclidean_algorithm (-> +31), function_returning_something:extended_euclidean_algorithm (-> +31)
    a = 0 # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:0, int_literal, literal:Num
    a_prime = 1 # assignment, assignment_lhs_identifier:a_prime, assignment_rhs_atom:1, int_literal, literal:Num
    b = 1 # assignment, assignment_lhs_identifier:b, assignment_rhs_atom:1, int_literal, literal:Num
    b_prime = 0 # assignment, assignment_lhs_identifier:b_prime, assignment_rhs_atom:0, int_literal, literal:Num
    q = 0 # assignment, assignment_lhs_identifier:q, assignment_rhs_atom:0, int_literal, literal:Num
    r = 0 # assignment, assignment_lhs_identifier:r, assignment_rhs_atom:0, int_literal, literal:Num
    if m > n: # comparison_operator:Gt, if (-> +5), if_test_id:m, if_test_id:n
        c = m # assignment, assignment_lhs_identifier:c, assignment_rhs_atom:m, if_then_branch (-> +1)
        d = n # assignment, assignment_lhs_identifier:d, assignment_rhs_atom:n
    else:
        c = n # assignment, assignment_lhs_identifier:c, assignment_rhs_atom:n, if_else_branch (-> +1)
        d = m # assignment, assignment_lhs_identifier:d, assignment_rhs_atom:m
    while True: # literal:True, while (-> +12)
        q = int(c / d) # assignment, assignment_lhs_identifier:q, assignment_rhs_atom:c, assignment_rhs_atom:d, binary_operator:Div, call_argument:, function_call:int
        r = c % d # assignment, assignment_lhs_identifier:r, assignment_rhs_atom:c, assignment_rhs_atom:d, binary_operator:Mod
        if r == 0: # comparison_operator:Eq, if (-> +1), if_test_id:r, int_literal, literal:Num
            break # if_then_branch
        c = d # assignment, assignment_lhs_identifier:c, assignment_rhs_atom:d
        d = r # assignment, assignment_lhs_identifier:d, assignment_rhs_atom:r
        t = a_prime # assignment, assignment_lhs_identifier:t, assignment_rhs_atom:a_prime
        a_prime = a # assignment, assignment_lhs_identifier:a_prime, assignment_rhs_atom:a
        a = t - q * a # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:a, assignment_rhs_atom:q, assignment_rhs_atom:t, binary_operator:Mult, binary_operator:Sub, update_variable:a:q, update_variable:a:t
        t = b_prime # assignment, assignment_lhs_identifier:t, assignment_rhs_atom:b_prime
        b_prime = b # assignment, assignment_lhs_identifier:b_prime, assignment_rhs_atom:b
        b = t - q * b # assignment, assignment_lhs_identifier:b, assignment_rhs_atom:b, assignment_rhs_atom:q, assignment_rhs_atom:t, binary_operator:Mult, binary_operator:Sub, update_variable:b:q, update_variable:b:t
    pair = None # assignment, assignment_lhs_identifier:pair, assignment_rhs_atom:None, literal:None
    if m > n: # comparison_operator:Gt, if (-> +3), if_test_id:m, if_test_id:n, suggest_conditional_expression (-> +3)
        pair = (a, b) # assignment, assignment_lhs_identifier:pair, assignment_rhs_atom:a, assignment_rhs_atom:b, if_then_branch
    else:
        pair = (b, a) # assignment, assignment_lhs_identifier:pair, assignment_rhs_atom:a, assignment_rhs_atom:b, if_else_branch
    return pair # return:pair
def main(): # function:main (-> +6), function_returning_nothing:main (-> +6)
    if len(sys.argv) < 3: # call_argument:, comparison_operator:Lt, function_call:len, if (-> +2), if_test_id:len, if_test_id:sys, int_literal, literal:Num, suggest_constant_definition
        print("2 integer arguments required") # call_argument:, function_call:print, if_then_branch (-> +1), literal:Str
        exit(1) # call_argument:1, function_call:exit, int_literal, literal:Num
    m = int(sys.argv[1]) # assignment, assignment_lhs_identifier:m, assignment_rhs_atom:1, assignment_rhs_atom:sys, call_argument:, function_call:int, index, int_literal, literal:Num
    n = int(sys.argv[2]) # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:2, assignment_rhs_atom:sys, call_argument:, function_call:int, index, int_literal, literal:Num
    print(extended_euclidean_algorithm(m, n)) # call_argument:, call_argument:m, call_argument:n, composition, function_call:extended_euclidean_algorithm, function_call:print

# ----------------------------------------------------------------------------------------
# ../Python/maths/factorial_python.py
# ----------------------------------------------------------------------------------------
def factorial(input_number: int) -> int: # function:factorial (-> +8), function_returning_something:factorial (-> +8)
    if input_number < 0: # comparison_operator:Lt, if (-> +1), if_test_id:input_number, int_literal, literal:Num
        raise ValueError("factorial() not defined for negative values") # call_argument:, function_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    if not isinstance(input_number, int): # call_argument:input_number, call_argument:int, function_call:isinstance, if (-> +1), if_test_id:input_number, if_test_id:int, if_test_id:isinstance, unary_operator:Not
        raise ValueError("factorial() only accepts integral values") # call_argument:, function_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    result = 1 # assignment, assignment_lhs_identifier:result, assignment_rhs_atom:1, int_literal, literal:Num
    for i in range(1, input_number): # accumulate_elements:result (-> +1), call_argument:1, call_argument:input_number, for:i (-> +1), for_range:1:input_number (-> +1), function_call:range, int_literal, literal:Num, range:1:input_number
        result = result * (i + 1) # assignment, assignment_lhs_identifier:result, assignment_rhs_atom:1, assignment_rhs_atom:i, assignment_rhs_atom:result, binary_operator:Add, binary_operator:Mult, int_literal, literal:Num, suggest_augmented_assignment, update_variable:result:1, update_variable:result:i
    return result # return:result

# ----------------------------------------------------------------------------------------
# ../Python/maths/factorial_recursive.py
# ----------------------------------------------------------------------------------------
def factorial(n: int) -> int: # body_recursive_function:factorial (-> +5), function:factorial (-> +5), function_returning_something:factorial (-> +5), recursive_function:factorial (-> +5)
    if n < 0: # comparison_operator:Lt, if (-> +1), if_test_id:n, int_literal, literal:Num
        raise ValueError("factorial() not defined for negative values") # call_argument:, function_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    if not isinstance(n, int): # call_argument:int, call_argument:n, function_call:isinstance, if (-> +1), if_test_id:int, if_test_id:isinstance, if_test_id:n, unary_operator:Not
        raise ValueError("factorial() only accepts integral values") # call_argument:, function_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    return 1 if n == 0 or n == 1 else n * factorial(n - 1) # binary_operator:Mult, binary_operator:Sub, boolean_operator:Or, call_argument:, comparison_operator:Eq, conditional_expression, function_call:factorial, int_literal, literal:Num, return

# ----------------------------------------------------------------------------------------
# ../Python/maths/factors.py
# ----------------------------------------------------------------------------------------
def factors_of_a_number(num: int) -> list: # function:factors_of_a_number (-> +1), function_returning_something:factors_of_a_number (-> +1)
    return [i for i in range(1, num + 1) if num % i == 0] # binary_operator:Add, binary_operator:Mod, call_argument:, call_argument:1, comparison_operator:Eq, comprehension:List, comprehension_for_count:1, divisibility_test, filtered_comprehension, function_call:range, int_literal, literal:Num, range:1:_, return

# ----------------------------------------------------------------------------------------
# ../Python/maths/fermat_little_theorem.py
# ----------------------------------------------------------------------------------------
def binary_exponentiation(a, n, mod): # body_recursive_function:binary_exponentiation (-> +7), function:binary_exponentiation (-> +7), function_returning_something:binary_exponentiation (-> +7), recursive_function:binary_exponentiation (-> +7)
    if n == 0: # comparison_operator:Eq, if (-> +6), if_test_id:n, int_literal, literal:Num
        return 1 # if_then_branch, int_literal, literal:Num, return:1
    elif n % 2 == 1: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +4), if_test_id:n, int_literal, literal:Num
        return (binary_exponentiation(a, n - 1, mod) * a) % mod # binary_operator:Mod, binary_operator:Mult, binary_operator:Sub, call_argument:, call_argument:a, call_argument:mod, function_call:binary_exponentiation, if_elif_branch, int_literal, literal:Num, return
    else:
        b = binary_exponentiation(a, n / 2, mod) # assignment, assignment_lhs_identifier:b, assignment_rhs_atom:2, assignment_rhs_atom:a, assignment_rhs_atom:mod, assignment_rhs_atom:n, binary_operator:Div, call_argument:, call_argument:a, call_argument:mod, function_call:binary_exponentiation, if_else_branch (-> +1), int_literal, literal:Num
        return (b * b) % mod # binary_operator:Mod, binary_operator:Mult, return
p = 701 # assignment, assignment_lhs_identifier:p, assignment_rhs_atom:701, int_literal, literal:Num, suggest_constant_definition
a = 1000000000 # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:1000000000, int_literal, literal:Num, suggest_constant_definition
b = 10 # assignment, assignment_lhs_identifier:b, assignment_rhs_atom:10, int_literal, literal:Num, suggest_constant_definition
print((a / b) % p == (a * binary_exponentiation(b, p - 2, p)) % p) # binary_operator:Div, binary_operator:Mod, binary_operator:Mult, binary_operator:Sub, call_argument:, call_argument:b, call_argument:p, comparison_operator:Eq, composition, divisibility_test, function_call:binary_exponentiation, function_call:print, int_literal, literal:Num
print((a / b) % p == (a * b ** (p - 2)) % p) # binary_operator:Div, binary_operator:Mod, binary_operator:Mult, binary_operator:Pow, binary_operator:Sub, call_argument:, comparison_operator:Eq, divisibility_test, function_call:print, int_literal, literal:Num

# ----------------------------------------------------------------------------------------
# ../Python/maths/fibonacci.py
# ----------------------------------------------------------------------------------------
import math # import:math, import_module:math
import functools # import:functools, import_module:functools
import time # import:time, import_module:time
from decimal import getcontext, Decimal # import:decimal:Decimal, import:decimal:getcontext, import_module:decimal, import_name:Decimal, import_name:getcontext
getcontext().prec = 100 # assignment, assignment_rhs_atom:100, function_call:getcontext, int_literal, literal:Num
def timer_decorator(func): # closure:timer_decorator (-> +10), function:timer_decorator (-> +10), function_returning_something:timer_decorator (-> +10), nested_function:timer_decorator (-> +10)
    def timer_wrapper(*args, **kwargs): # function:timer_wrapper (-> +8), function_returning_something:timer_wrapper (-> +8)
        start = time.time() # assignment, assignment_lhs_identifier:start, assignment_rhs_atom:time, method_call, method_call_name:time
        func(*args, **kwargs) # call_argument:, function_call:func
        end = time.time() # assignment, assignment_lhs_identifier:end, assignment_rhs_atom:time, method_call, method_call_name:time
        if int(end - start) > 0: # binary_operator:Sub, call_argument:, comparison_operator:Gt, function_call:int, if (-> +3), if_test_id:end, if_test_id:int, if_test_id:start, int_literal, literal:Num
            print(f"Run time for {func.__name__}: {(end - start):0.2f}s") # binary_operator:Sub, call_argument:, function_call:print, if_then_branch, literal:Str
        else:
            print(f"Run time for {func.__name__}: {(end - start)*1000:0.2f}ms") # binary_operator:Mult, binary_operator:Sub, call_argument:, function_call:print, if_else_branch, int_literal, literal:Num, literal:Str, suggest_constant_definition
        return func(*args, **kwargs) # call_argument:, function_call:func, function_tail_call:func, return
    return timer_wrapper # return:timer_wrapper
class Error(Exception):
    pass
class ValueTooLargeError(Error):
    pass
class ValueTooSmallError(Error):
    pass
class ValueLessThanZero(Error):
    pass
def _check_number_input(n, min_thresh, max_thresh=None): # function:_check_number_input (-> +22), function_returning_something:_check_number_input (-> +22), function_with_default_positional_arguments:_check_number_input (-> +22), literal:None
    try: # try (-> +19), try_except:ValueLessThanZero (-> +19), try_except:ValueTooLargeError (-> +19), try_except:ValueTooSmallError (-> +19), try_raise:ValueLessThanZero (-> +19), try_raise:ValueTooLargeError (-> +19), try_raise:ValueTooSmallError (-> +19)
        if n >= min_thresh and max_thresh is None: # boolean_operator:And, comparison_operator:GtE, comparison_operator:Is, if (-> +9), if_test_id:max_thresh, if_test_id:min_thresh, if_test_id:n, literal:None
            return True # if_then_branch, literal:True, return:True
        elif min_thresh <= n <= max_thresh: # chained_comparison:2, chained_inequalities:2, comparison_operator:LtE, if (-> +7), if_test_id:max_thresh, if_test_id:min_thresh, if_test_id:n
            return True # if_elif_branch, literal:True, return:True
        elif n < 0: # comparison_operator:Lt, if (-> +5), if_test_id:n, int_literal, literal:Num
            raise ValueLessThanZero # if_elif_branch, raise:ValueLessThanZero
        elif n < min_thresh: # comparison_operator:Lt, if (-> +3), if_test_id:min_thresh, if_test_id:n
            raise ValueTooSmallError # if_elif_branch, raise:ValueTooSmallError
        elif n > max_thresh: # comparison_operator:Gt, if (-> +1), if_test_id:max_thresh, if_test_id:n
            raise ValueTooLargeError # if_elif_branch, raise:ValueTooLargeError
    except ValueLessThanZero: # except:ValueLessThanZero
        print("Incorrect Input: number must not be less than 0") # call_argument:, function_call:print, literal:Str
    except ValueTooSmallError: # except:ValueTooSmallError
        print( # function_call:print
            f"Incorrect Input: input number must be > {min_thresh} for the recursive calculation" # call_argument:, literal:Str
        )
    except ValueTooLargeError: # except:ValueTooLargeError
        print( # function_call:print
            f"Incorrect Input: input number must be < {max_thresh} for the recursive calculation" # call_argument:, literal:Str
        )
    return False # literal:False, return:False
def fib_iterative(n): # function:fib_iterative (-> +8), function_returning_something:fib_iterative (-> +8)
    n = int(n) # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:n, call_argument:n, function_call:int
    if _check_number_input(n, 2): # call_argument:2, call_argument:n, function_call:_check_number_input, if (-> +6), if_test_id:_check_number_input, if_test_id:n, int_literal, literal:Num
        seq_out = [0, 1] # assignment, assignment_lhs_identifier:seq_out, assignment_rhs_atom:0, assignment_rhs_atom:1, if_then_branch (-> +5), int_literal, literal:List, literal:Num
        a, b = 0, 1 # assignment, assignment_lhs_identifier:a, assignment_lhs_identifier:b, assignment_rhs_atom:0, assignment_rhs_atom:1, int_literal, literal:Num, literal:Tuple
        for _ in range(n - len(seq_out)): # binary_operator:Sub, call_argument:, call_argument:seq_out, composition, for:_ (-> +2), for_range:_ (-> +2), function_call:len, function_call:range, range:_
            a, b = b, a + b # assignment, assignment_lhs_identifier:a, assignment_lhs_identifier:b, assignment_rhs_atom:a, assignment_rhs_atom:b, binary_operator:Add, update_variable:a:b, update_variable:b:a
            seq_out.append(b) # call_argument:b, method_call, method_call_name:append, method_call_object:seq_out, update_variable:seq_out:b
        return seq_out # return:seq_out
def fib_formula(n): # function:fib_formula (-> +12), function_returning_something:fib_formula (-> +12)
    seq_out = [0, 1] # assignment, assignment_lhs_identifier:seq_out, assignment_rhs_atom:0, assignment_rhs_atom:1, int_literal, literal:List, literal:Num
    n = int(n) # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:n, call_argument:n, function_call:int
    if _check_number_input(n, 2, 1000000): # call_argument:1000000, call_argument:2, call_argument:n, function_call:_check_number_input, if (-> +9), if_test_id:_check_number_input, if_test_id:n, int_literal, literal:Num, suggest_constant_definition
        sqrt = Decimal(math.sqrt(5)) # assignment, assignment_lhs_identifier:sqrt, assignment_rhs_atom:5, assignment_rhs_atom:math, call_argument:, call_argument:5, composition, function_call:Decimal, if_then_branch (-> +8), int_literal, literal:Num, method_call, method_call_name:sqrt, suggest_constant_definition
        phi_1 = Decimal(1 + sqrt) / Decimal(2) # assignment, assignment_lhs_identifier:phi_1, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:sqrt, binary_operator:Add, binary_operator:Div, call_argument:, call_argument:2, function_call:Decimal, int_literal, literal:Num
        phi_2 = Decimal(1 - sqrt) / Decimal(2) # assignment, assignment_lhs_identifier:phi_2, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:sqrt, binary_operator:Div, binary_operator:Sub, call_argument:, call_argument:2, function_call:Decimal, int_literal, literal:Num
        for i in range(2, n): # call_argument:2, call_argument:n, for:i (-> +4), for_range:2:n (-> +4), function_call:range, int_literal, literal:Num, range:2:n
            temp_out = ((phi_1 ** Decimal(i)) - (phi_2 ** Decimal(i))) * ( # assignment, assignment_lhs_identifier:temp_out, assignment_rhs_atom:i, assignment_rhs_atom:phi_1, assignment_rhs_atom:phi_2, binary_operator:Mult, binary_operator:Pow, binary_operator:Sub, call_argument:i, function_call:Decimal
                Decimal(sqrt) ** Decimal(-1) # assignment_rhs_atom:-1, assignment_rhs_atom:sqrt, binary_operator:Pow, call_argument:-1, call_argument:sqrt, function_call:Decimal, int_literal, literal:Num
            )
            seq_out.append(int(temp_out)) # call_argument:, call_argument:temp_out, composition, function_call:int, method_call, method_call_name:append, method_call_object:seq_out, update_variable:seq_out:, update_variable:seq_out:temp_out
        return seq_out # return:seq_out

# ----------------------------------------------------------------------------------------
# ../Python/maths/fibonacci_sequence_recursion.py
# ----------------------------------------------------------------------------------------
def recur_fibo(n): # body_recursive_function:recur_fibo (-> +1), function:recur_fibo (-> +1), function_returning_something:recur_fibo (-> +1), recursive_function:recur_fibo (-> +1)
    return n if n <= 1 else recur_fibo(n - 1) + recur_fibo(n - 2) # binary_operator:Add, binary_operator:Sub, call_argument:, comparison_operator:LtE, conditional_expression, function_call:recur_fibo, int_literal, literal:Num, return
def main(): # function:main (-> +6), function_returning_nothing:main (-> +6)
    limit = int(input("How many terms to include in fibonacci series: ")) # assignment, assignment_lhs_identifier:limit, call_argument:, composition, function_call:input, function_call:int, literal:Str
    if limit > 0: # comparison_operator:Gt, if (-> +4), if_test_id:limit, int_literal, literal:Num
        print(f"The first {limit} terms of the fibonacci series are as follows:") # call_argument:, function_call:print, if_then_branch (-> +1), literal:Str
        print([recur_fibo(n) for n in range(limit)]) # call_argument:, call_argument:limit, call_argument:n, composition, comprehension:List, comprehension_for_count:1, function_call:print, function_call:range, function_call:recur_fibo, range:limit
    else:
        print("Please enter a positive integer: ") # call_argument:, function_call:print, if_else_branch, literal:Str

# ----------------------------------------------------------------------------------------
# ../Python/maths/find_max.py
# ----------------------------------------------------------------------------------------
def find_max(nums): # function:find_max (-> +5), function_returning_something:find_max (-> +5)
    max_num = nums[0] # assignment, assignment_lhs_identifier:max_num, assignment_rhs_atom:0, assignment_rhs_atom:nums, index, int_literal, literal:Num
    for x in nums: # find_best_element (-> +2), for:x (-> +2), for_each (-> +2)
        if x > max_num: # comparison_operator:Gt, if (-> +1), if_test_id:max_num, if_test_id:x
            max_num = x # assignment, assignment_lhs_identifier:max_num, assignment_rhs_atom:x, if_then_branch
    return max_num # return:max_num
def main(): # function:main (-> +1), function_returning_nothing:main (-> +1)
    print(find_max([2, 4, 9, 7, 19, 94, 5])) # call_argument:, composition, function_call:find_max, function_call:print, int_literal, literal:List, literal:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/find_max_recursion.py
# ----------------------------------------------------------------------------------------
def find_max(nums, left, right): # body_recursive_function:find_max (-> +6), function:find_max (-> +6), function_returning_something:find_max (-> +6), recursive_function:find_max (-> +6)
    if left == right: # comparison_operator:Eq, if (-> +1), if_test_id:left, if_test_id:right
        return nums[left] # if_then_branch, index, return
    mid = (left + right) >> 1 # assignment, assignment_lhs_identifier:mid, assignment_rhs_atom:1, assignment_rhs_atom:left, assignment_rhs_atom:right, binary_operator:Add, binary_operator:RShift, int_literal, literal:Num
    left_max = find_max(nums, left, mid) # assignment, assignment_lhs_identifier:left_max, assignment_rhs_atom:left, assignment_rhs_atom:mid, assignment_rhs_atom:nums, call_argument:left, call_argument:mid, call_argument:nums, function_call:find_max
    right_max = find_max(nums, mid + 1, right) # assignment, assignment_lhs_identifier:right_max, assignment_rhs_atom:1, assignment_rhs_atom:mid, assignment_rhs_atom:nums, assignment_rhs_atom:right, binary_operator:Add, call_argument:, call_argument:nums, call_argument:right, function_call:find_max, int_literal, literal:Num
    return left_max if left_max >= right_max else right_max # comparison_operator:GtE, conditional_expression, return

# ----------------------------------------------------------------------------------------
# ../Python/maths/find_min.py
# ----------------------------------------------------------------------------------------
def find_min(nums): # function:find_min (-> +5), function_returning_something:find_min (-> +5)
    min_num = nums[0] # assignment, assignment_lhs_identifier:min_num, assignment_rhs_atom:0, assignment_rhs_atom:nums, index, int_literal, literal:Num
    for num in nums: # find_best_element (-> +2), for:num (-> +2), for_each (-> +2)
        if min_num > num: # comparison_operator:Gt, if (-> +1), if_test_id:min_num, if_test_id:num
            min_num = num # assignment, assignment_lhs_identifier:min_num, assignment_rhs_atom:num, if_then_branch
    return min_num # return:min_num
def main(): # function:main (-> +1), function_returning_nothing:main (-> +1)
    assert find_min([0, 1, 2, 3, 4, 5, -3, 24, -56]) == -56 # assertion, call_argument:, comparison_operator:Eq, function_call:find_min, int_literal, literal:List, literal:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/find_min_recursion.py
# ----------------------------------------------------------------------------------------
def find_min(nums, left, right): # body_recursive_function:find_min (-> +6), function:find_min (-> +6), function_returning_something:find_min (-> +6), recursive_function:find_min (-> +6)
    if left == right: # comparison_operator:Eq, if (-> +1), if_test_id:left, if_test_id:right
        return nums[left] # if_then_branch, index, return
    mid = (left + right) >> 1 # assignment, assignment_lhs_identifier:mid, assignment_rhs_atom:1, assignment_rhs_atom:left, assignment_rhs_atom:right, binary_operator:Add, binary_operator:RShift, int_literal, literal:Num
    left_min = find_min(nums, left, mid) # assignment, assignment_lhs_identifier:left_min, assignment_rhs_atom:left, assignment_rhs_atom:mid, assignment_rhs_atom:nums, call_argument:left, call_argument:mid, call_argument:nums, function_call:find_min
    right_min = find_min(nums, mid + 1, right) # assignment, assignment_lhs_identifier:right_min, assignment_rhs_atom:1, assignment_rhs_atom:mid, assignment_rhs_atom:nums, assignment_rhs_atom:right, binary_operator:Add, call_argument:, call_argument:nums, call_argument:right, function_call:find_min, int_literal, literal:Num
    return left_min if left_min <= right_min else right_min # comparison_operator:LtE, conditional_expression, return

# ----------------------------------------------------------------------------------------
# ../Python/maths/floor.py
# ----------------------------------------------------------------------------------------
def floor(x) -> int: # function:floor (-> +2), function_returning_something:floor (-> +2)
    return ( # return
        x if isinstance(x, int) or x - int(x) == 0 else int(x) if x > 0 else int(x - 1) # binary_operator:Sub, boolean_operator:Or, call_argument:, call_argument:int, call_argument:x, comparison_operator:Eq, comparison_operator:Gt, conditional_expression, function_call:int, function_call:isinstance, int_literal, literal:Num
    )

# ----------------------------------------------------------------------------------------
# ../Python/maths/gaussian.py
# ----------------------------------------------------------------------------------------
from numpy import pi, sqrt, exp # import:numpy:exp, import:numpy:pi, import:numpy:sqrt, import_module:numpy, import_name:exp, import_name:pi, import_name:sqrt
def gaussian(x, mu: float = 0.0, sigma: float = 1.0) -> int: # float_literal, function:gaussian (-> +1), function_returning_something:gaussian (-> +1), function_with_default_positional_arguments:gaussian (-> +1), literal:Num
    return 1 / sqrt(2 * pi * sigma ** 2) * exp(-((x - mu) ** 2) / 2 * sigma ** 2) # binary_operator:Div, binary_operator:Mult, binary_operator:Pow, binary_operator:Sub, call_argument:, function_call:exp, function_call:sqrt, int_literal, literal:Num, return, unary_operator:USub

# ----------------------------------------------------------------------------------------
# ../Python/maths/greatest_common_divisor.py
# ----------------------------------------------------------------------------------------
def greatest_common_divisor(a, b): # function:greatest_common_divisor (-> +1), function_returning_something:greatest_common_divisor (-> +1), recursive_function:greatest_common_divisor (-> +1), tail_recursive_function:greatest_common_divisor (-> +1)
    return b if a == 0 else greatest_common_divisor(b % a, a) # binary_operator:Mod, call_argument:, call_argument:a, comparison_operator:Eq, conditional_expression, function_call:greatest_common_divisor, function_tail_call:greatest_common_divisor, int_literal, literal:Num, return
def gcd_by_iterative(x, y): # function:gcd_by_iterative (-> +3), function_returning_something:gcd_by_iterative (-> +3)
    while y: # while (-> +1)
        x, y = y, x % y # assignment, assignment_lhs_identifier:x, assignment_lhs_identifier:y, assignment_rhs_atom:x, assignment_rhs_atom:y, binary_operator:Mod, update_variable:x:y, update_variable:y:x
    return x # return:x
def main(): # function:main (-> +10), function_returning_nothing:main (-> +10)
    try: # try (-> +9), try_except:IndexError (-> +9), try_except:UnboundLocalError (-> +9), try_except:ValueError (-> +9)
        nums = input("Enter two integers separated by comma (,): ").split(",") # assignment, assignment_lhs_identifier:nums, call_argument:, function_call:input, literal:Str, method_call, method_call_name:split
        num_1 = int(nums[0]) # assignment, assignment_lhs_identifier:num_1, assignment_rhs_atom:0, assignment_rhs_atom:nums, call_argument:, function_call:int, index, int_literal, literal:Num
        num_2 = int(nums[1]) # assignment, assignment_lhs_identifier:num_2, assignment_rhs_atom:1, assignment_rhs_atom:nums, call_argument:, function_call:int, index, int_literal, literal:Num
        print( # composition, function_call:print
            f"greatest_common_divisor({num_1}, {num_2}) = {greatest_common_divisor(num_1, num_2)}" # call_argument:, call_argument:num_1, call_argument:num_2, function_call:greatest_common_divisor, literal:Str
        )
        print(f"By iterative gcd({num_1}, {num_2}) = {gcd_by_iterative(num_1, num_2)}") # call_argument:, call_argument:num_1, call_argument:num_2, composition, function_call:gcd_by_iterative, function_call:print, literal:Str
    except (IndexError, UnboundLocalError, ValueError): # except:IndexError, except:UnboundLocalError, except:ValueError
        print("Wrong input") # call_argument:, function_call:print, literal:Str

# ----------------------------------------------------------------------------------------
# ../Python/maths/hardy_ramanujanalgo.py
# ----------------------------------------------------------------------------------------
import math # import:math, import_module:math
def exactPrimeFactorCount(n): # function:exactPrimeFactorCount (-> +15), function_returning_something:exactPrimeFactorCount (-> +15)
    count = 0 # assignment, assignment_lhs_identifier:count, assignment_rhs_atom:0, int_literal, literal:Num
    if n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +3), if_test_id:n, int_literal, literal:Num
        count += 1 # assignment_lhs_identifier:count, assignment_rhs_atom:1, augmented_assignment, if_then_branch (-> +2), int_literal, literal:Num, update_variable:count:1
        while n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, evolve_state (-> +1), int_literal, literal:Num, while (-> +1)
            n = int(n / 2) # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:2, assignment_rhs_atom:n, binary_operator:Div, call_argument:, function_call:int, int_literal, literal:Num, update_variable:n:2
    i = 3 # assignment, assignment_lhs_identifier:i, assignment_rhs_atom:3, int_literal, literal:Num, suggest_constant_definition
    while i <= int(math.sqrt(n)): # call_argument:, call_argument:n, comparison_operator:LtE, composition, evolve_state (-> +5), function_call:int, method_call, method_call_name:sqrt, while (-> +5)
        if n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, if (-> +3), if_test_id:i, if_test_id:n, int_literal, literal:Num
            count += 1 # assignment_lhs_identifier:count, assignment_rhs_atom:1, augmented_assignment, if_then_branch (-> +2), int_literal, literal:Num, update_variable:count:1
            while n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, int_literal, literal:Num, while (-> +1)
                n = int(n / i) # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:i, assignment_rhs_atom:n, binary_operator:Div, call_argument:, function_call:int, update_variable:n:i
        i = i + 2 # assignment, assignment_lhs_identifier:i, assignment_rhs_atom:2, assignment_rhs_atom:i, binary_operator:Add, int_literal, literal:Num, suggest_augmented_assignment, update_variable:i:2
    if n > 2: # comparison_operator:Gt, if (-> +1), if_test_id:n, int_literal, literal:Num
        count += 1 # assignment_lhs_identifier:count, assignment_rhs_atom:1, augmented_assignment, if_then_branch, int_literal, literal:Num, update_variable:count:1
    return count # return:count

# ----------------------------------------------------------------------------------------
# ../Python/maths/is_square_free.py
# ----------------------------------------------------------------------------------------
from typing import List # import:typing:List, import_module:typing, import_name:List
def is_square_free(factors: List[int]) -> bool: # function:is_square_free (-> +1), function_returning_something:is_square_free (-> +1), index
    return len(set(factors)) == len(factors) # call_argument:, call_argument:factors, comparison_operator:Eq, composition, function_call:len, function_call:set, return

# ----------------------------------------------------------------------------------------
# ../Python/maths/jaccard_similarity.py
# ----------------------------------------------------------------------------------------
def jaccard_similariy(setA, setB, alternativeUnion=False): # function:jaccard_similariy (-> +14), function_returning_something:jaccard_similariy (-> +14), function_with_default_positional_arguments:jaccard_similariy (-> +14), literal:False
    if isinstance(setA, set) and isinstance(setB, set): # boolean_operator:And, call_argument:set, call_argument:setA, call_argument:setB, function_call:isinstance, if (-> +6), if_test_id:isinstance, if_test_id:set, if_test_id:setA, if_test_id:setB
        intersection = len(setA.intersection(setB)) # assignment, assignment_lhs_identifier:intersection, assignment_rhs_atom:setA, assignment_rhs_atom:setB, call_argument:, call_argument:setB, composition, function_call:len, if_then_branch (-> +5), method_call, method_call_name:intersection
        if alternativeUnion: # if (-> +3), nested_if:1 (-> +3), suggest_conditional_expression (-> +3)
            union = len(setA) + len(setB) # assignment, assignment_lhs_identifier:union, assignment_rhs_atom:setA, assignment_rhs_atom:setB, binary_operator:Add, call_argument:setA, call_argument:setB, function_call:len, if_then_branch
        else:
            union = len(setA.union(setB)) # assignment, assignment_lhs_identifier:union, assignment_rhs_atom:setA, assignment_rhs_atom:setB, call_argument:, call_argument:setB, composition, function_call:len, if_else_branch, method_call, method_call_name:union
        return intersection / union # binary_operator:Div, return
    if isinstance(setA, (list, tuple)) and isinstance(setB, (list, tuple)): # boolean_operator:And, call_argument:, call_argument:setA, call_argument:setB, function_call:isinstance, if (-> +6), if_test_id:isinstance, if_test_id:list, if_test_id:setA, if_test_id:setB, if_test_id:tuple
        intersection = [element for element in setA if element in setB] # assignment, assignment_lhs_identifier:intersection, assignment_rhs_atom:element, assignment_rhs_atom:setA, assignment_rhs_atom:setB, comparison_operator:In, comprehension:List, comprehension_for_count:1, filtered_comprehension, if_then_branch (-> +5)
        if alternativeUnion: # if (-> +3), nested_if:1 (-> +3), suggest_conditional_expression (-> +3)
            union = len(setA) + len(setB) # assignment, assignment_lhs_identifier:union, assignment_rhs_atom:setA, assignment_rhs_atom:setB, binary_operator:Add, call_argument:setA, call_argument:setB, function_call:len, if_then_branch
        else:
            union = setA + [element for element in setB if element not in setA] # assignment, assignment_lhs_identifier:union, assignment_rhs_atom:element, assignment_rhs_atom:setA, assignment_rhs_atom:setB, binary_operator:Add, comparison_operator:NotIn, comprehension:List, comprehension_for_count:1, filtered_comprehension, if_else_branch
        return len(intersection) / len(union) # binary_operator:Div, call_argument:intersection, call_argument:union, function_call:len, return

# ----------------------------------------------------------------------------------------
# ../Python/maths/karatsuba.py
# ----------------------------------------------------------------------------------------
def karatsuba(a, b): # body_recursive_function:karatsuba (-> +11), function:karatsuba (-> +11), function_returning_something:karatsuba (-> +11), recursive_function:karatsuba (-> +11)
    if len(str(a)) == 1 or len(str(b)) == 1: # boolean_operator:Or, call_argument:, call_argument:a, call_argument:b, comparison_operator:Eq, composition, function_call:len, function_call:str, if (-> +10), if_test_id:a, if_test_id:b, if_test_id:len, if_test_id:str, int_literal, literal:Num
        return a * b # binary_operator:Mult, if_then_branch, return
    else:
        m1 = max(len(str(a)), len(str(b))) # assignment, assignment_lhs_identifier:m1, assignment_rhs_atom:a, assignment_rhs_atom:b, call_argument:, call_argument:a, call_argument:b, composition, function_call:len, function_call:max, function_call:str, if_else_branch (-> +7)
        m2 = m1 // 2 # assignment, assignment_lhs_identifier:m2, assignment_rhs_atom:2, assignment_rhs_atom:m1, binary_operator:FloorDiv, int_literal, literal:Num
        a1, a2 = divmod(a, 10 ** m2) # assignment, assignment_lhs_identifier:a1, assignment_lhs_identifier:a2, assignment_rhs_atom:10, assignment_rhs_atom:a, assignment_rhs_atom:m2, binary_operator:Pow, call_argument:, call_argument:a, function_call:divmod, int_literal, literal:Num, suggest_constant_definition
        b1, b2 = divmod(b, 10 ** m2) # assignment, assignment_lhs_identifier:b1, assignment_lhs_identifier:b2, assignment_rhs_atom:10, assignment_rhs_atom:b, assignment_rhs_atom:m2, binary_operator:Pow, call_argument:, call_argument:b, function_call:divmod, int_literal, literal:Num, suggest_constant_definition
        x = karatsuba(a2, b2) # assignment, assignment_lhs_identifier:x, assignment_rhs_atom:a2, assignment_rhs_atom:b2, call_argument:a2, call_argument:b2, function_call:karatsuba
        y = karatsuba((a1 + a2), (b1 + b2)) # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:a1, assignment_rhs_atom:a2, assignment_rhs_atom:b1, assignment_rhs_atom:b2, binary_operator:Add, call_argument:, function_call:karatsuba
        z = karatsuba(a1, b1) # assignment, assignment_lhs_identifier:z, assignment_rhs_atom:a1, assignment_rhs_atom:b1, call_argument:a1, call_argument:b1, function_call:karatsuba
        return (z * 10 ** (2 * m2)) + ((y - z - x) * 10 ** (m2)) + (x) # binary_operator:Add, binary_operator:Mult, binary_operator:Pow, binary_operator:Sub, int_literal, literal:Num, return, suggest_constant_definition
def main(): # function:main (-> +1), function_returning_nothing:main (-> +1)
    print(karatsuba(15463, 23489)) # call_argument:, call_argument:15463, call_argument:23489, composition, function_call:karatsuba, function_call:print, int_literal, literal:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/kth_lexicographic_permutation.py
# ----------------------------------------------------------------------------------------
def kthPermutation(k, n): # function:kthPermutation (-> +13), function_returning_something:kthPermutation (-> +13)
    factorials = [1] # assignment, assignment_lhs_identifier:factorials, assignment_rhs_atom:1, int_literal, literal:List, literal:Num
    for i in range(2, n): # call_argument:2, call_argument:n, for:i (-> +1), for_range:2:n (-> +1), function_call:range, int_literal, literal:Num, range:2:n
        factorials.append(factorials[-1] * i) # binary_operator:Mult, call_argument:, index, int_literal, literal:Num, method_call, method_call_name:append, method_call_object:factorials, negative_index:-1, update_variable:factorials:
    assert 0 <= k < factorials[-1] * n, "k out of bounds" # assertion, binary_operator:Mult, chained_comparison:2, comparison_operator:Lt, comparison_operator:LtE, index, int_literal, literal:Num, literal:Str, negative_index:-1
    permutation = [] # assignment, assignment_lhs_identifier:permutation, literal:List
    elements = list(range(n)) # assignment, assignment_lhs_identifier:elements, assignment_rhs_atom:n, call_argument:, call_argument:n, composition, function_call:list, function_call:range, range:n
    while factorials: # while (-> +4)
        factorial = factorials.pop() # assignment, assignment_lhs_identifier:factorial, assignment_rhs_atom:factorials, method_call, method_call_name:pop
        number, k = divmod(k, factorial) # assignment, assignment_lhs_identifier:k, assignment_lhs_identifier:number, assignment_rhs_atom:factorial, assignment_rhs_atom:k, call_argument:factorial, call_argument:k, function_call:divmod, update_variable:k:factorial
        permutation.append(elements[number]) # call_argument:, index, method_call, method_call_name:append, method_call_object:permutation, update_variable:permutation:
        elements.remove(elements[number]) # call_argument:, index, method_call, method_call_name:remove, method_call_object:elements
    permutation.append(elements[0]) # call_argument:, index, int_literal, literal:Num, method_call, method_call_name:append, method_call_object:permutation, update_variable:permutation:
    return permutation # return:permutation

# ----------------------------------------------------------------------------------------
# ../Python/maths/largest_of_very_large_numbers.py
# ----------------------------------------------------------------------------------------
import math # import:math, import_module:math
def res(x, y): # function:res (-> +7), function_returning_something:res (-> +7)
    if 0 not in (x, y): # comparison_operator:NotIn, if (-> +6), if_test_id:x, if_test_id:y, int_literal, literal:Num
        return y * math.log10(x) # binary_operator:Mult, call_argument:x, if_then_branch, method_call, method_call_name:log10, return
    else:
        if x == 0: # comparison_operator:Eq, if (-> +3), if_test_id:x, int_literal, literal:Num
            return 0 # if_elif_branch, int_literal, literal:Num, return:0
        elif y == 0: # comparison_operator:Eq, if (-> +1), if_test_id:y, int_literal, literal:Num
            return 1 # if_elif_branch, int_literal, literal:Num, return:1

# ----------------------------------------------------------------------------------------
# ../Python/maths/least_common_multiple.py
# ----------------------------------------------------------------------------------------
import unittest # import:unittest, import_module:unittest
def find_lcm(first_num: int, second_num: int) -> int: # function:find_lcm (-> +5), function_returning_something:find_lcm (-> +5)
    max_num = first_num if first_num >= second_num else second_num # assignment, assignment_lhs_identifier:max_num, assignment_rhs_atom:first_num, assignment_rhs_atom:second_num, comparison_operator:GtE, conditional_expression
    common_mult = max_num # assignment, assignment_lhs_identifier:common_mult, assignment_rhs_atom:max_num
    while (common_mult % first_num > 0) or (common_mult % second_num > 0): # binary_operator:Mod, boolean_operator:Or, comparison_operator:Gt, int_literal, literal:Num, while (-> +1)
        common_mult += max_num # assignment_lhs_identifier:common_mult, assignment_rhs_atom:max_num, augmented_assignment, update_variable:common_mult:max_num
    return common_mult # return:common_mult
class TestLeastCommonMultiple(unittest.TestCase):
    test_inputs = [ # assignment, assignment_lhs_identifier:test_inputs, literal:List
        (10, 20), # assignment_rhs_atom:10, assignment_rhs_atom:20, int_literal, literal:Num, literal:Tuple, suggest_constant_definition
        (13, 15), # assignment_rhs_atom:13, assignment_rhs_atom:15, int_literal, literal:Num, literal:Tuple, suggest_constant_definition
        (4, 31), # assignment_rhs_atom:31, assignment_rhs_atom:4, int_literal, literal:Num, literal:Tuple, suggest_constant_definition
        (10, 42), # assignment_rhs_atom:10, assignment_rhs_atom:42, int_literal, literal:Num, literal:Tuple, suggest_constant_definition
        (43, 34), # assignment_rhs_atom:34, assignment_rhs_atom:43, int_literal, literal:Num, literal:Tuple, suggest_constant_definition
        (5, 12), # assignment_rhs_atom:12, assignment_rhs_atom:5, int_literal, literal:Num, literal:Tuple, suggest_constant_definition
        (12, 25), # assignment_rhs_atom:12, assignment_rhs_atom:25, int_literal, literal:Num, literal:Tuple, suggest_constant_definition
        (10, 25), # assignment_rhs_atom:10, assignment_rhs_atom:25, int_literal, literal:Num, literal:Tuple, suggest_constant_definition
        (6, 9), # assignment_rhs_atom:6, assignment_rhs_atom:9, int_literal, literal:Num, literal:Tuple, suggest_constant_definition
    ]
    expected_results = [20, 195, 124, 210, 1462, 60, 300, 50, 18] # assignment, assignment_lhs_identifier:expected_results, assignment_rhs_atom:124, assignment_rhs_atom:1462, assignment_rhs_atom:18, assignment_rhs_atom:195, assignment_rhs_atom:20, assignment_rhs_atom:210, assignment_rhs_atom:300, assignment_rhs_atom:50, assignment_rhs_atom:60, int_literal, literal:List, literal:Num, suggest_constant_definition
    def test_lcm_function(self): # function:test_lcm_function (-> +4), function_returning_nothing:test_lcm_function (-> +4)
        for i, (first_num, second_num) in enumerate(self.test_inputs): # call_argument:, for:i:first_num:second_num (-> +3), for_indexes_elements (-> +3), function_call:enumerate
            actual_result = find_lcm(first_num, second_num) # assignment, assignment_lhs_identifier:actual_result, assignment_rhs_atom:first_num, assignment_rhs_atom:second_num, call_argument:first_num, call_argument:second_num, function_call:find_lcm
            with self.subTest(i=i): # method_call, method_call_name:subTest
                self.assertEqual(actual_result, self.expected_results[i]) # call_argument:, call_argument:actual_result, index, method_call, method_call_name:assertEqual, method_call_object:self

# ----------------------------------------------------------------------------------------
# ../Python/maths/lucas_series.py
# ----------------------------------------------------------------------------------------
def recur_luc(n): # body_recursive_function:recur_luc (-> +5), function:recur_luc (-> +5), function_returning_something:recur_luc (-> +5), recursive_function:recur_luc (-> +5)
    if n == 1: # comparison_operator:Eq, if (-> +1), if_test_id:n, int_literal, literal:Num
        return n # if_then_branch, return:n
    if n == 0: # comparison_operator:Eq, if (-> +1), if_test_id:n, int_literal, literal:Num
        return 2 # if_then_branch, int_literal, literal:Num, return:2
    return recur_luc(n - 1) + recur_luc(n - 2) # binary_operator:Add, binary_operator:Sub, call_argument:, function_call:recur_luc, int_literal, literal:Num, return

# ----------------------------------------------------------------------------------------
# ../Python/maths/matrix_exponentiation.py
# ----------------------------------------------------------------------------------------
import timeit # import:timeit, import_module:timeit
class Matrix(object):
    def __init__(self, arg): # function:__init__ (-> +6), function_returning_nothing:__init__ (-> +6)
        if isinstance(arg, list): # call_argument:arg, call_argument:list, function_call:isinstance, if (-> +5), if_test_id:arg, if_test_id:isinstance, if_test_id:list
            self.t = arg # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:arg, if_then_branch (-> +1)
            self.n = len(arg) # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:arg, call_argument:arg, function_call:len
        else:
            self.n = arg # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:arg, if_else_branch (-> +1)
            self.t = [[0 for _ in range(self.n)] for _ in range(self.n)] # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:0, assignment_rhs_atom:_, assignment_rhs_atom:self, call_argument:, comprehension:List, comprehension_for_count:1, function_call:range, int_literal, literal:Num, range:_, update_variable:self:0, update_variable:self:_
    def __mul__(self, b): # function:__mul__ (-> +6), function_returning_something:__mul__ (-> +6)
        matrix = Matrix(self.n) # assignment, assignment_lhs_identifier:matrix, assignment_rhs_atom:self, call_argument:, function_call:Matrix
        for i in range(self.n): # call_argument:, for:i (-> +3), for_range:_ (-> +3), function_call:range, range:_, square_nested_for (-> +3)
            for j in range(self.n): # call_argument:, for:j (-> +2), for_range:_ (-> +2), function_call:range, nested_for:1 (-> +2), range:_, square_nested_for (-> +2)
                for k in range(self.n): # call_argument:, for:k (-> +1), for_range:_ (-> +1), function_call:range, nested_for:2 (-> +1), range:_
                    matrix.t[i][j] += self.t[i][k] * b.t[k][j] # assignment_rhs_atom:b, assignment_rhs_atom:i, assignment_rhs_atom:j, assignment_rhs_atom:k, assignment_rhs_atom:self, augmented_assignment, binary_operator:Mult, index
        return matrix # return:matrix
def modular_exponentiation(a, b): # function:modular_exponentiation (-> +7), function_returning_something:modular_exponentiation (-> +7)
    matrix = Matrix([[1, 0], [0, 1]]) # assignment, assignment_lhs_identifier:matrix, assignment_rhs_atom:0, assignment_rhs_atom:1, call_argument:, function_call:Matrix, int_literal, literal:List, literal:Num
    while b > 0: # comparison_operator:Gt, evolve_state (-> +4), int_literal, literal:Num, while (-> +4)
        if b & 1: # binary_operator:BitAnd, if (-> +1), if_test_id:b, int_literal, literal:Num
            matrix *= a # assignment_lhs_identifier:matrix, assignment_rhs_atom:a, augmented_assignment, if_then_branch, update_variable:matrix:a
        a *= a # assignment_lhs_identifier:a, assignment_rhs_atom:a, augmented_assignment, update_variable:a:a
        b >>= 1 # assignment_lhs_identifier:b, assignment_rhs_atom:1, augmented_assignment, int_literal, literal:Num, update_variable:b:1
    return matrix # return:matrix
def fibonacci_with_matrix_exponentiation(n, f1, f2): # function:fibonacci_with_matrix_exponentiation (-> +7), function_returning_something:fibonacci_with_matrix_exponentiation (-> +7)
    if n == 1: # comparison_operator:Eq, if (-> +3), if_test_id:n, int_literal, literal:Num
        return f1 # if_then_branch, return:f1
    elif n == 2: # comparison_operator:Eq, if (-> +1), if_test_id:n, int_literal, literal:Num
        return f2 # if_elif_branch, return:f2
    matrix = Matrix([[1, 1], [1, 0]]) # assignment, assignment_lhs_identifier:matrix, assignment_rhs_atom:0, assignment_rhs_atom:1, call_argument:, function_call:Matrix, int_literal, literal:List, literal:Num
    matrix = modular_exponentiation(matrix, n - 2) # assignment, assignment_lhs_identifier:matrix, assignment_rhs_atom:2, assignment_rhs_atom:matrix, assignment_rhs_atom:n, binary_operator:Sub, call_argument:, call_argument:matrix, function_call:modular_exponentiation, int_literal, literal:Num, update_variable:matrix:2, update_variable:matrix:n
    return f2 * matrix.t[0][0] + f1 * matrix.t[0][1] # binary_operator:Add, binary_operator:Mult, index, int_literal, literal:Num, return
def simple_fibonacci(n, f1, f2): # function:simple_fibonacci (-> +11), function_returning_something:simple_fibonacci (-> +11)
    if n == 1: # comparison_operator:Eq, if (-> +3), if_test_id:n, int_literal, literal:Num
        return f1 # if_then_branch, return:f1
    elif n == 2: # comparison_operator:Eq, if (-> +1), if_test_id:n, int_literal, literal:Num
        return f2 # if_elif_branch, return:f2
    fn_1 = f1 # assignment, assignment_lhs_identifier:fn_1, assignment_rhs_atom:f1
    fn_2 = f2 # assignment, assignment_lhs_identifier:fn_2, assignment_rhs_atom:f2
    n -= 2 # assignment_lhs_identifier:n, assignment_rhs_atom:2, augmented_assignment, int_literal, literal:Num, update_variable:n:2
    while n > 0: # comparison_operator:Gt, evolve_state (-> +2), int_literal, literal:Num, while (-> +2)
        fn_1, fn_2 = fn_1 + fn_2, fn_1 # assignment, assignment_lhs_identifier:fn_1, assignment_lhs_identifier:fn_2, assignment_rhs_atom:fn_1, assignment_rhs_atom:fn_2, binary_operator:Add, update_variable:fn_1:fn_2, update_variable:fn_2:fn_1
        n -= 1 # assignment_lhs_identifier:n, assignment_rhs_atom:1, augmented_assignment, int_literal, literal:Num, update_variable:n:1
    return fn_1 # return:fn_1
def matrix_exponentiation_time(): # function:matrix_exponentiation_time (-> +8), function_returning_something:matrix_exponentiation_time (-> +8)
    setup = """ # assignment, assignment_lhs_identifier:setup
from random import randint
from __main__ import fibonacci_with_matrix_exponentiation
""" # literal:Str
    code = "fibonacci_with_matrix_exponentiation(randint(1,70000), 1, 1)" # assignment, assignment_lhs_identifier:code, literal:Str
    exec_time = timeit.timeit(setup=setup, stmt=code, number=100) # assignment, assignment_lhs_identifier:exec_time, assignment_rhs_atom:100, assignment_rhs_atom:code, assignment_rhs_atom:setup, assignment_rhs_atom:timeit, int_literal, literal:Num, method_call, method_call_name:timeit, suggest_constant_definition
    print("With matrix exponentiation the average execution time is ", exec_time / 100) # binary_operator:Div, call_argument:, function_call:print, int_literal, literal:Num, literal:Str, suggest_constant_definition
    return exec_time # return:exec_time
def simple_fibonacci_time(): # function:simple_fibonacci_time (-> +10), function_returning_something:simple_fibonacci_time (-> +10)
    setup = """ # assignment, assignment_lhs_identifier:setup
from random import randint
from __main__ import simple_fibonacci
""" # literal:Str
    code = "simple_fibonacci(randint(1,70000), 1, 1)" # assignment, assignment_lhs_identifier:code, literal:Str
    exec_time = timeit.timeit(setup=setup, stmt=code, number=100) # assignment, assignment_lhs_identifier:exec_time, assignment_rhs_atom:100, assignment_rhs_atom:code, assignment_rhs_atom:setup, assignment_rhs_atom:timeit, int_literal, literal:Num, method_call, method_call_name:timeit, suggest_constant_definition
    print( # function_call:print
        "Without matrix exponentiation the average execution time is ", exec_time / 100 # binary_operator:Div, call_argument:, int_literal, literal:Num, literal:Str, suggest_constant_definition
    )
    return exec_time # return:exec_time
def main(): # function:main (-> +2), function_returning_nothing:main (-> +2)
    matrix_exponentiation_time() # function_call:matrix_exponentiation_time
    simple_fibonacci_time() # function_call:simple_fibonacci_time

# ----------------------------------------------------------------------------------------
# ../Python/maths/mobius_function.py
# ----------------------------------------------------------------------------------------
from maths.prime_factors import prime_factors # import:maths.prime_factors:prime_factors, import_module:maths.prime_factors, import_name:prime_factors
from maths.is_square_free import is_square_free # import:maths.is_square_free:is_square_free, import_module:maths.is_square_free, import_name:is_square_free
def mobius(n: int) -> int: # function:mobius (-> +4), function_returning_something:mobius (-> +4)
    factors = prime_factors(n) # assignment, assignment_lhs_identifier:factors, assignment_rhs_atom:n, call_argument:n, function_call:prime_factors
    if is_square_free(factors): # call_argument:factors, function_call:is_square_free, if (-> +1), if_test_id:factors, if_test_id:is_square_free
        return -1 if len(factors) % 2 else 1 # binary_operator:Mod, call_argument:factors, conditional_expression, function_call:len, if_then_branch, int_literal, literal:Num, return
    return 0 # int_literal, literal:Num, return:0

# ----------------------------------------------------------------------------------------
# ../Python/maths/modular_exponential.py
# ----------------------------------------------------------------------------------------
def modular_exponential(base, power, mod): # function:modular_exponential (-> +10), function_returning_something:modular_exponential (-> +10)
    if power < 0: # comparison_operator:Lt, if (-> +1), if_test_id:power, int_literal, literal:Num
        return -1 # if_then_branch, int_literal, literal:Num, return:-1
    base %= mod # assignment_lhs_identifier:base, assignment_rhs_atom:mod, augmented_assignment, update_variable:base:mod
    result = 1 # assignment, assignment_lhs_identifier:result, assignment_rhs_atom:1, int_literal, literal:Num
    while power > 0: # comparison_operator:Gt, evolve_state (-> +4), int_literal, literal:Num, while (-> +4)
        if power & 1: # binary_operator:BitAnd, if (-> +1), if_test_id:power, int_literal, literal:Num
            result = (result * base) % mod # assignment, assignment_lhs_identifier:result, assignment_rhs_atom:base, assignment_rhs_atom:mod, assignment_rhs_atom:result, binary_operator:Mod, binary_operator:Mult, if_then_branch, update_variable:result:base, update_variable:result:mod
        power = power >> 1 # assignment, assignment_lhs_identifier:power, assignment_rhs_atom:1, assignment_rhs_atom:power, binary_operator:RShift, int_literal, literal:Num, suggest_augmented_assignment, update_variable:power:1
        base = (base * base) % mod # assignment, assignment_lhs_identifier:base, assignment_rhs_atom:base, assignment_rhs_atom:mod, binary_operator:Mod, binary_operator:Mult, update_variable:base:mod
    return result # return:result
def main(): # function:main (-> +1), function_returning_nothing:main (-> +1)
    print(modular_exponential(3, 200, 13)) # call_argument:, call_argument:13, call_argument:200, call_argument:3, composition, function_call:modular_exponential, function_call:print, int_literal, literal:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/newton_raphson.py
# ----------------------------------------------------------------------------------------
import math as m # import:math, import_module:math
def calc_derivative(f, a, h=0.001): # float_literal, function:calc_derivative (-> +1), function_returning_something:calc_derivative (-> +1), function_with_default_positional_arguments:calc_derivative (-> +1), literal:Num
    return (f(a + h) - f(a - h)) / (2 * h) # binary_operator:Add, binary_operator:Div, binary_operator:Mult, binary_operator:Sub, call_argument:, function_call:f, int_literal, literal:Num, return
def newton_raphson(f, x0=0, maxiter=100, step=0.0001, maxerror=1e-6, logsteps=False): # float_literal, function:newton_raphson (-> +17), function_returning_something:newton_raphson (-> +17), function_with_default_positional_arguments:newton_raphson (-> +17), int_literal, literal:False, literal:Num
    a = x0 # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:x0
    steps = [a] # assignment, assignment_lhs_identifier:steps, assignment_rhs_atom:a
    error = abs(f(a)) # assignment, assignment_lhs_identifier:error, assignment_rhs_atom:a, call_argument:, call_argument:a, composition, function_call:abs, function_call:f
    f1 = lambda x: calc_derivative(f, x, h=step) # assignment, assignment_lhs_identifier:f1, assignment_rhs_atom:f, assignment_rhs_atom:step, assignment_rhs_atom:x, call_argument:f, call_argument:x, function_call:calc_derivative, lambda_function
    for _ in range(maxiter): # call_argument:maxiter, for:_ (-> +9), for_range:maxiter (-> +9), function_call:range, range:maxiter
        if f1(a) == 0: # call_argument:a, comparison_operator:Eq, function_call:f1, if (-> +1), if_test_id:a, if_test_id:f1, int_literal, literal:Num
            raise ValueError("No converging solution found") # call_argument:, function_call:ValueError, if_then_branch, literal:Str, raise:ValueError
        a = a - f(a) / f1(a) # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:a, binary_operator:Div, binary_operator:Sub, call_argument:a, function_call:f, function_call:f1, suggest_augmented_assignment
        if logsteps: # if (-> +1)
            steps.append(a) # call_argument:a, if_then_branch, method_call, method_call_name:append, method_call_object:steps, update_variable:steps:a
        if error < maxerror: # comparison_operator:Lt, if (-> +1), if_test_id:error, if_test_id:maxerror
            break # if_then_branch
    else:
        raise ValueError("Iteration limit reached, no converging solution found") # call_argument:, function_call:ValueError, literal:Str, raise:ValueError
    if logsteps: # if (-> +1)
        return a, error, steps # if_then_branch, return
    return a, error # return

# ----------------------------------------------------------------------------------------
# ../Python/maths/perfect_square.py
# ----------------------------------------------------------------------------------------
import math # import:math, import_module:math
def perfect_square(num: int) -> bool: # function:perfect_square (-> +1), function_returning_something:perfect_square (-> +1)
    return math.sqrt(num) * math.sqrt(num) == num # binary_operator:Mult, call_argument:num, comparison_operator:Eq, method_call, method_call_name:sqrt, return

# ----------------------------------------------------------------------------------------
# ../Python/maths/polynomial_evaluation.py
# ----------------------------------------------------------------------------------------
from typing import Sequence # import:typing:Sequence, import_module:typing, import_name:Sequence
def evaluate_poly(poly: Sequence[float], x: float) -> float: # function:evaluate_poly (-> +1), function_returning_something:evaluate_poly (-> +1), index
    return sum(c * (x ** i) for i, c in enumerate(poly)) # binary_operator:Mult, binary_operator:Pow, call_argument:, call_argument:poly, composition, comprehension:Generator, comprehension_for_count:1, function_call:enumerate, function_call:sum, function_tail_call:sum, return
def horner(poly: Sequence[float], x: float) -> float: # function:horner (-> +4), function_returning_something:horner (-> +4), index
    result = 0.0 # assignment, assignment_lhs_identifier:result, assignment_rhs_atom:0.0, float_literal, literal:Num, suggest_constant_definition
    for coeff in reversed(poly): # accumulate_elements:result (-> +1), call_argument:poly, for:coeff (-> +1), function_call:reversed
        result = result * x + coeff # assignment, assignment_lhs_identifier:result, assignment_rhs_atom:coeff, assignment_rhs_atom:result, assignment_rhs_atom:x, binary_operator:Add, binary_operator:Mult, update_variable:result:coeff, update_variable:result:x
    return result # return:result

# ----------------------------------------------------------------------------------------
# ../Python/maths/prime_check.py
# ----------------------------------------------------------------------------------------
import math # import:math, import_module:math
import unittest # import:unittest, import_module:unittest
def prime_check(number): # function:prime_check (-> +8), function_returning_something:prime_check (-> +8)
    if number < 2: # comparison_operator:Lt, if (-> +1), if_test_id:number, int_literal, literal:Num
        return False # if_then_branch, literal:False, return:False
    if number < 4: # comparison_operator:Lt, if (-> +1), if_test_id:number, int_literal, literal:Num, suggest_constant_definition
        return True # if_then_branch, literal:True, return:True
    if number % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +1), if_test_id:number, int_literal, literal:Num
        return False # if_then_branch, literal:False, return:False
    odd_numbers = range(3, int(math.sqrt(number)) + 1, 2) # assignment, assignment_lhs_identifier:odd_numbers, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:3, assignment_rhs_atom:math, assignment_rhs_atom:number, binary_operator:Add, call_argument:, call_argument:2, call_argument:3, call_argument:number, composition, function_call:int, function_call:range, int_literal, literal:Num, method_call, method_call_name:sqrt, range:3:_:2, suggest_constant_definition
    return not any(number % i == 0 for i in odd_numbers) # binary_operator:Mod, call_argument:, comparison_operator:Eq, comprehension:Generator, comprehension_for_count:1, divisibility_test, function_call:any, int_literal, literal:Num, return, unary_operator:Not
class Test(unittest.TestCase):
    def test_primes(self): # function:test_primes (-> +10), function_returning_nothing:test_primes (-> +10)
        self.assertTrue(prime_check(2)) # call_argument:, call_argument:2, composition, function_call:prime_check, int_literal, literal:Num, method_call, method_call_name:assertTrue, method_call_object:self
        self.assertTrue(prime_check(3)) # call_argument:, call_argument:3, composition, function_call:prime_check, int_literal, literal:Num, method_call, method_call_name:assertTrue, method_call_object:self, suggest_constant_definition
        self.assertTrue(prime_check(5)) # call_argument:, call_argument:5, composition, function_call:prime_check, int_literal, literal:Num, method_call, method_call_name:assertTrue, method_call_object:self, suggest_constant_definition
        self.assertTrue(prime_check(7)) # call_argument:, call_argument:7, composition, function_call:prime_check, int_literal, literal:Num, method_call, method_call_name:assertTrue, method_call_object:self, suggest_constant_definition
        self.assertTrue(prime_check(11)) # call_argument:, call_argument:11, composition, function_call:prime_check, int_literal, literal:Num, method_call, method_call_name:assertTrue, method_call_object:self, suggest_constant_definition
        self.assertTrue(prime_check(13)) # call_argument:, call_argument:13, composition, function_call:prime_check, int_literal, literal:Num, method_call, method_call_name:assertTrue, method_call_object:self, suggest_constant_definition
        self.assertTrue(prime_check(17)) # call_argument:, call_argument:17, composition, function_call:prime_check, int_literal, literal:Num, method_call, method_call_name:assertTrue, method_call_object:self, suggest_constant_definition
        self.assertTrue(prime_check(19)) # call_argument:, call_argument:19, composition, function_call:prime_check, int_literal, literal:Num, method_call, method_call_name:assertTrue, method_call_object:self, suggest_constant_definition
        self.assertTrue(prime_check(23)) # call_argument:, call_argument:23, composition, function_call:prime_check, int_literal, literal:Num, method_call, method_call_name:assertTrue, method_call_object:self, suggest_constant_definition
        self.assertTrue(prime_check(29)) # call_argument:, call_argument:29, composition, function_call:prime_check, int_literal, literal:Num, method_call, method_call_name:assertTrue, method_call_object:self, suggest_constant_definition
    def test_not_primes(self): # function:test_not_primes (-> +12), function_returning_nothing:test_not_primes (-> +12)
        self.assertFalse(prime_check(-19), "Negative numbers are not prime.") # call_argument:, call_argument:-19, composition, function_call:prime_check, int_literal, literal:Num, literal:Str, method_call, method_call_name:assertFalse, method_call_object:self, suggest_constant_definition
        self.assertFalse( # composition, method_call, method_call_name:assertFalse, method_call_object:self
            prime_check(0), "Zero doesn't have any divider, primes must have two" # call_argument:, call_argument:0, function_call:prime_check, int_literal, literal:Num, literal:Str
        )
        self.assertFalse( # composition, method_call, method_call_name:assertFalse, method_call_object:self
            prime_check(1), "One just have 1 divider, primes must have two." # call_argument:, call_argument:1, function_call:prime_check, int_literal, literal:Num, literal:Str
        )
        self.assertFalse(prime_check(2 * 2)) # binary_operator:Mult, call_argument:, composition, function_call:prime_check, int_literal, literal:Num, method_call, method_call_name:assertFalse, method_call_object:self
        self.assertFalse(prime_check(2 * 3)) # binary_operator:Mult, call_argument:, composition, function_call:prime_check, int_literal, literal:Num, method_call, method_call_name:assertFalse, method_call_object:self, suggest_constant_definition
        self.assertFalse(prime_check(3 * 3)) # binary_operator:Mult, call_argument:, composition, function_call:prime_check, int_literal, literal:Num, method_call, method_call_name:assertFalse, method_call_object:self, suggest_constant_definition
        self.assertFalse(prime_check(3 * 5)) # binary_operator:Mult, call_argument:, composition, function_call:prime_check, int_literal, literal:Num, method_call, method_call_name:assertFalse, method_call_object:self, suggest_constant_definition
        self.assertFalse(prime_check(3 * 5 * 7)) # binary_operator:Mult, call_argument:, composition, function_call:prime_check, int_literal, literal:Num, method_call, method_call_name:assertFalse, method_call_object:self, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/prime_factors.py
# ----------------------------------------------------------------------------------------
from typing import List # import:typing:List, import_module:typing, import_name:List
def prime_factors(n: int) -> List[int]: # function:prime_factors (-> +11), function_returning_something:prime_factors (-> +11), index
    i = 2 # assignment, assignment_lhs_identifier:i, assignment_rhs_atom:2, int_literal, literal:Num
    factors = [] # assignment, assignment_lhs_identifier:factors, literal:List
    while i * i <= n: # binary_operator:Mult, comparison_operator:LtE, evolve_state (-> +5), while (-> +5)
        if n % i: # binary_operator:Mod, if (-> +4), if_test_id:i, if_test_id:n
            i += 1 # assignment_lhs_identifier:i, assignment_rhs_atom:1, augmented_assignment, if_then_branch, int_literal, literal:Num, update_variable:i:1
        else:
            n //= i # assignment_lhs_identifier:n, assignment_rhs_atom:i, augmented_assignment, if_else_branch (-> +1), update_variable:n:i
            factors.append(i) # call_argument:i, method_call, method_call_name:append, method_call_object:factors, update_variable:factors:i
    if n > 1: # comparison_operator:Gt, if (-> +1), if_test_id:n, int_literal, literal:Num
        factors.append(n) # call_argument:n, if_then_branch, method_call, method_call_name:append, method_call_object:factors, update_variable:factors:n
    return factors # return:factors

# ----------------------------------------------------------------------------------------
# ../Python/maths/prime_numbers.py
# ----------------------------------------------------------------------------------------
from typing import List # import:typing:List, import_module:typing, import_name:List
def primes(max: int) -> List[int]: # function:primes (-> +9), function_returning_something:primes (-> +9), index
    max += 1 # assignment_lhs_identifier:max, assignment_rhs_atom:1, augmented_assignment, int_literal, literal:Num, update_variable:max:1
    numbers = [False] * max # assignment, assignment_lhs_identifier:numbers, assignment_rhs_atom:False, assignment_rhs_atom:max, binary_operator:Mult, literal:False, literal:List
    ret = [] # assignment, assignment_lhs_identifier:ret, literal:List
    for i in range(2, max): # accumulate_elements:ret (-> +4), call_argument:2, call_argument:max, for:i (-> +4), for_range:2:max (-> +4), for_range:i:max:i (-> +4), function_call:range, int_literal, literal:Num, range:2:max
        if not numbers[i]: # if (-> +3), if_test_id:i, if_test_id:numbers, index, unary_operator:Not
            for j in range(i, max, i): # call_argument:i, call_argument:max, for:j (-> +1), for_range:i:max:i (-> +1), function_call:range, if_then_branch (-> +2), nested_for:1 (-> +1), range:i:max:i
                numbers[j] = True # assignment, assignment_lhs_identifier:numbers, assignment_rhs_atom:True, index, literal:True
            ret.append(i) # call_argument:i, method_call, method_call_name:append, method_call_object:ret, update_variable:ret:i
    return ret # return:ret

# ----------------------------------------------------------------------------------------
# ../Python/maths/prime_sieve_eratosthenes.py
# ----------------------------------------------------------------------------------------
def prime_sieve_eratosthenes(num): # function:prime_sieve_eratosthenes (-> +10), function_returning_nothing:prime_sieve_eratosthenes (-> +10)
    primes = [True for i in range(num + 1)] # assignment, assignment_lhs_identifier:primes, assignment_rhs_atom:1, assignment_rhs_atom:True, assignment_rhs_atom:i, assignment_rhs_atom:num, binary_operator:Add, call_argument:, comprehension:List, comprehension_for_count:1, function_call:range, int_literal, literal:Num, literal:True, range:_
    p = 2 # assignment, assignment_lhs_identifier:p, assignment_rhs_atom:2, int_literal, literal:Num
    while p * p <= num: # binary_operator:Mult, comparison_operator:LtE, while (-> +4)
        if primes[p] == True: # comparison_operator:Eq, if (-> +2), if_test_id:p, if_test_id:primes, index, literal:True
            for i in range(p * p, num + 1, p): # binary_operator:Add, binary_operator:Mult, call_argument:, call_argument:p, for:i (-> +1), for_range:_:_:p (-> +1), function_call:range, if_then_branch (-> +1), int_literal, literal:Num, range:_:_:p
                primes[i] = False # assignment, assignment_lhs_identifier:primes, assignment_rhs_atom:False, index, literal:False
        p += 1 # assignment_lhs_identifier:p, assignment_rhs_atom:1, augmented_assignment, int_literal, literal:Num, update_variable:p:1
    for prime in range(2, num + 1): # binary_operator:Add, call_argument:, call_argument:2, for:prime (-> +2), for_range:2:_ (-> +2), function_call:range, int_literal, literal:Num, range:2:_
        if primes[prime]: # if (-> +1), if_test_id:prime, if_test_id:primes, index
            print(prime, end=" ") # call_argument:prime, function_call:print, if_then_branch, literal:Str

# ----------------------------------------------------------------------------------------
# ../Python/maths/qr_decomposition.py
# ----------------------------------------------------------------------------------------
import numpy as np # import:numpy, import_module:numpy
def qr_householder(A): # function:qr_householder (-> +16), function_returning_something:qr_householder (-> +16)
    m, n = A.shape # assignment, assignment_lhs_identifier:m, assignment_lhs_identifier:n, assignment_rhs_atom:A
    t = min(m, n) # assignment, assignment_lhs_identifier:t, assignment_rhs_atom:m, assignment_rhs_atom:n, call_argument:m, call_argument:n, function_call:min
    Q = np.eye(m) # assignment, assignment_lhs_identifier:Q, assignment_rhs_atom:m, assignment_rhs_atom:np, call_argument:m, method_call, method_call_name:eye
    R = A.copy() # assignment, assignment_lhs_identifier:R, assignment_rhs_atom:A, method_call, method_call_name:copy
    for k in range(t - 1): # accumulate_elements:Q_k (-> +10), binary_operator:Sub, call_argument:, for:k (-> +10), for_range:_ (-> +10), function_call:range, int_literal, literal:Num, range:_
        x = R[k:, [k]] # assignment, assignment_lhs_identifier:x, assignment_rhs_atom:R, assignment_rhs_atom:k
        e1 = np.zeros_like(x) # assignment, assignment_lhs_identifier:e1, assignment_rhs_atom:np, assignment_rhs_atom:x, call_argument:x, method_call, method_call_name:zeros_like
        e1[0] = 1.0 # assignment, assignment_lhs_identifier:e1, assignment_rhs_atom:1.0, float_literal, index, int_literal, literal:Num, suggest_constant_definition
        alpha = np.linalg.norm(x) # assignment, assignment_lhs_identifier:alpha, assignment_rhs_atom:np, assignment_rhs_atom:x, call_argument:x, method_call, method_call_name:norm
        v = x + np.sign(x[0]) * alpha * e1 # assignment, assignment_lhs_identifier:v, assignment_rhs_atom:0, assignment_rhs_atom:alpha, assignment_rhs_atom:e1, assignment_rhs_atom:np, assignment_rhs_atom:x, binary_operator:Add, binary_operator:Mult, call_argument:, index, int_literal, literal:Num, method_call, method_call_name:sign
        v /= np.linalg.norm(v) # assignment_lhs_identifier:v, assignment_rhs_atom:np, assignment_rhs_atom:v, augmented_assignment, call_argument:v, method_call, method_call_name:norm, update_variable:v:np, update_variable:v:v
        Q_k = np.eye(m - k) - 2.0 * v @ v.T # assignment, assignment_lhs_identifier:Q_k, assignment_rhs_atom:2.0, assignment_rhs_atom:k, assignment_rhs_atom:m, assignment_rhs_atom:np, assignment_rhs_atom:v, binary_operator:MatMult, binary_operator:Mult, binary_operator:Sub, call_argument:, float_literal, literal:Num, method_call, method_call_name:eye, suggest_constant_definition
        Q_k = np.block([[np.eye(k), np.zeros((k, m - k))], [np.zeros((m - k, k)), Q_k]]) # assignment, assignment_lhs_identifier:Q_k, assignment_rhs_atom:Q_k, assignment_rhs_atom:k, assignment_rhs_atom:m, assignment_rhs_atom:np, binary_operator:Sub, call_argument:, call_argument:k, composition, method_call, method_call_name:block, method_call_name:eye, method_call_name:zeros, update_variable:Q_k:k, update_variable:Q_k:m, update_variable:Q_k:np
        Q = Q @ Q_k.T # assignment, assignment_lhs_identifier:Q, assignment_rhs_atom:Q, assignment_rhs_atom:Q_k, binary_operator:MatMult, suggest_augmented_assignment, update_variable:Q:Q_k
        R = Q_k @ R # assignment, assignment_lhs_identifier:R, assignment_rhs_atom:Q_k, assignment_rhs_atom:R, binary_operator:MatMult, update_variable:R:Q_k
    return Q, R # return

# ----------------------------------------------------------------------------------------
# ../Python/maths/quadratic_equations_complex_numbers.py
# ----------------------------------------------------------------------------------------
from math import sqrt # import:math:sqrt, import_module:math, import_name:sqrt
from typing import Tuple # import:typing:Tuple, import_module:typing, import_name:Tuple
def QuadraticEquation(a: int, b: int, c: int) -> Tuple[str, str]: # function:QuadraticEquation (-> +10), function_returning_something:QuadraticEquation (-> +10), index
    if a == 0: # comparison_operator:Eq, if (-> +1), if_test_id:a, int_literal, literal:Num
        raise ValueError("Coefficient 'a' must not be zero for quadratic equations.") # call_argument:, function_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    delta = b * b - 4 * a * c # assignment, assignment_lhs_identifier:delta, assignment_rhs_atom:4, assignment_rhs_atom:a, assignment_rhs_atom:b, assignment_rhs_atom:c, binary_operator:Mult, binary_operator:Sub, int_literal, literal:Num, suggest_constant_definition
    if delta >= 0: # comparison_operator:GtE, if (-> +1), if_test_id:delta, int_literal, literal:Num
        return str((-b + sqrt(delta)) / (2 * a)), str((-b - sqrt(delta)) / (2 * a)) # binary_operator:Add, binary_operator:Div, binary_operator:Mult, binary_operator:Sub, call_argument:, call_argument:delta, composition, function_call:sqrt, function_call:str, if_then_branch, int_literal, literal:Num, return, unary_operator:USub
    snd = sqrt(-delta) # assignment, assignment_lhs_identifier:snd, assignment_rhs_atom:delta, call_argument:, function_call:sqrt, unary_operator:USub
    if b == 0: # comparison_operator:Eq, if (-> +1), if_test_id:b, int_literal, literal:Num
        return f"({snd} * i) / 2", f"({snd} * i) / {2 * a}" # binary_operator:Mult, if_then_branch, int_literal, literal:Num, literal:Str, return
    b = -abs(b) # assignment, assignment_lhs_identifier:b, assignment_rhs_atom:b, call_argument:b, function_call:abs, unary_operator:USub
    return f"({b}+{snd} * i) / 2", f"({b}+{snd} * i) / {2 * a}" # binary_operator:Mult, int_literal, literal:Num, literal:Str, return
def main(): # function:main (-> +2), function_returning_nothing:main (-> +2)
    solutions = QuadraticEquation(a=5, b=6, c=1) # assignment, assignment_lhs_identifier:solutions, assignment_rhs_atom:1, assignment_rhs_atom:5, assignment_rhs_atom:6, function_call:QuadraticEquation, int_literal, literal:Num, suggest_constant_definition
    print("The equation solutions are: {} and {}".format(*solutions)) # call_argument:, composition, function_call:print, literal:Str, method_call, method_call_name:format

# ----------------------------------------------------------------------------------------
# ../Python/maths/radix2_fft.py
# ----------------------------------------------------------------------------------------
import mpmath # import:mpmath, import_module:mpmath
import numpy as np # import:numpy, import_module:numpy
class FFT:
    def __init__(self, polyA=[0], polyB=[0]): # function:__init__ (-> +17), function_returning_nothing:__init__ (-> +17), function_with_default_positional_arguments:__init__ (-> +17), int_literal, literal:List, literal:Num
        self.polyA = list(polyA)[:] # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:polyA, call_argument:polyA, function_call:list, slice
        self.polyB = list(polyB)[:] # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:polyB, call_argument:polyB, function_call:list, slice
        while self.polyA[-1] == 0: # comparison_operator:Eq, evolve_state (-> +1), index, int_literal, literal:Num, negative_index:-1, while (-> +1)
            self.polyA.pop() # method_call, method_call_name:pop
        self.len_A = len(self.polyA) # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:self, call_argument:, function_call:len
        while self.polyB[-1] == 0: # comparison_operator:Eq, evolve_state (-> +1), index, int_literal, literal:Num, negative_index:-1, while (-> +1)
            self.polyB.pop() # method_call, method_call_name:pop
        self.len_B = len(self.polyB) # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:self, call_argument:, function_call:len
        self.C_max_length = int( # assignment, assignment_lhs_identifier:self, composition, function_call:int, update_variable:self:1, update_variable:self:2, update_variable:self:np
            2 ** np.ceil(np.log2(len(self.polyA) + len(self.polyB) - 1)) # assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:np, assignment_rhs_atom:self, binary_operator:Add, binary_operator:Pow, binary_operator:Sub, call_argument:, composition, function_call:len, int_literal, literal:Num, method_call, method_call_name:ceil, method_call_name:log2
        )
        while len(self.polyA) < self.C_max_length: # call_argument:, comparison_operator:Lt, evolve_state (-> +1), function_call:len, while (-> +1)
            self.polyA.append(0) # call_argument:0, int_literal, literal:Num, method_call, method_call_name:append
        while len(self.polyB) < self.C_max_length: # call_argument:, comparison_operator:Lt, evolve_state (-> +1), function_call:len, while (-> +1)
            self.polyB.append(0) # call_argument:0, int_literal, literal:Num, method_call, method_call_name:append
        self.root = complex(mpmath.root(x=1, n=self.C_max_length, k=1)) # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:1, assignment_rhs_atom:mpmath, assignment_rhs_atom:self, call_argument:, composition, function_call:complex, int_literal, literal:Num, method_call, method_call_name:root, update_variable:self:1, update_variable:self:mpmath
        self.product = self.__multiply() # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:self, method_call, method_call_name:__multiply
    def __DFT(self, which): # function:__DFT (-> +23), function_returning_something:__DFT (-> +23)
        if which == "A": # comparison_operator:Eq, if (-> +3), if_test_id:which, literal:Str, suggest_conditional_expression (-> +3)
            dft = [[x] for x in self.polyA] # assignment, assignment_lhs_identifier:dft, assignment_rhs_atom:self, assignment_rhs_atom:x, comprehension:List, comprehension_for_count:1, if_then_branch
        else:
            dft = [[x] for x in self.polyB] # assignment, assignment_lhs_identifier:dft, assignment_rhs_atom:self, assignment_rhs_atom:x, comprehension:List, comprehension_for_count:1, if_else_branch
        if len(dft) <= 1: # call_argument:dft, comparison_operator:LtE, function_call:len, if (-> +1), if_test_id:dft, if_test_id:len, int_literal, literal:Num
            return dft[0] # if_then_branch, index, int_literal, literal:Num, return
        next_ncol = self.C_max_length // 2 # assignment, assignment_lhs_identifier:next_ncol, assignment_rhs_atom:2, assignment_rhs_atom:self, binary_operator:FloorDiv, int_literal, literal:Num
        while next_ncol > 0: # comparison_operator:Gt, evolve_state (-> +14), int_literal, literal:Num, while (-> +14)
            new_dft = [[] for i in range(next_ncol)] # assignment, assignment_lhs_identifier:new_dft, assignment_rhs_atom:i, assignment_rhs_atom:next_ncol, call_argument:next_ncol, comprehension:List, comprehension_for_count:1, function_call:range, literal:List, range:next_ncol
            root = self.root ** next_ncol # assignment, assignment_lhs_identifier:root, assignment_rhs_atom:next_ncol, assignment_rhs_atom:self, binary_operator:Pow
            current_root = 1 # assignment, assignment_lhs_identifier:current_root, assignment_rhs_atom:1, int_literal, literal:Num
            for j in range(self.C_max_length // (next_ncol * 2)): # binary_operator:FloorDiv, binary_operator:Mult, call_argument:, for:j (-> +3), for_range:_ (-> +3), for_range:next_ncol (-> +3), function_call:range, int_literal, literal:Num, range:_
                for i in range(next_ncol): # call_argument:next_ncol, for:i (-> +1), for_range:next_ncol (-> +1), function_call:range, nested_for:1 (-> +1), range:next_ncol
                    new_dft[i].append(dft[i][j] + current_root * dft[i + next_ncol][j]) # binary_operator:Add, binary_operator:Mult, call_argument:, index, index_arithmetic, method_call, method_call_name:append
                current_root *= root # assignment_lhs_identifier:current_root, assignment_rhs_atom:root, augmented_assignment, update_variable:current_root:root
            current_root = 1 # assignment, assignment_lhs_identifier:current_root, assignment_rhs_atom:1, int_literal, literal:Num
            for j in range(self.C_max_length // (next_ncol * 2)): # binary_operator:FloorDiv, binary_operator:Mult, call_argument:, for:j (-> +3), for_range:_ (-> +3), for_range:next_ncol (-> +3), function_call:range, int_literal, literal:Num, range:_
                for i in range(next_ncol): # call_argument:next_ncol, for:i (-> +1), for_range:next_ncol (-> +1), function_call:range, nested_for:1 (-> +1), range:next_ncol
                    new_dft[i].append(dft[i][j] - current_root * dft[i + next_ncol][j]) # binary_operator:Add, binary_operator:Mult, binary_operator:Sub, call_argument:, index, index_arithmetic, method_call, method_call_name:append
                current_root *= root # assignment_lhs_identifier:current_root, assignment_rhs_atom:root, augmented_assignment, update_variable:current_root:root
            dft = new_dft # assignment, assignment_lhs_identifier:dft, assignment_rhs_atom:new_dft
            next_ncol = next_ncol // 2 # assignment, assignment_lhs_identifier:next_ncol, assignment_rhs_atom:2, assignment_rhs_atom:next_ncol, binary_operator:FloorDiv, int_literal, literal:Num, suggest_augmented_assignment, update_variable:next_ncol:2
        return dft[0] # index, int_literal, literal:Num, return
    def __multiply(self): # function:__multiply (-> +35), function_returning_something:__multiply (-> +35)
        dftA = self.__DFT("A") # assignment, assignment_lhs_identifier:dftA, assignment_rhs_atom:self, call_argument:, literal:Str, method_call, method_call_name:__DFT
        dftB = self.__DFT("B") # assignment, assignment_lhs_identifier:dftB, assignment_rhs_atom:self, call_argument:, literal:Str, method_call, method_call_name:__DFT
        inverseC = [[dftA[i] * dftB[i] for i in range(self.C_max_length)]] # assignment, assignment_lhs_identifier:inverseC, assignment_rhs_atom:dftA, assignment_rhs_atom:dftB, assignment_rhs_atom:i, assignment_rhs_atom:self, binary_operator:Mult, call_argument:, comprehension:List, comprehension_for_count:1, function_call:range, index, range:_
        del dftA
        del dftB
        if len(inverseC[0]) <= 1: # call_argument:, comparison_operator:LtE, function_call:len, if (-> +1), if_test_id:inverseC, if_test_id:len, index, int_literal, literal:Num
            return inverseC[0] # if_then_branch, index, int_literal, literal:Num, return
        next_ncol = 2 # assignment, assignment_lhs_identifier:next_ncol, assignment_rhs_atom:2, int_literal, literal:Num
        while next_ncol <= self.C_max_length: # comparison_operator:LtE, evolve_state (-> +22), while (-> +22)
            new_inverseC = [[] for i in range(next_ncol)] # assignment, assignment_lhs_identifier:new_inverseC, assignment_rhs_atom:i, assignment_rhs_atom:next_ncol, call_argument:next_ncol, comprehension:List, comprehension_for_count:1, function_call:range, literal:List, range:next_ncol
            root = self.root ** (next_ncol // 2) # assignment, assignment_lhs_identifier:root, assignment_rhs_atom:2, assignment_rhs_atom:next_ncol, assignment_rhs_atom:self, binary_operator:FloorDiv, binary_operator:Pow, int_literal, literal:Num
            current_root = 1 # assignment, assignment_lhs_identifier:current_root, assignment_rhs_atom:1, int_literal, literal:Num
            for j in range(self.C_max_length // next_ncol): # binary_operator:FloorDiv, call_argument:, for:j (-> +16), for_range:_ (-> +16), function_call:range, range:_
                for i in range(next_ncol // 2): # binary_operator:FloorDiv, call_argument:, for:i (-> +13), for_range:_ (-> +13), function_call:range, int_literal, literal:Num, nested_for:1 (-> +13), range:_
                    new_inverseC[i].append( # index, method_call, method_call_name:append
                        ( # binary_operator:Div, call_argument:
                            inverseC[i][j] # binary_operator:Add, index
                            + inverseC[i][j + self.C_max_length // next_ncol] # binary_operator:Add, binary_operator:FloorDiv, index, index_arithmetic
                        )
                        / 2 # int_literal, literal:Num
                    )
                    new_inverseC[i + next_ncol // 2].append( # binary_operator:Add, binary_operator:FloorDiv, index, index_arithmetic, int_literal, literal:Num, method_call, method_call_name:append
                        ( # binary_operator:Div, call_argument:
                            inverseC[i][j] # binary_operator:Sub, index
                            - inverseC[i][j + self.C_max_length // next_ncol] # binary_operator:Add, binary_operator:FloorDiv, index, index_arithmetic
                        )
                        / (2 * current_root) # binary_operator:Mult, int_literal, literal:Num
                    )
                current_root *= root # assignment_lhs_identifier:current_root, assignment_rhs_atom:root, augmented_assignment, update_variable:current_root:root
            inverseC = new_inverseC # assignment, assignment_lhs_identifier:inverseC, assignment_rhs_atom:new_inverseC
            next_ncol *= 2 # assignment_lhs_identifier:next_ncol, assignment_rhs_atom:2, augmented_assignment, int_literal, literal:Num, update_variable:next_ncol:2
        inverseC = [round(x[0].real, 8) + round(x[0].imag, 8) * 1j for x in inverseC] # assignment, assignment_lhs_identifier:inverseC, assignment_rhs_atom:0, assignment_rhs_atom:1j, assignment_rhs_atom:8, assignment_rhs_atom:inverseC, assignment_rhs_atom:x, binary_operator:Add, binary_operator:Mult, call_argument:, call_argument:8, comprehension:List, comprehension_for_count:1, function_call:round, imaginary_literal, index, int_literal, literal:Num, suggest_constant_definition, update_variable:inverseC:0, update_variable:inverseC:1j, update_variable:inverseC:8, update_variable:inverseC:x
        while inverseC[-1] == 0: # comparison_operator:Eq, evolve_state (-> +1), index, int_literal, literal:Num, negative_index:-1, while (-> +1)
            inverseC.pop() # method_call, method_call_name:pop, method_call_object:inverseC
        return inverseC # return:inverseC
    def __str__(self): # function:__str__ (-> +10), function_returning_something:__str__ (-> +10)
        A = "A = " + " + ".join( # assignment, assignment_lhs_identifier:A, binary_operator:Add, composition, literal:Str, method_call, method_call_name:join
            f"{coef}*x^{i}" for coef, i in enumerate(self.polyA[: self.len_A]) # assignment_rhs_atom:coef, assignment_rhs_atom:i, assignment_rhs_atom:self, call_argument:, comprehension:Generator, comprehension_for_count:1, function_call:enumerate, literal:Str, slice
        )
        B = "B = " + " + ".join( # assignment, assignment_lhs_identifier:B, binary_operator:Add, composition, literal:Str, method_call, method_call_name:join
            f"{coef}*x^{i}" for coef, i in enumerate(self.polyB[: self.len_B]) # assignment_rhs_atom:coef, assignment_rhs_atom:i, assignment_rhs_atom:self, call_argument:, comprehension:Generator, comprehension_for_count:1, function_call:enumerate, literal:Str, slice
        )
        C = "A*B = " + " + ".join( # assignment, assignment_lhs_identifier:C, binary_operator:Add, composition, literal:Str, method_call, method_call_name:join
            f"{coef}*x^{i}" for coef, i in enumerate(self.product) # assignment_rhs_atom:coef, assignment_rhs_atom:i, assignment_rhs_atom:self, call_argument:, comprehension:Generator, comprehension_for_count:1, function_call:enumerate, literal:Str
        )
        return "\n".join((A, B, C)) # call_argument:, literal:Str, method_call, method_call_name:join, return

# ----------------------------------------------------------------------------------------
# ../Python/maths/runge_kutta.py
# ----------------------------------------------------------------------------------------
import numpy as np # import:numpy, import_module:numpy
def runge_kutta(f, y0, x0, h, x_end): # function:runge_kutta (-> +12), function_returning_something:runge_kutta (-> +12)
    N = int(np.ceil((x_end - x0) / h)) # assignment, assignment_lhs_identifier:N, assignment_rhs_atom:h, assignment_rhs_atom:np, assignment_rhs_atom:x0, assignment_rhs_atom:x_end, binary_operator:Div, binary_operator:Sub, call_argument:, composition, function_call:int, method_call, method_call_name:ceil
    y = np.zeros((N + 1,)) # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:1, assignment_rhs_atom:N, assignment_rhs_atom:np, binary_operator:Add, call_argument:, int_literal, literal:Num, method_call, method_call_name:zeros
    y[0] = y0 # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:y0, index, int_literal, literal:Num
    x = x0 # assignment, assignment_lhs_identifier:x, assignment_rhs_atom:x0
    for k in range(N): # accumulate_elements:y (-> +6), call_argument:N, for:k (-> +6), for_range:N (-> +6), function_call:range, range:N
        k1 = f(x, y[k]) # assignment, assignment_lhs_identifier:k1, assignment_rhs_atom:k, assignment_rhs_atom:x, assignment_rhs_atom:y, call_argument:, call_argument:x, function_call:f, index
        k2 = f(x + 0.5 * h, y[k] + 0.5 * h * k1) # assignment, assignment_lhs_identifier:k2, assignment_rhs_atom:0.5, assignment_rhs_atom:h, assignment_rhs_atom:k, assignment_rhs_atom:k1, assignment_rhs_atom:x, assignment_rhs_atom:y, binary_operator:Add, binary_operator:Mult, call_argument:, float_literal, function_call:f, index, literal:Num, suggest_constant_definition
        k3 = f(x + 0.5 * h, y[k] + 0.5 * h * k2) # assignment, assignment_lhs_identifier:k3, assignment_rhs_atom:0.5, assignment_rhs_atom:h, assignment_rhs_atom:k, assignment_rhs_atom:k2, assignment_rhs_atom:x, assignment_rhs_atom:y, binary_operator:Add, binary_operator:Mult, call_argument:, float_literal, function_call:f, index, literal:Num, suggest_constant_definition
        k4 = f(x + h, y[k] + h * k3) # assignment, assignment_lhs_identifier:k4, assignment_rhs_atom:h, assignment_rhs_atom:k, assignment_rhs_atom:k3, assignment_rhs_atom:x, assignment_rhs_atom:y, binary_operator:Add, binary_operator:Mult, call_argument:, function_call:f, index
        y[k + 1] = y[k] + (1 / 6) * h * (k1 + 2 * k2 + 2 * k3 + k4) # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:6, assignment_rhs_atom:h, assignment_rhs_atom:k, assignment_rhs_atom:k1, assignment_rhs_atom:k2, assignment_rhs_atom:k3, assignment_rhs_atom:k4, assignment_rhs_atom:y, binary_operator:Add, binary_operator:Div, binary_operator:Mult, index, index_arithmetic, int_literal, literal:Num, suggest_constant_definition, update_variable:y:1, update_variable:y:2, update_variable:y:6, update_variable:y:h, update_variable:y:k, update_variable:y:k1, update_variable:y:k2, update_variable:y:k3, update_variable:y:k4
        x += h # assignment_lhs_identifier:x, assignment_rhs_atom:h, augmented_assignment, update_variable:x:h
    return y # return:y

# ----------------------------------------------------------------------------------------
# ../Python/maths/segmented_sieve.py
# ----------------------------------------------------------------------------------------
import math # import:math, import_module:math
def sieve(n): # function:sieve (-> +33), function_returning_something:sieve (-> +33)
    in_prime = [] # assignment, assignment_lhs_identifier:in_prime, literal:List
    start = 2 # assignment, assignment_lhs_identifier:start, assignment_rhs_atom:2, int_literal, literal:Num
    end = int(math.sqrt(n)) # assignment, assignment_lhs_identifier:end, assignment_rhs_atom:math, assignment_rhs_atom:n, call_argument:, call_argument:n, composition, function_call:int, method_call, method_call_name:sqrt
    temp = [True] * (end + 1) # assignment, assignment_lhs_identifier:temp, assignment_rhs_atom:1, assignment_rhs_atom:True, assignment_rhs_atom:end, binary_operator:Add, binary_operator:Mult, int_literal, literal:List, literal:Num, literal:True
    prime = [] # assignment, assignment_lhs_identifier:prime, literal:List
    while start <= end: # comparison_operator:LtE, while (-> +6)
        if temp[start] is True: # comparison_operator:Is, if (-> +4), if_test_id:start, if_test_id:temp, index, literal:True
            in_prime.append(start) # call_argument:start, if_then_branch (-> +3), method_call, method_call_name:append, method_call_object:in_prime, update_variable:in_prime:start
            for i in range(start * start, end + 1, start): # binary_operator:Add, binary_operator:Mult, call_argument:, call_argument:start, for:i (-> +2), for_range:_:_:start (-> +2), function_call:range, int_literal, literal:Num, range:_:_:start
                if temp[i] is True: # comparison_operator:Is, if (-> +1), if_test_id:i, if_test_id:temp, index, literal:True, nested_if:1 (-> +1)
                    temp[i] = False # assignment, assignment_lhs_identifier:temp, assignment_rhs_atom:False, if_then_branch, index, literal:False
        start += 1 # assignment_lhs_identifier:start, assignment_rhs_atom:1, augmented_assignment, int_literal, literal:Num, update_variable:start:1
    prime += in_prime # assignment_lhs_identifier:prime, assignment_rhs_atom:in_prime, augmented_assignment, update_variable:prime:in_prime
    low = end + 1 # assignment, assignment_lhs_identifier:low, assignment_rhs_atom:1, assignment_rhs_atom:end, binary_operator:Add, int_literal, literal:Num
    high = low + end - 1 # assignment, assignment_lhs_identifier:high, assignment_rhs_atom:1, assignment_rhs_atom:end, assignment_rhs_atom:low, binary_operator:Add, binary_operator:Sub, int_literal, literal:Num
    if high > n: # comparison_operator:Gt, if (-> +1), if_test_id:high, if_test_id:n
        high = n # assignment, assignment_lhs_identifier:high, assignment_rhs_atom:n, if_then_branch
    while low <= n: # comparison_operator:LtE, while (-> +14)
        temp = [True] * (high - low + 1) # assignment, assignment_lhs_identifier:temp, assignment_rhs_atom:1, assignment_rhs_atom:True, assignment_rhs_atom:high, assignment_rhs_atom:low, binary_operator:Add, binary_operator:Mult, binary_operator:Sub, int_literal, literal:List, literal:Num, literal:True
        for each in in_prime: # accumulate_elements:t (-> +5), for:each (-> +5), for_each (-> +5), for_range:t:_:each (-> +5)
            t = math.floor(low / each) * each # assignment, assignment_lhs_identifier:t, assignment_rhs_atom:each, assignment_rhs_atom:low, assignment_rhs_atom:math, binary_operator:Div, binary_operator:Mult, call_argument:, method_call, method_call_name:floor
            if t < low: # comparison_operator:Lt, if (-> +1), if_test_id:low, if_test_id:t
                t += each # assignment_lhs_identifier:t, assignment_rhs_atom:each, augmented_assignment, if_then_branch, update_variable:t:each
            for j in range(t, high + 1, each): # binary_operator:Add, call_argument:, call_argument:each, call_argument:t, for:j (-> +1), for_range:t:_:each (-> +1), function_call:range, int_literal, literal:Num, nested_for:1 (-> +1), range:t:_:each
                temp[j - low] = False # assignment, assignment_lhs_identifier:temp, assignment_rhs_atom:False, binary_operator:Sub, index, index_arithmetic, literal:False
        for j in range(len(temp)): # call_argument:, call_argument:temp, composition, for:j (-> +2), for_indexes (-> +2), for_range:_ (-> +2), function_call:len, function_call:range, range:_
            if temp[j] is True: # comparison_operator:Is, if (-> +1), if_test_id:j, if_test_id:temp, index, literal:True
                prime.append(j + low) # binary_operator:Add, call_argument:, if_then_branch, method_call, method_call_name:append, method_call_object:prime, update_variable:prime:
        low = high + 1 # assignment, assignment_lhs_identifier:low, assignment_rhs_atom:1, assignment_rhs_atom:high, binary_operator:Add, int_literal, literal:Num
        high = low + end - 1 # assignment, assignment_lhs_identifier:high, assignment_rhs_atom:1, assignment_rhs_atom:end, assignment_rhs_atom:low, binary_operator:Add, binary_operator:Sub, int_literal, literal:Num
        if high > n: # comparison_operator:Gt, if (-> +1), if_test_id:high, if_test_id:n
            high = n # assignment, assignment_lhs_identifier:high, assignment_rhs_atom:n, if_then_branch
    return prime # return:prime
print(sieve(10 ** 6)) # binary_operator:Pow, call_argument:, composition, function_call:print, function_call:sieve, int_literal, literal:Num

# ----------------------------------------------------------------------------------------
# ../Python/maths/sieve_of_eratosthenes.py
# ----------------------------------------------------------------------------------------
"""
Sieve of Eratosthones
The sieve of Eratosthenes is an algorithm used to find prime numbers, less than or equal to a given value.
Illustration: https://upload.wikimedia.org/wikipedia/commons/b/b9/Sieve_of_Eratosthenes_animation.gif
Reference: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
doctest provider: Bruno Simas Hadlich (https://github.com/brunohadlich)
Also thanks Dmitry (https://github.com/LizardWizzard) for finding the problem
""" # literal:Str
import math # import:math, import_module:math
def sieve(n): # function:sieve (-> +15), function_returning_something:sieve (-> +15)
    l = [True] * (n + 1) # assignment, assignment_lhs_identifier:l, assignment_rhs_atom:1, assignment_rhs_atom:True, assignment_rhs_atom:n, binary_operator:Add, binary_operator:Mult, int_literal, literal:List, literal:Num, literal:True
    prime = [] # assignment, assignment_lhs_identifier:prime, literal:List
    start = 2 # assignment, assignment_lhs_identifier:start, assignment_rhs_atom:2, int_literal, literal:Num
    end = int(math.sqrt(n)) # assignment, assignment_lhs_identifier:end, assignment_rhs_atom:math, assignment_rhs_atom:n, call_argument:, call_argument:n, composition, function_call:int, method_call, method_call_name:sqrt
    while start <= end: # comparison_operator:LtE, while (-> +6)
        if l[start] is True: # comparison_operator:Is, if (-> +4), if_test_id:l, if_test_id:start, index, literal:True
            prime.append(start) # call_argument:start, if_then_branch (-> +3), method_call, method_call_name:append, method_call_object:prime, update_variable:prime:start
            for i in range(start * start, n + 1, start): # binary_operator:Add, binary_operator:Mult, call_argument:, call_argument:start, for:i (-> +2), for_range:_:_:start (-> +2), function_call:range, int_literal, literal:Num, range:_:_:start
                if l[i] is True: # comparison_operator:Is, if (-> +1), if_test_id:i, if_test_id:l, index, literal:True, nested_if:1 (-> +1)
                    l[i] = False # assignment, assignment_lhs_identifier:l, assignment_rhs_atom:False, if_then_branch, index, literal:False
        start += 1 # assignment_lhs_identifier:start, assignment_rhs_atom:1, augmented_assignment, int_literal, literal:Num, update_variable:start:1
    for j in range(end + 1, n + 1): # accumulate_elements:prime (-> +2), binary_operator:Add, call_argument:, for:j (-> +2), for_range:_:_ (-> +2), function_call:range, int_literal, literal:Num, range:_:_
        if l[j] is True: # comparison_operator:Is, if (-> +1), if_test_id:j, if_test_id:l, index, literal:True
            prime.append(j) # call_argument:j, if_then_branch, method_call, method_call_name:append, method_call_object:prime, update_variable:prime:j
    return prime # return:prime

# ----------------------------------------------------------------------------------------
# ../Python/maths/simpson_rule.py
# ----------------------------------------------------------------------------------------
def method_2(boundary, steps): # function:method_2 (-> +12), function_returning_something:method_2 (-> +12)
    h = (boundary[1] - boundary[0]) / steps # assignment, assignment_lhs_identifier:h, assignment_rhs_atom:0, assignment_rhs_atom:1, assignment_rhs_atom:boundary, assignment_rhs_atom:steps, binary_operator:Div, binary_operator:Sub, index, int_literal, literal:Num
    a = boundary[0] # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:0, assignment_rhs_atom:boundary, index, int_literal, literal:Num
    b = boundary[1] # assignment, assignment_lhs_identifier:b, assignment_rhs_atom:1, assignment_rhs_atom:boundary, index, int_literal, literal:Num
    x_i = make_points(a, b, h) # assignment, assignment_lhs_identifier:x_i, assignment_rhs_atom:a, assignment_rhs_atom:b, assignment_rhs_atom:h, call_argument:a, call_argument:b, call_argument:h, function_call:make_points
    y = 0.0 # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:0.0, float_literal, literal:Num, suggest_constant_definition
    y += (h / 3.0) * f(a) # assignment_lhs_identifier:y, assignment_rhs_atom:3.0, assignment_rhs_atom:a, assignment_rhs_atom:h, augmented_assignment, binary_operator:Div, binary_operator:Mult, call_argument:a, float_literal, function_call:f, literal:Num, suggest_constant_definition, update_variable:y:3.0, update_variable:y:a, update_variable:y:h
    cnt = 2 # assignment, assignment_lhs_identifier:cnt, assignment_rhs_atom:2, int_literal, literal:Num
    for i in x_i: # accumulate_elements:y (-> +2), for:i (-> +2), for_each (-> +2)
        y += (h / 3) * (4 - 2 * (cnt % 2)) * f(i) # assignment_lhs_identifier:y, assignment_rhs_atom:2, assignment_rhs_atom:3, assignment_rhs_atom:4, assignment_rhs_atom:cnt, assignment_rhs_atom:h, assignment_rhs_atom:i, augmented_assignment, binary_operator:Div, binary_operator:Mod, binary_operator:Mult, binary_operator:Sub, call_argument:i, function_call:f, int_literal, literal:Num, suggest_constant_definition, update_variable:y:2, update_variable:y:3, update_variable:y:4, update_variable:y:cnt, update_variable:y:h, update_variable:y:i
        cnt += 1 # assignment_lhs_identifier:cnt, assignment_rhs_atom:1, augmented_assignment, int_literal, literal:Num, update_variable:cnt:1
    y += (h / 3.0) * f(b) # assignment_lhs_identifier:y, assignment_rhs_atom:3.0, assignment_rhs_atom:b, assignment_rhs_atom:h, augmented_assignment, binary_operator:Div, binary_operator:Mult, call_argument:b, float_literal, function_call:f, literal:Num, suggest_constant_definition, update_variable:y:3.0, update_variable:y:b, update_variable:y:h
    return y # return:y
def make_points(a, b, h): # function:make_points (-> +4), generator:make_points (-> +4)
    x = a + h # assignment, assignment_lhs_identifier:x, assignment_rhs_atom:a, assignment_rhs_atom:h, binary_operator:Add
    while x < (b - h): # binary_operator:Sub, comparison_operator:Lt, while (-> +2)
        yield x # yield:x
        x = x + h # assignment, assignment_lhs_identifier:x, assignment_rhs_atom:h, assignment_rhs_atom:x, binary_operator:Add, suggest_augmented_assignment, update_variable:x:h
def f(x): # function:f (-> +2), function_returning_something:f (-> +2)
    y = (x - 0) * (x - 0) # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:0, assignment_rhs_atom:x, binary_operator:Mult, binary_operator:Sub, int_literal, literal:Num
    return y # return:y
def main(): # function:main (-> +6), function_returning_nothing:main (-> +6)
    a = 0.0 # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:0.0, float_literal, literal:Num, suggest_constant_definition
    b = 1.0 # assignment, assignment_lhs_identifier:b, assignment_rhs_atom:1.0, float_literal, literal:Num, suggest_constant_definition
    steps = 10.0 # assignment, assignment_lhs_identifier:steps, assignment_rhs_atom:10.0, float_literal, literal:Num, suggest_constant_definition
    boundary = [a, b] # assignment, assignment_lhs_identifier:boundary, assignment_rhs_atom:a, assignment_rhs_atom:b
    y = method_2(boundary, steps) # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:boundary, assignment_rhs_atom:steps, call_argument:boundary, call_argument:steps, function_call:method_2
    print("y = {0}".format(y)) # call_argument:, call_argument:y, composition, function_call:print, literal:Str, method_call, method_call_name:format

# ----------------------------------------------------------------------------------------
# ../Python/maths/softmax.py
# ----------------------------------------------------------------------------------------
import numpy as np # import:numpy, import_module:numpy
def softmax(vector): # function:softmax (-> +4), function_returning_something:softmax (-> +4)
    exponentVector = np.exp(vector) # assignment, assignment_lhs_identifier:exponentVector, assignment_rhs_atom:np, assignment_rhs_atom:vector, call_argument:vector, method_call, method_call_name:exp
    sumOfExponents = np.sum(exponentVector) # assignment, assignment_lhs_identifier:sumOfExponents, assignment_rhs_atom:exponentVector, assignment_rhs_atom:np, call_argument:exponentVector, method_call, method_call_name:sum
    softmax_vector = exponentVector / sumOfExponents # assignment, assignment_lhs_identifier:softmax_vector, assignment_rhs_atom:exponentVector, assignment_rhs_atom:sumOfExponents, binary_operator:Div
    return softmax_vector # return:softmax_vector

# ----------------------------------------------------------------------------------------
# ../Python/maths/sum_of_arithmetic_series.py
# ----------------------------------------------------------------------------------------
def sum_of_series(first_term, common_diff, num_of_terms): # function:sum_of_series (-> +2), function_returning_something:sum_of_series (-> +2)
    sum = (num_of_terms / 2) * (2 * first_term + (num_of_terms - 1) * common_diff) # assignment, assignment_lhs_identifier:sum, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:common_diff, assignment_rhs_atom:first_term, assignment_rhs_atom:num_of_terms, binary_operator:Add, binary_operator:Div, binary_operator:Mult, binary_operator:Sub, int_literal, literal:Num
    return sum # return:sum
def main(): # function:main (-> +1), function_returning_nothing:main (-> +1)
    print(sum_of_series(1, 1, 10)) # call_argument:, call_argument:1, call_argument:10, composition, function_call:print, function_call:sum_of_series, int_literal, literal:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/test_prime_check.py
# ----------------------------------------------------------------------------------------
from .prime_check import Test # import:prime_check:Test, import_module:prime_check, import_name:Test
Test() # function_call:Test

# ----------------------------------------------------------------------------------------
# ../Python/maths/trapezoidal_rule.py
# ----------------------------------------------------------------------------------------
def method_1(boundary, steps): # function:method_1 (-> +10), function_returning_something:method_1 (-> +10)
    h = (boundary[1] - boundary[0]) / steps # assignment, assignment_lhs_identifier:h, assignment_rhs_atom:0, assignment_rhs_atom:1, assignment_rhs_atom:boundary, assignment_rhs_atom:steps, binary_operator:Div, binary_operator:Sub, index, int_literal, literal:Num
    a = boundary[0] # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:0, assignment_rhs_atom:boundary, index, int_literal, literal:Num
    b = boundary[1] # assignment, assignment_lhs_identifier:b, assignment_rhs_atom:1, assignment_rhs_atom:boundary, index, int_literal, literal:Num
    x_i = make_points(a, b, h) # assignment, assignment_lhs_identifier:x_i, assignment_rhs_atom:a, assignment_rhs_atom:b, assignment_rhs_atom:h, call_argument:a, call_argument:b, call_argument:h, function_call:make_points
    y = 0.0 # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:0.0, float_literal, literal:Num, suggest_constant_definition
    y += (h / 2.0) * f(a) # assignment_lhs_identifier:y, assignment_rhs_atom:2.0, assignment_rhs_atom:a, assignment_rhs_atom:h, augmented_assignment, binary_operator:Div, binary_operator:Mult, call_argument:a, float_literal, function_call:f, literal:Num, suggest_constant_definition, update_variable:y:2.0, update_variable:y:a, update_variable:y:h
    for i in x_i: # accumulate_elements:y (-> +1), for:i (-> +1), for_each (-> +1)
        y += h * f(i) # assignment_lhs_identifier:y, assignment_rhs_atom:h, assignment_rhs_atom:i, augmented_assignment, binary_operator:Mult, call_argument:i, function_call:f, update_variable:y:h, update_variable:y:i
    y += (h / 2.0) * f(b) # assignment_lhs_identifier:y, assignment_rhs_atom:2.0, assignment_rhs_atom:b, assignment_rhs_atom:h, augmented_assignment, binary_operator:Div, binary_operator:Mult, call_argument:b, float_literal, function_call:f, literal:Num, suggest_constant_definition, update_variable:y:2.0, update_variable:y:b, update_variable:y:h
    return y # return:y
def make_points(a, b, h): # function:make_points (-> +4), generator:make_points (-> +4)
    x = a + h # assignment, assignment_lhs_identifier:x, assignment_rhs_atom:a, assignment_rhs_atom:h, binary_operator:Add
    while x < (b - h): # binary_operator:Sub, comparison_operator:Lt, while (-> +2)
        yield x # yield:x
        x = x + h # assignment, assignment_lhs_identifier:x, assignment_rhs_atom:h, assignment_rhs_atom:x, binary_operator:Add, suggest_augmented_assignment, update_variable:x:h
def f(x): # function:f (-> +2), function_returning_something:f (-> +2)
    y = (x - 0) * (x - 0) # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:0, assignment_rhs_atom:x, binary_operator:Mult, binary_operator:Sub, int_literal, literal:Num
    return y # return:y
def main(): # function:main (-> +6), function_returning_nothing:main (-> +6)
    a = 0.0 # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:0.0, float_literal, literal:Num, suggest_constant_definition
    b = 1.0 # assignment, assignment_lhs_identifier:b, assignment_rhs_atom:1.0, float_literal, literal:Num, suggest_constant_definition
    steps = 10.0 # assignment, assignment_lhs_identifier:steps, assignment_rhs_atom:10.0, float_literal, literal:Num, suggest_constant_definition
    boundary = [a, b] # assignment, assignment_lhs_identifier:boundary, assignment_rhs_atom:a, assignment_rhs_atom:b
    y = method_1(boundary, steps) # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:boundary, assignment_rhs_atom:steps, call_argument:boundary, call_argument:steps, function_call:method_1
    print("y = {0}".format(y)) # call_argument:, call_argument:y, composition, function_call:print, literal:Str, method_call, method_call_name:format

# ----------------------------------------------------------------------------------------
# ../Python/maths/volume.py
# ----------------------------------------------------------------------------------------
from math import pi # import:math:pi, import_module:math, import_name:pi
def vol_cube(side_length): # function:vol_cube (-> +1), function_returning_something:vol_cube (-> +1)
    return float(side_length ** 3) # binary_operator:Pow, call_argument:, function_call:float, function_tail_call:float, int_literal, literal:Num, return, suggest_constant_definition
def vol_cuboid(width, height, length): # function:vol_cuboid (-> +1), function_returning_something:vol_cuboid (-> +1)
    return float(width * height * length) # binary_operator:Mult, call_argument:, function_call:float, function_tail_call:float, return
def vol_cone(area_of_base, height): # function:vol_cone (-> +1), function_returning_something:vol_cone (-> +1)
    return (float(1) / 3) * area_of_base * height # binary_operator:Div, binary_operator:Mult, call_argument:1, function_call:float, int_literal, literal:Num, return, suggest_constant_definition
def vol_right_circ_cone(radius, height): # function:vol_right_circ_cone (-> +1), function_returning_something:vol_right_circ_cone (-> +1)
    return (float(1) / 3) * pi * (radius ** 2) * height # binary_operator:Div, binary_operator:Mult, binary_operator:Pow, call_argument:1, function_call:float, int_literal, literal:Num, return, suggest_constant_definition
def vol_prism(area_of_base, height): # function:vol_prism (-> +1), function_returning_something:vol_prism (-> +1)
    return float(area_of_base * height) # binary_operator:Mult, call_argument:, function_call:float, function_tail_call:float, return
def vol_pyramid(area_of_base, height): # function:vol_pyramid (-> +1), function_returning_something:vol_pyramid (-> +1)
    return (float(1) / 3) * area_of_base * height # binary_operator:Div, binary_operator:Mult, call_argument:1, function_call:float, int_literal, literal:Num, return, suggest_constant_definition
def vol_sphere(radius): # function:vol_sphere (-> +1), function_returning_something:vol_sphere (-> +1)
    return (float(4) / 3) * pi * radius ** 3 # binary_operator:Div, binary_operator:Mult, binary_operator:Pow, call_argument:4, function_call:float, int_literal, literal:Num, return, suggest_constant_definition
def vol_circular_cylinder(radius, height): # function:vol_circular_cylinder (-> +1), function_returning_something:vol_circular_cylinder (-> +1)
    return pi * radius ** 2 * height # binary_operator:Mult, binary_operator:Pow, int_literal, literal:Num, return
def main(): # function:main (-> +9), function_returning_nothing:main (-> +9)
    print("Volumes:") # call_argument:, function_call:print, literal:Str
    print("Cube: " + str(vol_cube(2))) # binary_operator:Add, call_argument:, call_argument:2, composition, function_call:print, function_call:str, function_call:vol_cube, int_literal, literal:Num, literal:Str
    print("Cuboid: " + str(vol_cuboid(2, 2, 2))) # binary_operator:Add, call_argument:, call_argument:2, composition, function_call:print, function_call:str, function_call:vol_cuboid, int_literal, literal:Num, literal:Str
    print("Cone: " + str(vol_cone(2, 2))) # binary_operator:Add, call_argument:, call_argument:2, composition, function_call:print, function_call:str, function_call:vol_cone, int_literal, literal:Num, literal:Str
    print("Right Circular Cone: " + str(vol_right_circ_cone(2, 2))) # binary_operator:Add, call_argument:, call_argument:2, composition, function_call:print, function_call:str, function_call:vol_right_circ_cone, int_literal, literal:Num, literal:Str
    print("Prism: " + str(vol_prism(2, 2))) # binary_operator:Add, call_argument:, call_argument:2, composition, function_call:print, function_call:str, function_call:vol_prism, int_literal, literal:Num, literal:Str
    print("Pyramid: " + str(vol_pyramid(2, 2))) # binary_operator:Add, call_argument:, call_argument:2, composition, function_call:print, function_call:str, function_call:vol_pyramid, int_literal, literal:Num, literal:Str
    print("Sphere: " + str(vol_sphere(2))) # binary_operator:Add, call_argument:, call_argument:2, composition, function_call:print, function_call:str, function_call:vol_sphere, int_literal, literal:Num, literal:Str
    print("Circular Cylinder: " + str(vol_circular_cylinder(2, 2))) # binary_operator:Add, call_argument:, call_argument:2, composition, function_call:print, function_call:str, function_call:vol_circular_cylinder, int_literal, literal:Num, literal:Str

# ----------------------------------------------------------------------------------------
# ../Python/maths/zellers_congruence.py
# ----------------------------------------------------------------------------------------
import datetime # import:datetime, import_module:datetime
import argparse # import:argparse, import_module:argparse
def zeller(date_input: str) -> str: # function:zeller (-> +46), function_returning_something:zeller (-> +46)
    days = { # assignment, assignment_lhs_identifier:days, literal:Dict
        "0": "Sunday", # literal:Str
        "1": "Monday", # literal:Str
        "2": "Tuesday", # literal:Str
        "3": "Wednesday", # literal:Str
        "4": "Thursday", # literal:Str
        "5": "Friday", # literal:Str
        "6": "Saturday", # literal:Str
    }
    convert_datetime_days = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 0} # assignment, assignment_lhs_identifier:convert_datetime_days, assignment_rhs_atom:0, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:3, assignment_rhs_atom:4, assignment_rhs_atom:5, assignment_rhs_atom:6, int_literal, literal:Dict, literal:Num, suggest_constant_definition
    if not 0 < len(date_input) < 11: # call_argument:date_input, chained_comparison:2, chained_inequalities:2, comparison_operator:Lt, function_call:len, if (-> +1), if_test_id:date_input, if_test_id:len, int_literal, literal:Num, suggest_constant_definition, unary_operator:Not
        raise ValueError("Must be 10 characters long") # call_argument:, function_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    m: int = int(date_input[0] + date_input[1]) # binary_operator:Add, call_argument:, function_call:int, index, int_literal, literal:Num
    if not 0 < m < 13: # chained_comparison:2, chained_inequalities:2, comparison_operator:Lt, if (-> +1), if_test_id:m, int_literal, literal:Num, suggest_constant_definition, unary_operator:Not
        raise ValueError("Month must be between 1 - 12") # call_argument:, function_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    sep_1: str = date_input[2] # index, int_literal, literal:Num
    if sep_1 not in ["-", "/"]: # comparison_operator:NotIn, if (-> +1), if_test_id:sep_1, literal:List, literal:Str
        raise ValueError("Date seperator must be '-' or '/'") # call_argument:, function_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    d: int = int(date_input[3] + date_input[4]) # binary_operator:Add, call_argument:, function_call:int, index, int_literal, literal:Num, suggest_constant_definition
    if not 0 < d < 32: # chained_comparison:2, chained_inequalities:2, comparison_operator:Lt, if (-> +1), if_test_id:d, int_literal, literal:Num, suggest_constant_definition, unary_operator:Not
        raise ValueError("Date must be between 1 - 31") # call_argument:, function_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    sep_2: str = date_input[5] # index, int_literal, literal:Num, suggest_constant_definition
    if sep_2 not in ["-", "/"]: # comparison_operator:NotIn, if (-> +1), if_test_id:sep_2, literal:List, literal:Str
        raise ValueError("Date seperator must be '-' or '/'") # call_argument:, function_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    y: int = int(date_input[6] + date_input[7] + date_input[8] + date_input[9]) # binary_operator:Add, call_argument:, function_call:int, index, int_literal, literal:Num, suggest_constant_definition
    if not 45 < y < 8500: # chained_comparison:2, chained_inequalities:2, comparison_operator:Lt, if (-> +2), if_test_id:y, int_literal, literal:Num, suggest_constant_definition, unary_operator:Not
        raise ValueError( # function_call:ValueError, if_then_branch (-> +1), raise:ValueError
            "Year out of range. There has to be some sort of limit...right?" # call_argument:, literal:Str
        )
    dt_ck = datetime.date(int(y), int(m), int(d)) # assignment, assignment_lhs_identifier:dt_ck, assignment_rhs_atom:d, assignment_rhs_atom:datetime, assignment_rhs_atom:m, assignment_rhs_atom:y, call_argument:, call_argument:d, call_argument:m, call_argument:y, composition, function_call:int, method_call, method_call_name:date
    if m <= 2: # comparison_operator:LtE, if (-> +2), if_test_id:m, int_literal, literal:Num
        y = y - 1 # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:1, assignment_rhs_atom:y, binary_operator:Sub, if_then_branch (-> +1), int_literal, literal:Num, suggest_augmented_assignment, update_variable:y:1
        m = m + 12 # assignment, assignment_lhs_identifier:m, assignment_rhs_atom:12, assignment_rhs_atom:m, binary_operator:Add, int_literal, literal:Num, suggest_augmented_assignment, suggest_constant_definition, update_variable:m:12
    c: int = int(str(y)[:2]) # call_argument:, call_argument:y, composition, function_call:int, function_call:str, int_literal, literal:Num, slice
    k: int = int(str(y)[2:]) # call_argument:, call_argument:y, composition, function_call:int, function_call:str, int_literal, literal:Num, slice
    t: int = int(2.6 * m - 5.39) # binary_operator:Mult, binary_operator:Sub, call_argument:, float_literal, function_call:int, literal:Num, suggest_constant_definition
    u: int = int(c / 4) # binary_operator:Div, call_argument:, function_call:int, int_literal, literal:Num, suggest_constant_definition
    v: int = int(k / 4) # binary_operator:Div, call_argument:, function_call:int, int_literal, literal:Num, suggest_constant_definition
    x: int = int(d + k) # binary_operator:Add, call_argument:, function_call:int
    z: int = int(t + u + v + x) # binary_operator:Add, call_argument:, function_call:int
    w: int = int(z - (2 * c)) # binary_operator:Mult, binary_operator:Sub, call_argument:, function_call:int, int_literal, literal:Num
    f: int = round(w % 7) # binary_operator:Mod, call_argument:, function_call:round, int_literal, literal:Num, suggest_constant_definition
    if f != convert_datetime_days[dt_ck.weekday()]: # comparison_operator:NotEq, if (-> +1), if_test_id:convert_datetime_days, if_test_id:dt_ck, if_test_id:f, index, method_call, method_call_name:weekday, method_call_object:dt_ck
        raise AssertionError("The date was evaluated incorrectly. Contact developer.") # call_argument:, function_call:AssertionError, if_then_branch, literal:Str, raise:AssertionError
    response: str = f"Your date {date_input}, is a {days[str(f)]}!" # call_argument:f, function_call:str, index, literal:Str
    return response # return:response
