

function like(id) {
  let parent = document.getElementById(id);

  // dislike
  let dislike = parent.children[0].children[0].children[0];

  // like
  let like = parent.children[1].children[0].children[0];

  fetch('/vote', {
    method: 'POST',
    body: JSON.stringify({
      action: 'like',
      post_id: id
    })
  })
    .then(response => response.json())
    .then(response => {
      like.innerHTML = response.totalLikes;
      dislike.innerHTML = response.totalDislikes
    });
}


function dislike(id) {
  let parent = document.getElementById(id);

  // dislike
  let dislike = parent.children[0].children[0].children[0];

  // like
  let like = parent.children[1].children[0].children[0];

  fetch('/vote', {
    method: 'POST',
    body: JSON.stringify({                
      action: 'dislike',
      post_id: id
    })
  })
    .then(response => response.json())
    .then(response => {
      like.innerHTML = response.totalLikes;
      dislike.innerHTML = response.totalDislikes
    });
}

function editPost(id) {
  fetch('/edit_post/'+id)
    .then(response => response.json())
    .then(response => {
      console.log(response);
      document.querySelector('#post_id').value=id;
      document.querySelector('#edit_post').value=response.body;
      document.querySelector('.edit-cont').style.display='block';
    })

    document.getElementById('edit-post-form').addEventListener('submit', function (e) {
      e.preventDefault();
      let id = document.querySelector('#post_id').value;
      let edited_post = document.querySelector('#edit_post').value;
      fetch('/edit_post', {
        method: 'POST',
        body: JSON.stringify({                
          id: id,
          edited_post: edited_post
        })
      })
        .then(response => response.json())
        .then(response => {
          document.querySelector('#post_body').innerHTML=response.body;
          document.querySelector('.edit-cont').style.display='none';
        });
    })
}


function closeEditPost() {
  document.querySelector('.edit-cont').style.display='none';
  document.querySelector('#edit_post').value='';
}
