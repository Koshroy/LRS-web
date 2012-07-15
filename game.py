class Walltype:
    Empty       = 0;
    Normal      = 1;
    Exploded    = 2;
    Hologram    = 3;
    Superhot    = 4;
    Nothot      = 5;
    Field       = 6;
    Brokenfield = 7;

class misc:
    NoPSource   = -1;
    TOP    = NonEuclidean.TOP;
    LEFT   = NonEuclidean.LEFT;
    RIGHT  = NonEuclidean.RIGHT;
    BOTTOM = NonEuclidean.BOTTOM;

class RobotIcon:
    Normal      = 0;
    Dead        = 1;
    Tiny        = 2;
    Carbon      = 3;
    Big         = 4;
    Stunned     = 5;

class NonEuclidean:
    TOP    = 0;
    LEFT   = 1;
    RIGHT  = 2;
    BOTTOM = 3;
    #{a,b} a = target sector number
    #      b = target side
    #TOP LEFT RIGHT BOTTOM
    Mapping = { {{{1,BOTTOM},{1,RIGHT},{1,LEFT},{1,TOP}},
                 {{0,BOTTOM},{0,RIGHT},{0,LEFT},{0,TOP}}}  #2
                
                {{{2,BOTTOM},{1,TOP},{1,BOTTOM},{2,TOP}},
                 {{0,LEFT},{2,RIGHT},{2,LEFT},{0,RIGHT}},
                 {{0,BOTTOM},{1,RIGHT},{1,LEFT},{0,TOP}}}  #3
                
                {{{1,RIGHT},{3,RIGHT},{1,LEFT},{2,TOP}},
                 {{2,BOTTOM},{0,RIGHT},{0,TOP},{3,TOP}},
                 {{0,BOTTOM},{3,BOTTOM},{3,LEFT},{1,TOP}},
                 {{1,BOTTOM},{2,RIGHT},{0,LEFT},{2,LEFT}}}  #4
                };

class Mazecell:
    def __init__(self,i):
        self.visited=false;
        

class Board(pcount):
    sectors = []
    players = []
    def __init__(self,pcount):
        for i in range(0,pcount-1,1)
            self.sectors.append(Sector());
            self.players.append(Player(i,this));

            
    #functions that are controlled directly by player
    #These return false if the action is not allowed
    #and true if it is. If it is allowed, then performs
    #action

    #I would LIKE to put this in the player class, but theres an issue of
    #being able to access the sector classes

    def TryGoUp(pnum):
        here = players[pnum].sector;
        crosswall = sectors[here].Walls.horz[players[pnum].x,players[pnum].y];
        if(crosswall.IsPassable == true && 
           players[pnum].movesleft>0):
            #if(crosswall.kind == Walltype.Superhot)
                #attack player
            if(crosswall.kind == Walltype.Empty):
                GoUp(pnum);
                return true;
        return false;
    def TryGoDown(pnum):
        here = players[pnum].sector;
        crosswall = sectors[here].Walls.horz[players[pnum].x,players[pnum].y+1];
        if(crosswall.IsPassable == true && 
           players[pnum].movesleft>0):
            if(crosswall.kind == Walltype.Empty):
                GoDown(pnum);
                return true;
        return false;
    def TryGoLeft(pnum):
        here = players[pnum].sector;
        crosswall = sectors[here].Walls.vert[players[pnum].x,players[pnum].y];
        if(crosswall.IsPassable == true && 
           players[pnum].movesleft>0):
            if(crosswall.kind == Walltype.Empty):
                GoLeft(pnum);
                return true;
        return false;
    def TryGoRight(pnum):
        here = players[pnum].sector;
        crosswall = sectors[here].Walls.vert[players[pnum].x+1,players[pnum].y];
        if(crosswall.IsPassable == true && 
           players[pnum].movesleft>0):
            if(crosswall.kind == Walltype.Empty):
                GoRight(pnum);
                return true;
        return false;

    def GoUp(pnum):
        players[pnum].movesleft--;
        if(players[pnum].y>0):
            players[pnum].y-=1;
        else:
            NonEucJump(pnum,misc.UP);
    def GoDown(pnum):
        players[pnum].movesleft--;
        if(players[pnum].y<4):
            players[pnum].y+=1;
        else:
            NonEucJump(pnum,misc.DOWN);
    def GoLeft(pnum):
        players[pnum].movesleft--;
        if(players[pnum].x>0):
            players[pnum].x-=1;
        else:
            NonEucJump(pnum,misc.LEFT);
    def GoRight(pnum):
        players[pnum].movesleft--;
        if(players[pnum].x<4):
            players[pnum].x+=1;
        else:
            NonEucJump(pnum,misc.RIGHT);
    def NonEucJump(pnum,side):
        here = players[pnum].sector;
        players[pnum].sector = NonEuclidean.Mapping[pcount-2][here][side][0];
        targetSide           = NonEuclidean.Mapping[pcount-2][here][side][1];
        if(targetSide == misc.TOP):
            players[pnum].y = 0;
        if(targetSide == misc.LEFT):
            players[pnum].x = 0;
        if(targetSide == misc.RIGHT):
            players[pnum].x = 4;
        if(targetSide == misc.BOTTOM):
            players[pnum].y = 4;

class Sector:
    def __init__(self):
        self.Walls = Wallmap();
        self.Floor = Floorplan();
        BuildMaze();
    def BuildMaze():
        #the maze must meet the following criterion:
        # each sector's center has a path to each exit
        # each sector is in itself, acyclic


        #Destroy walls until cells form connected acyclic graph
        w = [[i] in range(0,24)];
        random.shuffle(w);
        temp = Mazecell[25];
        for i in range(0,24):
            j=w[i];
            x=j%5;
            y=(j-x)/5;
            if(temp[j].visited==true):
                continue;
            temp[j].visited=true;
            
            v = random.randrange(0,3,1);
            if(v==misc.TOP && y>0):
                if(temp[j-5].visited==false):
                    temp[j-5].visited=true;
                    self.Walls.horz[x,y-1]=Walltype.Empty;
            if(v==misc.LEFT && x>0):
                if(temp[j-1].visited==false):
                    temp[j-5].visited=true;
                    self.Walls.horz[x-1,y]=Walltype.Empty;
            if(v==misc.RIGHT && x<4):
                if(temp[j+1].visited==false):
                    temp[j-5].visited=true;
                    self.Walls.horz[x+1,y]=Walltype.Empty;
            if(v==misc.BOTTOM && y<4):
                if(temp[j+5].visited==false):
                    temp[j-5].visited=true;
                    self.Walls.horz[x,y+1]=Walltype.Empty;
        #connect to other sectors
        self.Walls.horz[2,0]=Walltype.Empty;
        self.Walls.horz[0,2]=Walltype.Empty;
        self.Walls.horz[4,2]=Walltype.Empty;
        self.Walls.horz[2,4]=Walltype.Empty;
        #add force fields
        FieldCount = 0;
        while(FieldCount < 2):
            x = random.randrange(1,4,1);
            y = random.randrange(1,4,1);
            isHorz = random.choice([true,false]);
            if(isHorz):
                if(self.Walls.horz[x,y]==Walltype.Normal):
                    self.Walls.horz[x,y]==Walltype.Field;
                    FieldCount+=1;
            else:
                if(self.Walls.vert[x,y]==Walltype.Normal):
                    self.Walls.vert[x,y]==Walltype.Field;
                    FieldCount+=1;
                
        

    def RotL():
        self.Floor.RotL();
        self.Walls.RotL();
        
    def RotR():
        self.Floor.RotR();
        self.Walls.RotR();
        
class Wallmap:
    def __init__(self):
        self.horz = Wall[5,6];
        self.vert = Wall[6,5];
    #how we decide to define the counting order for horz and vert will affect
    #the correctness of the rotation
    def RotL():
        for x = range(0,4,1):
            for y = range(0,5,1):
                self.swap(x,y,y,x);
    def RotR():
        for x = range(0,4,1):
            for y = range(0,5,1):
                self.swap(x,y,6-y,5-x);
    def swap(x1,y1,x2,y2):
        temp = self.horz[x1,y1];
        self.horz[x1,y1] = self.vert[x2,y2];
        self.vert[x2,y2] = temp;        

class Floorplan:
    def __init__(self):
        self.map = Tile[5,5];
    def RotL():
        for x = range(0,4,1):
            for y = range(0,4,1):
                self.swap(x,y,y,x);
    def RotR():
        for x = range(0,4,1):
            for y = range(0,4,1):
                self.swap(x,y,5-y,5-x);
    def swap(x1,y1,x2,y2):
        temp = self.map[x1,y1];
        self.map[x1,y1] = self.map[x2,y2];
        self.map[x2,y2] = temp;
        

class Tile:
    def __init__(self):
        self.hasPlayer  = false;
        self.hasPSource[4] = {false, false, false, false};
        self.BaseCol    = -1;
        self.isMelted   = false;
    

class Wall:
    def __init__(self):
        self.isPassable=true;
        self.kind=Walltype.Normal;
        self.cooldown = -1;
    def Explode():
        if(self.kind==Walltype.Normal):
            self.kind = Walltype.Exploded;
            self.isPassable = true;
    def Superheat(turns):
        if(self.kind != Walltype.Field &&
           self.kind != Walltype.Brokenfield):
            self.kind = Walltype.Superhot;
            self.isPassable = true;
            self.cooldown = turns;
    def Exist():
        if(self.kind == Walltype.Superhot):
            self.cooldown-=1;
            if(self.cooldown < 0):
                self.kind = Walltype.Nothot;

class Player:
    def __init__(self,pnum,board):
        self.maxmoves    = 3;
        self.movesleft   = 0;
        self.hp          = 15;
        self.maxattacks  = 1;
        self.attacksleft = 1;
        self.mayboost    = true;
        self.x           = 2;
        self.y           = 2;
        self.sector      = pnum;
        self.holding     = misc.NoPSource;
        self.iconstate   = RobotIcon.Normal;
        self.hand        = Hand();

class Hand:
    def __init__(self):
        self.Cards = [];
        for i in range(1,7):
            self.Draw();
    def Draw():
        #should fail here because both DECK and playerhandlimit undefined
        if(!DECK.IsEmpty() && self.Cards.size() < playerhandlimit):
            newcard = DECK.pop();
            self.Cards.append(newcard);
    def Discard(i):
        self.Cards.pop(i);

class Deck:
    self.Cards = Card[128];
    def __init__(self):
        #assign the correct ratios
        random.shuffle(self.Cards);

class Card:
    __init__(self):
        self.ID = 0;
        self.Active = 0;
    #if this were C, Id use jump tables.
    #Theres GOT to be a better way to do it in python than this
    def Play():
        if(self.ID == 0):#9-Volt Battery
            a = 0;
        else if(self.ID == 1):#Alternate Universe
            a = 0;
        else if(self.ID == 2):#Annihilate Wall
            a = 0;
        else if(self.ID == 3):#Anti-Anti-Matter
            a = 0;
        else if(self.ID == 4):#Big Bang
            a = 0;
        else if(self.ID == 5):#Boost 2
            a = 0;
        else if(self.ID == 6):#Boost 3
            a = 0;
        else if(self.ID == 7):#Boost 4
            a = 0;
        else if(self.ID == 8):#Boost 5
            a = 0;
        else if(self.ID == 9):#Boost 6
            a = 0;
        else if(self.ID == 10):#BSOD
            a = 0;
        else if(self.ID == 11):#Bypass Force Field
            a = 0;
        else if(self.ID == 12):#Destroy Panel
            a = 0;
        else if(self.ID == 13):#Displace Atoms
            a = 0;
        else if(self.ID == 14):#Drain Battery
            a = 0;
        else if(self.ID == 15):#Electrostatic Charge
            a = 0;
        else if(self.ID == 16):#Evaporate Water
            a = 0;
        else if(self.ID == 17):#Evil Twin
            a = 0;
        else if(self.ID == 18):#Friendly Neurons
            a = 0;
        else if(self.ID == 19):#GPS Error
            a = 0;
        else if(self.ID == 20):#Gravity Well
            a = 0;
        else if(self.ID == 21):#Holographic Wall
            a = 0;
        else if(self.ID == 22):#Holtzman Shield
            a = 0;
        else if(self.ID == 23):#Hull Plating
            a = 0;
        else if(self.ID == 24):#Hydrated Air
            a = 0;
        else if(self.ID == 25):#Intercept Packets
            a = 0;
        else if(self.ID == 26):#Internet Worm
            a = 0;
        else if(self.ID == 27):#Long Jump
            a = 0;
        else if(self.ID == 28):#Magnetic Restraints
            a = 0;
        else if(self.ID == 29):#Materialize Wall
            a = 0;
        else if(self.ID == 30):#Melt Hallway
            a = 0;
        else if(self.ID == 31):#Nanite Infusion
            a = 0;
        else if(self.ID == 32):#Panic
            a = 0;
        else if(self.ID == 33):#Port Scan
            a = 0;
        else if(self.ID == 34):#Power Surge
            a = 0;
        else if(self.ID == 35):#Projection Beam
            a = 0;
        else if(self.ID == 36):#Quantum Mirror
            a = 0;
        else if(self.ID == 37):#R2 Unit
            a = 0;
        else if(self.ID == 38):#RAM Upgrade
            a = 0;
        else if(self.ID == 39):#Reboot
            a = 0;
        else if(self.ID == 40):#Reconfigure Hull
            a = 0;
        else if(self.ID == 41):#Reconfigure Tile
            a = 0;
        else if(self.ID == 42):#Recycle
            a = 0;
        else if(self.ID == 43):#Repair Kit
            a = 0;
        else if(self.ID == 44):#Reprogram Module
            a = 0;
        else if(self.ID == 45):#Robocracy
            a = 0;
        else if(self.ID == 46):#Scan CPU
            a = 0;
        else if(self.ID == 47):#Security Camera
            a = 0;
        else if(self.ID == 48):#Short Jump
            a = 0;
        else if(self.ID == 49):#Siphon Power
            a = 0;
        else if(self.ID == 50):#Soldering Iron
            a = 0;
        else if(self.ID == 51):#Solitaire
            a = 0;
        else if(self.ID == 52):#Spyware
            a = 0;
        else if(self.ID == 53):#Superheated Air
            a = 0;
        else if(self.ID == 54):#Superheated Wall
            a = 0;
        else if(self.ID == 55):#Suppression Gas
            a = 0;
        else if(self.ID == 56):#Suspensor Shield
            a = 0;
        else if(self.ID == 57):#Time Crystals
            a = 0;
        else if(self.ID == 58):#Tractor Beam
            a = 0;
        else if(self.ID == 59):#Turbo Charge
            a = 0;
        else if(self.ID == 60):#Unlock Force Field
            a = 0;
        else if(self.ID == 61):#Virus
            a = 0;
        else if(self.ID == 62):#Wipe Memory
            a = 0;
        else if(self.ID == 63):#Wormhole
            a = 0;
        return false;
