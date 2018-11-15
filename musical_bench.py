import RPi.GPIO as GPIO
import pygame as pygame

pygame.mixer.pre_init(44100, -16, 2, 2048)
#pygame.mixer.init()
#pygame.mixer.Sound.set_volume(1.0)
pygame.init()

GPIO.setmode(GPIO.BCM)

GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

#GPIO.setup(25,GPIO.OUT,initial=GPIO.LOW)



#Four_bit = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110']

s13=pygame.mixer.Sound('15.wav')
s12=pygame.mixer.Sound('14.wav')
s11=pygame.mixer.Sound('13.wav')
s10=pygame.mixer.Sound('12.wav')
s9=pygame.mixer.Sound('11.wav')
s8=pygame.mixer.Sound('10.wav')
s7=pygame.mixer.Sound('9.wav')
s6=pygame.mixer.Sound('8.wav')
s5=pygame.mixer.Sound('7.wav')
s4=pygame.mixer.Sound('6.wav')
s3=pygame.mixer.Sound('5.wav')
s2=pygame.mixer.Sound('4.wav')
s1=pygame.mixer.Sound('3.wav')
s=pygame.mixer.Sound('2.wav')



while True:

	x=[GPIO.input(4),GPIO.input(17),GPIO.input(23),GPIO.input(24)]	
        print(x)
  #      mixer.init()
        if x == [False,False,False,False]:
         
        # mixer.init()

#         s.stop()
#         s1.stop()
#         s2.stop()       
#         s3.stop()
#         s4.stop()
#         s5.stop()
#         s6.stop()
#         s7.stop()
#         s8.stop()
#         s9.stop()
#         s10.stop()
#         s11.stop()
#         s12.stop()
#         s13.stop()
          pygame.mixer.music.pause()         
         
         #mixer.music.play()



       #  while mixer.music.get_busy():

        #    pass

		

        if x == [False,False,False,True]:

         

         #pygame.mixer.music.load('2.wav')
  
         #pygame.mixer.music.play()
        # s=pygame.mixer.Sound('2.wav')
         channel=s.play()

         #if x == [False,False,False,False]:
          #s.stop()

         #Sound.set_volume(s)
        


         while pygame.mixer.music.get_busy():

            pass

		

		

        elif x == [False,False,True,False]:

      #   mixer.init()

         #pygame.mixer.music.load('3.wav')

         #pygame.mixer.music.play()
        # s1=pygame.mixer.Sound('3.wav')
         channel=s1.play()

         #if x == [False,False,False,False]:
         # s1.stop()




         while pygame.mixer.music.get_busy():

            pass

		

        elif x == [False,False,True,True]:

        # mixer.init()

         #pygame.mixer.music.load('4.wav')

         #pygame.mixer.music.play()
         #s2=pygame.mixer.Sound('4.wav')
         channel=s2.play()


         #if x == [False,False,False,False]:
         # s2.stop()



         while pygame.mixer.music.get_busy():

            pass

		
        elif x == [False,True,False,False]:

       #  mixer.init()

         #pygame.mixer.music.load('5.wav')

         #pygame.mixer.music.play()
        # s3=pygame.mixer.Sound('5.wav')
         channel=s3.play()

        # if x == [False,False,False,False]:
         # s3.stop()




         while pygame.mixer.music.get_busy():

            pass

		

		

        elif x == [False,True,False,True]:

         #mixer.init()

         #pygame.mixer.music.load('6.wav')

         #pygame.mixer.music.play()
         #s4=pygame.mixer.Sound('6.wav')
         channel=s4.play()

         #if x == [False,False,False,False]:
         # s4.stop()




         while pygame.mixer.music.get_busy():

            pass

		

		

        elif x == [False,True,True,False]:

       #  mixer.init()

         #pygame.mixer.music.load('7.wav')

         #pygame.mixer.music.play()
       #  s5=pygame.mixer.Sound('7.wav')
         channel=s5.play()

         #if x == [False,False,False,False]:
         # s5.stop()



         while pygame.mixer.music.get_busy():

            pass

		

		

        elif x == [False,True,True,True]:

        # mixer.init()

         #pygame.mixer.music.load('8.wav')

         #pygame.mixer.music.play()
        # s6=pygame.mixer.Sound('8.wav')
         channel=s6.play()

        # if x == [False,False,False,False]:
        #  s6.stop()




         while pygame.mixer.music.get_busy():

            pass

		

        elif x == [True,False,False,False]:

        #  mixer.init()

         #pygame.mixer.music.load('9.wav')

         #pygame.mixer.music.play()
        # s7=pygame.mixer.Sound('9.wav')
         channel=s7.play()


       #  if x == [False,False,False,False]:
        #  s7.stop()



         while pygame.mixer.music.get_busy():

            pass

		

		

        elif x == [True,False,False,True]:

#         mixer.init()

         #pyame.mixer.music.load('10.wav')

         #pygame.mixer.music.play()
        # s8=pygame.mixer.Sound('10.wav')
         channel=s8.play()

       #  if x == [False,False,False,False]:
       #   s8.stop()




         while pygame.mixer.music.get_busy():

            pass

		

		

        elif x == [True,False,True,False]:

 #        mixer.init()

         #pygame.mixer.music.load('11.wav')

         #pygame.mixer.music.play()
       #  s9=pygame.mixer.Sound('11.wav')
         channel=s9.play()

        # if x == [False,False,False,False]:
        #  s9.stop()




         while pygame.mixer.music.get_busy():

            pass

		

        elif x == [True,False,True,True]:

  #       mixer.init()

         #pygame.mixer.music.load('12.wav')

         #pygame.mixer.music.play()
        # s10=pygame.mixer.Sound('12.wav')
         channel=s10.play()

        # if x == [False,False,False,False]:
        #  s10.stop()




         while pygame.mixer.music.get_busy():

            pass

		

        elif x == [True,True,False,False]:

   #      mixer.init()

         #pygame.mixer.music.load('13.wav')

         #pygame.mixer.music.play()
        # s11=pygame.mixer.Sound('13.wav')
         channel=s11.play()


        # if x == [False,False,False,False]:
        #  s11.stop()



         while pygame.mixer.music.get_busy():

            pass

		

        elif x == [True,True,False,True]:

    #     mixer.init()

         #pygame.mixer.music.load('14.wav')

         #pygame.mixer.music.play()
        # s12=pygame.mixer.Sound('14.wav')
         channel=s12.play()

         #if x == [False,False,False,False]:
         # s12.stop()




         while pygame.mixer.music.get_busy():

            pass

		

		

        elif x==[True,True,True,True]:

     #    mixer.init()

         #pygame.mixer.music.load('15.wav')

         #pygame.mixer.music.play()
         #s13=pygame.mixer.Sound('15.wav')
         channel=s13.play()

        # if x == [False,False,False,False]:
        #  s13.stop()




         while pygame.mixer.music.get_busy():

            pass
