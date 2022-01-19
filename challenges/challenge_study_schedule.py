def study_schedule(permanence_period, target_time):
  count = 0
  if not target_time:
    return None
  for (first, second) in permanence_period:
    try:
      if target_time in range(first, second+1):
        count += 1
    except:
      return None
  return count
