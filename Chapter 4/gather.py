from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

data = "Hello World from rank %d" % rank

# Gather messages from all processes to rank 0
received = comm.gather(data, root=0)

if rank == 0:
    print("Rank 0 gathering Hello World messages:")
    for i in range(size):
        print("Process %d sent: %s" % (i, received[i]))
