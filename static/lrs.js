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
	   function (data)
	   {
	       if (cnt++ < 20)
		   m.renderSector(t, 1, data.wallArr[0]);
	       
	   }, 'json');
}

function respFunc()
{
    console.log("uhuu");
}



$(document).ready(initFunc);