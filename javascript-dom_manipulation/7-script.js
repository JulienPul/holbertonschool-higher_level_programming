fectch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then (response => response.json())
    .then (data => {
        document.querySelector('#list_movies').testContent = data.title;
    }
    .catch(error => {
        console.error('error:', error);
    });