var player = {
  x: 384,
  y: 700,
  width: 128,
  height: 64,
}

function setup() {
  createCanvas(768, 1024);
  
}

function draw() {
  background(220);
  if (player.y < 1024 - player.height) {
    player.y += 3;
  }
  drawPlayer(player);
}

function drawPlayer(player) {
  rect(player.x, player.y, player.width, player.height);
  fill('red')
  
}
function mouseClicked(event) {
  player.y -= 100;
}