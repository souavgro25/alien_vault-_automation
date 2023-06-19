var startDateElement = document.getElementById("start_date");
var endDateElement = document.getElementById("end_date");
var username = document.getElementById("username_id");
var source_ip = document.getElementById("source_ip");
var dest_ip = document.getElementById("dest_ip");
var device_ip = document.getElementById("device_ip")
var attempts = document.getElementById("attempts");
var event_count = document.getElementById("event_count")
var ticket_option = document.getElementById("ticket_option")
var failure_code = document.getElementById("failure_code")
var pa_type = document.getElementById("pa_type")
var dept_name = document.getElementById("dept_name")
var raw_log = document.getElementById("raw_log")

console.log()

document.getElementById("myForm").addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent form submission

    // Get form values
    var inputString = document.getElementById("payload").value;
    var totalCount = document.getElementById("totalCount").value;
    var sourceIP = document.getElementById("sourceIP").value;
    var destinationIP = document.getElementById("destinationIP").value;
    var username_form = document.getElementById("username").value;
    var startdate = document.getElementById("startdate").value;
    var enddate = document.getElementById("enddate").value;
    var department = document.getElementById("department").value;

    // Log values to console
    console.log("Payload Text:", inputString);
    console.log("Total Count:", totalCount);
    console.log("Source IP:", sourceIP);
    console.log("Destination IP:", destinationIP);
    console.log("usernames:", username_form);

    // var  = payload
    // Use regular expression to extract the Ticket Options





    var pa_code_regex = /Ticket Options:  ([^\s]+)/;
    var match = inputString.match(pa_code_regex);

    // Extracted Ticket Options value
    var Ticketop = match ? match[1] : null;


    var failure_regex = /Failure Code:  ([^\s]+)/;
    var match = inputString.match(failure_regex);

    // Extracted Ticket Options value
    var failure_op = match ? match[1] : null;

    var ticketoption_regex = /Pre-Authentication Type: ([^\s]+)/;
    var match = inputString.match(ticketoption_regex);

    // Extracted Ticket Options value
    var pa_code = match ? match[1] : null;

    




    var hostRegex = /HOSTNAME: "" \((\w+)\)/;
    var hostMatch = inputString.match(hostRegex);
    var host = hostMatch ? hostMatch[1] : null;
console.log(pa_code,Ticketop,failure_op)

    startDateElement.textContent = startdate;
    endDateElement.textContent = enddate;
    username.textContent=username_form
    source_ip.textContent=sourceIP
    dest_ip.textContent=destinationIP
    device_ip.textContent=destinationIP
    attempts.textContent=totalCount
    failure_code.textContent=failure_op
    pa_type.textContent=pa_code
    event_count.textContent=totalCount
    dept_name.textContent=department
    raw_log.textContent=inputString





});





