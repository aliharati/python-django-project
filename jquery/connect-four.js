var blue = true
var rows = $("tr")
var btn = $("button")
btn.click(function(){
    var col = Number($(this).parent().attr('class').split("").pop())-1;
    var row = 5;
    while(row >= 0 && rows.eq(row).children().eq(col).children().eq(0).css("background-color")!='rgb(128, 128, 128)'){
        row--;
    }
    if(row!=-1){
        var cell = rows.eq(row).children().eq(col).children().eq(0);
        if(blue){
            cell.css("background-color","#42a1eb");
            blue = false
        }else{
            cell.css("background-color","#eb4034");
            blue = true
        }
        checkWin(row, col, cell);
    }
    
    
} )

function checkWin(row, col, cell){
    var color = cell.css("background-color");
    var rowWin= false;
    var colWin=1;
    if(row<3){
       rowWin = rows.eq(row).children().eq(col).children().eq(0).css("background-color")==color &&
                rows.eq(row+1).children().eq(col).children().eq(0).css("background-color")==color &&
                rows.eq(row+2).children().eq(col).children().eq(0).css("background-color")==color &&
                rows.eq(row+3).children().eq(col).children().eq(0).css("background-color")==color;
    }
    if(rowWin){
        console.log(color + " Won!");
        btn.off('click');
    }
    colLeft = col+1
    while(colLeft<=6 && rows.eq(row).children().eq(colLeft).children().eq(0).css("background-color")==color ){
        colWin++;
        colLeft++;
    }
    colRight = col-1;
    while(colRight>=0 && rows.eq(row).children().eq(colRight).children().eq(0).css("background-color")==color ){
        colWin++;
        colRight--;
    }
    if(colWin>=4){
        console.log(color + "Won!");
        btn.off('click');
    }

}