'use strict';

const e = React.createElement;

class LikeButton extends React.Component {
  constructor(props) {
    super(props);

    let liked = getLibraryProperty("liked");
    console.log("liked: ", liked);
    if(null == liked) {
       liked = false; // Ask api...
    } 
    if(liked == "true") {
       liked = true;
    } else {
       liked = false;
    }
    console.log("final state: ", liked);
    this.state = { liked: liked }; 
  }

  render() {
    
    if (this.state.liked) {
      const bookId = getLibraryProperty("bookid");
      const url = new URL(window.location.href);
      url.searchParams.set("liked", "true");
      url.searchParams.set("bookid", bookId);
      window.history.pushState({}, "", url.toString());
	
      return 'You liked book ' + getLibraryProperty("bookid"); // + JSON.stringify(this.props); // this.props.commentID;
    }

    return e(
      'button',
      { onClick: () => this.setState({ liked: true }) },
      'Like'
    );
  }
}

  // Find all DOM containers, and render Like buttons into them.
document.querySelectorAll('.like_button_container')
  .forEach(domContainer => {
    // Read the comment ID from a data-* attribute.
    const commentID = getLibraryProperty("bookid"); //"parseInt(domContainer.dataset.commentid, 10);"
    const root = ReactDOM.createRoot(domContainer);
    root.render(
      e(LikeButton, { commentID: commentID })
    );
  });




console.log("In do it");
// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal
//btn.onclick = function() {
	//modal.style.display = "block";
//}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
	modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
	if (event.target == modal) {
		modal.style.display = "none";
	}
}

function doit1 (myspan) {
	console.log(myspan);

	modal.style.display = "block";
}

const domContainer = document.querySelector('#like_button_container_div');
const root = ReactDOM.createRoot(domContainer);
root.render(e(LikeButton));

function getLibraryProperty(propKeyName) {
  const urlParams = new URLSearchParams(window.location.search);

  const value = urlParams.get(propKeyName);

  console.log(propKeyName + ": ", value);
  return value;
}

// All react renders take place at some point after this is executed.

