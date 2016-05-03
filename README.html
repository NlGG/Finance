<!DOCTYPE HTML>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Game of Life on HTML5 Canvas Element</title>
    <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.4.3/jquery.min.js"></script>
    <style type="text/css">
*{
    margin: 0;
    padding: 0;
    border: 0;
    font-size: 100%;
    line-height: 1;
    font-weight: normal;
    font-style: normal;
    text-decoration: none;
}

h1 {
    font-size: 200%;
    font-weight: bold;
    margin: 5px;
    padding: 2px;
}

body {
    background-color: black;
}

#container {
    margin: 0 auto;
    
    color: #00ff00;
    
    width: 540px;
    height: 540px;
/*    
    border-left: 1px solid #00ff00;
    border-right: 1px solid #00ff00;
*/
    font-family: monospace;
    
    margin-left: auto; margin-right: auto;
}

#menu {
    float: right;
    
    margin-right: 5px;
    padding-top: 70px;
    
    width: 100px;
    /* border: 1px solid #ffffff; */
}

#main {
    float: left;
    
    width: 400px;
    margin-left: 20px;
    
    /* border: 1px solid #ffffff; */
}

#canvas {
    border: 1px solid #00ff00;
}

.button {
    background-image: url('');
    font-size: 100%;
    font-weight: bold;
}

#status {
    margin-left: 20px;
    clear: both;
}

#header {
    margin: 10px;
}
#footer {
    margin-top: 40px;
    margin-left: 20px;
    margin-right: 20px;
    /* border: 1px solid #ffffff; */
}

.size {
    margin-left: 20px;
}
    </style>
    <script type="text/javascript">
//
// ref: https://developer.mozilla.org/en/drawing_graphics_with_canvas
//

alive = 0
dead = 1
function LifeGame()
{
    this.initialize.apply(this, arguments);
}
LifeGame.prototype =
{
    // LifeGame Class Constrcutor
    // @param width field width
    // @param height field height
    //
    initialize: function(width, height)
    {
        this.width = width;
        this.height = height;
        this.generation = 0;
        
        this.board = [0, 0];
        this.current_buffer_index = 0;
        this.alive = null;
        this.initboard(0.4);
    },
    // 
    // @param density density of alives on field, (0 < density <= 1)
    // @desc  initialize member variables related to field
    //
    initboard: function(density)
    {
        var w = this.width;
        var h = this.height;
        
        // allocate arrays
        this.board[0] = new Array(h);
        this.board[1] = new Array(h);
        this.alive = new Array(h);
        for (var i = 0; i < h; i++) {
            this.board[0][i] = new Array(w);
            this.board[1][i] = new Array(w);
            this.alive[i] = new Array(w);
        }
        // init cell state
        var b = this.board[this.current_buffer_index];
        for (var i = 0; i < h; i++)
            for (var j = 0; j < w; j++)
                b[i][j] = Math.random() <= density? alive: dead;
    },
    
    //
    // advance one step
    //
    step: function()
    {
        var curr = this.board[this.current_buffer_index];
        var next = this.board[1 - this.current_buffer_index];
        var alvs = this.alive;
        var w = this.width;
        var h = this.height;
        
        // count alive neighbors
        for (var i = 0; i < h; i++) {
            var ai = alvs[i];
            for (var j = 0; j < w; j++)
                ai[j] = 0;
        }
        for (var i = 0; i < h; i++)
            for (var j = 0; j < w; j++) {
                if (curr[i][j] == dead)
                    continue;
                for (var k = -1; k <= 1; k++)
                    for (var l = -1; l <= 1; l++)
                        if (k != 0 || l != 0)
                            alvs[(i + k + h) % h][(j + l + w) % w]++;
            }
        // step
        for (var i = 0; i < h; i++) {
            for (var j = 0; j < w; j++) {
                var cstate = curr[i][j];
                var nalive = alvs[i][j];
                if (cstate == dead)
                    next[i][j] = nalive == 3 ? alive: dead;
                else
                    next[i][j] = 1 < nalive && nalive < 4 ? alive: dead;
            }
        }

        // swap buffer
        this.current_buffer_index ^= 1;
        
        this.generation = this.generation + 1;
        
        return this.generation;
    },
    //
    // draw cell states to canvas
    //
    draw: function(canvas)
    {
        var cont = canvas.getContext('2d');
        var b = this.board[this.current_buffer_index];
        var w = this.width;
        var h = this.height;
        var cw = canvas.width / w;
        var ch = canvas.height / h;
        
        cont.clearRect(0, 0, canvas.width, canvas.height);
        for (var i = 0; i < h; i++)
            for (var j = 0; j < w; j++)
                if (b[i][j] == 0) {
                    cont.fillStyle = "rgb(0, 255, 0)";
                    cont.fillRect(i*ch, j*cw, ch, cw);
                }
    },
}

// 0: wait
// 1: init progress
// 2: init complete
// 3: stepping
var appstate = 0;
var enabled = 
{
    'init': false,
    'cont': false,
    'stop': false,
}
function syncbutton()
{
    var data = [
        [true, false, false],
        [false, false, false],
        [true, true, false],
        [false, false, true],
    ]
    var tags = ['#init', '#cont', '#stop'];
    for (var i = 0; i < data[appstate].length; i++) {
        $(tags[i]).css('color', ['gray', '#00ff00'][data[appstate][i] ?1: 0])
    }
}
function changeState(st)
{
    appstate = st;
    syncbutton();
}

var life = null;

$(function() {
    function busy(fun) {
        var backup = appstate;
        changeState(4);
        fun()
        appstate = backup;
        changeState(appstate);
    }
    function forceState(states, fn)
    {
        return function() {
            for (var i = 0; i < states.length; i++)
                if (appstate == states[i]) {
                    return fn();
                    break;
                }
        }
    }
    
    $('#init').click(forceState([0, 2], function(){ 
        $('#generation').text('0')
        changeState(1)
        life = new LifeGame(200, 200);
        life.draw($('canvas')[0]);
        changeState(2)
    }));
    
    $('#cont').click(forceState([2], function(){
        changeState(3);
        (function() {
            if (appstate == 3) {
                var g = life.step();
                $('#generation').html(g);
                life.draw($('canvas')[0]);
                setTimeout(arguments.callee, 100);
            }
        })();
    }));
    
    $('#stop').click(forceState([3], function(){
        changeState(2);
    }));
    $('#switch').click(function(){
        $('#main').css('border', 'none');
        $('#menu').css('border', 'none');
        $('#footer').css('border', 'none');
    });
})

    </script>
</head>
<body onload="changeState(0);">
    <div id="container">
        <h1>Conway's Game of Life<br/> on HTML5 Canvas Element</h1>
        <div id="header">
        </div>
        <div id="body">
            <div id="main">
                <canvas id="canvas" width="400" height="400"></canvas>
            </div>
            <div id="menu">
                <div id="init" class="button">init</div>
                <div id="cont" class="button">start</div>
                <div id="stop" class="button">stop</div>
            </div>
            <div id="status">generaiton:<span id="generation"></span></div>
        </div>
        <div id="footer">
        </div>
    </div>
</body>
</html>
