let Vacancy = () => {
};

Vacancy.prototype.createFromData = (data) => {
    let object = new Vacancy;
    object.id = data.id;
    object.name = data.name;
    object.description = data.description;
    object.pub_date = data.pub_date;
    object.company_name = data.company_name;
    object.p_language = data.p_language;
    addVacancyElement(object);
    return object;
};

let Company = () => {
};

Company.prototype.addToHtml = () => {
};

Company.prototype.createFromData = (data) => {
    let object = new Company;
    object.id = data.id;
    object.name = data.name;
    object.description = data.description;
    object.logo = data.logo;
    object.site_url = data.site_url;
    addCompanyElement(object);
    return object;
};

let Link = () => {
};

Link.prototype.createFromData = (data) => {
    let object = new Link;
    object.id = data.id;
    object.name = data.name;
    object.description = data.description;
    object.url = data.url;
    addLinkElement(object);
    return object;
};

Link.prototype.addToHtml = () => {
};

let links = [],
    vacancies = [],
    companies = [];

function getJsonOfVacancies() {
    let xhr = new XMLHttpRequest(),
        url = "http://138.68.77.7:8000/api/vacancy/";
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

function addVacancyElement(obj) {
    // создаем новый элемент div
    // и добавляем в него немного контента
    let newDiv = document.createElement("div");
    newDiv.setAttribute("class", "col-xs-4");
    newDiv.setAttribute("onclick", "show_more('vacancy', this.id)");
    newDiv.setAttribute("style", "cursor: pointer");
    newDiv.setAttribute("id", "vacancy-" + obj.id);
    newDiv.innerHTML = '<div class="title-box"><h4>' + obj.name + '</h4></div><div class="entry-container "><div class="entry-content"><p>' + obj.description.substr(0, 200) + '...</p></div></div></div>';
    // добавляем только что созданый элемент в дерево DOM
    document.getElementById("vacancy-block").appendChild(newDiv);
}

function addLinkElement(obj) {
    // создаем новый элемент div
    // и добавляем в него немного контента
    let newDiv = document.createElement("div");
    newDiv.setAttribute("class", "col-xs-12");
    newDiv.setAttribute("id", "link-" + obj.id);
    newDiv.innerHTML = '<div class="usefull-link"><a href="' + obj.url + '"><p>' + obj.name + '</p></a><h6>' + obj.description.substr(0, 200) + '...</h6></div>';
    // добавляем только что созданый элемент в дерево DOM
    document.getElementById("link-block").appendChild(newDiv);
}

function addCompanyElement(obj) {
    // создаем новый элемент div
    // и добавляем в него немного контента
    let newDiv = document.createElement("div");
    newDiv.setAttribute("class", "col-xs-4");
    newDiv.setAttribute("onclick", "show_more('company', this.id)");
    newDiv.setAttribute("style", "cursor: pointer");
    newDiv.setAttribute("id", "company-" + obj.id);
    newDiv.innerHTML = '<div class="title-box"><h4>' + obj.name + '</h4></div><div class="entry-logo"><img src="' + obj.logo + '"></div><div class="entry-content">' + obj.description.substr(0, 200) + '...</div></div>';
    // добавляем только что созданый элемент в дерево DOM
    document.getElementById("company-block").appendChild(newDiv);
}

function show_more(type_api, id) {
    if (type_api == "vacancy") {
        for (let vacancy in vacancies) {
            if (vacancies[vacancy].id == id.split('-')[1]) {
                showVacancyElement(vacancies[vacancy])
            }
        }
    }
    if (type_api == "company") {
        for (let company in companies) {
            if (companies[company].id == id.split('-')[1]) {
                showCompanyElement(companies[company]);
            }
        }
    }
}

function showCompanyElement(obj) {
    // создаем новый элемент div
    // и добавляем в него немного контента
    let newDiv = document.createElement("div");
    newDiv.setAttribute("class", "col-xs-4");
    newDiv.innerHTML = '<div class="title-box"><h4>' + obj.name + '</h4></div>' +
        '<div class="entry-image"><img src="/' + obj.logo + '"></div>' +
        '<div class="entry-content">' + obj.description + '</div>';
    // добавляем только что созданый элемент в дерево DOM
    document.getElementById("full-view").innerHTML = newDiv.innerHTML;
}

function showVacancyElement(obj) {
    // создаем новый элемент div
    // и добавляем в него немного контента
    let newDiv = document.createElement("div");
    newDiv.setAttribute("class", "col-xs-4");
    newDiv.innerHTML = '<div class="title-box"><h4>' + obj.name + '</h4></div>' +
        '<div><p>' + obj.company_name + '</p></div>' +
        '<div class="entry-content">' + obj.description + '</div>';
    // добавляем только что созданый элемент в дерево DOM
    document.getElementById("full-view").innerHTML = newDiv.innerHTML;
}

