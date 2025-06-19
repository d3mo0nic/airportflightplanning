#     IMPORTANT INFO     #
# The 3 letter airport 
# code is either BOH
# or LPL (make sure in all caps)
# All overseas airport codes are
# JFK,ORY,MAD,AMS,CAI
#
import time
import os

userdoneop1 = False
userdoneop2 = False
def main_menu():
  global userdoneop1
  global userdoneop2
  global overAirportName
  global distance
  global MaxflightRange
  global hasenteredaircrafttype
  global NstandardclassSeats
  global NfirstclassSeats
  print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
  print("│          ►Welcome To Flight Planning◄          │")
  print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
  print("│ » 1 To Enter Airport Details                   │")
  print("│ » 2 To Enter Flight Details                    │")
  print("│ » 3 To Enter Price Plan and Calculate Profits  │")
  print("│ » 4 To Clear data                              │")
  print("│ » 5 To Quit Program                            │")
  print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
  inputstart = input("  » ")
  print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
  if inputstart != "5":
    print("│           ⤇    Opening Terminal    ⤆           │", end="\r")
    time.sleep(1)
    print("│           ⤇    Opening Terminal.   ⤆           │", end="\r")
    time.sleep(1)
    print("│           ⤇    Opening Terminal..  ⤆           │", end="\r")
    time.sleep(1)
    print("│           ⤇    Opening Terminal... ⤆           │")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("│               ►Flight Terminal◄                │")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
  time.sleep(1)

  if inputstart == "1":
    print("│ » Please enter your 3 letter airport code      │")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    ThreeLetterAirportCode = input("  » ")
    ThreeLetterAirportCode.upper()
    if ThreeLetterAirportCode != "LPL" and ThreeLetterAirportCode != "BOH":
      print("│ » Invalid code                               │")
      time.sleep(1)
      print("│ » Returning to main menu                     │")
      print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
      time.sleep(1)
      os.system('cls' if os.name == 'nt' else 'clear')
      main_menu()
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("│ » Please enter your overseas airport code      │")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    OverAirportCode = input("  » ")
    OverAirportCode.upper()
    overAirportName = ""
    with open("Airports.txt", "r") as file:
      for line in file:
          if OverAirportCode in line:
              overAirportName = line.split(',')[1].strip()
              break
    #file.close()
    if(overAirportName == ""):
      print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
      print("│ » Invalid code                               │")
      time.sleep(1)
      print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
      print("│ » Returning to main menu                     │")
      print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
      time.sleep(1)
      os.system('cls' if os.name == 'nt' else 'clear')
      main_menu()

    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("  » Your full overseas Airport name is           ")
    print("  » ", overAirportName)
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    time.sleep(2)
    count = 0
    distance = ""
    file = open("Airports.txt", "r")
    for line in file:
      #airport distance from overseas airport
      if OverAirportCode in line:
        for i in range(0, len(line)):
          i + 1
          if ThreeLetterAirportCode == "BOH":
            if line[i] == ",":
              count = count + 1
            if count == 3:
              i = i + 1
              #break if max 

            if count >= 3:
              if i == len(line):
                break
              distance = distance + line[i]
          if ThreeLetterAirportCode == "LPL":
            if line[i] == ",":
              count = count + 1
              if count == 3:
                break
            if count == 2:
              i = i + 1
            if count >= 2:
              if count == 3:
                break
              distance = distance + line[i]
    #remove comma from diztance here
    distance = distance.replace(",", "")
    overAirportName = overAirportName.replace(",", "")
    print("  » Distance from ", overAirportName, "\n", " » in km",  "is ", distance)
    file.close()
    #convert distance to integer here
    distance = int(distance)
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("│ » Returning to main menu                       │")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    time.sleep(1)
    time.sleep(2)
    userdoneop1 = True
    os.system('cls' if os.name == 'nt' else 'clear')
    main_menu()
  elif inputstart == "2":
    hasenteredaircrafttype = False
    def enteraircraftType():
      global aircraftType
      global RcostPseatP100km 
      global MaxflightRange 
      global CapifallSeatsStandard
      global MinfirstclassSeats
      print("│ » Please enter your type of aircraft           │")
      print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
      print("│ » Input 1 For Medium Narrow Body               │")
      print("│ » Input 2 For Large Narrow Body                │")
      print("│ » Input 3 For Medium Wide Body                 │")
      print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
      aircraftType = input("  » ")
      print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
      if aircraftType == "1":
          RcostPseatP100km = 8
          MaxflightRange = 2650
          CapifallSeatsStandard = 180
          MinfirstclassSeats = 8
          print("  » Running cost per seat per 100km is", RcostPseatP100km)
          print("  » Max Flight range(km)", MaxflightRange)
          print("  » Cap if all seats are standard class is",CapifallSeatsStandard)
          print("  » Minimum first class seats are", MinfirstclassSeats)
      if aircraftType == "2":
        RcostPseatP100km = 7
        MaxflightRange = 5600
        CapifallSeatsStandard = 220
        MinfirstclassSeats = 10
        print("  » Running cost per seat per 100km is", RcostPseatP100km)
        print("  » Max Flight range(km)", MaxflightRange)
        print("  » Cap if all seats are standard class is ",CapifallSeatsStandard)
        print("  » Minimum first class seats are", MinfirstclassSeats)
      if aircraftType == "3":
        RcostPseatP100km = 5
        MaxflightRange = 4050
        CapifallSeatsStandard = 406
        MinfirstclassSeats = 14
        print("  » Running cost per seat per 100km is", RcostPseatP100km)
        print("  » Max Flight range(km)", MaxflightRange)
        print("  » Cap if all seats are standard class is",CapifallSeatsStandard)
        print("  » Minimum first class seats are", MinfirstclassSeats)
    time.sleep(2)
    enteraircraftType()
    while hasenteredaircrafttype == False:
      print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
      print("  » Are you sure you want this type of aircraft? |")
      print("  » Please input Y or N for Yes or No            |")
      print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
      def inputYorN():
        global hasenteredaircrafttype
        global YorN
        YorN = input("  » ")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        if YorN == "Y":
          hasenteredaircrafttype = True
        elif YorN == "N":
          enteraircraftType()
        else:
          print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
          print("│ » Please enter Y or N                        │")
          print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
          inputYorN()
      inputYorN()

    print("│ » Please enter number of first class seats     │")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    NfirstclassSeats = int(input("  » "))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    if aircraftType == "1":
        if NfirstclassSeats < 8:
            print("│ » Minumum number of seats exceed input          │")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            time.sleep(1)
            print("│ » Returning to main menu                       │")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            main_menu()

    elif aircraftType == "2":
        if NfirstclassSeats < 10:
            print("│ » Minumum number of seats exceed input          │")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            time.sleep(1)
            print("│ » Returning to main menu                       │")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            main_menu()
    elif aircraftType == "3":
        if NfirstclassSeats < 14:
            print("│ » Minumum number of seats exceed input          │")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            time.sleep(1)
            print("│ » Returning to main menu                       │")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

            main_menu()
    DoubleFirstClass = NfirstclassSeats * 2
    NstandardclassSeats = CapifallSeatsStandard - DoubleFirstClass
    print("  » Number of standard class seats are", NstandardclassSeats)
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    time.sleep(2)
    print("│ » Returning to main menu                       │")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    time.sleep(2)
    userdoneop2 = True
    os.system('cls' if os.name == 'nt' else 'clear')
    main_menu()
  elif inputstart == "3":
    if userdoneop1 == True and userdoneop2 == True:
      if MaxflightRange >= int(distance):
        print("│ » Please enter price of standard class seat (£)  │")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        PofStandardseat = input("  » ")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("│ » Please enter price of first class seat (£)     │")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        PofFirstseat = input("  » ")
        PofFirstseat = float(PofFirstseat)
        PofStandardseat = float(PofStandardseat)
        RcostTbyDistance = RcostPseatP100km * distance
        Flightcostperseat = RcostTbyDistance / 100
        print("│ » Flight cost per seat is £", Flightcostperseat)
        NofSeats = NstandardclassSeats + NfirstclassSeats
        FlightCost = Flightcostperseat * NofSeats
        print("│ » Flight cost is £", FlightCost)
        SclassFlightIncome = NstandardclassSeats * PofStandardseat
        FclassFlightIncome = NfirstclassSeats * PofFirstseat
        FlightIncome = FclassFlightIncome + SclassFlightIncome
        print("│ » Flight Income is £", FlightIncome)
        FlightProfit = FlightIncome - FlightCost
        RFlightProfit = round(FlightProfit, 2)
        print("│ » Flight Profit is £", RFlightProfit)
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        time.sleep(5)
        print("│ » Thank you for using our program             │")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        time.sleep(5)
        print("│ » Returning to main menu                       │")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
        main_menu()
      else: 
        print("│ » Max flight range of aircraft smaller than   │")
        print("│ » distance between airports                   │")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        time.sleep(1)
        print("│ » Returning to main menu                       │")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        main_menu()
    else:
      print("│ » Please Complete option 1 & 2                │")
      print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
      time.sleep(1)
      print("│ » Returning to main menu                       │")
      print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
      time.sleep(2)
      os.system('cls' if os.name == 'nt' else 'clear')
      main_menu()
  elif inputstart == "4":
    userdoneop1 = False
    userdoneop2 = False
    print("│ » cleared all data                              │")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    main_menu()
  elif inputstart == "5":
    print("│           ✖    Quiting Program    ✖            │", end="\r")
    time.sleep(1)
    print("│           ✖    Quiting Program.   ✖            │", end="\r")
    time.sleep(1)
    print("│           ✖    Quiting Program..  ✖            │", end="\r")
    time.sleep(1)
    print("│           ✖    Quiting Program... ✖            │")
    time.sleep(1)
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
main_menu()