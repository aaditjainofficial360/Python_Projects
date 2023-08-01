'''
Heavy Rain Alert
Difficulty: Medium
You can see information about when some of the areas around Bangalore start to get flooded.
“KR Puram” - Risk of flood if it rains more than 4 cm.
“Bellandur” - Risk of flood if it rains more than 5 cm.
“Gangothri Road” - Risk of flood if it rains more than 10 cm.
Create an object which stores the present amount of rain and the above information about the 3 given areas with the threshold rain in cm. The object should have a method, which will print the following message - “Heavy rain in {area}. Risk of flood” if rain exceeds the threshold value for any region.
Given the rain amount in cm as input, instantiating an object and calling the method should print the appropriate messages.
Examples:
Test Case 1:
Input: 5
Output:
Heavy rain in KR Puram. Risk of flood
Explanation: Rain threshold value for KR Puram is 4. Given rain amount is greater than 4. So we print a message for KR Puram. It isn’t greater than 5 or 10, so we don’t print any message for the other areas.
Test Case 2:
Input : 12
Output:
Heavy rain in KR Puram. Risk of flood
Heavy rain in Bellandur. Risk of flood
Heavy rain in Gangothri Road. Risk of flood
Explanation:
12 is greater than all thresholds 4, 5 and 10. So we print 3 messages.
'''

class Weather_Info:
    def __init__(self,rain_amount):
        self.rain_amount=rain_amount
    def heavy_rain_alert(self):
        if self.rain_amount>4 :
            print('Heavy rain in KR Puram. Risk of flood')
        if self.rain_amount>5:
            print('Heavy rain in Bellandur. Risk of flood')
        if self.rain_amount>10:
            print('Heavy rain in Gangothri Road. Risk of flood')
        return ''

# Test-case 1
# 5cm of Rainfall detected
Input1 = 5
T1=Weather_Info(Input1)
T1.heavy_rain_alert()

# Test-case 2
# 5cm of Rainfall detected
Input2 = 12
T2=Weather_Info(Input2)
T2.heavy_rain_alert()

