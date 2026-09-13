# Hamm 2 June 2026



def count_leap_years():
  leap_years = 0
  for i in range(1901, 2001):
    if i % 4 == 0 and i % 100 != 0:
      leap_years += 1
    elif i % 400 == 0 and i % 100 == 0:
      leap_years += 1
  return leap_years

def count_normal_years(leap_years):
  normal_years = (2001 - 1901) - leap_years
  return normal_years

def count_days(leap_years , normal_years):
  days = ((365 * normal_years) + (366 * leap_years))
  return days

def calendar(days):
  count_of_sundays = 0
    # 1 Jan 1901 is a TUESDAY, and this is d = 0
    # Another confusing thing here is that if you start at d = 0, and add 31 days (for january) now you are actual on d = 31 which is 1 FEB. Keeping this consistent throughout is important. 
  d = 0
  months = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12]
  duration = [31 , 28 , 31 , 30 , 31 , 30 , 31 , 31 , 30 , 31 , 30 , 31]
  year = 1901

  while year < 2001: # will process all of year 2000, then once it increments to 2001 will BREAK
    for i in months:
      # weekday_index is crucial. The relationship between d and weekday index is that d + 2 % 7 == 0 means that we are starting the month on a sunday, because the very first day, d = 0, is a TUESDAY. 
      # By building this var into the loop we can always be referencing it at the end to see if the month starts on a sunday.
      weekday_index = (d + 2) % 7
      if year % 4 == 0 and year % 100 != 0 and i == 2: # LEAP YEAR, NON Century
        d += 29
      elif year % 400 == 0 and year % 100 == 0 and i == 2: # LEAP YEAR,  Century
        d += 29
      else:  
        d += duration[i - 1]
      if i == 12:
        year += 1
      if weekday_index == 0:
        count_of_sundays += 1

  return count_of_sundays

def main():
  leap_years = count_leap_years()
  normal_years = count_normal_years(leap_years)
  days = count_days(leap_years, normal_years)
  sundays = calendar(days)
  print(f"leap years: {leap_years}")
  print(f"normal years: {normal_years}")
  print(f"days: {days}")
  print(f"Count of Sundays: {sundays}")

main()
