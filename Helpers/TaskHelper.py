from multiprocessing.dummy import Pool as ThreadPool 

def taskRun(functionName, data, threadCount):
    pool = ThreadPool(threadCount) 

    # open the urls in their own threads
    # and return the results
    pool.map(functionName, data)
    # close the pool and wait for the work to finish 
    pool.close() 
    pool.join() 