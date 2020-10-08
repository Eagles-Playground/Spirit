class Pipe {
    constructor(x, y, img) {
        this.x = x;
        this.y = y;
        //img must be a p5 loadimg() object
        this.img = img;
    }
    draw(){
        image(this.img, this.x, this.y)
    }
}

class PipeController {
    pipeSpacingX = 600;
    pipeSpacingY = 200;
    //gets random integer between two points
    //max is exclusive, minimum is inclusive
    //Citation: MDN docs
    randomInt(min, max){
        min = Math.ceil(min);
        max = Math.floor(max);
        return Math.floor(Math.random() * (max - min) + min);
    }
    constructor(topimg, botimg) {
        //img must be a p5 loadimg() object
        this.topimg = topimg;
        this.botimg = botimg;
        //initalize pipes
        //pipe[x][0]is always top, pipe[x][1] is bottom
        //y coords do not matter, will be overwritten later
        this.pipes = [[new Pipe(0, 0, this.topimg), new Pipe(0, 0, this.botimg)],
            [new Pipe(this.pipeSpacingX, 0, this.topimg), new Pipe(this.pipeSpacingX, 0, this.botimg)]];
        //set vetical pipe spacing
        for (var pipeset of this.pipes){
            pipeset[0].y = this.randomInt(-512, 0);
            pipeset[1].y = pipeset[0].y + pipeset[0].img.height + this.pipeSpacingY
        }
    }
    draw(){
        for (var pipeset of this.pipes){
            for (var pipe of pipeset){
                pipe.draw()
            }
        }
    }
    //scrolls pipe across screen
    regMovement(){
        for (var pipeset of this.pipes){
            for (var pipe of pipeset){
                pipe.x -= 3
            }
        }
    }
    //checks if pipe is offscreen, if it is, teleport behind
    teleport(){
        for (var i=0; i < this.pipes.length; i++){
            //sets other pipe set for comparison
            var comparison = i+1;
            if (comparison >= this.pipes.length){
                comparison = 0;
            }
            //checks if pipe is offscreen
            if (this.pipes[i][0].x + this.pipes[i][0].img.width < 0){
                //teleports pipes back
                this.pipes[i].forEach((item, index) =>{
                    item.x = this.pipes[comparison][0].x + this.pipeSpacingX
                })
                //randomizes vertical pipe spacing
                this.pipes[i][0].y = this.randomInt(-1000, 0);
                this.pipes[i][1].y = this.pipes[i][0].y + this.pipes[i][0].img.height + this.pipeSpacingY
            }
        }
    }
}