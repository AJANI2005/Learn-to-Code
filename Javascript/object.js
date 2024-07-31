// Create an Object
const person = {
    name: "John",
    age: 30,
    city: "New York"
  };

function Person(){
    this.name = "John";
    this.age = 30;
    this.city = "New York";
}
Person.prototype["bag"] = "Sachel"

p = new Person()
// Stringify Object
var hello = () => {
    console.log("hello world")
}
hello()

console.log(JSON.stringify(p));

let cow = {
    name: "Steve",
};

Object.defineProperty(cow,"moo",{
    get : function() {
        return ()=>{
            console.log("MOOOOOO!")
        }
    }
})
cow.moo();

function sum(){
    let total = 0;
    for(const x of arguments){
        total += +x;
    }
    return total;
}

let s = sum(1,2,3)
console.log(s)


const counter = function(){
    let i = 0;
    return function () {i += 1; return i}
}()

const print_counter = function(){
    console.log(counter())
}

let promise = new Promise((resolve,reject)=>{
    let x = 0;

    if(x==0){
        resolve("OK")
    }else{
        reject("Error")
    }
})

promise.then(
    (value)=>{
        console.log(value)
    },
    (error)=>{
        console.log(error)
    }

)

async function myAsyncFunction(){
    return "Hello";
}

function myPromiseFunction(){
    return Promise.resolve("Hello");
}

myPromiseFunction().then((value)=>{
    console.log("Promised: " + value)
})

myAsyncFunction().then((value)=>{
    console.log("Async: " + value)
});