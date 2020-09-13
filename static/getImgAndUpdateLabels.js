let canvas, context, prevX, prevY;
let coords = []

function init(){
	canvas = document.getElementById("canvas");
	context = canvas.getContext("2d");
	canvas.addEventListener("mousedown", startDrawing);
	canvas.addEventListener("touchstart", startDrawing);
}

function startDrawing(event){
	context.clearRect(0,0,canvas.width,canvas.height);
	coords = []
	prevX = event.clientX - canvas.offsetLeft;
	prevY = event.clientY - canvas.offsetTop;
	canvas.addEventListener("mousemove", draw);
	canvas.addEventListener("touchmove", draw);
	canvas.addEventListener("mouseup", stopDrawing);
	canvas.addEventListener("touchend", stopDrawing);
}
function draw(event){
	let x = event.clientX - canvas.offsetLeft
	let y = event.clientY - canvas.offsetTop
	let id = {
		row: x,
		column: y
	}
	coords.push(id)
	context.beginPath()
	context.moveTo(prevX, prevY)
	context.lineTo(x,y)
	context.lineWidth = 2
	context.strokeStyle = "black"
	context.stroke()
	context.closePath()
	prevX = x
	prevY = y
}

function stopDrawing(event){
	canvas.removeEventListener("mousedown", startDrawing)
	canvas.removeEventListener("touchstart", startDrawing)
	canvas.removeEventListener("mousemove", draw)
	canvas.removeEventListener("touchmove", draw)
	$.ajax({
		url: '/script',
		method: 'POST',
		contentType: 'application/json',
		data: JSON.stringify(coords)
	}).then(function(response){
		for(let i=0; i<Object.keys(response).length;i++){
			document.getElementById(i.toString()).textContent = `${i}: ${Math.round(response[i]*100)/100}%`	// update labels with predictions
		}
	})
	init();
}