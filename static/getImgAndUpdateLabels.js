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
	if(event.type === "mousedown") {
		prevX = event.clientX - canvas.offsetLeft;
		prevY = event.clientY - canvas.offsetTop;
		canvas.addEventListener("mousemove", draw);
		canvas.addEventListener("mouseup", stopDrawing);
	} else{
		prevX = Math.round(event.touches[0].clientX - canvas.offsetLeft)
		prevY = Math.round(event.touches[0].clientY - canvas.offsetTop)
		canvas.addEventListener("touchmove", draw);
		canvas.addEventListener("touchend", stopDrawing);
	}
	coords.push({row:prevX, column:prevY})

}
function draw(event){
	let x,y;
	if(event.type === "mousemove") {
		x = event.clientX - canvas.offsetLeft
		y = event.clientY - canvas.offsetTop
	} else {
		x = Math.round(event.touches[0].clientX - canvas.offsetLeft)
		y = Math.round(event.touches[0].clientY - canvas.offsetTop)
	}
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
	if(event.type === "mouseup") {
		canvas.removeEventListener("mousedown", startDrawing)
		canvas.removeEventListener("mousemove", draw)
	} else {
		canvas.removeEventListener("touchstart", startDrawing)
		canvas.removeEventListener("touchmove", draw)
	}
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