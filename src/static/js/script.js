/**
 * Created by Martynenko on 03.02.2017.
 */
;

var events = [],
    news = [],
    vacancies = [],
    companies = [],
    counter = 1,
    globalMarkers = [];

var Vacancy = function () {

};

Vacancy.prototype.createFromData = function (data, is_draw) {
    var object = new Vacancy;
    object.id = data.id;
    object.date = data.date;
    object.name = data.name;
    object.description = data.description;
    object.short_text = data.short_text;
    object.pub_date = data.pub_date;
    object.company_name = data.company_name;
    object.p_language = data.p_language;
    if (is_draw) {
        draw_html(object, "vacancy");
    }
    return object;
};


var Company = function () {

};

Company.prototype.createFromData = function (data, is_draw) {
    var object = new Company;
    object.id = data.id;
    object.name = data.name;
    object.date = data.date;
    object.description = data.description;
    object.short_text = data.short_text;
    object.logo = data.image;
    object.site_url = data.site_url;
    if (is_draw) {
        draw_html(object, "company");
    }
    return object;
};


var Event = function () {

};

Event.prototype.createFromData = function (data, is_draw) {
    var object = new Event;
    object.id = data.id;
    object.date = data.date;
    object.name = data.name;
    object.company_name = data.company_name;
    object.description = data.description;
    object.short_text = data.short_text;
    object.url = data.url;
    if (is_draw) {
        draw_html(object, "event");
    }
    return object;
};

var Article = function () {

};

Article.prototype.createFromData = function (data, is_draw) {
    var object = new Article;
    object.id = data.id;
    object.date = data.date;
    object.name = data.name;
    object.image = data.image;
    object.company_name = data.company_name;
    object.description = data.description;
    object.short_text = data.short_text;
    object.url = data.url;
    if (is_draw) {
        draw_html(object, "article");
    }
    return object;
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

function draw_html(obj, type) {
    // create general div for Company Entity
    var main_div = document.createElement("div");
    main_div.setAttribute("class", "row psv_block_padding");

    var separate_div = document.createElement("div");
    separate_div.setAttribute("class", "psv_row_indent");

    var date_div = document.createElement("div");
    date_div.setAttribute("class", "pull-right psv_default_font");
    date_div.innerHTML = obj.date;

    var link_div = document.createElement("div");
    link_div.setAttribute("class", "psv_link");
    link_div.setAttribute("id", type + "-" + obj.id);
    link_div.setAttribute("onclick", 'show_more("' + type + '", this.id)');
    link_div.innerHTML = obj.name;

    var short_text = document.createElement("div");
    short_text.setAttribute("class", "psv_default_font");
    short_text.innerHTML = obj.short_text;

    if (obj.logo || obj.image) {
        var left_div = document.createElement("div");
        left_div.setAttribute("class", "psv_left-half");

        var image = document.createElement("img");
        image.setAttribute("class", "psv_index_image");
        if (obj.logo) {
            image.setAttribute("src", obj.logo);
        } else {
            image.setAttribute("src", obj.image);
        }


        left_div.appendChild(image);

        var right_div = document.createElement("div");
        right_div.setAttribute("class", "psv_right-half");
        right_div.appendChild(date_div);
        right_div.appendChild(link_div);
        right_div.appendChild(short_text);

        main_div.appendChild(separate_div);
        main_div.appendChild(left_div);
        main_div.appendChild(right_div);
    } else {
        main_div.appendChild(separate_div);
        main_div.appendChild(date_div);
        main_div.appendChild(link_div);
        main_div.appendChild(short_text);
    }
    document.getElementById("element-list").appendChild(main_div);
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
    if (type_api == "event") {
        for (var event in events) {
            if (events[event].id == id.split('-')[1]) {
                showEventElement(events[event]);
            }
        }
    }
    if (type_api == "article") {
        for (var article in news) {
            if (news[article].id == id.split('-')[1]) {
                showArticleElement(news[article]);
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

function showEventElement(obj) {
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

function showArticleElement(obj) {
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

function dataProcessing(data, is_draw) {
    var data_dict = data;
    for (var dict_key in data_dict) {
        switch (dict_key) {
            case ("vacancies"):
                for (var key in data_dict[dict_key]) {
                    vacancies.push(Vacancy.prototype.createFromData(data_dict[dict_key][key], is_draw));
                }
                break;
            case ("companies"):
                for (var key in data_dict[dict_key]) {
                    companies.push(Company.prototype.createFromData(data_dict[dict_key][key], is_draw));
                }
                break;
            case ("events"):
                for (var key in data_dict[dict_key]) {
                    events.push(Event.prototype.createFromData(data_dict[dict_key][key], is_draw));
                }
                break;
            case ("news"):
                for (var key in data_dict[dict_key]) {
                    news.push(Article.prototype.createFromData(data_dict[dict_key][key], is_draw));
                }
                break;
        }
    }
}

