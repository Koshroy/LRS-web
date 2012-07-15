function TileSheet(canvas, sheetImg, tile_w, tile_h)
{
    this.canvas = canvas[0];
    this.sheet = sheetImg;
    this.tile_w = tile_w;
    this.tile_h = tile_h;

    this.horizTiles = this.sheet.width() / this.tile_w;
    this.vertTiles = this.sheet.height() / this.tile_h;

    
    this.writeTile = function(tileNum, tx, ty)
    {
	var tile_x = tileNum % this.horizTiles;
	var tile_y = tileNum / this.horizTiles;
	this.canvas.getContext("2d").drawImage(this.sheet[0], tile_x, tile_y, this.tile_w, this.tile_h, tx, ty, this.tile_w, this.tile_h);
    }
}

function Map(sizeX, sizeY, tile_w, tile_h)
{
    this.size_x = sizeX;
    this.size_y = sizeY;

    this.tile_w = tile_w;
    this.tile_h = tile_h;
    
    this.arr = new Array(sizeX*sizeY);

    this.drawTileOnMap = function(sheet, mx, my)
    {
	// Off bounds of map
	if ( (mx >= this.size_x) || (my >= this.size_y) )
	{
	    console.log("Bad dimensions!");
	    return;
	}

	var tnum = this.arr[my*this.size_x + mx];

	sheet.writeTile(tnum, mx*tile_w, my*tile_h);
    }
}
