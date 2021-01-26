"""
You are a doctor sorting through medical insurance cost data for some patients.

Using your knowledge of Python lists, you will store medical data and see what valuable insights you can gain from that data.

Let’s get started!
"""

"""
First, take a look at the two lists.

The list names stores the names of ten individuals, and insurance_costs stores their medical insurance costs.

Let’s add additional data to these lists:

Append a new individual, "Priscilla", to names.
Append her insurance cost, 8320.0, to insurance_costs.

"""

names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

names.append('Priscilla')
insurance_costs.append(8320.0)

"""

Currently, the names and insurance_costs lists are separate, but we want each insurance cost to be paired with a name.

Create a new variable called medical_records that combines insurance_costs and names into a list using the zip() function.

The list should have the following structure:
"""

medical_records = list(zip(names, insurance_costs))

# Print out medical_records in the terminal, and make sure the output is what you expected.
print(medical_records)

"""
Let’s explore our medical data.

We want to see how many medical records we’re dealing with. Create a variable called num_medical_records that stores the length of medical_records.
"""

num_medical_records = len(medical_records)

# Print num_medical_records with the following message:

print(f'There are {num_medical_records} medical records')

"""
Select the first medical record in medical_records, and save it to a variable called first_medical_record
"""
first_medical_record = medical_records[0]

# Print first_medical_record with the following message:
print(f'Here is the first medical record: Name:{first_medical_record[0]} , Cost:{first_medical_record[1]} ')

"""
Sort medical_records so that the individuals with the lowest insurance costs appear at the start of the list.

Print the sorted medical_records with the following message:
"""
medical_records.sort(key=lambda x: x[1])
print(f'Here are the medical records sorted by insurance cost: {medical_records}')

"""
Let’s look at the three cheapest insurance costs in our medical records.

Slice the medical_records list, and store the three cheapest insurance costs in a list called cheapest_three.
"""
cheapest_three = medical_records[:3]

# Print cheapest_three with the following message:
print(f'Here are the three cheapest insurance costs in our medical records: {cheapest_three}')

"""
Let’s look at the three most expensive insurance costs in our medical records.

Slice the medical_records list, and store the three most expensive insurance costs in a list called priciest_three.
"""

priciest_three = medical_records[-3:]

# Print priciest_three with the following message:
print(f'Here are the three most expensive insurance costs in our medical records: {priciest_three}')

"""
Some individuals in our medical records have the same name. For example, the name “Paul” shows up twice.

Count the number of occurrences of “Paul” in the names list, and store the result in a variable called occurrences_paul.

Print occurrences_paul with the following message:
"""
occurrences_paul = 0
for i in names:
    if i == 'Paul':
        occurrences_paul += 1

print(f'There are {occurrences_paul} individuals with the name Paul in our medical records. ')

"""

Great job! In this project, you worked with Python lists to store medical insurance cost data and then gained meaningful insight into that data.

You now have a better understanding of how to interact with data in lists – an important skill for a data scientist to have.

Our dataset in this project was pretty small – we only dealt with 11 medical records. However, as you progress in your data science journey, you will encounter larger and more complex datasets. You are now better prepared to work with data in lists moving forward.

If you’d like additional practice on lists, here are some ways you might extend this project:

Sort the medical records alphabetically by name. You’ll have to create a new list using zip() to do this.
Select the medical records starting at index 3 and ending at index 7 and save it in a variable called middle_five_records.
"""
medical_records.sort()
middle_five_records = medical_records[3:8]
print(middle_five_records)