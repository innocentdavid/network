function like(id) {
  // add 1 to totalLikes or remove 1 if already there
  // then updates totalLikes and totalDislikes in index
  let parent = document.getElementById(id);

  // dislike
  let dislike = parent.children[0].children[0].children[0];

  // like
  let like = parent.children[1].children[0].children[0];

  fetch('/vote', {
    method: 'POST',
    body: JSON.stringify({
      post_id: id
    })
  })
  .then(data => {
    console.log(data);
    // like.innerHTML = data.like
    // dislike.innerHTML = data.dislike
  });
}


function dislike(id) {
  alert(id);
}
// document.addEventListener('DOMContentLoaded', function () {

// }