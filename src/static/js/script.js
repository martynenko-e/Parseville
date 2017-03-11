;

var globalLinks = [],
    globalVacancies = [],
    globalCompanies = [],
    counter = 1;

var Vacancy = function () {
};

Vacancy.prototype.createFromData = function (data) {
    var object = new Vacancy;
    object.id = data.id;
    object.name = data.name;
    object.description = data.description;
    object.pub_date = data.pub_date;
    object.company_name = data.company_name;
    object.p_language = data.p_language;
    addVacancyElement(object);
    return object;
};

var Company = function () {
};

Company.prototype.addToHtml = function () {
};

Company.prototype.createFromData = function (data) {
    var object = new Company;
    object.id = data.id;
    object.name = data.name;
    object.description = data.description;
    object.logo = data.logo;
    object.site_url = data.site_url;
    addCompanyElement(object);
    return object;
};

var Link = function () {
};

Link.prototype.createFromData = function (data) {
    var object = new Link;
    object.id = data.id;
    object.name = data.name;
    object.description = data.description;
    object.url = data.url;
    addLinkElement(object);
    return object;
};

Link.prototype.addToHtml = function () {
};


/*function getJsonOfVacancies() {
 var xhr = new XMLHttpRequest(),
 url = "http://138.68.77.7:8000/api/vacancy/";
 xhr.open("GET", url, true);
 xhr.onreadystatechange = function () {
 if (xhr.readyState === 4) {
 let status = xhr.status;
 if (status >= 200 && status < 300 || status === 304) {
 let globalVacancies = JSON.parse(xhr.responseText); // returns string of JSON
 parseVacancies(globalVacancies);
 } else {
 console.log(xhr.status + ":" + xhr.statusText);
 }
 }
 };
 xhr.send(null);
 }*/

function addVacancyElement(obj) {
    // create general div for Vacancy Entity
    var vacancyDiv = document.createElement("div");
    vacancyDiv.setAttribute("class", "vacancy col-xs-4");
    vacancyDiv.setAttribute("onclick", "show_more('vacancy', this.id)");
    vacancyDiv.setAttribute("id", "vacancy-" + obj.id);

    //create div for vacancy Title
    var vacancyTitleDiv = document.createElement("div");
    vacancyTitleDiv.setAttribute("class", "title-box");
    //create h4 for vacancy Title
    //todo parser inserts h4 already, so do we need to create this element?
    var vacancyTitleDivH = document.createElement("h4");
    vacancyTitleDivH.setAttribute("class", "title-box-name");
    vacancyTitleDivH.innerHTML = obj.name;
    //create div for vacancy Container
    var vacancyContainerDiv = document.createElement("div");
    vacancyContainerDiv.setAttribute("class", "entry-container");
    //create div for vacancy Description
    var vacancyDescDiv = document.createElement("div");
    vacancyDescDiv.setAttribute("class", "entry-content");
    vacancyDescDiv.innerHTML = obj.description.substr(0, 200) + "...";

    vacancyTitleDiv.appendChild(vacancyTitleDivH);
    vacancyContainerDiv.appendChild(vacancyDescDiv);

    vacancyDiv.appendChild(vacancyTitleDiv);
    vacancyDiv.appendChild(vacancyContainerDiv);
    /* vacancyDiv.innerHTML = '<div class="title-box"><h4>' + obj.name + '</h4></div>' +
     '<div class="entry-container "><div class="entry-content"><p>' + obj.description.substr(0, 200) + '...</p></div></div></div>';*/
    // добавляем только что созданый элемент в дерево DOM
    document.getElementById("vacancy-block").appendChild(vacancyDiv);
}

function addLinkElement(obj) {
    // создаем новый элемент div
    // и добавляем в него немного контента
    // create general div for Link Entity
    var linkDiv = document.createElement("div");
    linkDiv.setAttribute("class", "col-xs-12");
    linkDiv.setAttribute("id", "link-" + obj.id);
    linkDiv.innerHTML = '<div class="usefull-link"><a href="' + obj.url + '"><p>' + obj.name + '</p></a><h6>' + obj.description.substr(0, 200) + '...</h6></div>';
    // добавляем только что созданый элемент в дерево DOM
    document.getElementById("link-block").appendChild(linkDiv);
}

function addCompanyElement(obj) {
    // create general div for Company Entity
    var companyDiv = document.createElement("div");
    companyDiv.setAttribute("class", "company col-xs-4");
    companyDiv.setAttribute("onclick", "show_more('company', this.id)");
    companyDiv.setAttribute("id", "company-" + obj.id);
    //todo swap desciption to short-text
    var desc = obj.description || '';
    //create div for company Title
    var companyTitleDiv = document.createElement("div");
    companyTitleDiv.setAttribute("class", "title-box");
    //create h4 for company Title
    var companyTitleDivH = document.createElement("h4");
    companyTitleDivH.setAttribute("class", "title-box-name");
    companyTitleDivH.innerHTML = obj.name;
    //create div for company Logo
    var companyLogoDiv = document.createElement("div");
    companyLogoDiv.setAttribute("class", "entry-logo");
    //create img for company Logo
    var companyLogoDivImg = document.createElement("img");
    companyLogoDivImg.setAttribute("class", "entry-logo-img");
    companyLogoDivImg.src = obj.logo;
    //create div for company Description
    var companyDescDiv = document.createElement("div");
    companyDescDiv.setAttribute("class", "entry-content");
    companyDescDiv.innerHTML = desc.substr(0, 150) + "...";

    companyTitleDiv.appendChild(companyTitleDivH);
    companyLogoDiv.appendChild(companyLogoDivImg);

    companyDiv.appendChild(companyTitleDiv);
    companyDiv.appendChild(companyLogoDiv);
    companyDiv.appendChild(companyDescDiv);
    // if not needed please delete the below
    /*companyDiv.innerHTML = '<div class="title-box"><h4>' + obj.name + '</h4></div>' +
     '<div class="entry-logo"><img src="' + obj.logo + '"></div>' +
     '<div class="entry-content">' + desc.substr(0, 200) + '...</div></div>';
     // добавляем только что созданый элемент в дерево DOM*/
    document.getElementById("company-block").appendChild(companyDiv);
}

function show_more(type_api, id) {
    if (type_api == "vacancy") {
        for (var vacancy in globalVacancies) {
            if (globalVacancies[vacancy].id == id.split('-')[1]) {
                showVacancyElement(globalVacancies[vacancy])
            }
        }
    }
    if (type_api == "company") {
        for (var company in globalCompanies) {
            if (globalCompanies[company].id == id.split('-')[1]) {
                showCompanyElement(globalCompanies[company]);
            }
        }
    }
}


function showCompanyElement(obj) {
    // создаем новый элемент div
    // и добавляем в него немного контента
    var newDiv = document.createElement("div");
    newDiv.setAttribute("class", "col-xs-4");
    newDiv.innerHTML = '<div class="title-box"><h4>' + obj.name + '</h4></div>' +
        '<div class="entry-image"><img src="' + obj.logo + '"></div>' +
        '<div class="entry-content">' + obj.description + '</div>';
    // добавляем только что созданый элемент в дерево DOM
    document.getElementById("side-bar").innerHTML = newDiv.innerHTML;
}

function showVacancyElement(obj) {
    // создаем новый элемент div
    // и добавляем в него немного контента
    var newDiv = document.createElement("div");
    newDiv.setAttribute("class", "col-xs-4");
    newDiv.innerHTML = '<div class="title-box"><h4>' + obj.name + '</h4></div>' +
        '<div><p>' + obj.company_name + '</p></div>' +
        '<div class="entry-content">' + obj.description + '</div>';
    // добавляем только что созданый элемент в дерево DOM
    document.getElementById("side-bar").innerHTML = newDiv.innerHTML;
}
// todo make below function work for globalVacancies and globalCompanies
function testPostScriptCompany() {
    var  url = 'http://' + window.location.hostname + ":" + window.location.port + '/api/company/' + counter++;
    showMoreEventHandler(url);
}

function testPostScriptVacancy() {
    var url = 'http://' + window.location.hostname + ":" + window.location.port + '/api/vacancy/' + counter++;
    showMoreEventHandler(url);
}

function showMoreEventHandler(url) {
    var xhr = new XMLHttpRequest(),
        vacancyUrl = url.indexOf('vacancy'),
        companyUrl = url.indexOf('company'),
        linkUrl = url.indexOf('link');

    if (vacancyUrl) {
        url = 'http://' + window.location.hostname + ":" + window.location.port + '/api/vacancy/' + counter++;
    } else if (companyUrl) {
        url = 'http://' + window.location.hostname + ":" + window.location.port + '/api/company/' + counter++;
    } else if (linkUrl) {
        url = 'for link url';
    }

    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            var status = xhr.status;
            if (status >= 200 && status < 300 || status === 304) {
                if (vacancyUrl) {
                    var vacanciesJson = JSON.parse(xhr.responseText),
                        vacancy = new Vacancy();
                    for (var dict in vacanciesJson) {
                        for (var elem in vacanciesJson[dict]) {
                            globalVacancies.push(vacancy.createFromData(vacanciesJson[dict][elem]));
                        }
                    }
                } else if (companyUrl) {
                    var companiesJson = JSON.parse(xhr.responseText),
                        company = new Vacancy();
                    for (var dict in companiesJson) {
                        for (var elem in companiesJson[dict]) {
                            globalVacancies.push(company.createFromData(companiesJson[dict][elem]));
                        }
                    }
                } else if (linkUrl) {
                    url = 'for link url';
                }
            } else {
                console.log(xhr.status + ":" + xhr.statusText);
            }
        }
    };
    xhr.send();
}