#counties = ["Arapahoe","Denver","Jefferson"]

#for county in counties:
#    print(county)

#numbers = [0, 1, 2, 3, 4]
#for num in numbers:
 #   print(num)
#for i in range(len(counties)):
 #   print(counties[i])
#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for county in counties_dict:
  #  print(counties_dict[county])

#for county in counties_dict:
#    print(counties_dict.get(county))

#for county, value in counties_dict.items():
  #print(f"{county} county has {value:,.0f} registered voters.")

#voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
 #               {"county":"Denver", "registered_voters": 463353},
  #              {"county":"Jefferson", "registered_voters": 432438}]
    
#for county_dict in voting_data:
   # print(county_dict)

#for county_dict in range(len(voting_data)):
#    print(voting_data[county_dict])

#for county_dict in voting_data:
  #  print(f"{county_dict['county']} county has {county_dict['registered_voters']:,.0f} registered voters.")

#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#message_to_print = (f"You received {my_votes} number of votes. "
  #f"The total number of votes in the election was {total_votes}. "
 # f"You received {(my_votes / total_votes * 100):.2f}% of the total votes.")

#print(message_to_print)
#print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

#for county_dict in voting_data:
#    print(county_dict["county"])

#import datetime as dt
#now = dt.datetime.now()
#print(now)

# Import the datetime class from the datetime module.
#import datetime
# Use the now() attribute on the datetime class to get the present time.
#now = datetime.datetime.now()
# Print the present time.
#print("The time right now is ", now)


# Import the datetime class from the datetime module.
# import datetime as dt
# # Use the now() attribute on the datetime class to get the present time.
# now = dt.datetime.now()
# # Print the present time.
# print("The time right now is ", now)

# import csv
# commands on the Python interpreter
# dir(csv)
# dir({'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438})
# dir(str)

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)







