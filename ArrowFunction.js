// Higher Order Array Methods -> map,filter, reduce
function Fun(...a){ // ye array bn jaega(...)lgaya h, agr (...) nhi lgy h to ek element aaye error nh aega
    console.log("Hyy",a)// Hyy [4, 7, 10, 5, 6, 3, 4,  9, 2, 1]
  
 

    return a + 5 // 4,7,10,5,6,3,4,9,2,15 , 5 concatenate ho gya
}
x = Fun(4,7,10,5,6,3,4,9,2,1 )
console.log(x);
console.log('---------------------');

function Fun1(b,c){ // higher order function
    if( b > 0 ){
        c(b); // call back function call
    }
}
function square(e){
    console.log( e * e);
}
function cube(e){
    console.log( e * e * e);
}
Fun1(2,square)  // 4 call back function
Fun1(3,cube)    // 27  call back function
Fun1(0,cube) // no output
Fun1(-1,square) // no output
console.log('---------------------')

let fun = function(){
    console.log('Hii')
}
fun();
console.log('---------------------')

function add(d,f){
    return d + f
}
let k =add(5,6)
console.log(k); //11 
console.log('---------------------')

// Arrow function 
let add1 = (g,h) => g + h;

// let i =add1(5,6)
// console.log(i); //11 
console.log(add1(5,6)) // 11
console.log('---------------------')

// setInterval(()=>{
//     console.log('Hii');
// },2000) // 2000 milisec
console.log('---------------------')

let arr = [13,34,56,45,33,3,9];
arr.forEach((e)=>{
    console.log(e*e)
})
console.log('---------------------')

let p2 ={
    name:"John",
    age:30,
    // intro:function()=>{ //yha arrow function nhi lekh skte 
    intro:function(){ //yha arrow function nhi lekh skte 
        console.log(this.name);
        console.log(this.age);
    }
}
p2.intro();
console.log('-------------------');

//Factory function
function Person(n,a,s){
    return {
        name:n,
        age : a,
        salary:s
    }
}
var p1 =Person("Pankaj",25 ,50000);
console.log(p1);
console.log('----------------------');

let arr1 = [2,5,6,7,4,7,6] 
function sqr(e){
    return e *e
}
//  map function
// Map()
// Purpose: Har element par ek function apply karna
// Return: Naya list/object jisme transformed elements hote 
// fiter or map me original array change nhi hota h 
let l = arr1.forEach(sqr); // for each return keye hue data ko nhi smjhta isleye function ki return value nhi dega vhi list de dega jo arr1 me h
console.log(l); // undefined 
let j = arr1.map(sqr) // ye return ki hue value ko smjhta h or return krta h
console.log(j);//[4, 25, 36, 49,  16, 49, 36]
console.log('-----------------------');

let arr3  = [5,8,9,43,5,2,1];
let z = arr3.map((e) => e*e);
console.log(z) //[  25, 64, 81, 1849, 25,  4,1]
console.log('-----------------------');

let arr4  = [5,7,3,1,4,9,10];
let v = arr4.map((e) => e>5);
console.log(v) //[false, true,false, false,false, true,true]
console.log('-----------------------');

let arr5  = [5,7,3,1,4,9,10];
let u = arr4.map((e) => {
    if(e>5){
        return e;
}
});
console.log(u) //[undefined, 7,undefined, undefined,undefined, 9,10]
console.log('-----------------------');

let nums = [1, 2, 3, 4];
let squared = nums.map(x => x * x);
console.log(squared); // [1, 4, 9, 16]
console.log('-----------------------');

let arr2 = [45,23,21]
let a1 =arr2.map((value)=>{ // ye function naya array deta h
    console.log(value)
    return value + 1
})
console.log(a1); // [ 46, 24, 22 ] 
console.log('-----------------------');

let arr7 = [45,23,21]
let a3 =arr2.map((value,index)=>{ // ye function naya array deta h
    console.log(value,index) // index bhi dega
    return value + 1
})
console.log(a1); // [ 46, 24, 22 ]  

// Filter function
// Filter()
// Purpose: Elements ko condition ke basis par filter karna
// Return: Naya list/object jisme sirf condition pass karne wale elements hote hain
let arr6 = [1,3,14,7,2,8,9,10,4,5]
let t = arr6.filter((e)=> e>5);
console.log(t) // [ 14, 7, 8, 9, 10 ] -> only vhi aaege jo bde h 5 se 
console.log("-----------------------");

let products  = [
   {id : 1, name : "Product 1" , price :1000 },
   {id: 2 , name : "Product 2" , price : 2000},
   {id: 3 , name : "Product 3" , price : 3000},
   {id: 4 , name : "Product 4" , price : 4000},
   {id: 5 , name : "Product 5 " , price : 5000},]

    let h = products.filter((p) => p.price >= 3000) 
    console.log(h) // greater than equal to 3000 kaa data aagyega 
    let i = products.map((e) => e.price) // [ 1000, 2000, 3000, 4000, 5000 ]
    console.log(i);
   
let m = products.map((e) => e.price - e.price * 0.05) // [ 1000, 2000, 3000, 4000, 5000 ]
    console.log(m);// [ 950, 1900, 2850, 3800, 4750 ] 5% less

let d = [3,8,6,5,0,3,1,2,7]   
d.map((e,i) => { // array ke sath index bhi mil jaegi
    console .log(e,i);
}) 
console.log('---------------------');
let nums1 = [1, 2, 3, 4, 5];
let even = nums1.filter(x => x % 2 === 0);
console.log(even); // [2, 4]
console.log('-----------------------');
// Reduce Function
// Reduce()
// Purpose: List ke elements ko single value me combine karna
// Return: Ek single value
let a = [3,8,6,5,0,3,1,2,7] 
let sum = a.reduce((e,i) => e+i , 100) // default value = 100 
console.log(sum); // 135
console.log('-----------------------');
let nums2 = [1, 2, 3, 4];
let sum_all = nums2.reduce((a, b) => a + b, 0);
console.log(sum_all); // 10
console.log('-----------------------');
let  arr8 = [1,2,3,4,5,6]
let newarr3 = arr8.reduce((h1,h2)=>{
    return h1 + h2
})
console.log(newarr3); // 21






