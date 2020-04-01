def weight_on_planets():
   # write your code here
   weightOnEarth = float(input("What do you weight on earth? "))
   weightOnMars = .38 * weightOnEarth
   weightOnJupiter = 2.34 * weightOnEarth
   print("\nOn Mars you would weigh", weightOnMars, "pounds.\n"
      "On Jupiter you would weigh", weightOnJupiter, "pounds.")

   
   
   
if __name__ == '__main__':
   weight_on_planets()