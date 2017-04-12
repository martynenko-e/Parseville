/**
 * Created by Martynenko on 03.02.2017.
 */
;

var Vacancy = function () {

};

Vacancy.prototype.createFromData = function (data) {
    var object = new Vacancy;
    object.id = data.id;
    object.name = data.name;
    object.description = data.description;
    object.short_text = data.short_text;
    object.pub_date = data.pub_date;
    object.company_name = data.company_name;
    object.p_language = data.p_language;
    // addVacancyElement(object);
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
    object.short_text = data.short_text;
    object.logo = data.logo;
    object.site_url = data.site_url;
    // addCompanyElement(object);
    return object;
};

var Link = function () {

};

Link.prototype.createFromData = function (data) {
    var object = new Link;
    object.id = data.id;
    object.name = data.name;
    object.short_text = data.short_text;
    object.url = data.url;
    // addLinkElement(object);
    return object;
};

Link.prototype.addToHtml = function () {

};

var links = [];
var vacancies = [];
var companies = [];

function getJsonOfVacancies() {
    var xhr = new XMLHttpRequest(),
        url = "http://138.68.77.7:8000/api/vacancy/";
    xhr.open("GET", url, true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            var status = xhr.status;
            if (status >= 200 && status < 300 || status === 304) {
                var vacancies = JSON.parse(xhr.responseText); // returns string of JSON
                parseVacancies(vacancies);
            } else {
                console.log(xhr.status + ":" + xhr.statusText);
            }
        }
    };
    xhr.send(null);
}

function show_more(type_api, id) {
    if (type_api == "vacancy") {
        for (var vacancy in vacancies) {
            if (vacancies[vacancy].id == id.split('-')[1]) {
                showVacancyElement(vacancies[vacancy])
            }
        }
    }
    if (type_api == "company") {
        for (var company in companies) {
            if (companies[company].id == id.split('-')[1]) {
                showCompanyElement(companies[company]);
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
    document.getElementById("full-view").innerHTML = newDiv.innerHTML;
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
    document.getElementById("full-view").innerHTML = newDiv.innerHTML;
}

function dataProcessing(data) {
    var data_dict = data;
    for (var dict_key in data_dict) {
        switch (dict_key) {
            case ("vacancy_list"):
                for (var key in data_dict[dict_key]) {
                    vacancies.push(Vacancy.prototype.createFromData(data_dict[dict_key][key]));
                }
                break;
            case ("company_list"):
                for (var key in data_dict[dict_key]) {
                    companies.push(Company.prototype.createFromData(data_dict[dict_key][key]));
                }
                break;
            case ("link_list"):
                for (var key in data_dict[dict_key]) {
                    links.push(Link.prototype.createFromData(data_dict[dict_key][key]));
                }
                break;
        }
    }
}