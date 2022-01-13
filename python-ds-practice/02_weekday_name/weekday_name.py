def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    day=['Sunday','Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday']
    
    if day_of_week >=1 and day_of_week<=7:
        print(day[day_of_week-1]) 
    else:
        print(None)
    
weekday_name(1)
weekday_name(7)
weekday_name(0)
weekday_name(9)