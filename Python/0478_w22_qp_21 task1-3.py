#Past paper taken from: 0478_w22_qp_21

#Task 1: setting up the system to store the membership details DONE
#- store the members' details in arrays DONE
#- populate the arrays with at least 20 members' details DONE
#- use the array index as the annual membership number DONE

user_name = ["Sophia", "Ethan", "Isabella", "Noah", "Ava", "William", "Mia", "Benjamin", "Olivia", "Jameson", "Emma", "Alexander", "Charlotte", "Liam", "Harper", "Lucas", "Amelia", "Henry", "Evelyn", "Jackson"]
user_age = [25, 17, 47, 18, 63, 10, 55, 67, 38, 50, 29, 36, 21, 81, 14, 58, 33, 12, 52, 41]
user_gender = ['Girl', 'Boy', 'Girl', 'Boy', 'Girl', 'Boy', 'Girl', 'Boy', 'Girl', 'Boy', 'Girl', 'Boy', 'Girl', 'Boy', 'Girl', 'Boy', 'Girl', 'Boy', 'Girl', 'Boy']
user_type_of_membership = []
user_type_of_membership_oneyear = []
user_team_member_or_not = ['yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no']
user_fee_paid_or_not = ['no', 'yes', 'yes', 'no', 'yes', 'yes', 'no', 'yes', 'yes', 'no', 'yes', 'yes', 'no', 'yes', 'yes', 'no', 'yes', 'yes', 'no', 'yes']
member_details = []
member_details_oneyear = []
junior_didnot_pay = 0
adult_didnot_pay = 0 
senior_didnot_pay = 0
golden_didnot_pay = 0
user_not_paid = 0
user_annual_fee = 0

print()
print()
print('----------Member Details (current updates)----------')

for data in range(0, 20):
  if user_age[data] >= 2 and user_age[data] < 18:
    user_type_of_membership.append('Junior')
  elif user_age[data] >= 18 and user_age[data] < 50:
    user_type_of_membership.append('Adult')
  elif user_age[data] >= 50 and user_age[data] < 80:
    user_type_of_membership.append('Senior')
  elif user_age[data] > 80:
    user_type_of_membership.append('Golden')

for data in range(0, 20):
  
  annual_membership_number = len(member_details) + 1

  if user_type_of_membership[data] == 'Junior' and user_fee_paid_or_not[data] == 'yes':
    user_annual_fee = 10
  elif user_type_of_membership[data] == 'Adult' and user_fee_paid_or_not[data] == 'yes':
    user_annual_fee = 20
  elif user_type_of_membership[data] == 'Senior' and user_fee_paid_or_not[data] == 'yes':
    user_annual_fee = 15
  elif user_type_of_membership[data] == 'Golden' and user_fee_paid_or_not[data] == 'yes':
    user_annual_fee = 0
  else:
    user_annual_fee = 0

  member_details.append([
    user_name[data],
    user_age[data],
    user_gender[data],
    user_type_of_membership[data],
    user_team_member_or_not[data],
    user_annual_fee,
    user_fee_paid_or_not[data],
    annual_membership_number
    ])

  if user_type_of_membership[data] == 'Junior' and user_fee_paid_or_not[data] == 'no':
    junior_didnot_pay += 1 
  elif user_type_of_membership[data] == 'Adult' and user_fee_paid_or_not[data] == 'no':
    adult_didnot_pay += 1
  elif user_type_of_membership[data] == 'Senior' and user_fee_paid_or_not[data] == 'no':
    senior_didnot_pay += 1
  elif user_type_of_membership[data] == 'Golden' and user_fee_paid_or_not[data] == 'no':
    golden_didnot_pay += 1

total_didnot_pay = junior_didnot_pay + adult_didnot_pay + senior_didnot_pay + golden_didnot_pay

print()
print()
print('-----MEMBER DATA-----')
print()
print('--2D Array of member data:--')
print()
print(member_details)
print()
print('--List of members:--')

for data in member_details:
  print()
  print()
  print("Membership number :", data[-1])
  print("Name :", data[0])
  print("Age :", data[1])
  print("Type of membership :", data[3])
  print("Part of the team member? :", data[4])
  print("Amount of annual fee :", data[5])
  print("Have paid your fee? :", data[-2])
print()
print('---------------------')

#Task 2: providing annual audit statistics DONE
#- count the number of current members by membership type DONE
#- for each type of membership: count the number of members who did not pay the annual fee DONE
#- display these counts as a percentage of the total number of members for each membership type DONE
#- calculate and display: 1. the total of the annual fees expected and the DONE
#                         2. annual fees received for this year DONE

print()
print()
print("--Number of member in each membership type:--")
print()
print("- Junior:", user_type_of_membership.count("Junior"))
print("- Adult:", user_type_of_membership.count("Adult"))
print("- Senior:", user_type_of_membership.count("Senior"))
print("- Golden:", user_type_of_membership.count("Golden"))
print()
print('Total:', user_type_of_membership.count('Junior') + user_type_of_membership.count('Adult') + user_type_of_membership.count('Senior') + user_type_of_membership.count('Golden'))

print()
print()
print("--Number of member in each membership type who didn't pay annual fee:--")
print()
print("- Junior:", junior_didnot_pay, ", in percent:", round(junior_didnot_pay / user_type_of_membership.count('Junior') * 100) if user_type_of_membership.count('Junior') > 0 else 0, "% (of Junior)")
print('- Adult:', adult_didnot_pay, ", in percent:", round(adult_didnot_pay / user_type_of_membership.count('Adult') * 100) if user_type_of_membership.count('Adult') > 0 else 0, "% (of Adult)")
print('- Senior:', senior_didnot_pay, ", in percent:", round(senior_didnot_pay / user_type_of_membership.count('Senior') * 100) if user_type_of_membership.count('Senior') > 0 else 0, "% (of Senior)")
print('- Golden:', golden_didnot_pay, ", in percent:", round(golden_didnot_pay / user_type_of_membership.count('Golden') * 100) if user_type_of_membership.count('Golden') > 0 else 0, "% (of Golden)")
print()
print('Total:', total_didnot_pay)

expected = (user_type_of_membership.count('Junior') * 10) + (user_type_of_membership.count('Adult') * 20) + (user_type_of_membership.count('Senior') * 15) + (user_type_of_membership.count('Golden') * 0)
received = expected - ((junior_didnot_pay * 10) + (adult_didnot_pay * 20) + (senior_didnot_pay * 15) + (golden_didnot_pay * 0))

print()
print()
print("--Total annual fees in this year:--")
print()
print('- Expected: $', expected)
print('- Received: $', received)

print()
print()
print('--List of members who did not pay:--')

for data in member_details:
  if data[-2] == 'no':
    print()
    print()
    print("- Membership number :", data[-1])
    print("- Name :", data[0])
    print("- Age :", data[1])
    print('- Gender :', data[2])
    print("- Type of membership :", data[3])

    member_details.remove(data)

print()
print('Total:', total_didnot_pay)
print()
print('----------------------------------------------------')

#Task 3: updating the membership details for the next year
#- check if any member have not paid and output a list of all these members and remove them from the system DONE
#Several tasks: - update the age of all the members by one year and whether they are in a team DONE
#-              - update the type of membership and the annual fee if required DONE
#- set the fee for every member as not yet paid DONE
#- display lists of current team members grouped by membership type DONE

print()
print('-')
print()
print('----------Member Details (incoming year updates)----------')
print()

member_details_oneyear = member_details
user_annual_fee = 0

for data in member_details_oneyear:
  data[1] += 1
  if data[1] >= 2 and data[1] < 18:
    data[3] = 'Junior'
  elif data[1] >= 18 and data[1] < 50:
    data[3] = 'Adult'
  elif data[1] >= 50 and data[1] < 80:
    data[3] = 'Senior'
  elif data[1] > 80:
    data[3] = 'Golden'

  if data[3] == 'Junior':
    data[-3] = 10
  elif data[3] == 'Adult':
    data[-3] = 20
  elif data[3] == 'Senior':
    data[-3] = 15
  elif data[3] == 'Golden':
    data[-3] = 0

  data[-2] = 'no'

print('-----MEMBER DATA-----')
print()
print('--2D Array of member data:--')
print()
print(member_details_oneyear)
print()
print('--List of members:--')

for data in member_details_oneyear:
  print()
  print()
  print("Membership number :", data[-1])
  print("Name :", data[0])
  print("Age :", data[1])
  print("Type of membership :", data[3])
  print("Part of the team member? :", data[4])
  print("Amount of annual fee :", data[5])
  print("Have paid your fee? :", data[-2])

print()
print('---------------------')

for data in member_details_oneyear:
  user_type_of_membership_oneyear.append(data[3])

print()
print()
print('--Number of member in each membership type:--')
print()
print('- Junior:', user_type_of_membership_oneyear.count('Junior'))
print('- Adult:', user_type_of_membership_oneyear.count('Adult'))
print('- Senior:', user_type_of_membership_oneyear.count('Senior'))
print('- Golden:', user_type_of_membership_oneyear.count('Golden'))
print()
print('Total:', user_type_of_membership_oneyear.count('Junior') + user_type_of_membership_oneyear.count('Adult') + user_type_of_membership_oneyear.count('Senior') + user_type_of_membership_oneyear.count('Golden'))
print()
print('----------------------------------------------------------')