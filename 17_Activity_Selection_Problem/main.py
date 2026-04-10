def activity_selection(activities):
    # Sort activities by finish time
    activities.sort(key=lambda x: x[2])
    
    i = 0
    selected_activities = [activities[i]]
    
    for j in range(1, len(activities)):
        # If this activity has start time greater than or
        # equal to the finish time of previously selected
        # activity, then select it
        if activities[j][1] >= activities[i][2]:
            selected_activities.append(activities[j])
            i = j
            
    return selected_activities

if __name__ == '__main__':
    # Activities: (name, start_time, finish_time)
    activities = [("A1", 0, 6),
                  ("A2", 3, 4),
                  ("A3", 1, 2),
                  ("A4", 5, 8),
                  ("A5", 5, 7),
                  ("A6", 8, 9)]

    selected = activity_selection(activities)
    
    print("Following activities are selected:")
    for activity in selected:
        print(activity[0], end=" ")
    print()
