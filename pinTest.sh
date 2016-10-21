
gordon @ pi2: ./pintest
PinTest
=======

This is a simple utility to test the GPIO pins on your revision 1
Raspberry Pi.

NOTE: All GPIO peripherals must be removed to perform this test. This
  includes serial, I2C and SPI connections. You may get incorrect results
  if something is connected and it interferes with the test.

This test can only test the input side of things. It uses the internal
pull-up and pull-down resistors to simulate inputs. It does not test
the output drivers.

You will need to reboot your Pi after this test if you wish to use the
serial port as it will be left in GPIO mode rather than serial mode.

Please make sure everything is removed and press the ENTER key to continue,
or Control-C to abort...

          The main 8 GPIO pins  0: 7:  OK
                The 5 SPI pins 10:14:  OK
               The serial pins 15:16:  OK
                  The I2C pins  8: 9:  OK
