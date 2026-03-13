let main = document.querySelector("main")

async function getData(topic = "India"){
    let res = await fetch(`https://newsapi.org/v2/everything?q=${topic}&sortBy=publishedAt&apiKey=babd0ada65644def98a918aa9cb4b7ba`);
    res = await res.json();
    display(res.articles);
}


function display(data){
   for(let i of data){
    main.innerHTML +=`
    <div class="newsCard">
            <img src=${i.urlToImage} alt="">
            <h2>${i.title} </h2>
            <p> ${i.description} </p>
            <a href = ${i.url} target="_blank" > <button> Read More </button> </a>
        </div> `
   }
}
getData()
