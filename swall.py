import random

class WallIcon:
   Empty       = -1;
   Nothot      = 0;
   Normal      = 1;
   Hologram    = 1;
   Exploded    = 2;
   Superhot    = 3;
   Field       = 4;
   Brokenfield = 5;

def get_random_wall(num_players, num_rand):
    for i in xrange(num_players):
        arr = [WallIcon.Empty]*30
        for j in range(0,num_rand,1):
            arr[random.randint(0, 29)] = WallIcon.Normal
        arr[random.randint(0, 29)] = WallIcon.Field
    return arr

if __name__ == "__main__":
    print get_random_wall(1, 12)
