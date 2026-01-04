// OOPS in JavaScript ka matlab hota hai Object-Oriented Programming System — ek programming style jisme code ko objects ke through organize kiya jata hai.
// JavaScript prototype-based OOP follow karta hai (class-based nahi, jaise Java), lekin ES6 ke baad class syntax aa gaya hai jo OOP ko easy bana deta hai 
// Object-> Collection of properties and method
 // Function Constructer and OOPS
// function Func(){
//     this.n ="5"
// }
//  let f  = new Func();
//  console.log(a.n);

  


let student = {
  name: "Rahul",
  age: 21,
  study() {
    console.log("Studying...");
  }
};

student.study();
console.log('-----------------------');

const user ={
    firstName : "Anurag",
    lastName : "Singh",
    age:21
}
function getBirthYear(age){
    return new Date().getFullYear() - age
}
let year = getBirthYear(user.age) 
console.log(year); // 2004 
console.log('-----------------------');

const user1 ={
    firstName : "Anurag",
    lastName : "Singh",
    age:21,
    // getBirthYear(){} ase bhi lekh skyte  h function
    getBirthYear:function(){
        return new Date().getFullYear() - user.age
        
    }
}
console.log(getBirthYear(user.age));//2004
console.log('-----------------------');
// Factory Function
function createUser(firstName,lastName,age){
    const user ={
    firstName : firstName,
    lastName : lastName,
    age:age 
    }
    return user
}
console.log(createUser("Aman","Misra",32)) // { firstName: 'Aman', lastName: 'Misra', age: 32 }
console.log('-----------------------');

function createUser(firstName,lastName,age){
    const user ={
    firstName,
    lastName,
    age, // key or value same ho tosirf value denge to vo key bna legab 
    getBirthYear(){
        return new Date().getFullYear() - user.age //ye hr user ke object ke leye baar baar bnega or memory consume krega to issko sovee krne ke leye constructor function use hote h
    }
}
    return user
}
console.log(createUser("Aman","Misra",32)) // { firstName: 'Aman', lastName: 'Misra', age: 32 }
const user2 = createUser("Priya","Misra",24)
console.log(user2);
console.log(user2.getBirthYear());// 2002
console.log('-----------------------');

// Constructer Function
function getBirthYear(){ // iss function ko bahar lekhnee se abstraction or encapsulation  role break ho gya
        // return new Date().getFullYear() - user1.age 
        return new Date().getFullYear() - this.age // current object ko point krega
    }
function createUser1(firstName,lastName,age){
    const user1 ={
    firstName,
    lastName,
    age, // key or value same ho tosirf value denge to vo key bna legab 
    getBirthYear // ye ek hi baar create hoga
}
    return user1
}
// console.log(createUser1("Aman","Misra",32));
const user3 = createUser1("Priya","Misra",24) 
const user4 = createUser1("Priyal","Soni",21) 
console.log(user3);
console.log(user4); // pura object aajaega 
// console.log(user3.getBirthYear()) // ReferenceError: Cannot access 'user1' before initialization using this to solve this

// console.log(new Date().getFullYear());// 2026 current year
console.log(user3.getBirthYear()); // 2002 
console.log(user4.getBirthYear()); // 2005 -> 2026 ko bhi calculation me le rha h
console.log(user3.getBirthYear===user4.getBirthYear); // true mtlb ye memory me ek hi baar create hua h agar false aata to hr new user ke leye alg alg create hota
console.log(getBirthYear()); //NaN not a number  break encapsulation and abstraction rule
console.log("-----------------------------");
createUser1.hello = "World"
console.log(createUser1.hello); // World  ye store ho gya h createuser1 to ek function h lekin behind the scene object bhi h to hum kuch store bhi kr skte h
console.dir(createUser1); // [Function: createUser1] { hello: 'World' }
console.log(createUser1.commonMethods); // { getBirthYear: [Function: getBirthYear] }
console.dir(createUser1) //[Function: createUser1] { hello: 'World',commonMethods: { getBirthYear: [Function: getBirthYear] }}
console.log("-----------------------------");


function createUser2(firstName,lastName,age){
    const user2 ={
        firstName,
        lastName,
        age, // key or value same ho tosirf value denge to vo key bna legab 
        getBirthYear : createUser2.commonMethods.getBirthYear// ye ek hi baar create hoga
    }
    return user2
}
createUser2.commonMethods = {
    getBirthYear: function(){ // iss function ko bahar lekhnee se abstraction or encapsulation  role break ho gya
        // return new Date().getFullYear() - user1.age 
        return new Date().getFullYear() - this.age // current object ko point krega
    }
    
}
const user5 = createUser2("Priya","Misra",24) 
const user6 = createUser2("Priyal","Soni",21) 
console.log(createUser2.commonMethods.getBirthYear); // [Function: getBirthYear]
console.log("-----------------------------");

function sayHii(){
    console.log("hii");
    console.log(this); // ye ek object ko point krrha jisko isne create keya h(khudka object)  new ka use krege to object hi return krega
    return "hello";
}
console.dir(sayHii) // [Function: sayHii]
console.log(sayHii.prototype);
console.log(new sayHii());// sayHii {}  hum kuch bhi return krenge to bhi ye object hi return krega
console.log("-----------------------------");

function createUser3(firstName,lastName,age){
    this.firstName = firstName
    this.lastName = lastName
    this.age = age
}
// new ka usse krke function ko call keya h to vo constructor h
console.log(new createUser3("Priyal","Soni",21))// createUser3 { firstName: 'Priyal', lastName: 'Soni', age: 21 }
const user7 = new createUser3("Pari","Mishra",24) 
console.log(user7); // createUser3 { firstName: 'Pari', lastName: 'Mishra', age: 24 }
console.log(createUser3.prototype);// {}
// console.log(createUser.__proto__);//[Function (anonymous)] Object
console.log(user7.__proto__);// {}
console.log(user7.__proto__.constructor); // [Function: createUser3]
console.log(user7.constructor); // [Function: createUser3]
 // prototype me by default constructor property hote h jo usi object ko point krte h jiske under ye property hoti h
createUser3.prototype.getBirthYear = function(){ // __proto__ ke under iss pure prototype object ko daal deya jaega
    return new Date().getFullYear() - this.age
}
createUser3.prototype.getFullName = function(){ // __proto__ ke under iss pure prototype object ko daal deya jaega
    return this.firstName + " " + this.lastName
}
//  Constructor function ko capital se start  keya jaata h
console.log(createUser3.prototype); // { getBirthYear: [Function (anonymous)] }
 console.log(user7); // createUser3 { firstName: 'Pari', lastName: 'Mishra', age: 24 }
 console.log(user7.getBirthYear()); // 2002 
console.log(user7.getFullName()); // Pari Mishra

// OOPS 
// Object : Collection of properties and methods
// toLowerCase
// Parts of OOP
// object literal -> object hi h
// Constructer Function
// Prototype
// Classes
// Instances(new,this)
// 4 pillars of oops
// Abstraction - hiding the details ex fetch()
// Encapsulation-> wrap the method and function
// Inheritance -> parent to child property and method pass krna
// Polymorphism -> many forms (ek hi method alg alg behave krte h )

// Object Literal
const user8 = {
    username: "Anurag",
    loginCount: 8,
    SignedIn: true,
    getUserDetails: function() {
        console.log("Got user details from database!");
        console.log(`Username:${this.username}`);// Username:Anurag
        console.log(this); // { username: 'Anurag', loginCount: 8, SignedIn: true, getUserDetails: [Function: getUserDetails] -> ye pura object h }current context

}}
console.log(user8); // { username: 'Anurag', loginCount: 8, SignedIn: true }
console.log(user8.username); // Anurag
console.log(user8.getUserDetails()); //  Got user details from database!] 
console.log(this);// {}  node pr ye khali object h browser me window object hota h 
console.log('------------------------------');

// Constructer Function
// const promise1 = new Promise () 
// const date = new Date();// ye new keyword se create hua  constructer function h new context bnane ke kaam aata h

function User(username,loginCount,SignedIn){
    this.username = username ;
    this.loginCount = loginCount;
    this.SignedIn = SignedIn;
    this.greeting = function(){ // abstraction and encapsulation
        console.log(`Welcome , ${this.username}`);
    }
    return this ; // agar hum return nhi krenge to bhi new keyword se naya object create hoga or return ho jaega  but agar hum kuch aur return krenge to vo return ho jaega
}
const user9 =  User("Anurag",10,true)
const user10 =  User("Anu",11,false)
const user11 = new User("Anup",13,true)   // new keyword se call keya h to naya object create hoga 
const user12 = new User("Anjali",14,true)   // new keyword se call keya h to naya object create hoga 
console.log(user9); // User { username: 'Anurag', loginCount: 10, SignedIn: true } new nhi use krenge to inke alawa bhi or properties function ka jaegi 
console.log(user10); // User { username: 'Anu', loginCount: 11, SignedIn: false } new nhi use krenge to inke alawa bhi or properties function ka jaegi  or override bhi ho jaegi purani value se
console.log(user11); // User { username: 'Anup', loginCount: 13, SignedIn: true } new keyword se call keya h to naya object create hoga 
console.log(user12); // User { username: 'Anjali', loginCount: 14, SignedIn: true } new keyword se call keya h to naya object create hoga or  override nhi hoga purani value se 
console.log('------------------------------');
// New keyword kaam kaise krta h
// 1. New ek naya empty object(instance) create krta h
// 2. Fir us empty object ko function ke this se link kr deta h
// 3. Fir function ke andar ka code execute krta h
// 4. Aur last me by default ye new created object ko return kr deta h agar hum kuch aur return nhi krte
// 5. new keyword constructer function ke sath hi use hota h(constructor call hota h new keyword ke karan)
console.log(user10.constructor);//[Function: Object] ->  [Function: User]
console.log(user11 instanceof User); // true // ye check krta h ki user11 ka prototype User ke prototype se linked h ya nhi mtlb ye User ka hi object h
console.log(user12 instanceof User); // true // ye check krta h ki user12 ka prototype User ke prototype se linked h ya nhi mtlb ye User ka hi object h
console.log('------------------------------');

// Prototype
/*
// Har function ke sath ek prototype property attach hoti h jo ek object hota h jisme hum shared methods and properties define kr skte h jo us function se bane sare objects ke liye accessible hote h
Prototype JavaScript ka ek mechanism hai jisse objects properties aur methods share karte hain.
JavaScript me har object ke paas ek hidden property hoti hai jise [[Prototype]] kehte hain.
 Agar object ke andar koi property/method nahi mili, to JavaScript uske prototype me dhoondhta hai.
let obj = {
  name: "Rahul"
}

console.log(obj.toString());
// toString() method obj me nahi h to ye uske prototype me dhoondhega jo Object.prototype me hota h
// Prototype chaining: Jab ek object ke prototype me bhi property/method nahi milti, to JavaScript uske prototype ke prototype me dhoondhta hai, aur ye chain tab tak chalta hai jab tak null tak nahi pahuchta.
toString() kaha se aaya?
✔️ obj me nahi hai
✔️ JavaScript ne dekha → obj ka prototype (Object.prototype)
✔️ Wahi mil gaya 
✔️ toString() method Object.prototype me hota hai
obj → Object.prototype → null
JavaScript chain me upar upar search karta rehta hai jab tak method/property mil na jaye.
*/

function multiplyBy5(num){
    return num * 5;

}
multiplyBy5.power = 2; // ye multiplyBy5 function ke under ek property add ho gyi
console.log(multiplyBy5(5)); // 25
console.log(multiplyBy5.power); // 2 kyunki humne add keya h kyunki behind the scene function ek object hi hota h 
console.log(multiplyBy5.prototype); // {} -> ye ek empty object hota h jisme hum shared method and property add kr skte h by default jo context set h ye uska method ka  this h or ye internal property bhi deta h  
console.log("-----------------------");

function createUser4(userName,score){
    this.userName = userName;
    this.score = score;
}
createUser4.prototype.increment = function(){
    // score++; // this nhi use kiya h to pta nhi chal rha h  kisne call keya h kiska score increment krna h
    this.score++; // this se current object ka score milega
}
createUser4.prototype.printMe = function(){
    console.log(`UserName : ${this.userName} , Price : ${this.score}`);
}
// const chai = createUser4("Chai",25) // new nhi use keya to undefined aajaega 
// const tea = createUser4("Tea",30) // function kee under prototype me additional property  aayi h but chai or tea ko btaya hi nhi or usme kuch bhi nhi hoga kyunki new nhi use keya h
const chai = new createUser4("Chai",25) // new use keya to naya object create hoga 
const tea = new createUser4("Tea",30) //

chai.printMe(); // Cannot read properties of undefined (reading 'printMe' ->TypeError: chai.printMe is not a function  new nhi use keya to ye function nhi bana

// Constructor Function + Prototype
/* function User(name, age) {
  this.name = name;
  this.age = age;
}

// method prototype me add kiya
User.prototype.getAge = function () {
  return this.age;
};

let u1 = new User("Aman", 22);
let u2 = new User("Riya", 25);

console.log(u1.getAge()); // 22
console.log(u2.getAge()); // 25
🔥 Fayda kya?
getAge() har object ke liye alag-alag nahi banta

Memory save hoti hai

Sab objects same method share karte hain

Agar Prototype na use karein?
function User(name, age) {
  this.name = name;
  this.age = age;

  this.getAge = function () {
    return this.age;
  };
}


❌ Har object ke liye naya function banega
✔️ Isliye prototype better hai

🔸 __proto__ kya hota hai?
u1.__proto__ === User.prototype // true


__proto__ → object ka prototype reference

prototype → constructor ka property

🔹 Class bhi Prototype hi use karti hai
class User {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  getAge() {
    return this.age;
  }
}


⚠️ Behind the scenes → prototype hi chal raha hai

🔹 Short Summary (Interview Ready ✅)

Prototype JS ka inheritance system hai

Objects methods prototype se access karte hain

Prototype → memory efficient

Class syntax → prototype ka sugar version
 */

let myName = "Anurag   ";
console.log(myName.length); // 9 -> ye string ke prototype me length property hoti h or ye behind the scene ek object hi h agar space ho to unhe bhi count krta h
// console.log(myName.trim().length);  // "Anurag" -> 6 trim() method string ke prototype me hota h jo string ke starting or ending ke space ko remove krta h
let myHeros = ["thor","spiderman","ironman"];
let heroPower = {
    thor : "hammer",
    spiderman : "web",
    ironman : "suit",
    getSpiderPower : function(){
        console.log(`Spidy power is ${this.spiderman}`);
    }
}
Object.prototype.Priyal = function(){ // ye sab object ke under chala jaega  inheritance ke through
    console.log("Priyal is present in all objects");
}
heroPower.Priyal(); // Priyal is present in all objects
myName.Priyal(); // Priyal is present in all objects
myHeros.Priyal(); // Priyal is present in all objects
Array.prototype.heyPriyal = function(){ // ye sab array ke under chala jaega  inheritance ke through
    console.log("Hey Priyal , how are you?");
} 
myHeros.Priyal(); // Priyal is present in all objects  
myHeros.heyPriyal(); // Hey Priyal , how are you? array ke under h to ye chala (acess h array ke prototype me )
// String.prototype.hello = function(){ // ye sab string ke under chala jaega  inheritance ke through
//     console.log("Hello Priyal , how are you?");
// }   
// myName.hello(); // Hello Priyal , how are you?
// heroPower.heyPriyal(); // Error: heroPower.heyPriyal is not a function iske pass heyPriyal method nhi h(acess nhi h) kyunki ye array ke prototype me h string ke prototype me nhi h or object ke prototype me nhi h
console.log('------------------------');
// Inherirtance -> ek object ke properties and method ko dusre object me use krna
const UserProfile = {
    name : "Anurag",    
    email : "Anurag@example.com"
}
const Teacher = {   
    makeVideos : true
}
const TeachingSupport = {
    isavailable : false
}
const TASupport = {
    makeAssignment : 'js assignment',
    fullTime : true,
    __proto__ : TeachingSupport // ye inheritance h
}
Teacher.__proto__ = UserProfile // ye inheritance h
// modern syntax
Object.setPrototypeOf(TeachingSupport,Teacher) // teaching support ke prototype me teacher ka sara data chala jaega
console.log(Teacher.name); // Anurag -> inheritance ke through chala jaega
console.log(TASupport.isavailable); // false -> inheritance ke through chala jaega
console.log('------------------------');

let  anotherUsername = "Anurag    ";
String.prototype.trueLength = function(){
    console.log(`${this}`); // Anurag     -> this se current string milegi
    // console.log(`${this.name}`); // undefined -> string me name property nhi hoti h
    console.log(`True length is : ${this.trim().length}`); // this se current string milegi
}
anotherUsername.trueLength(); // True length is : 6
"Priyal".trueLength(); // True length is : 6
"Soni   ".trueLength(); // True length is : 4
console.log('------------------------');    

