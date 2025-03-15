// let a = 'global'

// function outerPrint(){
//    let b = 'outerprint'
//    function InnerPrint(){
//       let c = 'InnerPrint'
//       return `${a}-->${b}-->${c}`
//    }
//    // let show = InnerPrint()
//    // console.log(show)
//    return InnerPrint
// }

// let show =outerPrint()
// let printInner = show()
// console.log(printInner)

////////////////////////////////////////////
function generateID(num){
   //Implement Your function here
       let id = `A_2023_`
       let i = num
       return function genid(){
         if (i == num){
            i++
            return id + num
         }
         return id+i++
       }
   }
   
   const func = generateID(99);
   console.log(func());//Output : A_2023_99
   console.log(func()); // Output: A_2023_100
   console.log(func()); 
   console.log(func()); 