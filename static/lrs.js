function initFunc()
{
    var a = [0, 0, 0, 0,
	     0, 0, 0, 0,
	     0, 0, 0, 0,
	     0, 0, 0, 0];
    var t = new TileSheet($("#gameCanvas"), $("#tileSheet"), 64, 64);
    //var m = new Map(20, 20, 40, 40);
    t.writeTile(0, 0, 0);

    //m.drawTileOnMap(t, 0, 0);
}


$(document).ready(initFunc);