var mqtt=require('mqtt')
var mongodb=require('mongodb');

var mongodbClient=mongodb.MongoClient;
var mongodbURI='mongodb://localhost:27017/db'
var deviceRoot='home/bedroom/'
var collection,client;

mongodbClient.connect(mongodbURI,setupCollection);

function setupCollection(err,db) {
	if(err) throw err;
	collection=db.collection("bedroom");
	client=mqtt.connect('mqtt://192.168.1.2', 1883)
	client.on('connect', deviceConnected)
	client.subscribe(deviceRoot+"+")
	client.on('message', insertEvent);
}

function insertEvent(topic, message) {
	var key=topic.replace(deviceRoot, '')
	collection.update(
		{ _id:key },
		{ $push: { value:message.toString(), when:new Date() } },
		{ upsert:true },
		function(err,docs) {
			if(err) { console.log("Insert fail"); }
		}
		)
}

function deviceConnected() {
	console.log('connected to mqtt')
}