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
    '{a,b} a = target sector number
    '      b = target side
    'TOP LEFT RIGHT BOTTOM
    Mapping = { {{{1,BOTTOM},{1,RIGHT},{1,LEFT},{1,TOP}},
                 {{0,BOTTOM},{0,RIGHT},{0,LEFT},{0,TOP}}}  '2
                
                {{{2,BOTTOM},{1,TOP},{1,BOTTOM},{2,TOP}},
                 {{0,LEFT},{2,RIGHT},{2,LEFT},{0,RIGHT}},
                 {{0,BOTTOM},{1,RIGHT},{1,LEFT},{0,TOP}}}  '3
                
                {{{1,RIGHT},{3,RIGHT},{1,LEFT},{2,TOP}},
                 {{2,BOTTOM},{0,RIGHT},{0,TOP},{3,TOP}},
                 {{0,BOTTOM},{3,BOTTOM},{3,LEFT},{1,TOP}},
                 {{1,BOTTOM},{2,RIGHT},{0,LEFT},{2,LEFT}}}  '4
                };

class Board(pcount):
    sectors = []
    players = []
    def __init__(self,pcount):
        for i in range(0,pcount-1,1)
            self.sectors.append(Sector());
            self.players.append(Player(i));


    'functions that are controlled directly by player
    'These return false if the action is not allowed
    'and true if it is. If it is allowed, then performs
    'action

    'I would LIKE to put this in the player class, but theres an issue of
    'being able to access the sector classes

    def TryGoUp(pnum):
        here = players[pnum].sector;
        crosswall = sectors[here].Walls.horz[players[pnum].x,players[pnum].y];
        if(crosswall.IsPassable == true):
            'if(crosswall.kind == Walltype.Superhot)
                'attack player
            if(crosswall.kind == Walltype.Empty):
                GoUp(pnum);
                return true;
        return false;
    def TryGoDown(pnum):
        here = players[pnum].sector;
        crosswall = sectors[here].Walls.horz[players[pnum].x,players[pnum].y+1];
        if(crosswall.IsPassable == true):
            if(crosswall.kind == Walltype.Empty):
                GoDown(pnum);
                return true;
        return false;
    def TryGoLeft(pnum):
        here = players[pnum].sector;
        crosswall = sectors[here].Walls.vert[players[pnum].x,players[pnum].y];
        if(crosswall.IsPassable == true):
            if(crosswall.kind == Walltype.Empty):
                GoLeft(pnum);
                return true;
        return false;
    def TryGoRight(pnum):
        here = players[pnum].sector;
        crosswall = sectors[here].Walls.vert[players[pnum].x+1,players[pnum].y];
        if(crosswall.IsPassable == true):
            if(crosswall.kind == Walltype.Empty):
                GoRight(pnum);
                return true;
        return false;

    def GoUp(pnum):
        if(players[pnum].y>0):
            players[pnum].y-=1;
        else:
            NonEucJump(pnum,misc.UP);
    def GoDown(pnum):
        if(players[pnum].y<4):
            players[pnum].y+=1;
        else:
            NonEucJump(pnum,misc.DOWN);
    def GoLeft(pnum):
        if(players[pnum].x>0):
            players[pnum].x-=1;
        else:
            NonEucJump(pnum,misc.LEFT);
    def GoRight(pnum):
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
    'how we decide to define the counting order for horz and vert will affect
    'the correctness of the rotation
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
        self.kind=Walltype.Empty;
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
    def __init__(self,pnum):
        self.maxmoves    = 3;
        self.movesleft   = 0;
        self.hp          = 15;
        self.maxattacks  = 1;
        self.attacksleft = 1;
        self.x           = 2;
        self.y           = 2;
        self.sector      = pnum;
        self.holding     = misc.NoPSource;
        self.iconstate   = RobotIcon.Normal;
    
