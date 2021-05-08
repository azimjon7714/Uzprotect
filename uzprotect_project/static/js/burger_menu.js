menu.onclick = function myFunction(){
    var burger = document.getElementById('myTopnav');

    if (burger.classList = 'topnav'){
        burger.classList = ' responsive';
    } else {
        burger.className = 'topnav';
    }
    this.onclick = function close(){
        if (burger.classList = 'responsive'){
            burger.classList = ' topnav';
        } 
    }
}