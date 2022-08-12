# -*- coding: utf-8 -*-
"""
Created on Fri May 27 11:51:16 2022

@author: Oliver
"""

import variables_and_imported_libraries as vil

"""
The Somos Arithmetic Sequence Class and Algorithm

The Somos algorithm produces a somos sequence for both odd and even somos
numbers. Due to the triviality of Somos-1, it was not taken into consideration
in this algorithm, thus please do not specify it. The algorithm initializes by
producing an array that is filled in with 1s until the Somos number is reached.

For ODD Somos numbers it takes out the divisibility factor 
(The first element of the array) and then divides the rest of the array into 
two equal ones. It then flips the second array and multiplies them together.
Then the sum of the multiplied array is taken and is divided by the divisibility
factor. Its then appended to the original array, as all of these operations are
done on the copy of it. 

For EVEN Somos numbers it also takes out the divisibility factor (The first
element of the array), however in this case it is left with an ODD array. The 
algorithm finds the middle of that array and appends it to a new array called
middle. It then deletes the middle from the original copy and divides that array
into two again as in the ODD somos number array. It then multiplies the left
and right arrays and sums them together as well as adds the square of the middle
array, which is just one value at all times. The new somos value is calculated
and appended to the original somos array.

"""

class Somos:
    def __init__(self, s_n, itt):
        self.somos_number = s_n
        self.itteration = itt
        self.time = 0
        self.counter = 0
        self.summ = 0
        self.somos_array = []
        self.type_of_somos = ""
        self.multiplied_array = []
        
    def Somos_setup(self):
        for i in range(self.somos_number):
            self.somos_array.append(1)
        if self.somos_number%2 ==0:
            self.type_of_somos = "even"
        else:
            self.type_of_somos = "odd"
        return self.somos_array, self.type_of_somos
    
    def Somos_algorithm(self):
        while self.itteration - self.counter > 0:
            self.summ = 0
            if self.type_of_somos == "odd":
                div_factor = self.somos_array[self.counter]
                somos_array_2 = self.somos_array.copy()
                while len(somos_array_2) - (self.somos_number-1) > 0:
                    somos_array_2.pop(0)
                middle_index = int((self.somos_number-1)/2)
                first_half = somos_array_2[:middle_index]
                second_half = somos_array_2[middle_index:]
                second_half_rev = second_half[::-1]
                for i,j in zip(first_half, second_half_rev):
                    self.multiplied_array.append(int(i*j))
                for element in self.multiplied_array:
                    self.summ += element
                new_somos_value = self.summ/div_factor
                self.somos_array.append(new_somos_value)
                self.counter += 1
                self.multiplied_array = []
            if self.type_of_somos == "even":
                div_factor = self.somos_array[self.counter]
                somos_array_2 = self.somos_array.copy()
                while len(somos_array_2) - (self.somos_number-1) > 0:
                    somos_array_2.pop(0)
                middle_index = int((self.somos_number)/2-1)
                middle = somos_array_2[middle_index]
                somos_array_2.pop(middle_index)
                first_half = somos_array_2[:middle_index]
                second_half = somos_array_2[middle_index:]
                second_half_rev = second_half[::-1]
                for i,j in zip(first_half, second_half_rev):
                    self.multiplied_array.append(int(i*j))
                for element in self.multiplied_array:
                    self.summ += element
                self.summ += middle**2
                new_somos_value = self.summ/div_factor
                self.somos_array.append(new_somos_value)
                self.counter += 1
                self.multiplied_array = []
        return self.somos_array
    
    def plot(self):
        y_values = []
        x_values = []
        self.counter = 0
        for element in self.somos_array:
            if element == 1:
                continue
            else:
                y_values.append(vil.np.log(element))
                x_values.append(self.counter)
            self.counter += 1
        return vil.plt.plot(x_values,y_values)
n = 40    
obj= Somos(5,n)
obj.Somos_setup()
obj.Somos_algorithm()
obj.plot()
vil.plt.xlabel("Itteration")
vil.plt.ylabel("Value of Somos Sequence")
vil.plt.show()
