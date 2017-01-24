function getJsonOfVacancies() {
    let xhr = new XMLHttpRequest();
    let url = "http://138.68.77.7:8000/api/vacancy/";
    xhr.open("GET", url, true);
    xhr.onreadystatechange = () => {
        if (xhr.readyState === 4) {
            let status = xhr.status;
            if (status >= 200 && status < 300 || status === 304) {
                let vacancies = JSON.parse(xhr.responseText); // returns string of JSON
                parseVacancies(vacancies);
            } else {
                console.log(xhr.status + ":" + xhr.statusText);
            }
        }
    };
    xhr.send(null);
}

//todo try to use jQuery Template plug in to parse vacancy with below method
/*dummy realisation*/
function parseVacancies(arrayOfVacancies) {
    let div = document.getElementById('vacancies');
    for (let i = 0; i < arrayOfVacancies.length; i++) {
        div.appendChild(document.createTextNode('Programming language: ' + arrayOfVacancies[i].programming_language));
        div.appendChild(document.createTextNode('city: ' + arrayOfVacancies[i].city));
        div.appendChild(document.createTextNode('name: ' + arrayOfVacancies[i].name));
        div.appendChild(document.createTextNode('url: ' + arrayOfVacancies[i].url));
        div.appendChild(document.createTextNode('company: ' + arrayOfVacancies[i].company));
        div.appendChild(document.createTextNode('description: ' + arrayOfVacancies[i].description));
    }
    let test = document.getElementById('button');
    test.style.color = 'red';
}
function renderHTML(vacancy) {
    let div = document.getElementById('vacancies');
    /*for (let property in vacancy) {
        /!*switch (vacancy[property]) {
            case ('programming_language'):
                let programmingLanguage = div.appendChild(document.createElement('p'));
                programmingLanguage.innerHTML = vacancy[property];
                break;
            case ('city'):
                let city = div.appendChild(document.createElement('p'));
                city.innerHTML = vacancy[property];
                break;
            case ('name'):
                let name = div.appendChild(document.createElement('p'));
                name.innerHTML = vacancy[property];
                break;
            case ('url'):
                let url = div.appendChild(document.createElement('p'));
                url.innerHTML = vacancy[property];
                break;
            case ('company'):
                let company = div.appendChild(document.createElement('p'));
                company.innerHTML = vacancy[property];
                break;
            case ('description'):
                let description = div.appendChild(document.createElement('p'));
                description.innerHTML = vacancy[property];
                break;
            default:
                throw new Error('There is no proper item in vacancy found');
        }*!/
    }*/
}
