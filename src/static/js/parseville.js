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
function parseVacancies(arrayOfVacancies) {
    for (let i = 0; i < arrayOfVacancies.length; i++) {
        renderHTML(arrayOfVacancies[i]);
    }
}
//todo try to use jQuery Template plug in to parse vacancy with below method
function renderHTML(vacancy) {
    let div = document.getElementById('vacancies'),
        divVacancy = document.createElement('div');
    divVacancy.className = 'vacancy';
    div.appendChild(divVacancy);
    for (let property in vacancy) {
        switch (property) {
            case ('programming_language'):
                let programmingLanguage = divVacancy.appendChild(document.createElement('p'));
                programmingLanguage.className = 'vacancy-prog-lang';
                programmingLanguage.innerHTML = "Programming language: " + vacancy[property];
                break;
            case ('city'):
                let city = divVacancy.appendChild(document.createElement('p'));
                city.className = 'vacancy-city';
                city.innerHTML = "City: " + vacancy[property];
                break;
            case ('name'):
                let name = divVacancy.appendChild(document.createElement('p'));
                name.className = 'vacancy-name';
                name.innerHTML = "Name: " + vacancy[property];
                break;
            case ('url'):
                let url = divVacancy.appendChild(document.createElement('p'));
                url.className = 'vacancy-url';
                url.innerHTML = "Url: " + vacancy[property];
                break;
            case ('company'):
                let company = divVacancy.appendChild(document.createElement('p'));
                company.className = 'vacancy-company';
                company.innerHTML = "Company: " + vacancy[property];
                break;
            case ('description'):
                let description = divVacancy.appendChild(document.createElement('p'));
                description.className = 'vacancy-description';
                description.innerHTML = "Description: " + vacancy[property];
                break;
            default:
                throw new Error('There is no proper item in vacancy found');
        }
    }
}
