var xhr = new XMLHttpRequest();

xhr.open('POST', 'https://httpbin.org/post');
xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');

xhr.send( 'name=taro&age=30' );

xhr.onreadystatechange = function() {
 
    if(xhr.readyState === 4 && xhr.status === 200) {
 
        console.log( xhr.responseText );
      
    }
}