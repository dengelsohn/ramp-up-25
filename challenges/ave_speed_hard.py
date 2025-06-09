def ave_spd(up_time, up_spd, down_spd):
	total_up = up_time/60 * up_spd
	down_time = total_up / down_spd
	return (2 * total_up) / (down_time + (up_time/60))