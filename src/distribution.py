#Functions to create a set of numbers following different distributions
#implemented by one and only Abhijeet Anand
import numpy as np
def poisson_function(lambdaa,req_no):
    return np.random.poisson(lambdaa,req_no).tolist()

def binomial_function(total,prob_success,req_no):
    return np.random.binomial(total,prob_success,req_no).tolist()

def uniform_function(lower_value,higher_value,req_no):
    return np.random.uniform(lower_value,higher_value,req_no).tolist()

def exponential_function(scale,req_no):
    return np.random.exponential(scale,req_no).tolist()

def lognormal_function(mean,sigma,req_no):
    return np.random.lognormal(mean,sigma,req_no).tolist()

def normal_function(mean,st_dev,req_no):
    return np.random.normal(mean,std_dev,req_no).tolist()

def triangular_function(left,mode,right,req_no):
    return np.random.triangular(left,mode,right,req_no).tolist()

#here shape is shape of the distribution and should be greater than zero
def weibull_function(shape,req_no):
    return np.random.weibull(shape,req_no).tolist()

    
    
    
#if __name__=="__main__":
#    print exponential_function(8.57,50)

