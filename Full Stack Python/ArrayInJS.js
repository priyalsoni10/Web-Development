/* Array in JavaaScript-> ek aisa data structure hai jo multiple values ko ek single variable me store karne ka tareeka deta hai.   
 JavaScript me Array ek collection (group) hota hai jisme hum multiple values ek hi variable me store kar sakte hain.
Jaise ek dabba jisme bahut saari cheezein number-wise rakhi hoti hain.
Array ko define karne ke liye square brackets [] ka use kiya jata hai, aur values ko comma (,) se separate kiya jata hai.
Array me hum kisi bhi type ki values store kar sakte hain, jaise numbers, strings, objects, aur even doosre arrays bhi.
Array me values ko access karne ke liye hum index ka use karte hain, joki 0 se start hota hai.  
Array ek ordered list hoti hai.
Isme values index number se store hoti hain, jisme index 0 se start hota hai.*/

// Array define karna
let fruits = ["Apple", "Mango", "Banana"];
// Array me values ko access karna
console.log(fruits[0]); // Output: Apple
console.log(fruits[1]); // Output: Mango
console.log(fruits[2]); // Output: Banana   
console.log("----------------------");
// Array me values ko change karna
fruits[1] = "Orange";   
console.log(fruits); // Output: ["Apple", "Orange", "Banana"]
console.log("----------------------"); 
// Array me nayi value add karna
fruits.push("Grapes");   
console.log(fruits); // Output: ["Apple", "Orange", "Banana", "Grapes"]
console.log("----------------------");  
// Array me se value remove karna
fruits.pop();   
console.log(fruits); // Output: ["Apple", "Orange", "Banana"]
console.log("----------------------");
// Array length
console.log("Number of fruits: " + fruits.length); // Output: Number of fruits: 3   
console.log("----------------------");
delete fruits[2]; // Banana ko delete kar diya([ 'Apple', 'Orange', <1 empty item> ]) delete se place to rah jati hai, value gayab ho jati hai.Isliye empty item aata hai.
console.log(fruits); // Output: ["Apple", "Orange"] 
console.log("----------------------");
let arr = [1,2,3];
arr.unshift(0); // array ke starting me 0 add kar diya
console.log(arr);//[ 0, 1, 2, 3 ]
arr.shift(); // array ke starting se 0 remove kar diya (first value ko deleta krta h shift())
console.log(arr);//[ 1, 2, 3 ] 
console.log("----------------------");
let arr1 = [10, 20, 30, 40];
arr1.splice(2, 1);  
// index 2 se 1 element delete (30 delete)
console.log(arr1); // [ 10, 20, 40 ]
arr1.splice(1, 0, 15);  // index 1,(0->deletecount) par koi element delete nahi karna, balki 15 add karna (splice(index, deleteCount, newValue),)
console.log(arr1); // [ 10, 15, 20, 40 ]
console.log("----------------------");
let part = arr1.slice(1, 3);  
console.log(part);  // [15,20]
console.log(arr1); // [ 10, 15, 20, 40 ] original array me koi change nahi hua
console.log("----------------------");
console.log(arr1.indexOf(20)); // output: 2 (20 ka index 2 hai)
console.log(arr1.indexOf(50)); // output: -1 (50 array me nahi hai)
console.log(arr.includes(50));  // false
console.log(arr1.includes(20)); // output: true  (20 array me hai ya nhi vo check krta h)
console.log(arr.reverse()); // [ 3, 2, 1 ] (array ko reverse kar diya)
let nums = [3, 1, 4, 2];
nums.sort();
// [1, 2, 3, 4]
console.log(nums);  // array ko ascending order me sort kar diya
let arr3 = ["Apple", "Mango", "Banana"];
console.log(arr3.join(" - ")); // // Apple - Mango - Banana (- separate karke string me convert kar diya)
console.log("----------------------");
let arr4 = [1, 2, 3];
let result4 = arr4.map(x => x * 2);
console.log(result4); // [2, 4, 6]
console.log("----------------------"); 
let arr5= [10, 20, 30, 40];
let newArr = arr5.filter(x => x !== 30); // 30 ko remove kar diya 
console.log(newArr);// [10, 20, 40]
console.log("----------------------");
//Spread Operator (...) ->  ye ek special syntax hai jo iterable (like array, string) ko individual elements me spread (phailane) karne ke liye use hota hai.
//Iska use hum tab karte hain jab hume ek array ke elements ko dusre array me ya function arguments me individually pass karna hota hai.
let arr6 = [10, 20, 30];
let copy = [...arr];
console.log(copy);// Output: [10, 20, 30]  ye ek shallow copy banata hai arr6 ka
console.log("----------------------");
// Slice Method se Shallow Copy banna 
let arr7 = [10, 20, 30];
let copy2 = arr.slice();// ye bhi ek shallow copy banata hai arr7 ka
console.log(copy2);// Output: [10, 20, 30]
console.log("----------------------");
// Array.from() Method se Shallow Copy banna
let arr8 = [10, 20, 30];
let copy3 = Array.from(arr8); // ye bhi ek shallow copy banata hai arr8 ka
console.log(copy3);// Output: [10, 20, 30]
console.log("----------------------");


/*Shallow Copy kya hoti hai?
Meaning:
Agar array me normal values (numbers, strings) ho to shallow copy sahi copy banati hai.
Lekin agar array ke andar objects ya arrays ho (nested structure), to inner values shared hoti hain.*/
let arr9 = [10, 20, {a: 5}];

let copy4 = [...arr9]; // shallow copy banayi arr9 ki

// inner object ko change karte hain
copy4[2].a = 99;

console.log(arr9);
console.log(copy4); // dono me change reflect hoga kyunki inner object shared hai Kyuki shallow copy sirf outer array copy karta hai, andar ka object same memory share karta hai.

console.log("----------------------");
/*Deep Copy kya hoti hai?
Meaning:
Deep copy me poori array ki new copy banती hai,
aur inner objects/arrays bhi alag memory me banते हैं.
Agar aap copy me change karo → original par effect nahi.
Iske liye hum JSON methods ka use kar sakte hain ya phir recursive function bana sakte hain.
*/
let arr10 = [10, 20, {a: 5}];
let deepCopy = JSON.parse(JSON.stringify(arr10));
deepCopy[2].a = 99;
console.log(arr10);// [ 10, 20, { a: 5 } ]
console.log(deepCopy); //[ 10, 20, { a: 99 } ] original array unaffected rahega kyunki deep copy me inner object bhi alag memory me ban gaya hai.

const myArray = new Array(67,95,44,34,33,20); // ek array banaya jisme 5 empty slots hain
console.log("Original Array:", myArray);
console.log("First Element:", myArray[0]); // Accessing first element
console.log("Length of Array:", myArray.length); // Length of the array
console.log("----------------------");
const myArray1 = myArray.join()// array ko string me convert kar diya
console.log(" myArray:",  myArray);
console.log("Type of myArray:", typeof myArray); // string
console.log("Array as String:", myArray1);
console.log("Type of " ,typeof myArray1); // string type ka ho gaya
console.log("----------------------");

myArr= [56 ,84 ,30 ,20 ,44,78,67,90,89,32,23,11];
console.log("Original myArr:", myArr);
const slicedArray = myArr.slice(1,6); // index 1 se 6 tak (6 excluded)  [ 84, 30, 20, 44, 78 ]
console.log("Sliced Array:", slicedArray);
console.log("Original myArr after slicing:", myArr); // original array unaffected rahega  [56, 84, 30, 20, 44,78, 67, 90, 89, 32, 23, 1]
const splicedArray = myArr.splice(1,6);// index 1 se 6 elements remove kar diye 
console.log("Spliced Array:", splicedArray); // removed elements  [ 84  , 30, 20, 44, 78, 67 ]
console.log("Original myArr after splicing:", myArr); // original array changed ho jayega [ 56, 90, 89, 32, 23, 11 ]
console.log("----------------------");

// Arraay Spread Operator
let myyArr = [1, 2, 3];
let copy0 = [...myyArr];
console.log("Original myyArr:", myyArr);    
console.log("Copied Array using Spread Operator:", copy0);
console.log("----------------------");
let a = [4, 5, 6];
let b = [7, 8, 9];
let c = [...a, ...b]; // a aur b ke elements ko spread karke c me combine kar diya
console.log("Combined Array using Spread Operator:", c);
console.log("----------------------");
let obj = {x: 10, y: 20};
let newObj = {...obj};
console.log("Original Object:", obj);
console.log("Copied Object using Spread Operator:", newObj);// newObj me obj ki copy ban gayi
console.log("----------------------");
// Function and Array dono ka use karke ek example

function sum1(a, b, c) {
  return a + b + c;
}
let nums1 = [1, 2, 3];

console.log(sum1(...nums)); // Output: 6  nums1 ke elements ko spread karke function me pass kar diya
console.log("----------------------");
const fruits1 = ["Apple", "Orange", "Banana"];
const moreFruits = ["Mango", "Pineapple", "Grapes"];
fruits1.push(moreFruits); //   
console.log(fruits1); // Output: [ 'Apple', 'Orange', 'Banana', [ 'Mango', 'Pineapple', 'Grapes' ] ]  moreFruits ek nested array ban gaya
console.log(fruits1[3][1]);// pineapple  
console.log("----------------------");
fruits1.concat(moreFruits); // fruits1 me moreFruits ko add kar diya
console.log(fruits1); // Output: [ 'Apple', 'Orange', 'Banana', [ 'Mango', 'Pineapple', 'Grapes' ] ]  original array unaffected rahega
console.log("----------------------");

a = [1, 2, 3];
b = [4, 5, 6];  
c = a.concat(b); // a aur b ko combine kar diya
console.log(c); // Output: [1, 2, 3] original array unaffected rahega
const another_array = [2,5,7,9,[11,13,15],17,[19,21],23 ,[25,27]];
const flatArray = another_array.flat(); // nested arrays ko flatten kar diya
console.log("Original Array:", another_array);
console.log("Flattened Array:", flatArray); // Output: [2, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27]
console.log("----------------------");
console.log(Array.from("Priyal")); // Output: ['P', 'r', 'i', 'y', 'a', 'l']  string ko array me convert kar diya
console.log(Array.from({name: "Priyal"})); // Output: []  kyunki object iterable nahi hai isliye empty array milega
console.log("----------------------");
let score1 = 100;
let score2 = 200;
let score3 = 300;
console.log(Array.of(score1, score2, score3)); // Output: [100, 200, 300]  individual values ko array me convert kar diya   













