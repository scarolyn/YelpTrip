$(document).ready(function() {
    var selectedKeys = [];
    //follow keys until i get to the correct nested dict
    var currDict = clusterJSON.clusters;
    var businesses = clusterJSON.businesses;
    $(selectedKeys).each(function(index, element) {
        currDict = currDict[element];
        // console.log("level");
    });
    //make a list of keys to keep curr order
    var lstKeys = [];
    $.each(currDict, function(key, data) {
        // console.log(key);
        lstKeys.push(key);
        // $.each(data, function (index, data) {
        //     console.log('index', data)
        // });
    });
    // console.log(Object.keys(lstKeys).length);
    $(".choice").each(function(index, element) {
        var currKey = lstKeys[index];
  		$(element).prepend('<a href=' + businesses[currKey].url + '>' + businesses[currKey].name + '</a>');
    });
    //on click: add to selectedKeys
    //change tabs
    //repopulate choices
});