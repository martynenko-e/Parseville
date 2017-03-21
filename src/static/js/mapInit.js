/* Google API for Map */

var marker = {};
function initMap() {

    let uluru = {
        lat: 50.4501,
        lng: 30.5234
    };
    var lat = 50.4501,
        lng = 30.5234,
        mapOptions = {
            zoom: 15,
            scrollwheel: false,
            center: uluru,
            fullscreenControll: true
        },
        map = new google.maps.Map(document.getElementById('map'), mapOptions);

    marker = new google.maps.Marker({
        position: uluru,
        map: map,
        animation: google.maps.Animation.DROP
    });

    for (var i = 0; i < 10; i++) {
        marker = new google.maps.Marker({
            position: {
                lat,
                lng
            },
            map: map,
            animation: google.maps.Animation.DROP
        });

        lat += 0.01;
        lng += 0.01;
    }


    /* for (var i = 0; i < globalMarkers.length; i++) {
     var latt = globalMarkers[i].lat,
     lngg = globalMarkers[i].lng;
     var marker = new google.maps.Marker({
     position: {
     latt,
     lngg
     },
     map:map,
     animation: google.maps.Animation.DROP
     });
     }*/

    marker.addListener('click', toggleBounce);

    function toggleBounce() {
        if (marker.getAnimation() !== null) {
            marker.setAnimation(null);
        } else {
            marker.setAnimation(google.maps.Animation.BOUNCE);
        }
    }
}


/*var markerArray = [];

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
 console.log('array of offices array -------------------------------------------------------------------------');
 console.log(arrayOfOffices.length);
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

 test();
 }


 function toggleBounce() {
 if (marker.getAnimation() !== null) {
 marker.setAnimation(null);
 } else {
 marker.setAnimation(google.maps.Animation.BOUNCE);
 }
 }

 /!*marker = new google.maps.Marker({
 position: uluru,
 map: map,
 animation: google.maps.Animation.DROP
 });*!/*/
