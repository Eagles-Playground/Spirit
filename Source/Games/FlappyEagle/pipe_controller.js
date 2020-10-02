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
    pipeSpacing = 600;
    bottomYDefault = 1024;
    constructor(topimg, botimg) {
        //img must be a p5 loadimg() object
        this.topimg = topimg;
        this.botimg = botimg;
        //pipe[x][0]is always top, pipe[x][1] is bottom
        this.pipes = [[new Pipe(0, 0, this.topimg), new Pipe(0, this.bottomYDefault, this.botimg)],
            [new Pipe(this.pipeSpacing, 0, this.topimg), new Pipe(this.pipeSpacing, this.bottomYDefault, this.botimg)]];
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
                    item.x = this.pipes[comparison][0].x + this.pipeSpacing
                })
            }
        }
    }
}