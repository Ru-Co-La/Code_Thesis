import numpy as np
import matplotlib.pyplot as plt

class Frame:
    
    def __init__(self, chirps, samples_per_chirp, chirps_per_frame, antennas, chirp_period):
        #chirps is a (samples_per_chirp * chirps_per_frame) x (2 * antennas array)
        #samples_per_chirp is a scalar
        #antennas is a scalar
        self.sam_x_chir = samples_per_chirp
        self.chir_x_fr = chirps_per_frame
        self.num_antennas = antennas
        self.T = chirp_period
        self.chirp = np.zeros((samples_per_chirp, antennas, chirps_per_frame),dtype=complex)
        
        for chirp in range(chirps_per_frame):
            for antenna in range(antennas):
                self.chirp[:,antenna,chirp] = chirps[chirp * samples_per_chirp : (chirp + 1) * samples_per_chirp,2*antenna] + \
                1j*chirps[chirp * samples_per_chirp : (chirp + 1) * samples_per_chirp,2*antenna+1]
    
    def get_antenna(self, antenna_num):
        #antenna_num can be 0,1,2,...
        antenna = self.chirp[:,antenna_num,:]
        return antenna
    
    def get_chirp(self,chirp_num):
        #chirp_num can be 0,1,2,...
        chirp = self.chirp[:,:,chirp_num]
        return chirp
    
    def get_antenna_chirp(self,antenna_num,chirp_num):
        antenna_chirp = self.chirp[:,antenna_num,chirp_num]
        return antenna_chirp
    
    def plot_chirp(self,chirp_num):
        t = np.linspace(0,self.T,self.sam_x_chir)
        for antenna in range(self.num_antennas):
            plt.plot(t,np.real(self.chirp[:,antenna,chirp_num]),label='I_RX'+str(antenna))
            plt.plot(t,np.imag(self.chirp[:,antenna,chirp_num]),label="Q_RX"+str(antenna))
        plt.xlabel("time")
        plt.ylabel("signal")
        plt.legend(loc='lower left')
        plt.show()
        
    def calibrate(self,calibration_chirp):
        if calibration_chirp.shape == (self.sam_x_chir,self.num_antennas):
            for chirp in range(self.chir_x_fr):
                self.chirp[:,:,chirp] -= calibration_chirp