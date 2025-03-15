// const username = 'karunya'
// const lastname = 'Daniel'
// console.log(`hi ${username}`)

// function greetuser(name){
//    console.log('***************************************')
//    console.log(`welcome to the party ${name}`)
//    let currentyear =2030
//    const age = calculateAge(name,currentyear)
//    return age
// }

// function calculateAge(name,year){
//    let birthyear = 1980
//    console.log('calculating age')
//    return year - birthyear
// }

// let byear = greetuser(username)
// console.log(byear)
///////////////////////////////////////////////////////////////////////////////////////////
function factorial(n){
   if (n==0){
      return 1
   }
   return n* (n-1)
}

res =factorial(5)
console.log(res)