from Klok import Ds1307

try:

    klok = Ds1307()

    print("WRITE")

    klok.writeString("NMCT")

    print("READ")

    klok.getString()

    print(klok.getString())


except Exception as ex:
    str(ex)

finally:
    print("Program has ended")
    # GPIO.cleanup()