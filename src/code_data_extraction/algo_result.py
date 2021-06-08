import numpy as np
class algo_result:
    def __init__(self,target_idx,target_str,bin2range,target_radius):
        self.num_targets = len(target_idx)
        self.bin2range = bin2range
        self.location = [idx*bin2range for idx in target_idx]
        self.strength = target_str
        self.radius = target_radius
        self.last_added = 0
        self.print = np.zeros((2*round(target_radius/bin2range),len(target_idx)))
        self.print_location = np.zeros((2*round(target_radius/bin2range),len(target_idx)))
        
    def collect_target_info(self, target_info):
        self.print_location[:,self.last_added] = target_info[0]*self.bin2range
        self.print[:,self.last_added] = target_info[1]
        self.last_added += 1