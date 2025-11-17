from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# Every process creates a small array based on its rank
senddata = numpy.array([rank], dtype=int)
recvdata = numpy.empty(size, dtype=int)

# All processes exchange data with each other
comm.Alltoall(senddata, recvdata)

print("Process %s says Hello World! Send: %s  Receive: %s"
      % (rank, senddata, recvdata))
