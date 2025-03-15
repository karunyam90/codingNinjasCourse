

// (
//     function (){
//         console.log('karunya')
//     }
// )();


////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////
// FE actually used to keep some variables as private
// const user = (function(){
//     const userData = {
//         userName : 'john',
//         userAge :20
//     }
//     function getName(){
//         console.log(userData.userName)
//     }
//     function getAge(age){
//         console.log(userData.userAge + age)
//     }
//     return {
//         getName,
//         getAge
//         }
// })()

// console.log(user)
// user.getAge(10)
// user.getName()

///////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////
// function main(){
//     return (function(){
//         console.log('hi')
//     })();
// }

// const result = main()
///////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////
var x = 10
(function(){
    console.log(x)
})();