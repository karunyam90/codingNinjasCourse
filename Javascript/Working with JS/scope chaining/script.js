var a=10
let b=20
const c =30

function print(){
   var a='ten'
   let b="twenty"

   console.log('******inside print function******')
   console.log(a,b,c)
   console.log('***********')
   function innerprint(){
      var a='inner10'
      console.log('******inside innerprint function******')
      console.log(a,b,c)
   }
   innerprint()
}
print()