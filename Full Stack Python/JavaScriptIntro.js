/**Html : 1991-1993  ( Tim Berners-Lee in late 1991 and HTML 1.0 being released in 1993.
 * Css -1994-1996,1995 (CSS was first proposed by Håkon Wium Lie in 1994. The first official specification for CSS, known as CSS1, was published by the World Wide Web Consortium (W3C) in December 1996. Bert Bos also played a significant role in the development of CSS.)
 * JavaScript -1995 avaScript was invented in 1995 at Netscape by Brendan Eich. It was initially named Mocha, then LiveScript(1997), before being renamed JavaScript. It was released in September 1995. 1996 ,1999 me iska standard bnna start hua jise ECMAScript kaha gya.
 * Mocha-Netscape navigator -1995 // mocha sirf unhe ke browser pr chalti thi fir compiler alg alg bn gye jisse ye sb me chale 
 * ECMAScript -1997 (The first edition of ECMAScript was published in June 1997 by ECMA International as ECMA-262.)
 * JavaScript / ECMAScript​​ JavaScript was invented by Brendan Eich in 1995. It was developed for Netscape 2, and became the ECMA-262 standard in 1997
 * JavaScript Compiler -1996 V8-Engine (used in Chrome and Node.js)  (In 1996, Microsoft introduced JScript, a dialect of JavaScript, for its Internet Explorer browser.)
 *  PHP -1995
 * python -1991( Guido van Rossum created Python.Launch Date: Python was first released in 1991.)
 * Java -1995 (Java was developed by James Gosling and his team at Sun Microsystems. It was officially released in 1995 as a core component of Sun Microsystems' Java platform.)
 * FireFox js Compiler-SpiderMonkey 2002 (The Firefox web browser, developed by the Mozilla Foundation, was first released in November 2004. However, its JavaScript engine, known as SpiderMonkey, was created earlier and has been in use since the early versions of the Mozilla Application Suite, which dates back to 2002.)
 * Microsoft Edge-Chakra 2015 (Chakra is the JavaScript engine developed by Microsoft for its Edge browser. The first version of Microsoft Edge, which included the Chakra engine, was released in July 2015.)
 * 2010 me ek  naye compiler ki jarurat padi jo browser ke baahr backend ko chaal ske(browser ke under to backend hi chal skta h) isliye Node.js(JS Compiler) 2010 me aya jisme V8 engine ka use hua jo chrome me bhi use hota h.
 * 
 * */
// console.log(5+5); 
// // Variables in JavaScript
// var a =10;/* variable */ 
// let k =10;/* block scope variable (Integer variable) */
// let name="John";/* string variable  character yhi nhi hota h*/
// let isActive=true;/* boolean variable */    
// let score=99.5;/* float variable(but ye javascipt ki nagar se number he h) */
// let j=null;/* null variable  jisme koi value nhi h */
// let b=NaN; /* Not a number  jab hum kisi variable me number ki jagah string ya koi aur value daalte h to wo Nan ho jata h */
// let c=undefined;/* undefined variable  jisme koi value assign nhi ki gyi h */
// const PI=3.14;/* constant variable  hote h jo change nhi ho skte h ekbar lekhne ke baad*/

// // Naaming Conventions
// // 1. Variable names can contain letters, digits, underscores, and dollar signs.
// // 2. Variable names must begin with a letter, an underscore (_), or a dollar sign ($).
// // 3. Variable names are case-sensitive (myVar and myvar are different variables).
// // 4. Reserved words (like JavaScript keywords) cannot be used as variable names.
// // 5. Use camelCase for naming variables (e.g., myVariableName).
// // 6. Choose meaningful and descriptive names for better code readability.
// // let 1a=20; // Invalid: Cannot start with a digit
// // let var=25; // Invalid: 'var' is a reserved word
// //  let my-variable=30; // Invalid: Hyphens are not allowed(koe bhi special character ya space bech me nhi dal skte h)

// // Valid variable names
// let myVariableName = "Hello, World!";// camel case
// let a1=5;// starts with letter
// let _b=10;// underscore
// let $c=15;// dollar sign
// let my_age=12;// snake case

// console.log(5+"5");//55 (string concatenation)
// console.log(5 + + "2");//7 (unary plus operator converts string to number)
// console.log("5"+2-2);//50 (string concatenation first, then subtraction)
// console.log("10"-"4");//6 (string to number conversion during subtraction)
// console.log("10"*2);//20 (string to number conversion during multiplication)
// console.log("10"/2);//5 (string to number conversion during division)
// console.log("10"%3);//1 (string to number conversion during modulus)
// console.log("Hello"-"World");//NaN (not a number, invalid subtraction)
// console.log(true + true);//2 (true is treated as 1)
// console.log(true + false);//1 (true is 1, false is 0)
// console.log(false + false);//0 (both false are 0)

// Arithmetic Operators
// let x = 10;
// let y = 3;
// console.log(x + y); // Addition: 13
// console.log(x - y);// Subtraction: 7
// console.log(x * y);// Multiplication: 30
// console.log(x / y);// Division: 3.33333
// console.log(x % y);// Modulus: 1 (Remainder of 10 divided by 3)
// console.log(x ** y);// Exponentiation: 1000 (10 raised to the power of 3)   

//Comparision Operators
// let a = 5;
// let b = 6;
// console.log(a == b); // Equal to: false
// console.log(a != b); // Not equal to: true
// console.log(a > b); // Greater than: false
// console.log(a < b); // Less than: true
// console.log(a >= b); // Greater than or equal to: false
// console.log(a <= b); // Less than or equal to: true 
// console.log(a === b); // Strict equal to: false
// console.log(a !== b); // Strict not equal to: true
// Strict equality (===) checks both value and type
//console.log(5 === '5'); // false (different types)
// Loose equality (==) checks only value after type coercion
//Coercion ka simple meaning hota: “Automatically data type convert kar dena”
//console.log(5 == '5'); // true (string '5' is converted to number 5)
// Strict inequality (!==) checks both value and type
//console.log(5 !== '5'); // true (different types)
// Loose inequality (!=) checks only value after type coercion
// true → Agar value ya data type अलग हो
// false → Agar value aur type same ho
//console.log(5 != '5'); // false (string '5' is converted to number 5)
//console.log(5 !== "5")// true (different types)Ye tab TRUE deta है, agar:
//  Value alag हो
//  Type (data type) alag हो
// Dono me se ek bhi alag ho → Result = true
//(a<>b)// not equal to in sql (Standard SQL Not Equal Operator)
// d=10;
// e="20";
// console.log(d+ +e); // 30 (unary plus converts string to number and adds)  +e = "20" → 20 (number)
// // JavaScript me Unary Plus (+) operator kya karta hai? :String ko number me convert kar deta hai Agar string me number likha ho.
// e = "20";
// console.log(+e);//20 (string to number conversion using unary plus)

// //Operators Precedence
// let a="5";
// let b="2";
// let c= 3;
// // (a+b-c/a);// ("52"-0).6=51.4 (string concatenation first, then subtraction)
// console.timeLog(a+b-c/a);// 52-5/5=52-1=51.4 (string concatenation first, then subtraction and division)
// console.timeLog(+a + +b - c / +a);// 5 + 2 - 3 / 5 = 7 - 0.6 = 6.4 (unary plus converts strings to numbers before operations)
// console.log(c/a)//0.6 (3/5=0.6)
// console.log(5+2 > 4+2);//true (7 > 6)
// console.log(5+2 < 4+2);//false (7 < 6)
// let l=5;
// let m=true;
// console.log(l+m);//6 (true is treated as 1)

//Logical Operators
// let p = 5;
// let q = 10;
// let r = 12;
// console.log(p < q && q < r); // Logical AND: true (both conditions are true)
// console.log(p > q && q > r); // Logical AND: false (both conditions are false)
// console.log(p < q || q > r); // Logical OR: true (first condition is true)
// console.log(p > q || q > r); // Logical OR: false (both conditions are false)
// console.log(! (p < q)); // Logical NOT: false (negation of true)
// console.log(! (p > q)); // Logical NOT: true (negation of false)

// Assignment Operators
// let u = 5;// Assignment
// u += 3;// u = u + 3; (Addition assignment)
// u -= 2;// u = u - 2; (Subtraction assignment)
// u *= 4;// u = u * 4; (Multiplication assignment)
// u /= 2;// u = u / 2; (Division assignment)
// u %= 3;// u = u % 3; (Modulus assignment)
// console.log(u);
// let v = 5;
// v+=3;
// v*=3;
// v+=3; 
// console.log(v);//27
// let f=10;
// let c=f+100
// f+=100;
// console.log(c);//110 lekin f abhi bhi 10 h 
// console.log(f);// 110 ab f bhi 110 h

// Increment and Decrement Operators
// let s = 0;
// s++; // Increment by 1
// console.log(s);//1
// s--; // Decrement by 1
// console.log(s);//0
// ++s; // Pre-increment
// console.log(s);//1
// --s; // Pre-decrement
// console.log(s);//0
// s = s + 1; // Equivalent to s++
// console.log(s); //1
// s = s - 1; // Equivalent to s--
// console.log(s); //0 
// t =5;
// t = t++ +t - ++t/t;// t=5+6-7/7=5+6-1=10
// console.log(t);//10

// let a=4;
// // 4+6*7-7 = 4+42-7 = 39
// a=a++ + ++a * ++a - a++;
// console.log(a);
// let b=10;
// // 10-12+12*13=-2+156=154
// b=b++ - ++b + b*++b;
// console.log(b);
// let c=3;
// // 4+4*6/6=4+4*1=8
// c= ++c + c++ *++c/c++
// console.log(c)
// let d=6
// // 6*8-8/8 = 48-1=47 
// d=d++ *++d-d/d++;
// console.log(d);
// let e=2;
// // 3*3+5-5=9-0=9
// e= ++e * e++ + ++e - e++;
// console.log(e);

//Flow Control
// Decision Making
let age = 3;
if(age>=18){
     console.log("Yes, You can drive");
     }
else{
      console.log("No, You cannot drive");
}     
console.log("Bye");  
 
let a=3
let b=5
if(a>b){
    console.log("A is greater!")
}
else{
    console.log("B is greater!")
}

let a1=5;
if(a1%2==0){
    console.log("Even");
}

else{
    console.log("Odd");
} 
// Check if a2 is divisible by 2 and 5 both or not
a2 = 40
if(a2 % 2==0 && a2 % 5==0){
    console.log("a2 is divisible by both")
}
else{
    console.log("a2 is not divisible by both")
}
a2 = 5;
if(a2 % 2==0 || a2 % 5==0){
    console.log("a2 is divisible ");
}
else{
    console.log("a2 is not divisible ");
}

let marks=34;
if(marks>=35){
    console.log("Pass")
}
else{
    console.log("Fail")
}
let mark=68;
if(mark>=90){
    console.log("Grade is A");
}
else if(mark>=80){
    console.log("Grade is B");
}
else if(mark>=70){
    console.log("Grade is C");
}
else if(mark>=60){
    console.log("Grade is D")
}
else{
    console.log("Fail")
}

let a3 = 3;
if(a % 2==0 || a % 3==0){
   console.log("Yes by 2 or 3"); // or tb use keya jaata h jb kaam ek hi ho
}

let a4 = 9;
if(a % 2==0 ){
   console.log("Yes by 2"); // or tb use keya jaata h jb kaam ek hi ho
}
else if(a % 3==0){
   console.log("Yeeee 3 se ho gya ") // msg alag h tb else if ka use hota h
}

let a5 = 24;
if(a5%4==0){
    console.log("Yes by 4")
}
else{
    console.log("No by 4")
}
if(a5 % 3==0){
   console.log("Yes by 3")
}
else{
    console.log("No by 3")
}

let Age1 = 63;
if(Age1>=18){
    console.log("You can Drive")
} 
else{
    console.log("No you cannot drive")
}
if(Age1>60){
    console.log("Drive Carefully")
}

let Age = 63;
if(Age>=18){
    console.log("You can Drive")
    if(Age>60){
        console.log("Drive Carefully")
    }
} 
else{
    console.log("No you cannot drive")
}
// Loop
let b3 = 1;
//while loop
while(b3<10){
    console.log("Hello",b3)
    b3++;
}
console.log("Bye")

let b4 = 10; //Start
while(b4>=1){   //end
    console.log(b4);
    b4--; //Gap
}
console.log("Bye")

let b5 = 10; //Start
while(b5 >= 1){   //end
    console.log(b5);
    b5-=2; //Gap
}
console.log("Bye")

//  for loop
for(let b6 = 1;b6<=10; b6++){
    console.log(b6)
}
console.log("Bye")

a7=0
for(a7;a7<10; ){
    console.log(a7)
    a7++;
}
console.log("Bye")

let a8=8;
for(let i=1;i<=10;i++){
    console.log(a8,"x", i,"=",a8*i)

}
let a9 = 7;
let b9 = 55;
for(let i = a9 ; i<=b9;i++){
    if(i%3==0){
        console.log(i)
    }
}
let count =0;
for(let i =1;i<=5 ;i++){
    count++;
}
console.log("Loop count is:",count)

let count1 =0;
for(let i =1;i<=50 ;i++){
    if(i % 3 == 0)
       count1++;
}
console.log("Count number between 1 to 50 which is divisible by 3 is:",count1)

let count2 =0;
for(let i =1;i<=50 ;i++){
    if(i % 3 != 0)
       count2++;
}
console.log("Count number between 1 to 50 which is divisible not by 3 is:",count2)

let sum = 0;
for(let i=1;i<=5;i++){
    sum+=i;
}
console.log("Sum of number between 1 to 5:",sum)

let sum1 = 0;
for(let i=1;i<=50;i++){
    if(i % 7==0){
         sum1+=i;
    }
}
console.log("Sum of number between 1 to 50 which is divisible by 7:",sum1)

let start =1;
let end = 100;
let evenCount = 0;
let oddCount = 0;
for(let i=start;i<=end;i++){
    
    if(i % 2==0){
     evenCount++;
   
    }
   else{
    oddCount++
   }
   
  

}
console.log("Count of even number between to 100 is:",evenCount );
console.log("Count of odd number between to 100 is:",oddCount );

let n = 45;
sum3 =0;
count4=0
for(let i=2;i<n;i++){
    if(n%i==0){
        console.log("Factor of 45 is : ",i)
        count4+=1;
        sum3+=i;
    
}    
}
console.log(`Sum of factor of 45 is:${sum3}`); // (``) -> backticks
console.log(`Count of factor of 45 is:${count4}`); // (``) -> backticks

let a10 = 10;
let b10 = 3;

let result = parseInt(a10 / b10);
console.log(result); // 3

let a11 = 13;
let b11 = 3;

let result1 = (a / b) | 0; //Bitwise operator (fast but only 32-bit numbers)
console.log(result); // 3

let a12 = 19;
let b12 = 3;

let result2 = Math.trunc(a12 / b12); //Math.trunc() (decimal part remove kar deta hai)
console.log(result2); // 3

let a13 = 101;
let b13 = 3;

let result3 = Math.floor(a13 / b13); // Math.floor() (positive numbers ke liye best)
console.log(result3); // 3

//Maximum factor of 45
let n1 = 45;
max = 0;
for(let i=2;i<n;i++){
    if(n%i==0){
        max=i;
        
}  
     
}
console.log("Maximum factor of 45 is:",max)

// Common factor of two number
let p = 45;
let q = 135;
for(let i=2 ; i<q ;i++){
    if(p%i==0 && q%i==0)
        console.log("Common factor of p and q is : ",i)
}
console.log("Bye")
let p1 = 45;
let q2 = 135;

let limit = Math.min(p1, q2);

for (let i = 2; i <= limit; i++) {
    if(p1 % i == 0 && q2 % i == 0) {
        console.log("Common factor of p1 and q1 is:", i);
    }
}
// Minimum of factor of 45
let n2 = 45;
let min =0;
for(let i=2 ; i<n;i++){
    if(n%i== 0){
        min = i
        break
        
    }

}
console.log(`Minimum factor of 45 is:${min} `) 

// Minimum of factor of 45
let n3 = 45;
let max1 = 0;
for(let i=2 ; i < n;i++){
    if(n%i== 0){
        max1 = i
        
        
    }

}
console.log(`Maximum factor of 45 is:${max} `) 


let n4=45;
for(let i = n-1;i>=2;i--){
    if(n%i==0){
        console.log(i)
        break
    }
}

let m5=12;
let n5=24;
let min2=m5;
let gcd = 1;
if(n5<m5){
    min2 = n5;
}

for(let i=2;i<min2;i++){
    if(n5 % i==0 && m5 % i==0){
        gcd = i;
        console.log(` Common Factor of ${m5} and ${n5} is:${i}`);

    }
}
console.log(gcd)

let k = 345;
let count3 = 0;
while(k > 0){
    k = parseInt(k /10);
    count3++;
    
}
console.log("Count of digit is:",count3);


let j = 345;
let sum6 = 0; // 5,5+4=9,9+3 =12
while( j > 0){
    let rem = j % 10;//5,4,3
    sum6 += rem  ;
    j = parseInt(j /10);//34,,0
    
    
}
console.log(sum6);

let l = 345;
let s = 0;
while(l > 0){
    let r = l % 10;
    s = s * 10 + r;
    l = parseInt(l / 10);
}
console.log(s);
    

// Armstrong numbers
let num = 153;
let temp = num;
let sm = 0;

while (temp > 0) {
    let rem = temp % 10; // 3,5,1
    sm = sm + (rem * rem * rem);//(0+3*3*3=27)(27+5*5*5=152)(27+152+1*1*1=153)
    temp = parseInt(temp / 10);// 15,1
}
//Strong number
let u = 145;
let v = u;
let Sum = 0;

while (v > 0) {

    // last digit nikalna
    let r = v % 10;     // Example: 145 % 10 = 5 ,14%10 =4 ,1%10 =1

    // factorial of digit nikalna
    let f = 1;
    for (let i = 1; i <= r; i++) {
        f = f * i;         // Example: 1*2*3*4*5 = 120,1*2*3*4 =24, Factorial of 1 = 1
    }

    // factorial ko sum me add karna
    Sum = Sum + f;         // Example: sum = 0 + 120 = 120,sum = 120 + 24 = 144,144+1 =145

    // last digit ko remove karna
    v = parseInt(v / 10);   // Example: 145/10 = 14 ,14/10 =1
}

console.log("Sum of factorial = ", Sum);

// let n = 145;
// let temp = n;   // temp = 145
// let sum = 0;

// while (temp > 0) {

//     let r = temp % 10;  
//     // 1st loop: r = 145 % 10 = 5

//     let f = 1;
//     for (let i = 1; i <= r; i++) {
//         f = f * i;  
//         // 5 ka factorial:
//         // i=1 → f=1
//         // i=2 → f=2
//         // i=3 → f=6
//         // i=4 → f=24
//         // i=5 → f=120
//     }

//     sum = sum + f;
//     // sum = 0 + 120 = 120

//     temp = parseInt(temp / 10);
//     // temp = 145 / 10 = 14
// }

// // Next loop:
// // r = 14 % 10 = 4
// // factorial(4) = 24
// // sum = 120 + 24 = 144
// // temp = 14/10 = 1

// // Next loop:
// // r = 1 % 10 = 1
// // factorial(1) = 1
// // sum = 144 + 1 = 145
// // temp = 1/10 = 0 → loop stop

// console.log("Sum of factorial = ", sum);  // 145



























                                                                                                                                                                                                                                                          