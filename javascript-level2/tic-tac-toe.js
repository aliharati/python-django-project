document.querySelector(".btn").addEventListener("click",refreshTable );
var refreshIntervalId;
var x = true;
var arr = [];
var ongoing = true;
for(var i=0;i<3;i++){
    inner = [];
    for(var j=0;j<3;j++){
        inner.push('');
    }
    arr.push(inner);
}
dict = {
    "one": [0,0],
    "two": [0,1],
    "three": [0,2],
    "four": [1,0],
    "five": [1,1],
    "six": [1,2],
    "seven": [2,0],
    "eight": [2,1],
    "nine": [2,2]
}
var cells=  document.querySelectorAll("td")
function refreshTable(){
    var cells = document.querySelectorAll('td');
    cells.forEach(element => element.innerText='');
    document.querySelector("#win").innerText= "";
    for(var i=0;i<3;i++){
        for(var j=0;j<3;j++){
            arr[i][j] = '';
        }
    }
    ongoing = true
}

cells.forEach((e) =>e.addEventListener("click", tic));


function tic(e){
    if(e.target.innerText=="" && ongoing){
        if(x==true){
            e.target.innerText = "X";
            addToArr(e.target);
            x = false;
            
        }else{
            e.target.innerText = "O";
            addToArr(e.target);
            x = true;
        
    }   
}
}
function addToArr(e){
    var p = findTarget(e);
    arr[p[0]][p[1]] = e.innerText;
    lookForWin(e);
    console.log(arr);
}
function lookForWin(e){
    var tg = e.innerText;
    if((arr[0][0] === tg && arr[0][1] === tg && arr[0][2] === tg)||
        (arr[1][0] === tg && arr[1][1] === tg && arr[1][2] === tg)||
        (arr[2][0] === tg && arr[2][1] === tg && arr[2][2] === tg)||
        (arr[0][0] === tg && arr[1][0] === tg && arr[2][0] === tg)||
        (arr[0][1] === tg && arr[1][1] === tg && arr[2][1] === tg)||
        (arr[0][2] === tg && arr[1][2] === tg && arr[2][2] === tg)||
        (arr[1][0] === tg && arr[1][1] === tg && arr[1][2] === tg)||
        (arr[0][0] === tg && arr[1][1] === tg && arr[2][2] === tg)||
        (arr[0][2] === tg && arr[1][1] === tg && arr[2][0] === tg)
        ){
            document.querySelector("#win").innerText= tg + " Won!";
            this.refreshIntervalId = setInterval(randomColor,200);
            ongoing = false;
            return;
        
    }else{
        var full = true; 
        arr.forEach(e => full = full && e.every(e=> e=="X" || e=='O'))
        if(full){
            clearInterval(this.refreshIntervalId);
            document.querySelector("#win").innerText= " It's a Draw!"
        
        }
    }
    
        
    
    

}

function findTarget(e){
    return dict[e.id];
}
function randomColor(){
    const randomColor = Math.floor(Math.random()*16777215).toString(16);
    document.querySelector("#win").style.color = "#" + randomColor;
}

