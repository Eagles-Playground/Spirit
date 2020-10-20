class Player {
    constructor(x, y, img) {
        this.x = x;
        this.y = y;
        //img must be a p5 loadimg() object
        this.img = img;
    }
    draw(){
        image(this.img, this.x, this.y)
    }
    regMovement(){
        if (player.y < 512 - player.img.height) {
            player.y += 2;
        }
    }
}