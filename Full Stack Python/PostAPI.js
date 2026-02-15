const createTodo = async (todo) => {
let options = {
    method:"POST",
    headers:{
        "Content-Type":"application/json"
    },
    // body:JSON.stringify({  /**' JSON.stringify() -> converts a JavaScript object or value to a JSON string'**/
    //     title:"Post API",
    //     body:"This is post api",
    //     userId:100
    // })
    body:JSON.stringify(todo)

}
let p = await fetch('https://jsonplaceholder.typicode.com/posts',options) // fetch promise return karta h
        let response = await p.json();
        return response;

}
 

const getTodo = async (id) =>{
    let response = await fetch('https://jsonplaceholder.typicode.com/posts/'+id);
    let  r = await response.json();
      return r;
}


const mainFunc = async()=>{
    let todo = {
    title:"Post API",
    body:"This is post api",
    userId:100
}
    let todoRes = await createTodo(todo);
    console.log(todoRes);
    console.log(await getTodo(5));
}

mainFunc(); 
        

// json.stringify() -> converts a JavaScript object or value to a JSON string
//  json.parse() -> converts a JSON string into a JavaScript object



