var player;
var playerImage;
var bottomPipeImage;
var topPipeImage;
var score = 0;

// 3 states
//state 1 is start screen
//state 2 is playing
//state 3 is the high score/restart
var state = 1;

//Function gets a value of a cookie
//Citation: Django Docs
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

function preload(){
	playerImage = loadImage("../static/scripts/Games/FlappyEagle/assets/eagle1.png")
	bottomPipeImage = loadImage("../static/scripts/Games/FlappyEagle/assets/bottompipe.png")
	topPipeImage = loadImage("../static/scripts/Games/FlappyEagle/assets/toppipe.png")
}

function setup() {
  //create canvas, objects
	var canvas = createCanvas(384, 512);
  canvas = canvas.parent("sketch-holder");

	player = new Player(192, 256, playerImage);
	pipeController = new PipeController(topPipeImage, bottomPipeImage)

  //Text Styling
  textSize(24)
  textAlign(CENTER)
}

function draw() {
	background(220);
  //Game Logic
  if (state == 2){
    //collision/score checks
    if (pipeController.collision(player)){
      //send score to database
      var xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
        console.log(this.responseText)
        }
      };
      xhttp.open("POST", "/flappyEagleScoreUpdate/", true);
      xhttp.setRequestHeader("score", score);
      xhttp.setRequestHeader("X-CSRFToken", csrftoken);
      xhttp.send();
      //end the game
      state = 3;
    }
    if (pipeController.checkscore(player)){
      score += 1;
    }
    //movement
    player.regMovement()
    pipeController.regMovement()
    pipeController.teleport()
  }
	//draw objects below here
	pipeController.draw()
	player.draw()

  // Draw Title Card
  if (state == 1){
    text("Flappy Eagle\nClick To Play", width/2, height/2-50);
    text("Click the mouse button\n to make the Eagle go up\n Gravity will handle the rest", width/2, height/2+60)
  }
  //Draw end Card
  if (state == 3){
    text("You Died!\nScore: " + score, width/2, height/2);
    text("Please refresh the page\n to update score!", width/2, height/2+60);
  }
}

function mouseClicked(event) {
  switch (state){
    //starting game
    case 1:
      state = 2;
      player.y -= 50;
      break;
    //jumping
    case 2:
      player.y -= 50;
      if (player.y <= 0){
        player.y = 0;
      }
      break;
    //ending game
    case 3:
      score = 0;
      player = new Player(192, 256, playerImage);
	    pipeController = new PipeController(topPipeImage, bottomPipeImage);
      state = 1;
      break;
  }
}