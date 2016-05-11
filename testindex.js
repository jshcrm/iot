var server = require("./nodetest/server"),
	router = require("./nodetest/router"),
	requestHandlers = require("./nodetest/requestHandlers");

var handle = {}
handle["/"] = requestHandlers.start;
handle["/start"] = requestHandlers.start;
handle["/upload"] = requestHandlers.upload;
handle["/show"] = requestHandlers.show;

server.start(router.route, handle);