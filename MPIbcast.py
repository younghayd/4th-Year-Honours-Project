from mpi4py import MPI

comm = MPI.COMM_WORLD

rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    message = "Hello World"

else:
    message = None 

message = comm.bcast(message, root = 0)
print("Core:", rank, message, "recieved")
