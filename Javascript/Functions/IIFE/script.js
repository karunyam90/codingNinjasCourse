

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
// var x = 10
// (function(){
//     console.log(x)
// })();



/////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////
// /////////////////////////////////////////////////////////////////////////////////////////////////
// Problem statement
// You are required to build a user authentication system for a web application Using the IIFE.




// Requirements

// 1. Create an empty array called registeredUsers to store user data.
// 2. Create an IIFE that returns an object with two functions:
// registerUser: registerUser(username, password):
// (i) It should take two parameters "username" and "password" and add them to the registeredUsers array. 
// (ii) It should call the checkCredentials function to determine if a user with the same credentials already exists in the registeredUsers array.

// (iii) If the user is already registered then return `The user is already registered` otherwise push the user object to the registeredUsers array and return ` The user have been added to the registeredUser array`. 
// checkCredentials: checkCredentials(username, password): 
// (i)  It should take two arguments, "username" and "password".
// (ii) It should check if a user with the given credentials exists in the registeredUsers array. It should return false if the user is not present otherwise true.
// (iii) The checkCredentials function is NOT exposed outside the IIFE, so it can only be called from within the IIFE (e.g., inside registerUser).


// Input:

// userAuth.registerUser('testuser', 'password123');
// userAuth.registerUser('testuser','password123');



// Output:

// The user have been added to the registeredUser array
// The user is already registered
///////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////
// function main() {

//     let userAuth = (function() {
//        // Private array to store registered users
//        const registeredUsers = [];
   
//        // Private function to check credentials
//        function checkCredentials(username, password) {
//            return registeredUsers.some(user => user.username === username && user.password === password);
//        }
   
//        // Public method to register user
//        return {
//            registerUser: function(username, password) {
//                if (checkCredentials(username, password)) {
//                    return 'The user is already registered';
//                } else {
//                    registeredUsers.push({ username, password });
//                    return 'The user have been added to the registeredUser array';
//                }
//            }
//        };
//    })();
//      // Example usage
//      console.log(userAuth.registerUser("user1", "password123")); 
//      // Output: "The user have been added to the registeredUser array"
//      console.log(userAuth.registerUser("user1", "password123")); 
//      // Output: "The user is already registered"
   
//      return userAuth;
//    }
   