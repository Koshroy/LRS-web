function TileSheet(canvas, sheetImg, tile_w, tile_h, off_w, off_h, sheet_off, tile_spacing)
{
    this.canvas = canvas[0];
    this.sheet = sheetImg;
    this.tile_w = tile_w;
    this.tile_h = tile_h;
    this.off_w = off_w;
    this.off_h = off_h;
    this.sheet_off = sheet_off;
    this.tile_spacing = tile_spacing;

    this.real_tile_w = this.tile_w + this.off_w + this.tile_spacing;
    this.real_tile_h = this.tile_h + this.off_h + this.tile_spacing;

    this.horizTiles = (this.sheet.width() - this.sheet_off) / this.real_tile_w;
    this.vertTiles = (this.sheet.height() - this.sheet_off) / this.real_tile_h;

    console.log("real_tile_w: "+this.real_tile_w);
    console.log("real_tile_h: "+this.real_tile_h);


    console.log("horizTiles: "+this.horizTiles);
    console.log("vertTiles: "+this.vertTiles);

    
    this.writeTile = function(tileNum, tx, ty)
    {
	var tile_x = (tileNum % this.horizTiles);
	var tile_y = ((tileNum - tile_x) / this.horizTiles);

	console.log("tile_x: "+tile_x);
	console.log("tile_y: "+tile_y);

	console.log("tile_spacing: "+this.tile_spacing);
	console.log("off_w: "+this.off_w);

	
	this.canvas.getContext("2d").drawImage(this.sheet[0], (tile_x * this.real_tile_w) + this.off_w, (tile_y * this.real_tile_h)  + this.off_h , this.tile_w, this.tile_h, tx, ty, this.tile_w, this.tile_h);
    }
}

function Map(sizeX, sizeY, tile_w, tile_h, numPlayers)
{
    this.size_x = sizeX;
    this.size_y = sizeY;

    this.tile_w = tile_w;
    this.tile_h = tile_h;
    
    //this.arr = new Array(sizeX*sizeY);

    this.tileArr = [24, 24, 24, 24, 24,
	     24, 24, 24, 24, 24,
	     24, 24, 24, 24, 24,
	     24, 24, 24, 24, 24,
	     24, 24, 24, 24, 24];

    this.numPlayers = numPlayers;


    this.renderTiles = function(sheet)
    {
	switch(this.numPlayers)
	{
	default:
	case 1:
	case 2:
	    this.renderSector(sheet, 0, this.tileArr);
	    this.renderSector(sheet, 2, this.tileArr);
	    break;
	case 3:
	    this.renderSector(sheet, 1, this.tileArr);
	    this.renderSector(sheet, 2, this.tileArr);
	    this.renderSector(sheet, 3, this.tileArr);
	    break;
	case 4:
	    this.renderSector(sheet, 0, this.tileArr);
	    this.renderSector(sheet, 1, this.tileArr);
	    this.renderSector(sheet, 2, this.tileArr);
	    this.renderSector(sheet, 3, this.tileArr);
	    break;
	}
    }


    this.renderSector = function(sheet, sectorNum, arr)
    {
	x_off = 0;
	y_off = 0;
	switch(sectorNum)
	{
	case 0:
	    x_off = 0;
	    y_off = 0;
	    break;
	case 1:
	    x_off = 5;
	    y_off = 0;
	    break;
	case 2:
	    x_off = 0;
	    y_off = 5;
	    break;
	default:
	case 3:
	    x_off = 5;
	    y_off = 5;
	    break;
	}
	for(var i = 0; i < 5; i++)
	{
	    for(var j = 0; j < 5; j++)
	    {
		//console.log("arr: ", arr);
		sheet.writeTile(arr[i*5 + j], this.tile_w*(x_off+i), this.tile_h*(y_off+j));
	    }
	}

    }
}

