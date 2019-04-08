from multiprocessing.dummy import Pool as ThreadPool 
import traceback

def taskRun(functionName, data, threadCount):
    try:
        pool = ThreadPool(threadCount) 
        # open the urls in their own threads
        # and return the results
        pool.map(functionName, data)
        # close the pool and wait for the work to finish 
        pool.close() 
        pool.join() 
    except Exception:
        print ("Multitasking failed: " , traceback.print_exc())
