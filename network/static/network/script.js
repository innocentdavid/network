function follow(pUser) {
  fetch('/follow', {
    method: 'POST',
    body: JSON.stringify({
      action: 'follow',
      pUser: pUser
    })
  })
  .then(response => response.json())
  .then(response => {
    // console.log(response);
    if (response.message == 'success') {
      location.reload();
    } else {
      alert('something went wrong');
    }
  });
}
function unfollow(pUser) {
  fetch('/follow',
    {
      method: 'POST',
      body: JSON.stringify({
        action: 'unfollow',
        pUser: pUser
      })
    })
  .then(response => response.json())
  .then(response => {
    // console.log(response);
    if (response.message == 'success') {
      location.reload();
    } else {
      alert('something went wrong');
    }
  });
}

function like(id) {
  let parent = document.getElementById(id);

  // dislike
  let dislike = parent.children[0].children[0].children[0];

  // like
  let like = parent.children[1].children[0].children[0];

  fetch('/vote',
    {
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

  fetch('/vote',
    {
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
  fetch(`/get_post/${id}`)
  .then(response => response.json())
  .then(response => {
    // console.log(response);
    document.querySelector('#post_id').value = id;
    document.querySelector('#edit_post').value = response.body;
    document.querySelector('.edit-cont').style.display = 'block';
  })

  document.getElementById('edit-post-form').addEventListener('submit',
    function (e) {
      e.preventDefault();
      let id = document.querySelector('#post_id').value;
      let edited_post = document.querySelector('#edit_post').value;
      fetch('/update_post', {
        method: 'POST',
        body: JSON.stringify({
          post_id: id,
          edited_post: edited_post
        })
      })
      .then(response => response.json())
      .then(response => {
        // console.log(response);
        location.reload();
      });
    })
}


function closeEditPost() {
  document.querySelector('.edit-cont').style.display = 'none';
  document.querySelector('#edit_post').value = '';
}


window.addEventListener('DOMContentLoaded', () => {
  current_page();
})
function current_page() {
  let current_page = parseInt(document.getElementById('current_page').value) + 1;
  document.querySelector('.pagination').children[current_page].classList.add('active');
}

function pNext(current_page) {
  let pNext = parseInt(current_page)+1;
  window.location = '/page/'+pNext;
}
function pPrev(current_page) {
  let pPrev = parseInt(current_page)-1;
  window.location = '/page/'+pPrev;
}


function pNextF(current_page) {
  let pNext = parseInt(current_page)+1;
  window.location = '/following/page/'+pNext;
}
function pPrevF(current_page) {
  let pPrev = parseInt(current_page)-1;
  window.location = '/following/page/'+pPrev;
}


function pNextP(current_page) {
  var loginUser = document.querySelector('#loginUser').value;
  let pNext = parseInt(current_page)+1;
  window.location = '/profile/'+loginUser+'/'+pNext;
}
function pPrevP(current_page) {
  var loginUser = document.querySelector('#loginUser').value;
  let pPrev = parseInt(current_page)-1;
  window.location = '/profile/'+loginUser+'/'+pPrev;
}