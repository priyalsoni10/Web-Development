//API -> Application programming interface
//AJAX -> Asynchronous javascript and XML(XML replace to json -> AJAJ)
//JSON -> Javascript object Notation
//jSon ()-> return a second promise that resolves with the result of parsing the response body text as JSON(Input is json,outtput is js object)
// Api end point -> URL jaha se data fetch karna h
const apiEndPoint = "https://jsonplaceholder.typicode.com/posts";

// Select DOM elements
const getBtn = document.querySelector("#getPost");
const createBtn = document.querySelector("#createPost");
const updateBtn = document.querySelector("#updatePost");
const patchBtn = document.querySelector("#patchPost");
const deleteBtn = document.querySelector("#deletePost");

// get posts
const getPosts = async () => {
    try{
        const response = await fetch(apiEndPoint); // fetch(apiEndPoint , option ) -> option by default GET request hota h
        //         .then((response) =>{
        //            response.json().then(posts =>  console.log(posts));
        //         });
        if (response.status != 200) {
            throw new Error(`Failed to fetch posts with status Code: ${response.status}`);
        }
        const posts = await response.json();
        return posts;
} catch (error) {
    console.log("Error fetching posts:", error);
    // return [];

}
};

// create post
const createPost = async (newpost) => {
    try {
        const res = await fetch(apiEndPoint, {
                method: "POST",
                body: JSON.stringify(newpost),
                headers: {
                    "Content-Type": "application/json; charset = UTF-8"
                },
            })
            if (res.status != 201) {
                throw new Error(`Failed to create post with status Code: ${res.status}`);
            }
            const post = await res.json();
            return post;
    } catch (error) {
        console.log("Error creating post:", error);
        // return null;
    }
};

// update post
const updatePost = async (newpost, id) => {
    try {
        const res = await fetch(`${apiEndPoint}/${id}`, {
                method: "PUT",
                body: JSON.stringify(newpost),
                headers: {
                    "Content-Type": "application/json; charset = UTF-8"
                },
            });
            if (res.status != 200) {
                throw new Error(`Failed to update post with status Code: ${res.status}`);
            }
            const post = await res.json();
            return post;
    } catch (error) {
        console.log("Error updating post:", error);
        // return null;
    }
};

// patch post
const patchPost = async (newpost, id) => {
    try {
        const res = await fetch(`${apiEndPoint}/${id}`, {
                method: "PATCH",
                body: JSON.stringify(newpost),
                headers: {
                    "Content-Type": "application/json; charset = UTF-8"
                },
            });
            if (res.status != 200) {
                throw new Error(`Failed to update post with status Code: ${res.status}`);
            }
            const post = await res.json();
            return post;
    } catch (error) {
        console.log("Error updating post:", error);
        // return null;
    }};

// delete post
const deletePost = async (id) => {
    try {
        const res = await fetch(`${apiEndPoint}/${id}`, {
                method: "DELETE",
                
            });
            if (res.status != 200) {
                throw new Error(`Failed to update post with status Code: ${res.status}`);
            }
            const post = await res.json();
            return post;
    } catch (error) {
        console.log("Error updating post:", error);
        // return null;
    }};


getBtn.addEventListener("click", async () => {
    // alert("Get Posts");
    const postRes = await getPosts();
    // console.log(postRes);
    if(postRes){
    const table = `<table class="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Title</th>
      
    </tr>
  </thead>
  <tbody>
  ${postRes.map(post =>`<tr>
      <th scope="row">${post.id}</th>
      <td>${post.title}</td>
      
    </tr>` ).join("\n")   }
    
    
  </tbody>
</table>`;
    document.querySelector("#table").innerHTML = table;
  }
});

// Post
// create button
createBtn.addEventListener("click", async () => {
    // alert("Create Post");
    const newPost = {
        title: "New Post",
        body: "This is a new post",
        userId: 1
    };
    const createdPost = await createPost(newPost);
    console.log(createdPost);
});

updateBtn.addEventListener("click", async () => {
    // alert("Update Post");
    const newPost = {
        id:2,
        title: "Update Post",
        body: "This is a new post",
        userId: 1
    };
    const updatedPost = await updatePost(newPost,2);
    console.log(updatedPost);
});

//  PATCH 
patchBtn.addEventListener("click", async () => {
    // alert(" Patch Post");
    const newPost = {
        id:2,
        title: "Update Post",
        
    };
    const patchedPost = await patchPost(newPost,2);
    console.log(patchedPost);
});

// delete post
deleteBtn.addEventListener("click", async () => {
    // alert(" Delete Post");
    const deletedPost = await deletePost(2);
    console.log(deletedPost);
    console.log(" Post Deleted Successfully");
});



