

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