from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    message = "Hello World"
else:
    message = None

# Broadcast message from process 0 to all other processes
message = comm.bcast(message, root=0)

print("Process %d received message: %s" % (rank, message))
