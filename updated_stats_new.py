import pychecker.checker

stats = []

reroll = 'y'

def stat_maker(stats_hold):
	plyr_str = 0
	plyr_con = 0
	plyr_agi = 0
	plyr_int = 0
	plyr_stats_total = 13
	stats_hold = []
	while plyr_stats_total > 0:
		while plyr_str < 5:
			add_str = int(raw_input("Enter your str, you have %d points left: " % 	plyr_stats_total))
			if add_str > 5:
				print "Stats are 1, 2, 3, 4, 5. No greater"
				continue #use this to restart loop from while plyr_str < 5
			else:
				plyr_str = plyr_str + add_str
				plyr_stats_total -= add_str
				stats_hold.append(add_str)
				print plyr_stats_total
				break	
		while plyr_con < 5:
			add_con = int(raw_input("Enter your con, you have %d points left: " % 	plyr_stats_total))
			if add_con > 5:
				print "Stats are 1, 2, 3, 4, 5. No greater"
				continue #use this to restart loop from while plyr_con < 5
			else:	
				plyr_con = plyr_con + add_con
				plyr_stats_total -= add_con
				stats_hold.append(add_con)
				print plyr_stats_total
				break
		while plyr_agi < 5:
			add_agi = int(raw_input("Enter your agi, you have %d points left: " % 	plyr_stats_total))
			if add_agi > 5:
				print "Stats are 1, 2, 3, 4, 5"
				continue #use this to restart loop from while plyr_agi < 5
			elif add_agi > plyr_stats_total:
				print "Cannot exceed 13 points total"
				continue
			else:
				plyr_agi += add_agi
				plyr_stats_total -= add_agi
				stats_hold.append(add_agi)	
				break
		while plyr_int < 5:
			if plyr_stats_total == 0:
				print "You can only have 0 points in this stat"
				stats.append(0)
				break
			else:
				add_int = int(raw_input("Enter your int, you have %d points left: " % plyr_stats_total))
				if add_int > 5:
					print "Stats are 1, 2, 3, 4, 5. No greater"
					continue #use this to restart loop from while plyr_int < 5
				else:
					plyr_int += add_int
					plyr_stats_total -= add_int
					stats_hold.append(add_int)
					break
	print stats_hold

stat_maker(stats)

while reroll == 'y':
	reroll_yesno = raw_input("Do you wanna reroll? ")
	if reroll_yesno == 'y':
		new_stats = []
		stat_maker(new_stats)
	else:
		print "okay, good"
		break
	

