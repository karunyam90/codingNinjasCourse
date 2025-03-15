// var varnum =10
// let letnum =20
// const constnum =30

// console.log(varnum)
// console.log(letnum)
// console.log(constnum)

// function scopecheck(){
//    var varnum1 =20
//    let letnum1 =30
//    const constnum1 =40
//    console.log(varnum1)
//    console.log(letnum1)
//    console.log(constnum1)
//    /////////////////////////
   // console.log(varnum)
//    console.log(letnum)
//    console.log(constnum)
// }
// scopecheck()
// console.log(varnum1) //throw an err
// console.log(letnum1)//throw an err
// console.log(constnum1)//throw an err


///////////////////
var x =10
function foo(){
   console.log(x)
   var x=20
}
foo()