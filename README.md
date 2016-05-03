# Finance

<script type="text/javascript">
var canvas;
var ctx;
var cellSize = 10;   // セル1マスのサイズ
var cols;
var rows;
var cells = new Array();
var x_myplace;
var y_myplace;
window.onload = function()
{
    canvas = document.getElementById('canvas');
    ctx = canvas.getContext('2d');
    cols = Math.floor(canvas.width / cellSize);
    rows = Math.floor(canvas.height / cellSize);
    initCells();
    drawCell2({{past_x}}, {{past_y}})
    canvas.addEventListener('click', canvasClick, false);
    document.getElementById('id_x_place2').value = {{past_x}}
    document.getElementById('id_y_place2').value = {{past_y}}
};
 
// 初期化
function initCells(){
    ctx.fillStyle = 'rgb(60, 60, 60)';
    ctx.fillRect(0,0, canvas.width, canvas.height);
    for(col=0;col<cols;col++){
        cells[col] = new Array();
        for(row=0;row<rows;row++){
            cells[col][row] = 0;
        }
    }
    redraw();
}
 
// 全体を再描画
function redraw(){
    for(col=0;col<cols;col++){
        for(row=0;row<rows;row++){
            drawCell(col, row);
        }
    }
}
 
// セルを描画
function drawCell(x, y){
    var value = cells[x][y];
    var style = value ? "rgb(156, 255,0)" : "rgb(40,40,40)"; 
    ctx.fillStyle = style;
    ctx.fillRect(x * cellSize, y * cellSize,
        cellSize - 1, cellSize - 1);
}
function drawCell2(x, y){
    var value = cells[x][y];
    ctx.fillStyle = "rgb(156, 255,0)";
    ctx.fillRect(x * cellSize, y * cellSize,
        cellSize - 1, cellSize - 1);
}
 
 function expect(x1, y1, x2, y2){
    var Fx = 0.0
        for (i=0;i<50;i++){
            for (j=0;j<20;j++){
                mytotalcomsumer = Math.pow((x1 - i),(y1 - j))
                othertotalcomsumer= Math.pow((x2- i),(y2 - j))
                if (mytotalcomsumer < othertotalcomsumer){
                    Fx += 1.0
                } else if (mytotalcomsumer == othertotalcomsumer){
                    Fx += 0.5
                }
            }
        }
    var mycomsumer = 0.0
    var othercomsumer = 0.0
    for (i=0;i<50;i++){
        for (j=0;j<20;j++){
            mytotalprice = 100 + Math.pow((x1 - i),(y1 - j))
            othertotalprice= ((1000-Fx)/Fx*100) + Math.pow((x2- i),(y2 - j))
            if (mytotalprice < othertotalprice){
                mycomsumer += 1.0
            } else if (mytotalprice == othertotalprice){
                mycomsumer += 0.5
                othercomsumer += 0.5
            }else{
                othercomsumer += 1.0
            }
        }
    }
    return ((1000-Fx)/Fx*100)*othercomsumer
}
// Canvasクリック
function canvasClick(e){
	initCells()
    drawCell2({{past_x}}, {{past_y}})
    var x = 0;
    var y = 0;
    var col = 0;
    var row = 0;
    x = e.clientX - canvas.offsetLeft;
    y = e.clientY - canvas.offsetTop;
    col = Math.floor(x / cellSize);
    row = Math.floor(y / cellSize);
    cells[col][row] = !cells[col][row];
    drawCell(col, row);
    clickplace(cells);
    document.getElementById('id_x_place').value= x_myplace;
    document.getElementById('id_y_place').value=20.0-y_myplace;
    document.getElementById('id_x_place1').value = x_myplace
    document.getElementById('id_y_place1').value = y_myplace
    document.getElementById('id_expect_payoff').value = expect({{past_x}}, {{past_y}}, x_myplace, y_myplace)
}
function clickplace(cells){
	for (var i = 0; i < cells.length; i++) {
		for (var j = 0; j < cells[i].length; j++) {
			if(cells[i][j] == 1){
				x_myplace = i
				y_myplace = j
			}
    	}
	}
}
</script>
</head>
<body>
<canvas id="canvas" width="510" height="210"></canvas>
</body>
