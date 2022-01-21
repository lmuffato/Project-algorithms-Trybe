def study_schedule(permanence_period, target_time):
    counter = 0
    
    for period in permanence_period:
        end = period[1]
        begin = period[0]

        if(target_time == None or end == None or begin == None):
            return None
        
        if(end == target_time):
            counter += 1
        elif(begin == target_time):
            counter += 1
        elif((end - begin) >= target_time and begin < target_time ):
            counter += 1

    return counter