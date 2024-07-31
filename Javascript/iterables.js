
count = {};
count[Symbol.iterator] = function(){
    n = 0;
    return{
        next(){
            n+=1;
            return {value : n, done : n >= 10};
        }
    }
}
for (const x of count){
    console.log(x);
}