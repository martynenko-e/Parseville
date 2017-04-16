/**
 * Created by marty on 16.04.17.
 */
function showMoreEvent(url) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            var status = xhr.status;
            if (status >= 200 && status < 300 || status === 304) {
                var data = JSON.parse(xhr.responseText);
                dataProcessing(data, true);
            } else {
                console.log(xhr.status + ":" + xhr.statusText);
            }
        }
    };
    xhr.send();
}

(function showMoreEventHandler() {
    var companyShowMoreBtn = document.getElementById('btn-load-company');
    var vacancyShowMoreBtn = document.getElementById('btn-load-vacancy');
    var articleShowMoreBtn = document.getElementById('btn-load-article');
    var eventShowMoreBtn = document.getElementById('btn-load-event');
    if (companyShowMoreBtn) {
        companyShowMoreBtn.onclick = function () {
            let url = window.location.protocol + '//' + window.location.hostname + ":" + window.location.port + '/api/company/' + counter++;
            console.log(url);
            showMoreEvent(url);
        };
    }
    else if (vacancyShowMoreBtn) {
        vacancyShowMoreBtn.onclick = function () {
            let url = window.location.protocol + '//' + window.location.hostname + ":" + window.location.port + '/api/vacancy/' + counter++;
            console.log(url);
            showMoreEvent(url);
        };
    }
    else if (articleShowMoreBtn) {
        articleShowMoreBtn.onclick = function () {
            let url = window.location.protocol + '//' + window.location.hostname + ":" + window.location.port + '/api/article/' + counter++;
            console.log(url);
            showMoreEvent(url);
        };
    }
    else if (eventShowMoreBtn) {
        eventShowMoreBtn.onclick = function () {
            let url = window.location.protocol + '//' + window.location.hostname + ":" + window.location.port + '/api/event/' + counter++;
            console.log(url);
            showMoreEvent(url);
        };
    }

})();