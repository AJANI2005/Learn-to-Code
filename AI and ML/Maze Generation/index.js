
const canvas_width = 400;
const canvas_height = 400;
const scl = 20;
class Cell {
    constructor(x, y) {
        this.x = x;
        this.y = y;
        this.visited = false;
        //Walls
        this.top = true;
        this.bottom = true;
        this.right = true;
        this.left = true;
    }

    show() {
        push();
        stroke(255);
        let x = this.x * scl;
        let y = this.y * scl;
        if (this.visited) {
            push();
            fill(255, 0, 0, 100);
            noStroke();
            rect(x, y, scl, scl)
            pop();
        }
        if (this.top == true) {
            line(x, y, x + scl, y);
        }
        if (this.bottom == true) {
            line(x, y + scl, x + scl, y + scl);
        }
        if (this.left == true) {
            line(x, y, x, y + scl);
        }
        if (this.right == true) {
            line(x + scl, y, x + scl, y + scl);
        }

        pop();
    }
}


class Maze {
    constructor() {
        this.cols = floor(canvas_width / scl);
        this.rows = floor(canvas_height / scl);

        this.stack = [];
        this.cells = [];

        for (let y = 0; y < this.rows; y++) {
            for (let x = 0; x < this.cols; x++) {
                this.cells.push(new Cell(x, y))
            }
        }

        this.current = this.cells[0];
        this.current.visited = true;
    }
    index(x, y) {
        if (x < 0 || y < 0 || x >= this.cols || y >= this.rows) {
            return undefined;
        }
        return y * this.cols + x;
    }
    getCellNeighbor(cell) {


        let sides = [];
        sides.push(this.cells[this.index(cell.x, cell.y - 1)]);
        sides.push(this.cells[this.index(cell.x, cell.y + 1)]);
        sides.push(this.cells[this.index(cell.x - 1, cell.y)]);
        sides.push(this.cells[this.index(cell.x + 1, cell.y)]);

        let valid = [];
        for (let i = 0; i < sides.length; i++) {
            if (sides[i] == undefined) {
                continue;
            }
            if (!sides[i].visited) {
                valid.push(sides[i]);
            }
        }
        if (valid.length === 0) {
            return undefined;
        }
        
        return valid[floor(random(0, valid.length))];


    }
    algo() {
        let next = this.getCellNeighbor(this.current);

        if (next != undefined) {
            //Modify Walls
            if (this.current.x < next.x) {
                this.current.right = false;
                next.left = false;
            }
            if (this.current.x > next.x) {
                this.current.left = false;
                next.right = false;
            }
            if (this.current.y < next.y) {
                this.current.bottom = false;
                next.top = false;
            }
            if (this.current.y > next.y) {
                this.current.top = false;
                next.bottom = false;
            }

            this.stack.push(this.current);
            this.current = next;
            this.current.visited = true;
            
        } else {
            if (this.stack.length > 0) {
                this.current = this.stack.pop();
            }else{
                
                this.reset();
                
             
            }

        }

    }

    reset(){
        for (let i = 0; i < this.cells.length; i++) {
           
            this.cells[i] = new Cell(this.cells[i].x, this.cells[i].y);
        }
    }
    show() {
        
        for (let i = 0; i < this.cells.length; i++) {
            this.cells[i].show();
        }
        push();
        noStroke();
        fill(100,0,0,100)
        rect(this.current.x * scl,this.current.y * scl,scl,scl);
        pop();
    }
}


let maze;
function setup() {
    createCanvas(canvas_width, canvas_height);
    maze = new Maze()

}



function draw() {
    background(51)
 
    maze.algo();
    maze.show();

}

