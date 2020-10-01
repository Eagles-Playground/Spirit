var player;
var playerImage;

function preload(){
	playerImage = loadImage("assets/eagle1.png")
}

function setup() {
	createCanvas(768, 1024);
	player = new Player(370, 700, playerImage);
	console.log(player.img.height)
  
}

function draw() {
	background(220);
	player.regMovement()
  	//draw objects below here
  	player.draw()
}

function mouseClicked(event) {
	player.y -= 100;
}