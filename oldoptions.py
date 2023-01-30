"""""
docstring
"""""

marvin_image = r"""
         _                      _______                      _
   _dMMMb._              .adOOOOOOOOOba.              _,dMMMb_
  dP'  ~YMMb            dOOOOOOOOOOOOOOOb            aMMP~  `Yb
  V      ~"Mb          dOOOOOOOOOOOOOOOOOb          dM"~      V
           `Mb.       dOOOOOOOOOOOOOOOOOOOb       ,dM'
            `YMb._   |OOOOOOOOOOOOOOOOOOOOO|   _,dMP'
       __     `YMMM| OP'~"YOOOOOOOOOOOP"~`YO |MMMP'     __
     ,dMMMb.     ~~' OO     `YOOOOOP'     OO `~~     ,dMMMb.
  _,dP~  `YMba_      OOb      `OOO'      dOO      _aMMP'  ~Yb._
 <MMP'     `~YMMa_   YOOo   @  OOO  @   oOOP   _adMP~'      `YMM>
              `YMMMM\`OOOo     OOO     oOOO'/MMMMP'
      ,aa.     `~YMMb `OOOb._,dOOOb._,dOOO'dMMP~'       ,aa.
    ,dMYYMba._         `OOOOOOOOOOOOOOOOO'          _,adMYYMb.
   ,MP'   `YMMba._      OOOOOOOOOOOOOOOOO       _,adMMP'   `YM.
   MP'        ~YMMMba._ YOOOOPVVVVVYOOOOP  _,adMMMMP~       `YM
   YMb           ~YMMMM\`OOOOI`````IOOOOO'/MMMMP~           dMP
    `Mb.           `YMMMb`OOOI,,,,,IOOOO'dMMMP'           ,dM'
      `'                  `OObNNNNNdOO'                   `'
                            `~OOOOO~'   TISSUE
"""



def old_options():

    """Docstring"""

    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(marvin_image)
    print("Hi, I'm Bob. And I know all things there is to know.")
    print("So what can I do for you mortal?")
    print("1) Give me two words and I will check if they are anagrams of eachother")
    print("2) Give me some numbers and I will filter out 10 and anything below ")
    print("q) Quit.")
