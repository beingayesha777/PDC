from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

print("My rank is:", rank)

if rank == 0:
    data = "Hello World"
    destination = 4
    comm.send(data, dest=destination)
    print("Sending '%s' to process %d" % (data, destination))

if rank == 1:
    data = "Hello World"
    destination = 8
    comm.send(data, dest=destination)
    print("Sending '%s' to process %d" % (data, destination))

if rank == 4:
    data = comm.recv(source=0)
    print("Process 4 received:", data)

if rank == 8:
    data = comm.recv(source=1)
    print("Process 8 received:", data)
