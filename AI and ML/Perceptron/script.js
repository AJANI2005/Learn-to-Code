
//Perceptron Example using lines
//function to determine linear classification
//points above 1 below -1


//HELPER FUNCTIONS
function F(x){
    return 0.3 * x + 0.2;
}
//Convert unit coordinates to pixel coordinates
function pixelX(x){
    return map(x,-1,1,0,width);
}
function pixelY(y){
    return map(y,-1,1,height,0);
}


class Point{
    constructor(){

        //Inputs
        this.x = random(-1,1);
        this.y = random(-1,1);
        this.bias = 1;
        this.label = 0;
    }

    show(){
        push();
        //Class Visualization
        if(this.label == 1){
            fill(255)
        }else{
            fill(0)
        }

        ellipse(pixelX(this.x),pixelY(this.y),10,10);
        pop();
    }
}

//Random Weight Perceptron
class Perceptron{
    constructor(n){
        this.weights = [];
        this.lr = 0.001;
        for(let i = 0; i < n; i++){
            this.weights.push(random(-1,1))
        }
    }
    //*
    prediction(n){
        return n >= 0 ? 1 : -1;
    }
    weighted_sum(inputs){
        //len(inputs) == len(weights)
        let sum = 0;
        for(let i = 0; i < inputs.length; i++) {
            sum += inputs[i] * this.weights[i];
        }
        return sum;
    }
    guess(inputs){
        return this.prediction(this.weighted_sum(inputs));
    }

    train(inputs,guess,target){
        let error = target - guess;
        for(let i = 0; i < this.weights.length; i++){
            //Linear Regression with Gradient Descent
            this.weights[i] += this.lr * error * inputs[i];
        }
    }

}


let points = [];
var perceptron;
function setup(){
    createCanvas(400,400)

    perceptron = new Perceptron(3);
    //Initialize Training Data
    for(let i = 0; i < 20; i++){
        let p = new Point();
        let lineY = F(p.x);
        if(p.y < lineY){
            p.label = -1;
        }else{
            p.label = 1;
        }
        points.push(p);
    }
}

function draw(){
    background(50)

    //Draw Classification Line
  
    let y1 = F(-1);
    let y2 = F(1);
    push();
    stroke(255);
    line(pixelX(-1), pixelY(y1), pixelX(1),pixelY(y2));
    pop();


    //Draw Perceptron Line
    //1-Determine y for x = -1 and x = 1
    let w0 = perceptron.weights[0]; 
    let w1 = perceptron.weights[1];
    let w2 = perceptron.weights[2];

    let y3 = -(w2/w1) - (w0 * -1/w1);
    let y4 = -(w2/w1) - (w0 * 1/w1);


    push();
    stroke(255,255);
    line(pixelX(-1), pixelY(y3), pixelX(1),pixelY(y4));
    pop();

    //Visualize Inputs
    for(let i = 0; i < points.length; i++){
        points[i].show();
    }
    //Run Perceptron
    for(let i = 0; i < points.length; i++) {
        let p = points[i];
        let inputs = [p.x,p.y,p.bias];
        let target = p.label;
        let guess = perceptron.guess(inputs)
        perceptron.train(inputs,guess,target);
        

        //Visualize Progress
        push();
        noFill();
        if(guess == target){
            stroke(0,255,0);
        }else{
            stroke(255,0,0);
        }
        ellipse(pixelX(p.x),pixelY(p.y),10,10);
        pop();

      
    }

    
    

}