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

    // console.log("real_tile_w: "+this.real_tile_w);
    // console.log("real_tile_h: "+this.real_tile_h);


    // console.log("horizTiles: "+this.horizTiles);
    // console.log("vertTiles: "+this.vertTiles);

    
    this.writeTile = function(tileNum, tx, ty,direction)
    {
      var tile_x = (tileNum % this.horizTiles);
      var tile_y = ((tileNum - tile_x) / this.horizTiles);
      if(direction==0)
         this.canvas.getContext("2d").drawImage(this.sheet[0], (tile_x * this.real_tile_w) + this.off_w, (tile_y * this.real_tile_h)  + this.off_h , this.tile_w, this.tile_h, tx, ty, this.tile_w, this.tile_h);
      else
      {
         //holy fuck is this rotation expensive
         //it saves the ENTIRE canvas, translates it, rotates it, and translates it again
         //...for EVERY TILE
         //There are more efficient ways to do this, but this is the simplest implementation for now
         this.canvas.getContext("2d").save();
         this.canvas.getContext("2d").translate(tx+this.tile_w/2,ty+this.tile_h/2);
         this.canvas.getContext("2d").rotate(90*direction*(Math.PI/180));
         this.canvas.getContext("2d").translate(0-(tx+this.tile_w/2),0-(ty+this.tile_h/2));
         this.canvas.getContext("2d").drawImage(this.sheet[0], (tile_x * this.real_tile_w) + this.off_w, (tile_y * this.real_tile_h)  + this.off_h , this.tile_w, this.tile_h, tx, ty, this.tile_w, this.tile_h);

         this.canvas.getContext("2d").restore();
      }
    }
    
    //I thought an x,y interface would be easier
    this.writeTileXY = function(tile_x,tile_y, tx, ty,direction)
    {
      this.writeTile(tile_y*this.horizTiles+tile_x,tx,ty,direction);
    }
}


function Map(sizeX, sizeY, tile_w, tile_h, numPlayers)
{
    this.size_x = sizeX;
    this.size_y = sizeY;

    this.tile_w = tile_w;
    this.tile_h = tile_h;
    
    //this.arr = new Array(sizeX*sizeY);

    this.vwalls  =  [-1,-1,-1,-1,-1,-1,
                     -1,-1,-1,-1,-1,-1,
                     -1,-1,-1,-1,-1,-1,
                     -1,-1,-1,-1,-1,-1,
                     -1,-1,-1,-1,-1,-1];
    
    this.hwalls  =  [-1,-1,-1,-1,-1,
                     -1,-1,-1,-1,-1,
                     -1,-1,-1,-1,-1,
                     -1,-1,-1,-1,-1,
                     -1,-1,-1,-1,-1,
                     -1,-1,-1,-1,-1];
   /*this.notwalls = [24, 24, 24, 24, 24,
                     24, 24, 24, 24, 24,
                     24, 24, 24, 24, 24,
                     24, 24, 24, 24, 24,
                     24, 24, 24, 24, 24]; */
    this.notwalls = [[], [], [], [], [],
                     [], [], [], [0], [],
                     [], [], [1,30], [], [],
                     [], [0], [], [], [],
                     [], [], [], [], []];
   this.tileArr = [this.hwalls,this.vwalls,this.notwalls];
                     
   this.numPlayers = numPlayers;


    this.renderTiles = function(sheet)
    {
	switch(this.numPlayers)
	{
	default:
	case 2:
       //Reminder:      SectorNum, ArrowCfg
	    this.renderSector(sheet, 0.5, 0, this.tileArr);
	    this.renderSector(sheet, 2.5, 1, this.tileArr);
	    break;
	case 3:
	    this.renderSector(sheet, 1, 2, this.tileArr);
	    this.renderSector(sheet, 2, 3, this.tileArr);
	    this.renderSector(sheet, 3, 4, this.tileArr);
	    break;
	case 4:
	    this.renderSector(sheet, 0, 5, this.tileArr);
	    this.renderSector(sheet, 1, 6, this.tileArr);
	    this.renderSector(sheet, 2, 7, this.tileArr);
	    this.renderSector(sheet, 3, 8, this.tileArr);
	    break;
	}
    }


    this.renderSector = function(sheet, sectorNum, ArrowCfg, SectorState)
    {
      var hwalls   = SectorState[0];
      var vwalls   = SectorState[1];
      var notwalls = SectorState[2];
      x_off = 0;
      y_off = 0;
      switch(sectorNum)
      {
      default:
      case 0:
          x_off = 0;
          y_off = 0;
          break;
      case 0.5:
          x_off = 2.5;
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
      case 2.5:
          x_off = 2.5;
          y_off = 5;
          break;
      case 3:
          x_off = 5;
          y_off = 5;
          break;
      }
      //DRAW THE FLOOR
      for(var y = 0; y < 5; y++)
      {
          for(var x = 0; x < 5; x++)
          {
            sheet.writeTileXY(0,4, this.tile_w*(x_off+x), this.tile_h*(y_off+y),0);
          }
      }
      //DRAW THE ARROWS
      switch(ArrowCfg)
      {
      case 0:
         sheet.writeTileXY(5,1, this.tile_w*(x_off+2), this.tile_h*(y_off+0),1);
         sheet.writeTileXY(2,0, this.tile_w*(x_off+0), this.tile_h*(y_off+2),0);
         sheet.writeTileXY(2,1, this.tile_w*(x_off+4), this.tile_h*(y_off+2),2);
         break;
      case 1:
         sheet.writeTileXY(5,1, this.tile_w*(x_off+2), this.tile_h*(y_off+4),3);
         sheet.writeTileXY(2,0, this.tile_w*(x_off+4), this.tile_h*(y_off+2),2);
         sheet.writeTileXY(2,1, this.tile_w*(x_off+0), this.tile_h*(y_off+2),0);
         break;
      case 2:
         sheet.writeTileXY(2,1, this.tile_w*(x_off+2), this.tile_h*(y_off+0),1);
         sheet.writeTileXY(5,1, this.tile_w*(x_off+0), this.tile_h*(y_off+2),0);
         sheet.writeTileXY(2,0, this.tile_w*(x_off+4), this.tile_h*(y_off+2),2);
         break;
      case 3:
         sheet.writeTileXY(5,1, this.tile_w*(x_off+2), this.tile_h*(y_off+0),1);
         sheet.writeTileXY(5,0, this.tile_w*(x_off+0), this.tile_h*(y_off+2),0);
         sheet.writeTileXY(2,0, this.tile_w*(x_off+2), this.tile_h*(y_off+4),3);
         break;
      case 4:
         sheet.writeTileXY(2,1, this.tile_w*(x_off+2), this.tile_h*(y_off+4),3);
         sheet.writeTileXY(5,0, this.tile_w*(x_off+4), this.tile_h*(y_off+2),2);
         break;
      case 5:
         sheet.writeTileXY(5,1, this.tile_w*(x_off+2), this.tile_h*(y_off+0),1);
         sheet.writeTileXY(2,0, this.tile_w*(x_off+0), this.tile_h*(y_off+2),0);
         break;
      case 6:
         sheet.writeTileXY(2,1, this.tile_w*(x_off+2), this.tile_h*(y_off+0),1);
         sheet.writeTileXY(4,1, this.tile_w*(x_off+4), this.tile_h*(y_off+2),2);
         break;
      case 7:
         sheet.writeTileXY(5,0, this.tile_w*(x_off+0), this.tile_h*(y_off+2),0);
         sheet.writeTileXY(2,1, this.tile_w*(x_off+2), this.tile_h*(y_off+4),3);
         break;
      case 8:
         sheet.writeTileXY(2,0, this.tile_w*(x_off+4), this.tile_h*(y_off+2),2);
         sheet.writeTileXY(5,0, this.tile_w*(x_off+2), this.tile_h*(y_off+4),3);
         break;
      }
      //HORZ WALLS
      for(var y = 0; y < 6; y++)
      {
         for(var x = 0; x < 5; x++)
         {
            if(hwalls[y*5+x]==-1)
               continue;
            if(y!=0)
               sheet.writeTileXY(hwalls[y*5 + x],2, this.tile_w*(x_off+x), this.tile_h*(y_off+y-1),0);
            if(y!=5)
               sheet.writeTileXY(hwalls[y*5 + x],3, this.tile_w*(x_off+x), this.tile_h*(y_off+y),0);
         }
      }
      //VERT WALLS
      for(var y = 0; y < 5; y++)
      {
         for(var x = 0; x < 6; x++)
         {
            if(vwalls[y*6+x]==-1)
               continue;
            if(x!=0)
               sheet.writeTileXY(vwalls[y*6 + x],2, this.tile_w*(x_off+x-1), this.tile_h*(y_off+y),3);
            if(x!=5)
               sheet.writeTileXY(vwalls[y*6 + x],3, this.tile_w*(x_off+x), this.tile_h*(y_off+y),3);
         }
      }
      //NOT WALLS (STUFF THAT'S IN THE MIDDLE OF A TILE)
      for(var y = 0; y < 5; y++)
      {
          for(var x = 0; x < 5; x++)
          {
            var tilearray = notwalls[y*5 + x];
            var i;
            if(tilearray.length==0)
               continue;
            for(i=0;i<tilearray.length;i++)
            {
               sheet.writeTile(notwalls[y*5+x][i], this.tile_w*(x_off+x), this.tile_h*(y_off+y),0);
            }
          }
      }

    }
}

