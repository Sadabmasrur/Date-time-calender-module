def hotel_cost(nights):
    return 140*nights

def plane_ride_cost(city):
    
    if city=="London":
        return 740
    
    elif city=="Paris":
        return 945
    
    elif city=="New York":
        return 1010
    
    elif city=="Berlin":
        return 610
    
    
def rental_car_cost(days):
    if days>=7:
        return(40*days)-50
    elif days>=3:
        return(40*days)-20
    else:
        return(40*days)   
    
    
    
def trip_cost(city, days):
    h_c=hotel_cost(days)
    r_c=rental_car_cost(days)
    p_c=plane_ride_cost(city)   
    
    
    sum=h_c + r_c + p_c
    return sum

d=int(input("Enter the amount of days you wish to stay(In digit): ")) 
c=input("Enter the city you are going to\n1. Paris\n2. London\n3. Berlin\n4. New York :")   

print()
print(f"Hotel cost: ${hotel_cost(d)}") 
print(f"Car cost: ${rental_car_cost(d)}") 
print(f"Plane cost: ${plane_ride_cost(c)}") 
print(f"Total trip cost: ${trip_cost(c,d)}") 
    
    
    