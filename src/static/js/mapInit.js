/* Google API for Map */

var markerArray = [];

function initMap() {

    let uluru = {lat: 50.4501, lng: 30.5234};
    let mapOptions = {
        zoom: 15,
        scrollwheel: false,
        center: uluru,
        fullscreenControll: true
    };

    let map = new google.maps.Map(document.getElementById('map'), mapOptions);

    function test() {
        var url = 'http://localhost:8000/api/office',
            officesArray = [],
            xhr = new XMLHttpRequest();
        xhr.open("GET", url, true);
        xhr.onreadystatechange = function () {
            // on this stage xhr responses as status == 1 ????? why????
            if (xhr.readyState === 4) {
                var status = xhr.status;
                if (status >= 200 && status < 300 || status === 304) {
                    officesArray = JSON.parse(xhr.responseText);
                    addMarker(officesArray);
                } else {
                    console.log(xhr.status + ":" + xhr.statusText);
                }
            }
        };
        xhr.send();
    }

    function addMarker(arrayOfOffices) {

        for (var i = 0; i < arrayOfOffices.length; i++) {
            console.log('------------------------------arrayOfOffices[i] before -------------------------------------------');
            console.log(arrayOfOffices[i]);
            console.log('-------------------------------arrayOfOffices[i] after ------------------------------------------');
            var latitude = arrayOfOffices[i].lat,
                longitude = arrayOfOffices[i].lng;
            console.log('----------------------------------marker before creation---------------------------------------');
            console.log(marker);
            var marker = new google.maps.Marker({
                position: {
                    latitude,
                    longitude
                },
                map: map,
                animation: google.maps.Animation.DROP
            });
            console.log('----------------------------------maker after creation ---------------------------------------');
            console.log(marker);
            marker.addListener('click', toggleBounce);
            markerArray.push(marker);
        }
    }

    function drop() {
        for (let i = 0; i < markerArray.length; i++) {
            setTimeout(function () {
                addMarker();
            }, i * 200);
        }
    }
}


function toggleBounce() {
    if (marker.getAnimation() !== null) {
        marker.setAnimation(null);
    } else {
        marker.setAnimation(google.maps.Animation.BOUNCE);
    }
}

 /*marker = new google.maps.Marker({
     position: uluru,
     map: map,
     animation: google.maps.Animation.DROP
     });*/
