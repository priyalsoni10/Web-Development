/* Async / Await kya hota hai? (Hinglish me)
Async / Await JavaScript me Promises ko easy aur readable banane ka tareeka hai 😊
Same kaam jo .then() se hota hai, woh simple normal code jaise likh sakte ho.
async:
Function ko batata hai: yeh Promise return karega
Iske andar await use kar sakte ho
await:
Ruk jao jab tak kaam complete na ho”
Page freeze nahi hota (non-blocking)
EX:
await fetch = waiter order lene gaya
await response.json() = khana plate me aaya
console.log(data) = khana kha liya
*/

// async function Abc(){
//     return 5 // async  function se ye ensure hota h ki promise return ho rha h
// }
// Abc().then((x)=>{
//     // alert(x)
//     console.log(x);
// })
console.log("-----------------------");


async function Abc(){
   let delhiWeather = new Promise((resolve,reject)=>{
    setTimeout(()=>{
        resolve("27deg")
    },3000)
})
let bangaloreWeather = new Promise((resolve,reject)=>{
    setTimeout(()=>{
        resolve("21deg")
    },6000)
})
  //delhiWeather.then(alert) // 27  but alert function yha kaam nhi krega vo html page se connect nhi h
  //bangaloreWeather.then(alert) // 21
  console.log(" Fetching Delhi Weather Please Wait...");
  let DW = await delhiWeather
  console.log("Fetching Delhi Weather is:" + DW);

  console.log(" Fetching Bangalore Weather Please Wait...");
  let BW = await bangaloreWeather
  console.log("Fetching Bangalore Weather is:" + BW);
  return[DW,BW]
}

const cherry = async()=>{
    console.log("I am cherry and I am  waiting....");
}
const main1 = async()=>{
     console.log("Welcome to Weather Control Room");
// console.log(DW);
// console.log(BW);
    let a =  await  Abc()
    let b = await cherry()
// console.log(a); // ye hmesha promise return krtah
a.then((value)=>{
    console.log(value);
})
// console.log(a);
}
main1()



