import numpy as np
class DATA(object):
    def __init__(self):
        super().__init__()
        self.map_1_1=np.array([[0,0,0,0,0,0,0]])
        self.map_3_4=np.array([[0,0,0,0,0,-1,-1,-1],[0,0,0,0,0,0,-1,-1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]])
        self.map_6_4=np.array([[0,0,0,0,0,0,-1,-1],[0,0,0,0,0,0,0,-1],[0,-1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0])
        self.map_7_2=np.array([[0,-1,0,0,0,0,0,0],[0,-1,-1,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,-1,-1],[0,0,0,0,0,0,-1,-1]])
        self.map_8_4=np.array([[-1,0,0,0,0,0,0,0],[0,0,0,0,0,-1,-1,0],[0,0,0,-1,-1,0,0,0],[-1,-1,0,-1,-1,0,0,0],[0,-1,0,0,0,0,0,-1],[0,0,0,0,-1,-1,0,0],[0,0,0,0,0,0,0,0]])
        