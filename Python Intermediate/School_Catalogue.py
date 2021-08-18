"""
1.
Let’s start by making a parent class for Primary, Middle, and High classes.
Create an empty class named School.

2.
Inside the School class, create a constructor that accepts three parameters in addition to self.
The names of these parameters should match the properties listed in the narrative above.

3.
inside the constructor, set the School properties equal to the values passed into the constructor.
Remember to use the self keyword when setting these properties.

4.
Create getters for the name, level, and numberOfStudents properties.
Each getter should return the value saved to the property.

5.
Create a setter for numberOfStudents.
This method should take one parameter (in addition to self) and
set self.numberOfStudents equal to the value passed into the method.

6.

Create a __repr__() method so when a School is printed,
it displays relevant information about the object.
You can choose what you want displayed, but we printed:

A {level} school named {name} with {numberOfStudents} students

7.
At this point, it’s probably a good idea to test your code if you haven’t already.
Try creating a School object, use the getter and setter methods you created, and print that object

8.
Next, we’ll build a PrimarySchool class that inherits from School.
If you feel comfortable building the PrimarySchool class on your own, give it a shot.
If not, use the steps below to help you along the way.
Whether you want to follow the steps or not,
it’s important to note, the PrimarySchool class only has one additional property, pickupPolicy.
Create an empty PrimarySchool class that inherits from School.

9.
Inside the PrimarySchool class, create a constructor that accepts three arguments in addition to self.
Think about which three properties we’ll need arguments for.

10.
Call super().__init__() on the first line of the PrimarySchool‘s constructor.
Pass it any arguments that the parent constructor uses.
Since this is the PrimarySchool class, pass 'primary' as the argument for the level parameter in the parent constructor.

11.
You’ve used two of the arguments you’ve passed to the PrimarySchool constructor.
Now use the third argument to set the value of a new property named self.pickupPolicy.

12.
Since our PrimarySchool class inherits Schools‘s properties and getters,
we only need to create one new getter in the PrimarySchool class.
Add this getter to the PrimarySchool class. Each getter should return the value saved to that property.

13.
Finally, we probably want the __repr__() method for a PrimarySchool to display information about
the pickupPolicy variable. Override the __repr__() method so when a PrimarySchool is printed,
information about the pickup policy is displayed in addition to the other information about the school.
You can call super().__repr__() to avoid repeating some code.

14.
Create a PrimarySchool object and verify your new constructor, getter method, and __repr__() method work as expected.

15.
.
In this task, you will create a HighSchool class that inherits from the School class. In addition to the properties,
getters, and methods in School, the HighSchool includes the following:
Properties: sportsTeams (list of strings)
Getters: A getter for the sportsTeams array. The getter should return the list of the sports teams.
Override the __repr__() method to display information about sportsTeams.
"""


class School:
    def __init__(self, name, level, number_of_students):
        self._name = name
        self._level = level
        self._number_of_students = number_of_students

    def __repr__(self):
        return f'A {self._level} school named {self._name} with {self._number_of_students} students'

    @property
    def name(self):
        return self._name

    @property
    def level(self):
        return self._level

    @property
    def number_of_students(self):
        return self._number_of_students

    @number_of_students.setter
    def number_of_students(self, number):
        if isinstance(number, int):
            self._number_of_students = number

    @level.setter
    def level(self, level):
        levels = ['primary', 'middle', 'high']
        if level.lower() in levels:
            self._level = level.lower()


class PrimarySchool(School):
    def __init__(self, name, number_of_students, pickup_policy):
        super().__init__(name, 'primary', number_of_students)
        self._pickup_policy = pickup_policy

    @property
    def pickup_policy(self, policy):
        self._pickup_policy = policy

    def __repr__(self):
        inherited = super().__repr__()
        return f'{inherited}. The pickup polity is: {self._pickup_policy}'


class HighSchool(School):
    def __init__(self, name, number_of_students, sports_teams):
        super().__init__(name, 'high', number_of_students)
        self._sports_teams = sports_teams

    @property
    def sports_teams(self, teams):
        self._sports_teams = teams

    def __repr__(self):
        inherited = super().__repr__()
        return f'{inherited}. Sport Teams Are: {self._sports_teams}'

a = PrimarySchool('Neapoli', 50, 'Pickup after 3pm')
b = HighSchool('Itea', 20, ['Basketball', 'Football'])
print(a)
print(b)
