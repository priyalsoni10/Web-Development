/* JavaScript me function ek aisa block hota hai jo kaam (task) ko ek jagah store karke baar-baar use karne ka tareeka deta hai.
Function = code ka group + naam
Jab chahe tab aap ise bula (call)  sakte ho
Function ko define karne ke liye "function" keyword ka use kiya jata hai, uske baad function ka naam, parentheses () aur curly braces {} ka use
Function ek reusable code block hota hai.
javascript ka array resizable hota hai, yani hum array me jitni marzi values add ya remove kar sakte hain.
*/
// Function define karna
function greet() {
    console.log("Hello, World!")   
};

// Function ko call karna
greet(); // Output: Hello, World!

function sayMyName() {
    console.log("Priyal");
}
sayMyName(); // Output: Priyal
console.log("----------------------");
// Function with parameters
function greetPerson(name) {
    console.log("Hello, " + name + "!");
}
greetPerson("Priyal"); // Output: Hello, Priyal!
console.log("----------------------");
// Function with return value
function addTwoNumbers(num1, num2) { // parameters: num1, num2
    console.log(num1 + num2);
    return num1+ num2;
}
addTwoNumbers(5, 10); // 15  Function call karne par yeh value return karega
addTwoNumbers(5, "4"); // 54 argument:5 ,"4" (5 , "4" ye dono ko string hi smjhega (string hai, to yeh concatenation karega)
addTwoNumbers(5, "a"); // 3a
addTwoNumbers(5, null); // 3
let sum = addTwoNumbers(5, 10);
console.log("Sum: " + sum); // Output: Sum: 15
console.log("----------------------");
// Function with multiple parameters
function multiplyNumbers(a, b) {
    return a * b;
}
let product = multiplyNumbers(4, 5);
console.log("Product: " + product); // Output: Product: 20
console.log("----------------------");
// Function without parameters
function displayDate() {
    let currentDate = new Date(); // Current date ko get karta hai system (computer/mobile) se current date & time lekar ek Date object banata hai.
    console.log("Current Date: " + currentDate.toDateString());
} //toDateString() date ko short readable format me convert karta hai, jaise: "Mon Jun 24 2024"
displayDate(); // Output: Current Date: [current date]  Current Date: Fri Dec 05 2025
console.log("----------------------");
// Function expression
let square = function(number) { // parameter: number
    return number * number;
};
let result = square(6);
console.log("Square: " + result);
console.log("----------------------");

function add(x, y) {
    console.log(x+y);
}
const result1 = add(3, 4); // 7
console.log(result1); // undefined, kyunki function me return statement nahi hai

console.log("----------------------");
function  add1(x, y) {
    let sum = x + y; // local variable sum
    console.log("The result is returned now");
    return sum;
    console.log("This line will never be executed"); // ye line kabhi execute nahi hogi, kyunki return ke baad function exit ho jata hai
}
const result2 = add1(3, 4); // 7 global scope me result2 variable banega aur usme function ka return value store hoga
console.log(result2); // 7
console.log("----------------------");

function LoginUserMessage(username) {
    //  if(!username) { //"(!) Logical NOT Operator -> agar username false value hai(nhi deya ho to) to ye condition true ho jayegi"    
     if(username === undefined) { //" (===) Strict Equality Operator -> Value bhi same hona chahiye + Type bhi same hona chahiye"
        console.log("Username is missing, please provide a username!");
        return;
    }
     return `${username} just logged in`;
    }
loginMessage = LoginUserMessage("Priyal");
console.log(loginMessage); // Priyal just logged in
console.log(LoginUserMessage("Abc")); // Priyal just logged in
console.log(LoginUserMessage()); // undefined  just logged in
console.log("----------------------");

function LoginUserMessage1(username="Guest") { // default parameter value "Guest"
     if(!username) { 
        return "Username is missing, please provide a username!";
     
    }
     return `${username} just logged in`;
    }
loginMessage1 = LoginUserMessage1();
console.log(loginMessage); // Guest just logged in
console.log(LoginUserMessage1("Abc")); // Abc just logged in
console.log(LoginUserMessage1("")); // Username is missing, please provide a username!
console.log(LoginUserMessage1());// Guest just logged in
console.log("----------------------");

let a21 = true;
if(a21){
    // var sum21 =10 ;// var global scope variable bnata h
    let sum21 = 10 ;// local scope variable
    console.log(" ai s true");
    sum21 +=10
}
// console.log(sum21) // agar khi ksi ki body me(like  if, function etc) to vo local mana jaega vo bahar access nhi ho skta
console.log("-------------------");

function add(x,y){
   let sum = x + y
   return sum // return see hum function me jo local variable ki value ko bahar la skte h
} 
let x = add(10,20);
console.log(x);
console.log('---------------');

function findArea(length,width){
    let area = length * width
    return  area;
    
 }
function costOfTile(area,){
    let tile_cost = area *  120 + 2000 + 500 //  fixed pricee h =120
    console.log("Cost of tile  is: ",tile_cost);

}
function costOfMarbles(area){
    let marble_cost = area * 190 + 4500 + 800;
    console.log("Cost of Marble is: ",marble_cost);

}
costOfTile(1250) ;//Cost of tile  is:  152500
let h1 =  findArea(22,50);
console.log(h1) ; //1100
costOfMarbles(h1); // Cost of Marble is:  214300
console.log("-------------------");

function add(x,y){
    return x + y ;
}
function square1(p){
     console.log( p * p);
}
square1(add(4,5)) //81
console.log('--------------------');

// Javascript me jo function hote h unko hum first citizen consider krte h
// Javascript me function ko variable me store krskte h or jb chahe use kr skte h 

function fun(){
    console.log('Hello By fun...'); //Hello By fun... 

}
let x2 = fun(); // call
console.log(x2) ; //undefined (function kuch return nhi keya  h isleye undefined aaya h )

function fun1(){
    console.log('Hello By fun1...'); //Hello By fun... 

}
let x3 = fun1;// jo x3 me h vhi fun mee bhi 
let q = x3; // function declaration
// console.log(x3) ; //undefined (function kuch return nhi keya  h isleye undefined aaya h )
fun1() // Hello By fun1...
x3()  // Hello By fun1...
console.log(x3); // [Function: fun1] ->bina call keye kisi function ko print krne pr function ka original name(fun1) aayega (x3) nhi aayega  
console.log(fun1);// [Function: fun1] -> x3 = fun1 krne pr function name  fun1 change nhi hua  h bs store ho gya h
console.log(q);// [Function: fun1] ->  q = x3 krne pr function name  fun1 change nhi hua  h bs store ho gya h
console.log('------------------------');

let k = function(){
    // ye bhi ek function ko declare krne ka tarika h
} 

function A(){
    console.log('Hy by A');
}
function B(){
    console.log('Hy by B');
}
function C(){
    console.log('Hy by C');
}
let arr = [A,B,C];
arr[1]() // B call hoga-> Hy by B
for(let i of arr){
    i(); // A,B,C teno call ho jaegee
}
console.log('----------------')

function Intro(){
    console.log('Hy By Person!');
}
let d = { // d object h javascript vala
   Name : "Ajay",
   Age : 34,
   I : Intro // I me function store h

} ;
console.log(d); // { Name: 'Ajay', Age: 34, I: [Function: Intro] }-> I me function ka declaration print hua
d.I(); // Hy By Person!
console.log('--------------------')

let c = {
   Name : "Krishna",
   Age : 23,
   I1 : function(){ // I me function store h
    console.log('Hy I am !'); 
    // console.log(Name); // name sidha variable nhi h name object ke under h  
    // console.log(c.Name); // Krishna  
    // console.log(c.Age); // 23
    console.log(this); // c -> { Name: 'Krishna', Age: 23, I1: [Function: I1] }
    console.log(this.Name)// this -> current object c -> Krishna
    console.log(this.Age)// this -> current object c ->  23
    }
} ;
c.I1() // Hy By Person! 
console.log('-------------------')

function fun2(e){ // jo function apne under kisi or function ko as a argument lerha h usse  higher order function kehte h
    e(); // Hello , Good Morning.... // Call back 
    console.log(e); // [Function: greet]
}
function greet(){
       console.log('Hello , Good Morning....');
}
fun2(greet); // jb koe functionkisi dure function ko as a argument dete h to use call back kehte h -> greet call back function h
console.log('--------------------');

function Fun(){
    console.log('Hyy this is Fun! ');
}
setInterval(Fun,1000);// inbuild function  callback deya or time interval bhi(1000 millisecond h automatic call hoga)




































































































































































