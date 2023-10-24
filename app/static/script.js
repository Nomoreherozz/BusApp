function choose_basemap() {
  var basemap = document.getElementById("select_basemap").value;

  if (basemap == "GOOGLE MAP") {
    var choosenBasemap = L.tileLayer(
      "http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}",
      {
        maxZoom: 20,
        subdomains: ["mt0", "mt1", "mt2", "mt3"],
      }
    ).addTo(map);
  } else if (basemap == "OPENSTREETMAP") {
    choosenBasemap = L.tileLayer;
    "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
      {
        maxZoom: 19,
      }().addTo(map);
  } else if (basemap == "GOOGLE SATELITE") {
    L.tileLayer("http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}", {
      maxZoom: 20,
      subdomains: ["mt0", "mt1", "mt2", "mt3"],
    }).addTo(map);
  } else {
    choosenBasemap = L.tileLayer(
      "http://{s}.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}",
      {
        maxZoom: 20,
        subdomains: ["mt0", "mt1", "mt2", "mt3"],
      }
    ).addTo(map);
  }
}

function randomInt(n) {
  return Math.floor(Math.random() * n);
}

function congest_segment(e) {
  let nWp = e.routes[0].coordinates.length;
  let start = randomInt(nWp / 4);
  let end = randomInt(nWp / 4);
  var coords = [];

  // Swap value if start point after (bigger than) end point
  if (start > end) {
    [start, end] = [end, start];
  }
  coords.push(L.latLng(e.routes[0].coordinates[start]));
  console.log(start, end);
  for (let i = 0; i < e.routes[0].waypointIndices.length; i++) {
    if (
      start < e.routes[0].waypointIndices[i] &&
      e.routes[0].waypointIndices[i] < end
    ) {
      coords.push(
        L.latLng(e.routes[0].coordinates[e.routes[0].waypointIndices[i]])
      );
    }
  }
  coords.push(L.latLng(e.routes[0].coordinates[end]));

  L.Routing.control({
    show: false,
    addWaypoints: false,
    draggableWaypoints: false,
    fitSelectedRoutes: false,
    waypoints: coords,
    lineOptions: {
      styles: [{ color: "red", opacity: 1, weight: 6 }],
    },
    createMarker: function (i, wp, nWps) {
      if ((i == 0) | (i == nWps - 1)) {
        return L.marker(wp.latLng, { icon: redIcon })
          .bindPopup("Đoạn Đường này hiện đang kẹt xe")
          .openPopup();
      }
    },
  }).addTo(map);
}

function getVelocity() {
  const str = Math.random() * (150 - 75) + 75;
  var speed = ((parseFloat(str) * 5) / 18).toFixed(2);
  return speed;
}

function showPath_Marker(coords, stopDict) {
  route = L.Routing.control({
    show: false,
    addWaypoints: false,
    draggableWaypoints: false,
    fitSelectedRoutes: false,
    waypoints: coords,
    lineOptions: {
      styles: [{ color: "green", opacity: 1, weight: 3 }],
    },
    createMarker: function (i, wp, nWps) {
      return L.marker(wp.latLng).bindPopup(stopDict[i + 1].name);
    },
  }).addTo(map);
  return route;
}

function drivePath_Marker(coords, stopDict) {
  drive = L.Routing.control({
    show: false,
    addWaypoints: false,
    draggableWaypoints: false,
    fitSelectedRoutes: false,
    waypoints: coords,
    lineOptions: {
      styles: [{ color: "blue", opacity: 1, weight: 2 }],
    },
    createMarker: function (i, wp, nWps) {
      return L.marker(wp.latLng).bindPopup(stopDict[i + 1].name);
    },
  });
  return drive;
}

function getDetail(points, number) {
  let stopDict = {};
  let coords = [];

  for (var i = 0; i < points.length; i++) {
    if (points[i].number == number) {
      coords.push(L.latLng([points[i].latitude, points[i].longitude]));
      stopDict[points[i].stop_id] = {
        latitude: points[i].latitude,
        longitude: points[i].latitude,
        name: points[i].name,
        distance: points[i].distance,
      };
    }
  }

  return [stopDict, coords];
}

function run(e, stopDict) {
  var station_id = 0;
  var station_index = e.routes[0].waypointIndices;
  var dist_from_src;

  e.routes[0].coordinates.forEach(function (coord, index) {
    setTimeout(function () {
      if (station_index.includes(index)) {
        station_id = station_index.indexOf(index) + 1;
        dist_from_src = stopDict[station_id.toString()].distance;
      }

      dist_from_src -= getVelocity();

      hoverBusInfo(bux, station_id);

      console.log(
        "Trạm: " +
          station_id.toString() +
          ", " +
          stopDict[station_id.toString()].name +
          ", khoảng cách đến trạm kế tiếp: " +
          dist_from_src.toString()
      );
      bux.setLatLng([coord.lat, coord.lng]);
    }, 1000 * index);
  });
  congest_segment(e);
}

function hoverBusInfo(mrk, station_id) {
  mrk.bindPopup(
    "Đang ở trạm " +
      station_id.toString() +
      ", vận tốc hiện tại là: " +
      getVelocity()
  );
  mrk.on("mouseover", function (e) {
    this.openPopup();
  });
  mrk.on("mouseout", function (e) {
    this.closePopup();
  });
}

function firstStop(number) {
  var first_point;

  if (["39", "51", "55"].includes(number)) {
    first_point = L.marker([10.9758774, 106.6705121], { icon: busIcon });
  } else if (number == 66) {
    first_point = L.marker([11.0525335, 106.6670739], { icon: busIcon });
  } else if (number == 67) {
    first_point = L.marker([11.0551582, 106.6870726], { icon: busIcon });
  } else {
    first_point = L.marker([11.0571726, 106.6846084], { icon: busIcon });
  }

  return first_point;
}

var busIcon = L.icon({
  iconUrl: "https://cdn-icons-png.flaticon.com/512/5030/5030991.png",
  iconSize: [40, 40],
  // iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41],
});

var greenIcon = new L.Icon({
  iconUrl:
    "https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png",
  shadowUrl:
    "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.3.4/images/marker-shadow.png",
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41],
});

var redIcon = new L.Icon({
  iconUrl:
    "https://cdn.jsdelivr.net/gh/pointhi/leaflet-color-markers@master/img/marker-icon-2x-red.png",
  shadowUrl:
    "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.3.4/images/marker-shadow.png",
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41],
});

var bux = L.marker();
route = L.Routing.control({});
drive = L.Routing.control({});

function choose_bus() {
  var bus = document.getElementById("select_bus").value;
  let points = JSON.parse(document.getElementById("stop-json").textContent);

  map.removeLayer(bux);
  map.removeControl(route);

  bux = firstStop(bus).addTo(map);

  var [stopDict, coords] = getDetail(points, bus);

  showPath_Marker(coords, stopDict);

  bux.on("click", function () {
    map.removeControl(route);
    map.removeControl(drive);

    drivePath_Marker(coords, stopDict)
      .on("routesfound", function (e) {
        run(e, stopDict);
      })
      .addTo(map);
  });
}
