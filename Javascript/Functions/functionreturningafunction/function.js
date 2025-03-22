function greet(message){
    return function(wishes){
        return `hello ${wishes},thank you for ${message} me`
    }
}

var greetings = greet('asking')
console.log(greetings('fara'))
//Way 2 of calling the functions
