import multiprocessing

def f1(x):
    print(x*x )

def f2(x):
    print(x*x*x)


if __name__ =="__main__":
    p1 = multiprocessing.Process(target=f1,args=(10,))
    p2 = multiprocessing.Process(target=f2,args=(20,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()



