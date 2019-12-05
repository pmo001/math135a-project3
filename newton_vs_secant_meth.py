import sympy #for fcn manip
import math #for sqrt and log
#Newton iteration: one var(not a system)
#prints iterations of Newton method
def newton_meth(fcn_str, x_init, num_its):
    x = sympy.Symbol('x') #declaring x var for fcns
    #converts string into a sympy math expression
    fcn = sympy.sympify(fcn_str)
    print("sympy fcn: ", fcn)
    deriv_fcn = sympy.diff(fcn)
    #Newton iteration
    #for x0 = 1
    for i in range(num_its):
        x_nplus1_expr = x - fcn / deriv_fcn
        x_init = x_nplus1_expr.subs(x, x_init)
        print("{} iteration of Newton's method: {}".format(i+1, sympy.Float(x_init)))

        if i == 0:
            print("x1 val to be used for Secant method: ", x_init)

    return

#used if Newton method: fcn/fcn' become too difficult to compute
def secant_meth(x0, x1, fcn_str, num_its):
    x = sympy.Symbol('x')
    f = sympy.Function('f') #declaring 'f' for function use
    f = sympy.sympify(fcn_str) #converts fcn(str) into sympy
    #secant_line = ((x1 - x)*f(x0) + (x - x0)*f(x1)) / (x1 - x0)
    #print("sympified fcn: ", f)
    x0_tmp = x0
    x1_tmp = x1

    for i in range(num_its):
        tmp_store_x1 = x1_tmp
        #solving secant line = 0
        x1_tmp = x1_tmp - f.subs(x, x1_tmp) * (x1_tmp - x0_tmp) / (f.subs(x, x1_tmp) - f.subs(x, x0_tmp))
        x0_tmp = tmp_store_x1
        #expr.evalf() to convert expr to floating point
        print("{} iteration of Secant Method: {}".format(i+1, x1_tmp.evalf()))
    return

def main():
    ######x = sympy.Symbol('x') #declaring x var for fncs
    #print("deriv of cosx = -sinx: ", sympy.diff(sympy.cos(x)))
    ###fcn_a = x**3 - 3*x + 1
    ###deriv_a = sympy.diff(fcn_a)
    
        #chose x0 = 1
    #lec_fcn_str = "x**3 - x + 1" #tested; #ans: .5; 3
        #chose x0 = 1
    #hw4_4_fcn_str = "x**2 - 25" #tested; #converges to 5
        #               exp(x) == e**x
        # chose x0 = .5
    #hw4_3_fcn_str = "exp(x) - 3*x" #tested; converges to .619

    #newton:3rd it:1.532
    project3_fcn_str = "x**3 - 3*x + 1"
    num_its = 10
    x_initial = 2
    x1_initial = 5/3
        #secant: x0=1, x1=2, numits=4; converges to .56714
    #litm3_fcn_str = "x - exp(-x)"
        #secant: x0=1; x1=2; numits=6; converges to 1.85558
    #litm2_fcn_str = "x**4 - x - 10"
    
    newton_meth(project3_fcn_str, x_initial, num_its)
    ##print("results: after human analysis: gets to convergence on 3rd iteration for 4 sig figs")
    print("      >>>end<<<")
    secant_meth(x_initial, x1_initial, project3_fcn_str, num_its)
    print("      >>>end<<<")

    project3_2_fcn_str = "x**3 - 2*sin(x)"
    x0_initial = .5
    x1_initial = -.3295663
    newton_meth(project3_2_fcn_str, x0_initial, num_its)
    print("      >>>end<<<")
    secant_meth(x0_initial, x1_initial, project3_2_fcn_str, num_its)
    print("      >>>end<<<")

    return
main()

def newton_meth2(fcn_str, x_init, num_its):
    x = sympy.Symbol('x') #declaring x var for fcns
    #converts string into a sympy math expression
    fcn = sympy.sympify(fcn_str)
    print("sympy fcn: ", fcn)
    deriv_fcn = sympy.diff(fcn)
    deriv2_fcn = sympy.diff(deriv_fcn)
    #Newton iteration
    for i in range(num_its):
        x_init = x_init - fcn.subs(x, x_init) / math.sqrt((deriv_fcn.subs(x, x_init)**2 - fcn.subs(x, x_init) * deriv2_fcn.subs(x, x_init)))
        print("{} iteration of Newton's method: {}".format(i+1, sympy.Float(x_init)))
    return

def main2():

    prob2_fcn_str = "x**6 + 6*x**5 + 9*x**4 - 2*x**3 - 6*x**2 + 1"
    multiple_root_fcn_str = "((x - 1)**2) * (x - 2)"
   # simple_root_fcn_str = "(x-1) * (x-2)"
    
    num_its = 7
 ###   x0_initial = .3

###?     x0_initial = .1
###    newton_meth2(prob2_fcn_str, x0_initial, num_its)
#   ~~~~~~~~~
##    print("       >>>>simple root Newton approx: ")
 ##   x0_initial = 50
 # ~~~~~~~~

    x0_initial = 1.5
    print("x_initial = 1.5")
    newton_meth2(multiple_root_fcn_str, x0_initial, num_its)
    it_list = [1.78867513459481, 1.98628779019761, 1.99999735034616, 2, 2, 2, 2]
 #test cubic(3) converg  it_list = [1.6735 * 10**-2, 1.8743 * 10**-6, 2.6336 * 10**-18, 7.3068 * 10**-54]
 #test quadratic (2) converg  it_list = [4.7327 * 10**-5, 5.0083 * 10**-10, 5.6088 * 10**-20, 7.0343 * 10**-40]
  
    #ref: https://en.wikipedia.org/wiki/Rate_of_convergence#Convergence_speed_for_iterative_methods
    convergence_rate = math.log(abs((it_list[3] - it_list[2])) / 
                                abs((it_list[2] - it_list[1]))) / math.log(abs((it_list[2] - it_list[1])) /
                                                                    abs((it_list[1] - it_list[0])))
    print("convergence rate: ", convergence_rate)
    print("Since convergence rate, q, is approximately 3, this indicates cubic convergence at the simple root: 2")

    print("~~~~~~~~~~~~~~~~~")
    x0_initial = -5
    print("x_initial = -5")
    newton_meth2(multiple_root_fcn_str, x0_initial, num_its)
    #last 4 iteration results
    it_list2 = [0.913876405257185, 0.974679481567971, 0.992581062724645, 0.997826972456446]
    convergence_rate = math.log(abs((it_list2[3] - it_list2[2])) / 
                                abs((it_list2[2] - it_list2[1]))) / math.log(abs((it_list2[2] - it_list2[1])) /
                                                                    abs((it_list2[1] - it_list2[0])))
    print("convergence rate: ", convergence_rate)
    print("Since convergence rate, q, is approximately 1, this indicates linear convergence at the multiple root: 1")

    
    return
#fixmeproject3.2 main2()
