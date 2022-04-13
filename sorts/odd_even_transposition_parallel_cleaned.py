
from multiprocessing import Lock, Pipe, Process


processLock = Lock()



def oeProcess(position, value, LSend, RSend, LRcv, RRcv, resultPipe):
    global processLock

    
    
    
    for i in range(0, 10):

        if (i + position) % 2 == 0 and RSend is not None:
            
            processLock.acquire()
            RSend[1].send(value)
            processLock.release()

            
            processLock.acquire()
            temp = RRcv[0].recv()
            processLock.release()

            
            value = min(value, temp)
        elif (i + position) % 2 != 0 and LSend is not None:
            
            processLock.acquire()
            LSend[1].send(value)
            processLock.release()

            
            processLock.acquire()
            temp = LRcv[0].recv()
            processLock.release()

            
            value = max(value, temp)
    
    resultPipe[1].send(value)



def OddEvenTransposition(arr):
    processArray = []
    resultPipe = []
    
    for _ in arr:
        resultPipe.append(Pipe())
    
    
    
    tempRs = Pipe()
    tempRr = Pipe()
    processArray.append(
        Process(
            target=oeProcess,
            args=(0, arr[0], None, tempRs, None, tempRr, resultPipe[0]),
        )
    )
    tempLr = tempRs
    tempLs = tempRr

    for i in range(1, len(arr) - 1):
        tempRs = Pipe()
        tempRr = Pipe()
        processArray.append(
            Process(
                target=oeProcess,
                args=(i, arr[i], tempLs, tempRs, tempLr, tempRr, resultPipe[i]),
            )
        )
        tempLr = tempRs
        tempLs = tempRr

    processArray.append(
        Process(
            target=oeProcess,
            args=(
                len(arr) - 1,
                arr[len(arr) - 1],
                tempLs,
                None,
                tempLr,
                None,
                resultPipe[len(arr) - 1],
            ),
        )
    )

    
    for p in processArray:
        p.start()

    
    for p in range(0, len(resultPipe)):
        arr[p] = resultPipe[p][0].recv()
        processArray[p].join()
    return arr



def main():
    arr = list(range(10, 0, -1))
    print("Initial List")
    print(*arr)
    arr = OddEvenTransposition(arr)
    print("Sorted List\n")
    print(*arr)


if __name__ == "__main__":
    main()
