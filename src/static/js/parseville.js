;
/* ==============    Vacancies Parser ==================*/
/* -- a chance to cut descriptions -- */
String.prototype.trunc = String.prototype.trunc ||
    function(n){
        return (this.length > n) ? this.substr(0,n-1)+'&hellip;' : this;
    };

function getJsonOfVacancies() {
    let xhr = new XMLHttpRequest(),
        url = "http://138.68.77.7:8000/api/vacancy/";
    xhr.open("GET", url, true);
    xhr.onreadystatechange = function () {
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
        renderVacancyHTML(arrayOfVacancies[i]);
    }
}
//todo try to use jQuery Template plug in to parse vacancy with below method
function renderVacancyHTML(vacancy) {
    var div = document.getElementById('vacancies'),
        divVacancy = document.createElement('div'),
        divider = document.createElement('hr');
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
                description.innerHTML = "Description: " + vacancy[property].trunc(120);
                break;
            default:
                throw new Error('There is no proper item in vacancy found');
        }
        divVacancy.appendChild(divider);
    }
}
/* ==============  END OF   ---- >   Vacancies Parser ==================*/

/* ==============    Companies  Parser    ==================*/
function getJsonOfCompanies() {
    let xhr = new XMLHttpRequest(),
        url = "http://138.68.77.7:8000/api/company/";
    xhr.open("GET", url, true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            let status = xhr.status;
            if (status >= 200 && status < 300 || status === 304) {
                let companies = JSON.parse(xhr.responseText); // returns string of JSON
                parseCompanies(companies);
            } else {
                console.log(xhr.status + ":" + xhr.statusText);
            }
        }
    };
    xhr.send(null);
}
function parseCompanies(arrayOfCompanies) {
    for (let i = 0; i < arrayOfCompanies.length; i++) {
        renderCompanyHTML(arrayOfCompanies[i]);
    }

}
function renderCompanyHTML(company) {
    let div = document.getElementById('companies'),
        divCompany = document.createElement('div'),
        divider = document.createElement('hr');
    divCompany.className = 'company';
    div.appendChild(divCompany);
    for (let property in company) {
        switch (property) {
            case ('logo'):
                let logo = divCompany.appendChild(document.createElement('img'));
                logo.className = 'company-logo company-param';
                logo.src = "http://138.68.77.7:8000" + company[property];
                logo.style.float = 'right';
                break;
            case ('name'):
                let name = divCompany.appendChild(document.createElement('p'));
                name.className = 'company-name company-param';
                name.innerHTML = "Name: " + company[property];
                break;
            case ('office'):
                let office = divCompany.appendChild(document.createElement('p'));
                office.className = 'company-office company-param';
                office.innerHTML = "Office: " + company[property];
                break;
            case ('country'):
                let country = divCompany.appendChild(document.createElement('p'));
                country.className = 'company-country company-param';
                country.innerHTML = "Country: " + company[property];
                break;
            case ('site_url'):
                let site_url = divCompany.appendChild(document.createElement('p'));
                site_url.className = 'company-url company-param';
                site_url.innerHTML = "Url: " + company[property];
                break;
            case ('description'):
                let description = divCompany.appendChild(document.createElement('p'));
                description.className = 'company-description company-param';
                description.innerHTML = "Description: " + company[property].trunc(100);
                break;
            default:
                throw new Error('There is no proper item in Company found');
        }
        divCompany.appendChild(divider);
    }
}
/* ==============  END OF --->   Companies  Parser ==================*/

/* ---------   jQuery Testing    --------------*/
