var globalLinks = [],
    globalVacancies = [],
    globalCompanies = [],
    globalNews = [],
    globalEvents = [],
    globalMarkers = [],
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

function Marker() {
}

Marker.prototype.createFromData = function (data) {
    var object = new Marker();
    object.name = data.name;
    object.company = data.company;
    object.phone = data.phone;
    object.address = data.address;
    object.lat = data.lat;
    object.lng = data.lng;
    return object;
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
    var vacancyDivWrapper = document.createElement("div");
    vacancyDivWrapper.setAttribute("class", "col-xs-12 col-md-4");
    vacancyDivWrapper.setAttribute("onclick", "show_more('vacancy', this.id)");
    vacancyDivWrapper.setAttribute("id", "vacancy-" + obj.id);

    var vacancyDiv = document.createElement("div");
    vacancyDiv.setAttribute("class", "vacancy");

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

    vacancyDiv.appendChild(vacancyTitleDiv)
        .appendChild(vacancyContainerDiv);

    vacancyDivWrapper.appendChild(vacancyDiv);

    document.getElementById("vacancy-block").appendChild(vacancyDivWrapper);
}

function addLinkElement(obj) {
    // создаем новый элемент div
    // и добавляем в него немного контента
    // create general div for Link Entity
    var linkDiv = document.createElement("div");
    linkDiv.setAttribute("class", "col-xs-12");
    linkDiv.setAttribute("id", "link-" + obj.id);
    linkDiv.innerHTML = '<div class="usefull-link"><a href="' + obj.url + '"><p>' + obj.name + '</p></a><h6>' + obj.short_text + '...</h6></div>';
    // добавляем только что созданый элемент в дерево DOM
    document.getElementById("link-block").appendChild(linkDiv);
}

function addCompanyElement(obj) {
    // create general div for Company Entity
    var companyDivWrapper = document.createElement("div");
    companyDivWrapper.setAttribute("class", "col-xs-12 col-md-4");
    companyDivWrapper.setAttribute("onclick", "show_more('company', this.id)");
    companyDivWrapper.setAttribute("id", "company-" + obj.id);

    var companyDiv = document.createElement("div");
    companyDiv.setAttribute("class", "company");

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

    companyDiv.appendChild(companyTitleDiv)
        .appendChild(companyLogoDiv)
        .appendChild(companyDescDiv);

    companyDivWrapper.appendChild(companyDiv);

    document.getElementById("company-block").appendChild(companyDivWrapper);
}

function show_more(type_api, id) {
    if (type_api == "vacancy") {
        for (var vacancy in globalVacancies) {
            if (globalVacancies[vacancy].id == id.split('-')[1]) {
                showVacancyElementOnSideBar(globalVacancies[vacancy])
            }
        }
    }
    if (type_api == "company") {
        for (var company in globalCompanies) {
            if (globalCompanies[company].id == id.split('-')[1]) {
                showCompanyElementOnSideBar(globalCompanies[company]);
            }
        }
    }
    if (type_api == "new") {
        for (var item in globalNews) {
            if (globalNews[item].id == id.split('-')[1]) {
                //do we need to show it on side bar? if yes --> what kind of info we would like to see there?
            }
        }
    }
    if (type_api == "event") {
        for (var event in globalEvents) {
            if (globalEvents[event].id == id.split('-')[1]) {
                //do we need to show it on side bat?
            }
        }
    }
}

function showCompanyElementOnSideBar(obj) {
    // create general div for company entity on side bar
    var sideBarCompanyDiv = document.createElement("div");
    sideBarCompanyDiv.setAttribute("class", "col-xs-4");
    // create title div for general company div
    var sideBarCompanyTitleDiv = document.createElement('div');
    sideBarCompanyTitleDiv.setAttribute('class', 'title-box');
    // create h4 for title div
    var sideBarCompanyTitleH4 = document.createElement('h4');
    sideBarCompanyTitleH4.setAttribute('class', 'title-box-text');
    sideBarCompanyTitleH4.innerHTML = obj.name;
    //create img div for general div
    var sideBarCompanyImageDiv = document.createElement('div');
    sideBarCompanyImageDiv.setAttribute('class', 'entry-image');
    //create img el for img div
    var sideBarCompanyImage = document.createElement('img');
    sideBarCompanyImage.setAttribute('class', 'entry-image-img');
    sideBarCompanyImage.src = obj.logo;
    //create div for description
    var sideBarCompanyDescriptionDiv = document.createElement('div');
    sideBarCompanyDescriptionDiv.setAttribute('class', 'entry-content');
    sideBarCompanyDescriptionDiv.innerHTML = obj.description;

    sideBarCompanyTitleDiv.appendChild(sideBarCompanyTitleH4);
    sideBarCompanyImageDiv.appendChild(sideBarCompanyImage);

    sideBarCompanyDiv.appendChild(sideBarCompanyTitleDiv)
        .appendChild(sideBarCompanyImageDiv)
        .appendChild(sideBarCompanyDescriptionDiv);

    document.getElementById("full-view").appendChild(sideBarCompanyDiv);

    // old realization below... check if works new one and in case of success  -- > delete:
    /*newDiv.innerHTML = '<div class="title-box"><h4>' + obj.name + '</h4></div>' +
        '<div class="entry-image"><img src="' + obj.logo + '"></div>' +
        '<div class="entry-content">' + obj.description + '</div>';
    // добавляем только что созданый элемент в дерево DOM
     document.getElementById("full-view").innerHTML = newDiv.innerHTML;*/
}

function showVacancyElementOnSideBar(obj) {
    // создаем новый элемент div
    // и добавляем в него немного контента
    var sideBarVacancyDiv = document.createElement("div");
    sideBarVacancyDiv.setAttribute("class", "col-xs-4");
    // create title div for general vacancy div
    var sideBarVacancyTitleDiv = document.createElement('div');
    sideBarVacancyTitleDiv.setAttribute('class', 'title-box');
    //create title el for title div
    var sideBarVacancyTitleH4 = document.createElement('h4');
    sideBarVacancyTitleH4.setAttribute('class', 'title-box-text');
    sideBarVacancyTitleH4.innerHTML = obj.name;
    //create div for Company that vacancy belongs to
    var sideBarVacancyCompanyNameDiv = document.createElement('div');
    sideBarVacancyCompanyNameDiv.setAttribute('class', 'company-name-of-vacancy');
    //create p el for div for Company that vacancy belongs to
    var sideBarVacancyCompanyNameP = document.createElement('p');
    sideBarVacancyCompanyNameP.setAttribute('class', 'company-name-of-vacancy-text');
    sideBarVacancyCompanyNameP.innerHTML = obj.company_name;
    //create div for description
    var sideBarVacancyDescriptionDiv = document.createElement('div');
    sideBarVacancyDescriptionDiv.setAttribute('class', 'entry-content');
    sideBarVacancyDescriptionDiv.innerHTML = obj.description;

    sideBarVacancyTitleDiv.appendChild(sideBarVacancyTitleH4);
    sideBarVacancyCompanyNameDiv.appendChild(sideBarVacancyCompanyNameP);

    sideBarVacancyDiv.appendChild(sideBarVacancyTitleDiv)
        .appendChild(sideBarVacancyCompanyNameDiv)
        .appendChild(sideBarVacancyDescriptionDiv);

    document.getElementById("full-view").appendChild(sideBarVacancyDiv);

    // old realization below... check if works new one and in case of success  -- > delete:
    /*sideBarVacancyDiv.innerHTML = '<div class="title-box"><h4>' + obj.name + '</h4></div>' +
        '<div><p>' + obj.company_name + '</p></div>' +
        '<div class="entry-content">' + obj.description + '</div>';
    // добавляем только что созданый элемент в дерево DOM
     document.getElementById("full-view").innerHTML = sideBarVacancyDiv.innerHTML;*/
}

// in doubt with naming
function showMoreEvent(url) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            var status = xhr.status;
            if (status >= 200 && status < 300 || status === 304) {
                postProcessing(JSON.parse(xhr.responseText));
            } else {
                console.log(xhr.status + ":" + xhr.statusText);
            }
        }
    };
    xhr.send();
}

function postProcessing(data) {
    var myArray = data,
        vacancy = new Vacancy(),
        company = new Company(),
        marker = new Marker(),
        link = new Link();
    console.log(myArray);
    //clearGlobalMarkers();
    for (var dict in myArray) {
        switch (dict) {
            case ("vacancy_list"):
                for (var elem in myArray[dict]) {
                    globalVacancies.push(vacancy.createFromData(myArray[dict][elem]));
                }
                break;
            case ("company_list"):
                for (var elem in myArray[dict]) {
                    globalCompanies.push(company.createFromData(myArray[dict][elem]));
                }
                break;
            case ("link_list"):
                for (var elem in myArray[dict]) {
                    globalLinks.push(link.createFromData(myArray[dict][elem]));
                }
                break;
            case ('office_list'):
                for (elem in myArray[dict]) {
                    globalMarkers.push(marker.createFromData(myArray[dict][elem]));
                }
                break;
            default:
                throw new Error('---------------------------failed to parse input data----------------------------------------');
        }
    }
}

function clearGlobalMarkers() {
    if (globalMarkers) {
        globalMarkers = [];
        clearMarkers(markers);
    }
}

function getJsonDataViaAjax(path, async) {
    $.ajax({
        url: window.location.protocol + '//' + window.location.hostname + ":" + window.location.port + path,
        type: 'post',
        dataType: 'json',
        cache: false,
        success: postProcessing,
        async: async
    });
}

/*
 (function showMoreEventHandler() {
 var companyShowMoreBtn = document.getElementById('btn-load-company'),
 vacancySHowMoreBtn = document.getElementById('btn-load-vacancy');
 vacancySHowMoreBtn.onclick = function () {
 let url = 'http://' + window.location.hostname + ":" + window.location.port + '/api/vacancy/' + counter++;
 showMoreEvent(url);
 };
 companyShowMoreBtn.onclick = function () {
 let url = 'http://' + window.location.hostname + ":" + window.location.port + '/api/company/' + counter++;
 showMoreEvent(url);
 };
 })();*/
