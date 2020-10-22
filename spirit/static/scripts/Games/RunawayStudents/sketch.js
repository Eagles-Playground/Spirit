var wall1;
var wall2;
var wall3;
var wall4;
var score = 0;
var stu;
var chr;
let timer = 60;
var playing = true;
function preload() {
  stuImg = loadImage ('kid.png'); //the image used for the student
  chrImg = loadImage ('d4.png'); //the image used for the character
}
function setup() {
  createCanvas(400, 400);
  stu = new Group();
  stu = createSprite(
    random(100, width-100),
    random(100, height-100),
      100, 100);
  stu.velocity.y = random (-5, 5); //student speed and direction
  stu.velocity.x =random (-5, 5);
  stu.addImage(stuImg);
  chr = createSprite(
    width/4, height/4, 150, 150);
  chr.addImage(chrImg);
  wall1 = createSprite( 0, 0, 800, 50); //wall colliders
  wall1.shapeColor = color( 220);
  wall2 = createSprite( 0,  0, 50, 800)
  wall2.shapeColor = color( 220);
  wall3 = createSprite(400,400, 800, 50)
  wall3.shapeColor = color( 220);
  wall4 = createSprite(400,400, 50, 800)
  wall4 .shapeColor = color( 220);
}

function draw() {
  background(50); //background image
  drawSprites();
  if ( frameCount % 60 == 0 && timer > 0) {  //game timer
    timer --;
  }
  if ( timer > 0) {
  chr.collide(wall1); //character collider
  chr.collide(wall2);
  chr.collide(wall3);
  chr.collide(wall4);
  stu.overlap(chr, overide);
  stu.collide(wall1);
  stu.collide(wall2);
  stu.collide(wall3);
  stu.collide(wall4);
  drawSprites();
  noStroke();                        
  textSize(72);
  textAlign(CENTER, CENTER);
  if ( score > 0 ) {
    text( score, width/2, height/2);
  }
  stu.velocity.y = random (-5, 5);
  stu.velocity.x = random (-5, 5);
  if (stu.position.x > 349, stu.position.x < 51) {
    stu.velocity.x = -1;
      }
  if (stu.position.y > 349,  stu.position.y < 51) {
    stu.velocity.y = -1;
    }
  }
  if ( timer == 0) {
    chr.collide(wall1);
    chr.collide(wall2);
    chr.collide(wall3);
    chr.collide(wall4);
    stu.collide(wall1);
    stu.collide(wall2);
    stu.collide(wall3);
    stu.collide(wall4);
    stop();
    playing = false;
    if (mouseIsPressed) {
      restart();
      playing = true;
    }
  }
}
function keyPressed () {
  if (playing == true) {
    if (keyCode == RIGHT_ARROW) {
      chr.setSpeed (5,0);
  }
  else if (keyCode == LEFT_ARROW) {
    chr.setSpeed (5,180);
  }
  else if (keyCode == UP_ARROW) {
    chr.setSpeed (5, 270);
  }
  else if (keyCode == DOWN_ARROW) {
    chr.setSpeed ( 5,90);
  }
  else {
    chr.setSpeed (0,0);
  }
  return false;
  }
  if (playing == false) {
    chr.setSpeed (0,0);
  }
}
function overide ( stu) {
  score += 1;
  stu.position.x = random ( 50, 350);
  stu.position.y = random ( 50,350);
}
function stop() {
  stu.velocity.y = 0;
  stu.velocity.x = 0
  textSize(20);
  text("Click to Restart", 125,100);
  textSize(13);
}
function restart() {
  stu.velocity.y = random (-5, 5);
  stu.velocity.x = random (-5, 5);
  if (stu.position.x > 349, stu.position.x < 51) {
    stu.velocity.x = -1;
      }
  if (stu.position.y > 349,  stu.position.y < 51) {
    stu.velocity.y = -1;R
    }
  timer = 60;
  score = 0;
}