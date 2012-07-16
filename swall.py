import random

class Walltype:
   Empty       = 0;
   Normal      = 1;
   Exploded    = 2;
   Hologram    = 3;
   Superhot    = 4;
   Nothot      = 5;
   Field       = 6;
   Brokenfield = 7;

def get_random_wall(num_players, num_rand):
    out_arr = []
    for i in xrange(num_players):
        arr = [Walltype.Empty]*25
        for j in xrange(num_rand):
            arr[random.randint(0, 23)] = Walltype.Normal
        out_arr.append(arr)
    return out_arr

if __name__ == "__main__":
    print get_random_wall(2, 12)
