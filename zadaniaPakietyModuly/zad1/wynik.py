
import predkosc

run_distance = int(input("Ile przebiegłeś kilometrów? "))
run_time = int(input("Ile godzin biegłeś? "))
avarage_speed = predkosc.average_speed(run_distance, run_time)
print(f"Twoja średnia prędkość biegu to {avarage_speed} km/h!")

