import os
import platform
def clear_screen():
    command = "cls" if platform.system().lower()=="windows" else "clear"
    os.system(command)


def showWelcome():
    clear_screen()
    print("\033[96m {}\033[00m" .format(""" 
 WWWWWWWW                           WWWWWWWW                    lllllll                                                                                  
W::::::W                           W::::::W                    l:::::l                                                                                  
W::::::W                           W::::::W                    l:::::l                                                                                  
W::::::W                           W::::::W                    l:::::l                                                                                  
 W:::::W           WWWWW           W:::::W     eeeeeeeeeeee     l::::l     cccccccccccccccc   ooooooooooo      mmmmmmm    mmmmmmm       eeeeeeeeeeee    
  W:::::W         W:::::W         W:::::W    ee::::::::::::ee   l::::l   cc:::::::::::::::c oo:::::::::::oo  mm:::::::m  m:::::::mm   ee::::::::::::ee  
   W:::::W       W:::::::W       W:::::W    e::::::eeeee:::::ee l::::l  c:::::::::::::::::co:::::::::::::::om::::::::::mm::::::::::m e::::::eeeee:::::ee
    W:::::W     W:::::::::W     W:::::W    e::::::e     e:::::e l::::l c:::::::cccccc:::::co:::::ooooo:::::om::::::::::::::::::::::me::::::e     e:::::e
     W:::::W   W:::::W:::::W   W:::::W     e:::::::eeeee::::::e l::::l c::::::c     ccccccco::::o     o::::om:::::mmm::::::mmm:::::me:::::::eeeee::::::e
      W:::::W W:::::W W:::::W W:::::W      e:::::::::::::::::e  l::::l c:::::c             o::::o     o::::om::::m   m::::m   m::::me:::::::::::::::::e 
       W:::::W:::::W   W:::::W:::::W       e::::::eeeeeeeeeee   l::::l c:::::c             o::::o     o::::om::::m   m::::m   m::::me::::::eeeeeeeeeee  
        W:::::::::W     W:::::::::W        e:::::::e            l::::l c::::::c     ccccccco::::o     o::::om::::m   m::::m   m::::me:::::::e           
         W:::::::W       W:::::::W         e::::::::e          l::::::lc:::::::cccccc:::::co:::::ooooo:::::om::::m   m::::m   m::::me::::::::e          
          W:::::W         W:::::W           e::::::::eeeeeeee  l::::::l c:::::::::::::::::co:::::::::::::::om::::m   m::::m   m::::m e::::::::eeeeeeee  
           W:::W           W:::W             ee:::::::::::::e  l::::::l  cc:::::::::::::::c oo:::::::::::oo m::::m   m::::m   m::::m  ee:::::::::::::e  
            WWW             WWW                eeeeeeeeeeeeee  llllllll    cccccccccccccccc   ooooooooooo   mmmmmm   mmmmmm   mmmmmm    eeeeeeeeeeeeee  
                                                                                                                                                       
    """))

def showQuit():
    clear_screen()
    print("\033[96m {}\033[00m" .format("""
                                                                                                                                                      
                                                                   dddddddd                                                                           
        GGGGGGGGGGGGG                                              d::::::d     BBBBBBBBBBBBBBBBB                                                 !!! 
     GGG::::::::::::G                                              d::::::d     B::::::::::::::::B                                               !!:!!
   GG:::::::::::::::G                                              d::::::d     B::::::BBBBBB:::::B                                              !:::!
  G:::::GGGGGGGG::::G                                              d:::::d      BB:::::B     B:::::B                                             !:::!
 G:::::G       GGGGGG   ooooooooooo      ooooooooooo       ddddddddd:::::d        B::::B     B:::::Byyyyyyy           yyyyyyy    eeeeeeeeeeee    !:::!
G:::::G               oo:::::::::::oo  oo:::::::::::oo   dd::::::::::::::d        B::::B     B:::::B y:::::y         y:::::y   ee::::::::::::ee  !:::!
G:::::G              o:::::::::::::::oo:::::::::::::::o d::::::::::::::::d        B::::BBBBBB:::::B   y:::::y       y:::::y   e::::::eeeee:::::ee!:::!
G:::::G    GGGGGGGGGGo:::::ooooo:::::oo:::::ooooo:::::od:::::::ddddd:::::d        B:::::::::::::BB     y:::::y     y:::::y   e::::::e     e:::::e!:::!
G:::::G    G::::::::Go::::o     o::::oo::::o     o::::od::::::d    d:::::d        B::::BBBBBB:::::B     y:::::y   y:::::y    e:::::::eeeee::::::e!:::!
G:::::G    GGGGG::::Go::::o     o::::oo::::o     o::::od:::::d     d:::::d        B::::B     B:::::B     y:::::y y:::::y     e:::::::::::::::::e !:::!
G:::::G        G::::Go::::o     o::::oo::::o     o::::od:::::d     d:::::d        B::::B     B:::::B      y:::::y:::::y      e::::::eeeeeeeeeee  !!:!!
 G:::::G       G::::Go::::o     o::::oo::::o     o::::od:::::d     d:::::d        B::::B     B:::::B       y:::::::::y       e:::::::e            !!! 
  G:::::GGGGGGGG::::Go:::::ooooo:::::oo:::::ooooo:::::od::::::ddddd::::::dd     BB:::::BBBBBB::::::B        y:::::::y        e::::::::e               
   GG:::::::::::::::Go:::::::::::::::oo:::::::::::::::o d:::::::::::::::::d     B:::::::::::::::::B          y:::::y          e::::::::eeeeeeee   !!! 
     GGG::::::GGG:::G oo:::::::::::oo  oo:::::::::::oo   d:::::::::ddd::::d     B::::::::::::::::B          y:::::y            ee:::::::::::::e  !!:!!
        GGGGGG   GGGG   ooooooooooo      ooooooooooo      ddddddddd   ddddd     BBBBBBBBBBBBBBBBB          y:::::y               eeeeeeeeeeeeee   !!! 
                                                                                                          y:::::y                                     
                                                                                                         y:::::y                                      
                                                                                                        y:::::y                                       
                                                                                                       y:::::y                                        
                                                                                                      yyyyyyy                                         
                                                                                                                                                      
                                                                                                                                                      
    """))

def showLogo():
    print("\033[96m {}\033[00m" .format("""
                                                                                                                                                             
                                                                                                                                                             
HHHHHHHHH     HHHHHHHHH                                      lllllll          tttt          hhhhhhh                                                          
H:::::::H     H:::::::H                                      l:::::l       ttt:::t          h:::::h                                                          
H:::::::H     H:::::::H                                      l:::::l       t:::::t          h:::::h                                                          
HH::::::H     H::::::HH                                      l:::::l       t:::::t          h:::::h                                                          
  H:::::H     H:::::H      eeeeeeeeeeee      aaaaaaaaaaaaa    l::::l ttttttt:::::ttttttt     h::::h hhhhh       ppppp   ppppppppp   yyyyyyy           yyyyyyy
  H:::::H     H:::::H    ee::::::::::::ee    a::::::::::::a   l::::l t:::::::::::::::::t     h::::hh:::::hhh    p::::ppp:::::::::p   y:::::y         y:::::y 
  H::::::HHHHH::::::H   e::::::eeeee:::::ee  aaaaaaaaa:::::a  l::::l t:::::::::::::::::t     h::::::::::::::hh  p:::::::::::::::::p   y:::::y       y:::::y  
  H:::::::::::::::::H  e::::::e     e:::::e           a::::a  l::::l tttttt:::::::tttttt     h:::::::hhh::::::h pp::::::ppppp::::::p   y:::::y     y:::::y   
  H:::::::::::::::::H  e:::::::eeeee::::::e    aaaaaaa:::::a  l::::l       t:::::t           h::::::h   h::::::h p:::::p     p:::::p    y:::::y   y:::::y    
  H::::::HHHHH::::::H  e:::::::::::::::::e   aa::::::::::::a  l::::l       t:::::t           h:::::h     h:::::h p:::::p     p:::::p     y:::::y y:::::y     
  H:::::H     H:::::H  e::::::eeeeeeeeeee   a::::aaaa::::::a  l::::l       t:::::t           h:::::h     h:::::h p:::::p     p:::::p      y:::::y:::::y      
  H:::::H     H:::::H  e:::::::e           a::::a    a:::::a  l::::l       t:::::t    tttttt h:::::h     h:::::h p:::::p    p::::::p       y:::::::::y       
HH::::::H     H::::::HHe::::::::e          a::::a    a:::::a l::::::l      t::::::tttt:::::t h:::::h     h:::::h p:::::ppppp:::::::p        y:::::::y        
H:::::::H     H:::::::H e::::::::eeeeeeee  a:::::aaaa::::::a l::::::l      tt::::::::::::::t h:::::h     h:::::h p::::::::::::::::p          y:::::y         
H:::::::H     H:::::::H  ee:::::::::::::e   a::::::::::aa:::al::::::l        tt:::::::::::tt h:::::h     h:::::h p::::::::::::::pp          y:::::y          
HHHHHHHHH     HHHHHHHHH    eeeeeeeeeeeeee    aaaaaaaaaa  aaaallllllll          ttttttttttt   hhhhhhh     hhhhhhh p::::::pppppppp           y:::::y           
                                                                                                                 p:::::p                  y:::::y            
                                                                                                                 p:::::p                 y:::::y             
                                                                                                                p:::::::p               y:::::y              
                                                                                                                p:::::::p              y:::::y               
                                                                                                                p:::::::p             yyyyyyy                
                                                                                                                ppppppppp                                    
                                                                                                                                                             

    """))
