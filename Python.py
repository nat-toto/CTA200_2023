def f(x:float) -> float:
    '''This is the function f, a third degree polynomial'''
    return x**3 - x**2 - 1

def df(x:float) -> float:
    '''This is the derivative of our polynomial,f.'''
    return 3*x**2 - 2*x

def newton(f,df,x0,epsilon=1e-6 ,max_iter=30):
    '''This finds x intercepts (roots) using Newton iteration

Keeping epsilon and max_iter as default values:

    >>>newton(f,df,1,1e-6,30)
    Found root in 5 iterations.
    1.4655713749070918

    >>>newton(f,df,2,1e-6,30)
    Found root in 4 iterations.
    1.4655713749070918

    >>>newton(f,df,3,1e-6,30)
    Found root in 6 iterations.
    1.4655712318902172

    >>>newton(f,df,4,1e-6,30)
    Found root in 7 iterations.
    1.4655712318772516
    
Reducing epsilon to 1e-8, and varying x0:

    >>>newton(f,df,1,1e-8,30)
    Found root in 6 iterations.
    1.4655712318767877
    
    >>>newton(f,df,2,1e-8,30)
    Found root in 5 iterations.
    1.4655712318767877

    >>>newton(f,df,3,1e-8,30)
    Found root in 6 iterations.
    1.4655712318902172

    >>>newton(f,df,4,1e-8,30)
    Found root in 7 iterations.
    1.4655712318772516

    As shown above, reducing epsilon still works with either 1 extra iteration or the same number of iterations.
    '''

    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print ('Found root in ' + str(n) + ' iterations.')
            return xn
        dfxn = df(xn)
        if dfxn == 0:
           print('Iteration failed')
           return none
        xn = xn - fxn/dfxn
    print('Iteration failed')
  
