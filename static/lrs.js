function initFunc()
{
    var a = [0, 0, 0, 0,
	     0, 0, 0, 0,
	     0, 0, 0, 0,
	     0, 0, 0, 0];
    var t = new TileSheet($("#gameCanvas"), $("#tileSheet"), 40, 40);
    var m = new Map(20, 20, 40, 40);

    m.drawTileOnMap(t, 0, 0);
}


$(document).ready(initFunc);