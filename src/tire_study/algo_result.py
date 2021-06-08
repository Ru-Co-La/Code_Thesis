import numpy as np
from scipy.fft import fftn,fftshift
class algo_result:
    def __init__(self,target_idx,target_str,bin2range,target_radius,chirps_per_frame,doppler_len,wav_spa_rat,angle_bins):
        self.num_targets = len(target_idx)
        self.bin2range = bin2range
        self.location = [idx*bin2range for idx in target_idx]
        self.strength = target_str
        self.radius = target_radius
        self.chirps_per_frame = chirps_per_frame
        self.doppler_len = doppler_len
        self.wavelength_spacing_ratio = wav_spa_rat
        self.last_added = 0
        self.print = np.zeros((2*round(target_radius/bin2range),chirps_per_frame,len(target_idx)))
        self.print_location = np.zeros((2*round(target_radius/bin2range),len(target_idx)))
        self.doppler_mark = np.zeros((chirps_per_frame,len(target_idx)), dtype='complex')
        self.doppler_spectrum = np.zeros((doppler_len,len(target_idx)))
        
    def collect_target_range_spectrum(self, target_spectrum_info):
        self.print_location[:,self.last_added] = target_spectrum_info[0]*self.bin2range
        self.print[:,:,self.last_added] = target_spectrum_info[1]
        self.last_added += 1
        
    def collect_target_doppler_mark(self, doppler_mark):
        self.doppler_mark[:,self.last_added-1] = doppler_mark
        #divide by self.doppler_len to normalize
        self.doppler_spectrum[:,self.last_added-1] = fftshift(np.abs(fftn(np.pad(doppler_mark,(0,self.doppler_len-self.chirps_per_frame)))))/np.sqrt(self.doppler_len)
    