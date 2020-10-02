var player;
var playerImage;
var bottomPipeImage;
var topPipeImage;

function preload(){
	playerImage = loadImage("assets/eagle1.png")
	bottomPipeImage = loadImage("assets/bottompipe.png")
	topPipeImage = loadImage("assets/toppipe.png")
}

function setup() {
	createCanvas(768, 1024);
	player = new Player(370, 700, playerImage);
	pipeController = new PipeController(topPipeImage, bottomPipeImage)
	console.log(player.img.height)
  
}

function draw() {
	background(220);
	player.regMovement()
	pipeController.regMovement()
	pipeController.teleport()
	//draw objects below here
	pipeController.draw()
  	player.draw()
}

function mouseClicked(event) {
	player.y -= 100;
}