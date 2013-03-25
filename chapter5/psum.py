from mpi4py import MPI
import numpy as np

# This function will be executed on all processes.
def psum(a):
    # "a" only contains a subset of all integers.
    # They are summed locally on this process. 
    locsum = np.sum(a)

    # We allocate a variable that will contain the final result, that is,
    # the sum of all our integers.
    rcvBuf = np.array(0.0,'d')

    # We use a MPI reduce operation:
    #   * locsum is combined from all processes
    #   * these local sums are summed with the MPI.SUM operation
    #   * the result (total sum) is distributed back to all processes in
    #     the rcvBuf variable
    MPI.COMM_WORLD.Allreduce([locsum, MPI.DOUBLE],
        [rcvBuf, MPI.DOUBLE],
        op=MPI.SUM)
    return rcvBuf
