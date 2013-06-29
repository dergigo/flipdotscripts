from hqstatus import HqStatusFlipdotAdapter
from flipdot.FlipdotMatrixSimulator import FlipdotMatrixSimulator
import thread
from Tkinter import mainloop


if __name__ == '__main__':
    flipdotmatrix = FlipdotMatrixSimulator()
    hqstatusFlipdotAdapter = HqStatusFlipdotAdapter (flipdotmatrix)
    thread.start_new_thread(hqstatusFlipdotAdapter.run())
    mainloop()
    
    
