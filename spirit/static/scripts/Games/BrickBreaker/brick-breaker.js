let playerScore = 0
let paddle
let ball
let bricks
let gameState = false;
let start = false;

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

function setup() {
  var canvas = createCanvas(800, 450);
  
  canvas = canvas.parent("sketch-holder");

  background(245, 230, 156);

  let colors = createColors()

  textSize(24)
  textAlign(CENTER)
  paddle = new Paddle()
  ball = new Ball(paddle)
  bricks = createBricks(colors)
}

function createColors() {
  const colors = []
  colors.push(color(265, 165, 0))
  colors.push(color(135, 206, 250))
  colors.push(color(147, 112, 219))
  for (let i = 0; i < 10; i++) {
    colors.push(color(random(0, 255), random(0, 255), random(0, 255)))
  }
  return colors
}

function createBricks(colors) {
  const bricks = []
  const rows = 10
  const bricksPerRow = 10
  const brickWidth = width / bricksPerRow
  for (let row = 0; row < rows; row++) {
    for (let i = 0; i < bricksPerRow; i++) {
      brick = new Brick(createVector(brickWidth * i, 25 * row), brickWidth, 25, colors[floor(random(0, colors.length))])
      bricks.push(brick) 
    }
  }
  return bricks
}

function draw() {
  if(state==2) {
    
    document.getElementById('playerScore').innerHTML = playerScore;
    background(0)

    ball.bounceEdge()
    ball.bouncePaddle()
    
    ball.update()

    if (keyIsDown(LEFT_ARROW)) {
      paddle.move('left')
    } else if (keyIsDown(RIGHT_ARROW)) {
      paddle.move('right')
    }

    for (let i = bricks.length - 1; i >= 0; i--) {
      const brick = bricks[i]
      if (brick.isColliding(ball)) {
        ball.reverse('y')
        bricks.splice(i, 1)
        playerScore += brick.points
      } else {
        brick.display()
      }
    }

    paddle.display()
    ball.display()

    textSize(32)
    fill(255)
    //text('Score: '  + playerScore, width - 150, 50)
    
    if (ball.belowBottom()) {
      var xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
        console.log(this.responseText)
        }
      };
      if (playerScore == 99){
        playerScore += 1;
      }
      xhttp.open("POST", "/brickBreakerScoreUpdate/", true);
      xhttp.setRequestHeader("score", playerScore);
      xhttp.setRequestHeader("X-CSRFToken", csrftoken)
      xhttp.send();
      state = 3
    }

    if (bricks.length === 0) {
      state = 3
    }
  }
  if (state == 1){
    fill(135, 120, 39)
    text("Brick Break\n \n Click to begin!", width/2, height/2-40);
    text("Move the paddle with the Left and Right arrow keys\n The goal is to destroy all the bricks or as many as you can!", width/2, height/2+60);
  }

  if (state == 3){
    text("Game Over!!\n Your Score: " + playerScore, width/2, height/2-40);
    text("Please refresh the page to update score!", width/2, height/2+40);
  }
}

function mouseClicked(event) {
  switch (state){
    //starting game
    case 1:
      state = 2;
      break;
    //jumping
    case 2:
      break;
    //ending game
    case 3:
      playerScore = 0;
      state = 1;
      setup();
      break;
  }
}