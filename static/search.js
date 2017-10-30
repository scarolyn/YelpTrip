$(document).ready(function() {
    var selectedKeys = [];
    var businesses = clusterJSON.businesses;
    document.getElementById("tab-1").classList.add("is-active");
    function populateChoices() {
    	var currDict = clusterJSON.clusters;
	    $.each(selectedKeys, function(index, element) {
	    	// console.log(element);
	    	// console.log(currDict);
	        currDict = currDict[element];
	    });
	    var lstKeys = [];
	    $.each(currDict, function(key, data) {
	        lstKeys.push(key);
	        console.log("pushing to list: " + key);
	    });
	    // console.log(currDict);
	    // console.log(Object.keys(lstKeys).length);
	    $(".choice").each(function(index, element) {
	        var currKey = lstKeys[index];
	        console.log("populating button: " + currKey);
	  		$(element).find(".option-link").attr("href", businesses[currKey].url).text(businesses[currKey].name);
	    });
	    $(".select-button").off("click");
	    $(".select-button").click(function() {
	    	selectedKeys.push(lstKeys[this.id - 1]);
	    	if (Object.keys(currDict[lstKeys[this.id - 1]]).length === 0) {
	    		$(".choices").addClass("is-hidden");
	    		$(".results-page").removeClass("is-hidden");
	    		$("#tab-results").addClass("is-active");
	    		displayResults();
	    	} else {
	    		populateChoices();
	    		$(`#tab-${selectedKeys.length + 1}`).addClass("is-active");
	    	}
    		$(`#tab-${selectedKeys.length}`).removeClass("is-active");
	    });
    }
    populateChoices();
    function displayResults() {
    	$(".result").each(function (index, element) {
    		var business = businesses[selectedKeys[index]];
    		$(element).attr("href", business.url).text(business.name);
    	});
    }
});