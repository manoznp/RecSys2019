if(navigator.geolocation)
{
		navigator.geolocation.getCurrentPosition(onPositionReceived);
}





var places = [

	{name:'ABC', latitude:'28.5300', longitude:'83.8780'},
	{name:'Everest Base Camp', latitude:'28.0026', longitude:'86.8528'},
	{name:'Ghandruak', latitude:'28.4633', longitude:'83.8261'},
	{name:'Mustang', latitude:'28.9985', longitude:'83.8473'},
	{name:'poonHill', latitude:'28.4002', longitude:'83.6893'}
];

function onPositionReceived(position)
{
	var data = new Array();
	data['user_lat'] = position.coords.latitude;
	data['user_lon'] = position.coords.longitude;

	document.getElementById("id_latitude").value = position.coords.latitude;
	document.getElementById('id_longitude').value = position.coords.longitude;

	var hamro = findDistance(data, places);
	console.log(hamro);
  // data['address'] = {'ko':position.coords.latitude, 'user_lon':position.coords.longitude};
  // data['user_lat'] = position.coords.latitude;
  // data['user_lon'] = position.coords.longitude;
  // user = new UserPosition(position.coords.latitude, position.coords.longitude);
}



// var mam = data.user_lat;
// console.log(mam);
// console.log(data.user_lat);

function findDistance(data, places)
{
  var duration = [];

	console.log(places["0"]);

	console.log(data.user_lat);
	console.log(data.user_lon);

	console.log(data.user_lat);


	// console.log(data['user_lat']);

  console.log(typeof data);



  // console.log(data['0'].user_lat);

  for(i=0; i<places.length; i++){
    // console.log(places[i]);
    var R = 6371e3; // metres
  	console.log(R);
  	var lat_user_radian = data['user_lat']*Math.PI/180;
  	 // Math.toRad(lat_user);
  	 // lat_user.toRadians();
     console.log(lat_user_radian);
  	var lat_database_radian = places[i]["latitude"]*Math.PI/180;
  	// .toRadians();
  	var lat_diff = (places[i]["latitude"]-data['user_lat'])*Math.PI/180;
  	// toRadians(); places["longitude"]
  	var lon_diff = (places[i]["longitude"]-data['user_lon'])*Math.PI/180;
  	console.log(lon_diff);
  	// toRadians();

  	var a = Math.sin(lat_diff/2) * Math.sin(lat_diff/2) +
          Math.cos(lat_diff) * Math.cos(lat_diff) *
          Math.sin(lon_diff/2) * Math.sin(lon_diff/2);
  	var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));

  	console.log(c);

  	var d = (R * c)/1000;

    duration[i] = {name:places[i].name, distance:d};
  }

  return duration;
}








// const place = new UserPosition(45.454, 34.3434);
//
// console.log(place.findLocation);
