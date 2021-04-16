"""
You have been asked to develop a system that makes it easier to organize patient data. You will create a class that does the following:

Takes in patient parameters regarding their personal information
Contains methods that allow users to update their information
Gives patients insight into their potential medical fees.
"""
# STEP 1
"""
If you look at script.py, you will see that we have started a class called Patient. It currently has an __init__ method with two class variables: self.name and self.age.

Let’s start by adding in some more patient parameters:

sex: patient’s biological identification, 0 for male and 1 for female
bmi: patient BMI
num_of_children: number of children patient has
smoker: patient smoking status, 0 for a non-smoker and 1 for a smoker
Add these into the __init__ method so that we can use them as we create our class methods.
"""
# STEP 2
"""
Let’s test out our __init__ method and create our first instance variable.

Create an instance variable outside of our class called patient1.

patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
Next, print out the name of patient1 using the following line of code:

print(patient1.name)
Print out the rest of patient1’s information to ensure the __init__ method is functioning properly.
"""
# STEP 3
"""
Now that our constructor is built out and ready to go, let’s start creating some methods! Our first method will be 
estimated_insurance_cost(), which takes our instance’s parameters (representing our patient’s information) and returns 
their expected yearly medical fees.
Below the __init__ constructor, define our estimated_insurance_cost() constructor which only takes self as an argument.
Inside of this method, add the following formula:
estimated_cost=250∗age−128∗sex+370∗bmi+425∗num_of_children+24000∗smoker−12500
Note that we are using class variables in our formula here, so be sure to remember to use the self keyword.
"""
# STEP 4
"""
Inside of our estimated_insurance_cost() method, let’s add a print statement that displays the following in the terminal:
{Patient Name}’s estimated insurance costs is {estimated cost} dollars.
Then, test out this method using the patient1 instance variable.
"""
# STEP 5
"""
We already have one super useful method in our class! Let’s add some more and make our Patient class even more powerful.
What if our patient recently had a birthday? Or had a fluctuation in weight? Or had a kid? Let’s add some methods that
allow us to update these parameters and recalculate the estimated medical fees in one swing.
First, create an update_age() method. It should take in two arguments: self and new_age. In this method reassign 
self.age to new_age.
"""
# STEP 6
"""
Let’s flesh out this method some more!
Add a print statement that outputs the following statement in the terminal:
{Patient Name} is now {Patient Age} years old.
Test out your method using the patient1 instance variable.
"""
# STEP 7
"""
We also want to see what the new insurance expenses are.
Call the estimated_insurance_cost() method in update_age()using this line of code:
self.estimated_insurance_cost()
Test out your method with patient1.
"""
# STEP 8
"""
Let’s make another update method that modifies the num_of_children parameter.
Below the update_age() method, define a new one called update_num_children(). This method should have two arguments, 
self and new_num_children. Inside the method, self.num_of_children should be set equal to new_num_children.
"""
# STEP 9
"""
Similarly to the method we wrote before, 
let’s add in a print statement that clarifies the information that is being updated.
Your print statement should output the following in the terminal:
{Patient Name} has {Patient’s Number of Children} children.
Use the patient1 instance variable to test out this method. Set the new_num_children argument to 1.
Do you notice anything strange about the output?
"""
# STEP 10
"""
You may have noticed our terminal output is grammatically incorrect because John Doe only has 1 child.
Let’s update our method to accurately convey when we should use the noun “children” versus when we should use “child”.
To do this we can use control flow.
If the patient has 1 offspring, we should see the following output:
{Patient Name} has {Patient Number of Children} child.
Otherwise, we should see this output:
{Patient Name} has {Patient Number of Children} children.
Write out your control flow program, and test it out using patient1.
"""
# STEP 11
"""
To finish off the update_num_children() method, let’s call our estimated_insurance_cost() method at the end.
Use patient1 to ensure that everything is functioning as expected!
"""
# STEP 12
"""
Let’s create one last method that uses a dictionary to store a patient’s information in one convenient variable. 
We can use our parameters as the keys and their specific data as the values.
Define a method called patient_profile() that builds a dictionary called patient_information to hold all 
of our patient’s information.
Note: See the Hint to find out how to use a dictionary to store this data.
"""
# STEP 13
"""
Let’s test out our final method! Use patient1 to call the method patient_profile().
Remember that in patient_profile() we used a return statement rather than a print statement.
In order to see our dictionary outputted to the terminal, we must wrap a print statement around our method call. 
Use patient1 to call the method patient_profile().
"""

# STEP 14
"""Congratulations! You have successfully made a powerful Patient class! Classes are an incredibly useful programming 
tool because they allow you to create a blueprint that can be used to build many objects off of. In this case, 
you can organize any patient’s information and apply all methods from Patient to update and arrange their data. There 
are endless possibilities for extending the capabilities of this class. If you would like to continue to work on this 
Patient class, take a look at the following challenges: 
Build out more methods that allow users to update more patient parameters, such as update_bmi() or 
update_smoking_status(). Use try and except statements to ensure that patient data is uploaded using numerical 
values. Update the class so that users can upload lists of patient data rather than just individual numbers. Happy 
coding! """
class Patient:
    def __init__(self, name, age, sex, bmi, num_of_children, smoker):
        self.name = name
        self.age = age
        self.sex = sex  # STEP 1
        self.bmi = bmi
        self.num_of_children = num_of_children
        self.smoker = smoker

    def estimated_insurance_cost(self):  # STEP 3
        estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
        print(f"{self.name}’s estimated insurance costs is {estimated_cost} dollars.")  # STEP 4

    def update_age(self, new_age):  # STEP 5
        self.age = new_age
        print(f"{self.name} is now {self.age} years old")  # STEP 6
        self.estimated_insurance_cost()  # STEP 7

    def update_num_children(self, new_num_children):  # STEP 8
        self.num_of_children = new_num_children
        (print(f'{self.name} has {self.num_of_children} children.') if self.num_of_children > 1 else
         print(f'{self.name} has {self.num_of_children} child.'))  # STEP 9 / STEP 10
        self.estimated_insurance_cost()  # STEP 11

    def patient_profile(self):  # STEP 12
        patient_information = {}
        patient_information["Name"] = self.name
        patient_information["Age"] = self.age
        patient_information["Sex"] = self.sex
        patient_information["BMI"] = self.bmi
        patient_information["Number of Children"] = self.num_of_children
        patient_information["Smoker"] = self.smoker
        return patient_information


patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)  # STEP 2

patient1.estimated_insurance_cost()
patient1.update_age(20)
print(patient1.age)
patient1.update_num_children(1)
print(patient1.patient_profile())
