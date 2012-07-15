function initFunc()
{
    var a = [24, 24, 24, 24, 24,
	     24, 24, 24, 24, 24,
	     24, 24, 24, 24, 24,
	     24, 24, 24, 24, 24,
	     24, 24, 24, 24, 24];
    var t = new TileSheet($("#gameCanvas"), $("#tileSheet"), 64, 64, 2, 2, 1, 1);
    //var m = new Map(20, 20, 40, 40);
    //t.writeTile(24, 0, 0);
    m = new Map(0, 0, 64, 64, 3);
    //m.renderSector(t, 3, a);
    m.renderTiles(t);

    //m.drawTileOnMap(t, 0, 0);
}


$(document).ready(initFunc);