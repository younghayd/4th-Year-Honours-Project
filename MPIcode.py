from mpi4py import MPI

comm = MPI.COMM_WORLD
rank=comm.Get_rank()
size=comm.Get_size()

#print(rank)
#print(size)

if rank == 0:
    msg = "Hello World"
    print(rank, ":", msg)
    comm.send(msg, dest = 1)

elif rank == 1:
    transmission = comm.recv()
    print(rank,":", transmission, "recieved")
 
