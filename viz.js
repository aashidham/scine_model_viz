/*<!DOCTYPE html>
<html>
<head>
<title>Test</title>
<script src="http://code.jquery.com/jquery-2.0.0.js"></script> <!-- <script src="http://code.jquery.com/jquery-1.10.0.js"></script> -->
<script src="http://dygraphs.com/1.0.1/dygraph-combined.js"></script>
</head>
<body>
<br/>
Probe Data: (format is [[x,y,cpe-α,cpe-k,Neher],...,]) <br/>
<textarea id="probedata" cols=100 rows=2>
[[0.0, 1e-7, 0.5, 0.0003, 100000000.0], [3.7499999999999998e-08, 1.8998355191963336e-07, 0.5, 0.0003, 100000000.0], [7.4999999999999997e-08, 2.6339134382131854e-07, 0.5, 0.0003, 100000000.0], [1.1249999999999999e-07, 3.1598061649411345e-07, 0.5, 0.0003, 100000000.0], [1.4999999999999999e-07, 3.5707142142714254e-07, 0.5, 0.0003, 100000000.0], [1.875e-07, 3.903123748998999e-07, 0.5, 0.0003, 100000000.0], [2.2499999999999999e-07, 4.1758232721225167e-07, 0.5, 0.0003, 100000000.0], [2.6249999999999997e-07, 4.39992897669951e-07, 0.5, 0.0003, 100000000.0], [2.9999999999999999e-07, 4.58257569495584e-07, 0.5, 0.0003, 100000000.0], [3.375e-07, 4.7285700798444346e-07, 0.5, 0.0003, 100000000.0], [3.7500000000000001e-07, 4.841229182759271e-07, 0.5, 0.0003, 100000000.0], [4.1249999999999997e-07, 4.922842166878804e-07, 0.5, 0.0003, 100000000.0], [4.4999999999999998e-07, 4.9749371855331e-07, 0.5, 0.0003, 100000000.0], [4.8749999999999999e-07, 4.998437255783051e-07, 0.5, 0.0003, 100000000.0], [5.2499999999999995e-07, 4.993746088859545e-07, 0.5, 0.0003, 100000000.0], [5.6250000000000001e-07, 4.960783708246107e-07, 0.5, 0.0003, 100000000.0], [5.9999999999999997e-07, 4.898979485566356e-07, 0.5, 0.0003, 100000000.0], [6.3749999999999993e-07, 4.807221130757353e-07, 0.5, 0.0003, 100000000.0], [6.75e-07, 4.6837484987987984e-07, 0.5, 0.0003, 100000000.0], [7.1249999999999995e-07, 4.525966747557918e-07, 0.5, 0.0003, 100000000.0], [7.5000000000000002e-07, 4.330127018922193e-07, 0.5, 0.0003, 100000000.0], [7.8749999999999998e-07, 4.090767042988393e-07, 0.5, 0.0003, 100000000.0], [8.2499999999999994e-07, 3.799671038392666e-07, 0.5, 0.0003, 100000000.0], [8.625e-07, 3.4437443284889773e-07, 0.5, 0.0003, 100000000.0], [8.9999999999999996e-07, 3.0000000000000004e-07, 0.5, 0.0003, 100000000.0], [8.9999999999999996e-07, 3e-07, 0.4, 0.0003, 100000000.0], [9.4583333333333331e-07, 3e-07, 0.4, 0.0003, 100000000.0], [9.9166666666666656e-07, 3e-07, 0.4, 0.0003, 100000000.0], [1.0375e-06, 3e-07, 0.4, 0.0003, 100000000.0], [1.0833333333333333e-06, 3e-07, 0.4, 0.0003, 100000000.0], [1.1291666666666667e-06, 3e-07, 0.4, 0.0003, 100000000.0], [1.175e-06, 3e-07, 0.4, 0.0003, 100000000.0], [1.2208333333333332e-06, 3e-07, 0.4, 0.0003, 100000000.0], [1.2666666666666667e-06, 3e-07, 0.4, 0.0003, 100000000.0], [1.3124999999999999e-06, 3e-07, 0.4, 0.0003, 100000000.0], [1.3583333333333332e-06, 3e-07, 0.4, 0.0003, 100000000.0], [1.4041666666666666e-06, 3e-07, 0.4, 0.0003, 100000000.0], [1.4500000000000001e-06, 3e-07, 0.4, 0.0003, 100000000.0], [1.4958333333333333e-06, 3e-07, 0.4, 0.0003, 100000000.0], [1.5416666666666666e-06, 3e-07, 0.4, 0.0003, 100000000.0], [1.5875e-06, 3e-07, 0.4, 0.0003, 100000000.0], [1.6333333333333333e-06, 3e-07, 0.4, 0.0003, 100000000.0], [1.6791666666666665e-06, 3e-07, 0.4, 0.0003, 100000000.0], [1.725e-06, 3e-07, 0.4, 0.0003, 100000000.0], [1.7708333333333332e-06, 3e-07, 0.4, 0.0003, 100000000.0], [1.8166666666666665e-06, 3e-07, 0.4, 0.0003, 100000000.0], [1.8625e-06, 3e-07, 0.4, 0.0003, 100000000.0], [1.9083333333333334e-06, 3e-07, 0.4, 0.0003, 100000000.0], [1.9541666666666665e-06, 3e-07, 0.4, 0.0003, 100000000.0], [1.9999999999999999e-06, 3e-07, 0.4, 0.0003, 100000000.0]]
</textarea><br/>
<br/>Env region from <textarea id="h_low" type="number" cols=10 rows=1 style="height:10px;">1e-6</textarea> to <textarea id="h_high" type="number" cols=10 rows=1 style="height:10px;">1.7e-6</textarea><br/>
<br/><button id="update">Update Graph Below</button><br/><br/>
Env plot:
<div id="demodiv"></div><br/><br/>
Materials plot:
<div id="demodiv2"></div>
<script>

var maxX = data[data.length-1][0]
for (i=0;i<data.length;i++)
{
	var temp = data[i][0];
	data[i][0] = data[i][1];
	data[i][1] = maxX - temp;
}
*/
function rainbow(numOfSteps, step) {
    // This function generates vibrant, "evenly spaced" colours (i.e. no clustering). This is ideal for creating easily distinguishable vibrant markers in Google Maps and other apps.
    // Adam Cole, 2011-Sept-14
    // HSV to RBG adapted from: http://mjijackson.com/2008/02/rgb-to-hsl-and-rgb-to-hsv-color-model-conversion-algorithms-in-javascript
    var r, g, b;
    var h = step / numOfSteps;
    var i = ~~(h * 6);
    var f = h * 6 - i;
    var q = 1 - f;
    switch(i % 6){
        case 0: r = 1, g = f, b = 0; break;
        case 1: r = q, g = 1, b = 0; break;
        case 2: r = 0, g = 1, b = f; break;
        case 3: r = 0, g = q, b = 1; break;
        case 4: r = f, g = 0, b = 1; break;
        case 5: r = 1, g = 0, b = q; break;
    }
    var c = "#" + ("00" + (~ ~(r * 255)).toString(16)).slice(-2) + ("00" + (~ ~(g * 255)).toString(16)).slice(-2) + ("00" + (~ ~(b * 255)).toString(16)).slice(-2);
    return (c);
}	

function redraw()
{
	var data = eval($("#probedata").val());
	var data2 = [];
	for (var i=0; i < data.length; i++)
	{
		data2.push([data[i][0],data[i][1]]);
	}
	g = new Dygraph(
		document.getElementById("demodiv"),
		data2,
		{
			labels: ["Distance from tip", "Probe Radius"],
			xlabel: "Distance from tip",
			interactionModel: {},
			underlayCallback: function(canvas, area, g) {
				var bottom_left = g.toDomCoords(parseFloat($("#h_low").val()), -20);
				var top_right = g.toDomCoords(parseFloat($("#h_high").val()), +20);
				
				var left = bottom_left[0];
				var right = top_right[0];
				
				canvas.fillStyle = "rgba(255, 255, 102, 1.0)";
				canvas.fillRect(left, area.y, right - left, area.h);
			}
		});
	g = new Dygraph(
		document.getElementById("demodiv2"),
		data2,
		{
			labels: ["Distance from tip", "Probe Radius"],
			xlabel: "Distance from tip",
			interactionModel: {},
			underlayCallback: function(canvas, area, g) {
				var idxChanged = [0];
				for (var i=0; i < data.length-1; i++)
				{
					if(data[i][2] != data[i+1][2] || data[i][3] != data[i+1][3] || data[i][4] != data[i+1][4])
					{
						idxChanged.push(i+1);
					}
				}
				idxChanged.push(data.length-1);
				console.log(idxChanged);
				for (var i=0; i < idxChanged.length-1; i++)
				{
					var bottom_left = g.toDomCoords(data[idxChanged[i]][0], -20);
					var top_right = g.toDomCoords(data[idxChanged[i+1]][0], +20);
					var left = bottom_left[0];
					var right = top_right[0];
					canvas.fillStyle = rainbow(idxChanged.length,i);
					canvas.fillRect(left, area.y, right - left, area.h);	
				}
			}
		});

}

$(function(){
	redraw();
	$("#update").click(function()
		{
			redraw();
		});
});
