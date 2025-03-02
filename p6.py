# design pattern 
# structural  ==> decorator 

import time 

def timing_decorator(func):
    def wrapper(*args,**kwargs):
        start_time =time.time()
        result=func(*args,**kwargs)
        end_time = time.time()
        print(f"function {func.__name__} took {end_time - start_time} ")
        return result
    return wrapper


@timing_decorator
def f():
    time.sleep(2)
    print("function executed!")


if __name__ == "__main__":
    f()
