#%% Test cases
test_cases = [
    [[13, 5, 6, 2, 5], [5, 2, 5, 13]],
    [[14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50]],
    [[2,4,5,9,0,0,0], [2,4,5,16,9,0,0,0]],
    [[37,-5,25], [37,0,-5,25]],
    [ [1]*50     , [1]*51 ],
    [ [1000]*50  , [1000]*51],
    [ [1000]*99  , [1000]*98],
    [ [1000]*50  , [1000]*50 + [-999]],
    [ [1000]*98  , [1000]*98 + [-999]],
    [ [1000]*98  , [1000]*98 + [999]],
    [ [0]*98     ,  [0]*99 ],
    [ [0]*98     ,  [0]*98 + [37] ],
    [  range(500,500+90), range(500,500+90)+[-87]],
    [  range(-500,-530)+range(900,900+30), range(-500,-530)+[-5]+range(900,900+30)]

]
expected_results=[
    6,
    -4,
    16,
    0,
    1,
    1000,
    1000,
    -999,
    -999,
    999,
    0,
    37,
    -87,
    -5
]

assert len(test_cases)==len(expected_results)
#%% Test new solutions
import solution
reload(solution)
for case,expected in zip(test_cases,expected_results):
    print 'Expected Result:' +str(expected)
    for name, val in solution.__dict__.iteritems(): 
        if callable(val):                      # check if callable (normally functions)
            result1 = val(case[0], case[1])   
            result2 = val(case[1], case[0])
            assert (result1==expected) & (result2==expected), val.func_name+ ' failed'
            print(val.func_name+': ' +str(result1) +',' +str(result2))
#%% Benchmark new solutions
from timeit import timeit
tested_module = solution
funcs_str =''
for name, val in tested_module.__dict__.iteritems(): 
    if callable(val):
        funcs_str += (val.func_name+ '| ')
print('   ' + funcs_str)
for i,case in enumerate(test_cases):
    results_str = (str(i) +'|')
    for name, val in tested_module.__dict__.iteritems(): 
        if callable(val):
            t = timeit(tested_module.__name__+'.'+val.func_name+'('+str(case[0]) +','+str(case[1]) +')',
                         setup='import '+tested_module.__name__+'\nreload('+tested_module.__name__+')', number=10000)
            results_str += ( "{:6.1f}".format(t) + ' | ')
    print(results_str[:-3])
#%% Test old solutions
import solutionold
reload(solutionold)
for case,expected in zip(test_cases,expected_results):
    print '**Expected Result:' +str(expected)+'**'
    for name, val in solutionold.__dict__.iteritems(): 
        if callable(val):                      # check if callable (normally functions)
            result1 = val(case[0], case[1])   
            result2 = val(case[1], case[0])
            assert (result1==expected) & (result2==expected) , val.func_name+ ' failed'
            print(val.func_name+': ' +str(result1) +',' +str(result2))

#%% Benchmark old versions
from timeit import timeit
import solutionold
funcs_str =''
for name, val in solutionold.__dict__.iteritems(): 
    if callable(val):
        funcs_str += (val.func_name+ '| ')
print('   ' + funcs_str)
for i,case in enumerate(test_cases):
    # print (str(i) +'  ')
    results_str = (str(i) +'|')
    for name, val in solutionold.__dict__.iteritems(): 
        if callable(val):
            t = timeit('solutionold.'+val.func_name+'('+str(case[0]) +','+str(case[1]) +')',
                         setup='import solutionold\nreload(solutionold)', number=10000)
            results_str += ( "{:7.2f}".format(t) + ' | ')
    print(results_str[:-3])

# %%
