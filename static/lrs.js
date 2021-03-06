var m;
var t;

var cnt = 0;

function initFunc()
{
    t = new TileSheet($("#gameCanvas"), $("#tileSheet"), 64, 64, 2, 2, 1, 1);
    //var m = new Map(20, 20, 40, 40);
    //t.writeTile(24, 0, 0);
    m = new Map(0, 0, 64, 64, 3);
    //m.renderSector(t, 3, a);
    m.renderTiles(t);

    setInterval(pollFunc, 1000);

    $(document).keydown( function(e)
			       {
				   if (e.keyCode == 37)
				   {
				       $.post("/clientevent",
					      {
						  event : 'key',
						  dir : 'left'
					      }, respFunc, 'json');
				       return false;
				   }
				   else if (e.keyCode == 38)
				   {
				       $.post("/clientevent",
					      {
						  event : 'key',
						  dir : 'up'
					      }, respFunc, 'json');
				       return false;
				   }
				   else if (e.keyCode == 39)
				   {
				       $.post("/clientevent",
					      {
						  event : 'key',
						  dir : 'right'
					      }, respFunc, 'json');
				       return false;
				   }
				   else if (e.keyCode == 40)
				   {
				       $.post("/clientevent",
					      {
						  event : 'key',
						  dir : 'down'
					      }, respFunc, 'json');
				       return false;
				   }
				   else { return true; }
			       });

    //m.drawTileOnMap(t, 0, 0);
}

function pollFunc()
{
    $.post("/pollstate", {},
	   getstate, 'json');
}

function respFunc(data)
{
    console.log("uhuu");
    getstate(data);
}

function getstate(data)
{
   var pcount = data.pcount;
   var i;
   var offset;
   Position = [[0.5,2.5],[1,2,3],[0,1,2,3]];
   switch(pcount)
   {
   default:
   case 2:
      offset = 0;
      break;
   case 3:
      offset = 2;
      break;
   case 4:
      offset = 5;
      break;
   }
   for (i=0;i<pcount;i++)
   {
     // SectorState = [.hwalls,data.sector[i].vwalls,data.sector[i].notwalls];
      //   if (cnt++ < 20)
      m.renderSector(t, Position[pcount-2][i], offset+i, data.sector[i]);
   }
}


$(document).ready(initFunc);