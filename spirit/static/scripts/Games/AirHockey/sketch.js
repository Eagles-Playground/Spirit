//Sprites and background variables (keep all)
var spr,
    ai,
    puck;
var paddles;
var computerPos;
var scoreText;
var counter;
var finalscore;

var state = 1;

const canvasDimensions = [600, 400];
const RAD2DEG = 180 / Math.PI;
const DEG2RAD = Math.PI / 180;

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

function rand(a, b) {
    return (a + Math.random() * (b - a));
}

function setup() {
    createCanvas(canvasDimensions[0], canvasDimensions[1]);
    background(20);

    fill(255);
    textAlign(CENTER);

    paddles = new Group();
    goals = new Group();

    spr = createSprite(15, height / 2, 5, 50);
    spr.shapeColor = 'white';
    paddles.add(spr);
  
    ai = createSprite(width - 15, height / 2, 5, 50);
    ai.shapeColor = 'white';
    paddles.add(ai);
  
    p1goal = createSprite(5, height/2, 5, 100);
    p1goal.shapeColor = 'blue';
    goals.add(p1goal);
  
    p2goal = createSprite(width-5, height / 2, 5, 100);
    p2goal.shapeColor = 'red';
    goals.add(p2goal);

    puck = createSprite(width / 2, height / 2, 8, 8);
    puck.shapeColor = '#c6ed2c';

    aiPos = Array.apply(null, Array(10)).map(Number.prototype.valueOf, height / 2);
    score = [0,0];
}

function draw() {
  background(20);
  drawSprites();
  console.log(state);

  if(state==3){
    // set play paddle position to mouse position, within bounds
    spr.position.y = Math.max(0, Math.min(height, mouseY));

    // perfect computer player
    // computer.position.y = ball.position.y;

    // delayed computer player
    aiPos.push(puck.position.y);
    ai.position.y = aiPos.shift();

    // wall collisions
    if (puck.position.y < 4 || puck.position.y > height - 4) {
        puck.velocity.y *= -1;
    }

    // goal collisions
    puck.overlap(p1goal, function(ball, goal){
        score[1]++;
        puck.position.x = width/2;
        puck.position.y = height/2;
        puck.setSpeed(10, rand(170,190));
    });
  
    puck.overlap(p2goal, function(ball, paddle){
        score[0]++;
        puck.position.x = width/2;
        puck.position.y = height/2;
        puck.setSpeed(10, rand(170,190));
    });
  
    //wall bounce
    if (puck.position.x < 4) {
        puck.velocity.x *= -1;
    }
    else if (puck.position.x > width - 4) {
        puck.velocity.x *= -1;
    }

    // ball/paddle collisions
    puck.overlap(paddles, function(ball, paddle) {
        puck.velocity.x *= -1.01;
        puck.velocity.y += (puck.position.y - paddle.position.y) / 20;
    });

    scoreText = score[0] + " – " + score[1];
    text(scoreText, width/2, 20);
  
   if (score[0] == 8){
      puck.setSpeed(0, rand(-15,15))
      scoreText = "Player 1 is the winner";
      text(scoreText, width/2, 40);
      finalscore = 0;
      finalscoreText = finalscore;
      if(score[0] == 8){
        finalscore = finalscore + 25;
      }
      //send score to database
      var xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
        console.log(this.responseText)
        }
      };
      xhttp.open("POST", "/airHockeyScoreUpdate/", true);
      xhttp.setRequestHeader("score", finalscore);
      xhttp.setRequestHeader("X-CSRFToken", csrftoken);
      xhttp.send();
      //end the game
      state = 4;
    } else if (score[1] == 8){
      puck.setSpeed(0, rand(-15,15));
      scoreText = "AI is the winner";
      if(score[1] == 8){
        finalscore = 25 - score[1] + score[0];
      }
      //send score to database
      var xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
        console.log(this.responseText)
        }
      };
      xhttp.open("POST", "/airHockeyScoreUpdate/", true);
      xhttp.setRequestHeader("score", finalscore);
      xhttp.setRequestHeader("X-CSRFToken", csrftoken);
      xhttp.send();
      //end the game
      state = 4;
    }
  }
  
  // Draw Title Card
  if (state == 1){
    text("Air Hockey", width/2, height/2-20);
    text("Click to start click, click again to start puck!", width/2, height/2+20);
    text("Move mouse up and down to move the left side paddle to bounce\n the puck in the AI player's goal.", width/2, height/2+40);
  }
  //Draw end Card
  if (state == 4){
    text("Game Over! Final Score: " + finalscore, width/2, 60);
    text("Please refresh page to update score!", width/2, height/2-20);
  }
}

function mouseClicked(event) {
  switch (state){
    //starting game
    case 1:
      state = 2;
      
      break;

    case 2:
      state = 3;
      puck.setSpeed(10, rand(-15, 15));
      break;
    case 3:
      break;
    //ending game
    case 4:
      score[0] = 0;
      score[1] = 0;
      state = 1;
      //setup();
      break;
  }
}