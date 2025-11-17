from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    messages = ["Hello World"] * 10   # list of 10 messages
else:
    messages = None

# Scatter sends one element to each process
received_message = comm.scatter(messages, root=0)

print("Process %d received: %s" % (rank, received_message))
