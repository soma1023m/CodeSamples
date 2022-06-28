# JSON

`JSON` stands for JavaScript Object Notation

`JSON` is a text format for storing and transporting data

`JSON` is "self-describing" and easy to understand

## What is JSON?
* JSON stands for JavaScript Object Notation
* JSON is a lightweight data-interchange format
* JSON is plain text written in JavaScript object notation
* JSON is used to send data between computers
* JSON is language independent

***

## Why Use JSON?
The JSON format is syntactically similar to the code for creating JavaScript objects. Because of this, a JavaScript program can easily convert JSON data into JavaScript objects.
Since the format is text only, JSON data can easily be sent between computers, and used by any programming language.

JavaScript has a built in function for converting JSON strings into JavaScript objects:
```
JSON.parse()
```

JavaScript also has a built in function for converting an object into a JSON string:
```
JSON.stringify()
```
***
## Storing Data
When storing data, the data has to be a certain format, and regardless of where you choose to store it, text is always one of the legal formats.
`JSON` makes it possible to store `JavaScript objects` as text.

***

## JSON Syntax Rules
JSON syntax is derived from JavaScript object notation syntax:

* Data is in name/value pairs
* Data is separated by commas
* Curly braces hold objects
* Square brackets hold arrays
* JSON Data - A Name and a Value
* JSON data is written as name/value pairs (aka key/value pairs).

A name/value pair consists of a `field name (in double quotes), followed by a colon, followed by a value`:
```
Example
"name":"John"
JSON names require double quotes.
```

JSON - Evaluates to JavaScript Objects
The JSON format is almost identical to JavaScript objects.

In JSON, keys must be strings, written with double quotes:
```
JSON
{"name":"John"}
In JavaScript, keys can be strings, numbers, or identifier names:

JavaScript
{name:"John"}
```
***
## JSON Values
In JSON, values must be one of the following data types:

* a string
* a number
* an object
* an array
* a boolean
* null

In JavaScript values can be all of the above, plus any other valid JavaScript expression, including:

* a function
* a date
* undefined

In JSON, string values must be written with double quotes:

JSON
```
{"name":"John"}
```
In JavaScript, you can write string values with double or single quotes:
```
JavaScript
{name:'John'}
```
***
## JavaScript Objects
Because JSON syntax is derived from JavaScript object notation, very little extra software is needed to work with JSON within JavaScript.

With JavaScript you can create an object and assign data to it, like this:
```
Example
person = {name:"John", age:31, city:"New York"};
You can access a JavaScript object like this:

Example
// returns John
person.name;
It can also be accessed like this:

Example
// returns John
person["name"];
Data can be modified like this:

Example
person.name = "Gilbert";
It can also be modified like this:

Example
person["name"] = "Gilbert";
You will learn how to convert JavaScript objects into JSON later in this tutorial.
```
***
## JavaScript Arrays as JSON
The same way JavaScript objects can be written as JSON, JavaScript arrays can also be written as JSON.
***
## JSON Files
The file type for JSON files is `".json"`
The MIME type for JSON text is `"application/json"`
***
## JSON vs XML
oth JSON and XML can be used to receive data from a web server.

The following JSON and XML examples both define an employees object, with an array of 3 employees:
```
JSON Example
{"employees":[
  { "firstName":"John", "lastName":"Doe" },
  { "firstName":"Anna", "lastName":"Smith" },
  { "firstName":"Peter", "lastName":"Jones" }
]}
```
XML Example
```
<employees>
  <employee>
    <firstName>John</firstName> <lastName>Doe</lastName>
  </employee>
  <employee>
    <firstName>Anna</firstName> <lastName>Smith</lastName>
  </employee>
  <employee>
    <firstName>Peter</firstName> <lastName>Jones</lastName>
  </employee>
</employees>
```
`JSON is Like XML Because`
* Both JSON and XML are "self describing" (human readable)
* Both JSON and XML are hierarchical (values within values)
* Both JSON and XML can be parsed and used by lots of programming languages
* Both JSON and XML can be fetched with an XMLHttpRequest
* JSON is Unlike XML Because
* JSON doesn't use end tag
* JSON is shorter
* JSON is quicker to read and write
* JSON can use arrays

The biggest `difference` is:

 * XML has to be parsed with an XML parser. JSON can be parsed by a standard JavaScript function.

### Why JSON is Better Than XML
* XML is much more difficult to parse than JSON.
* JSON is parsed into a ready-to-use JavaScript object.
* For AJAX applications, JSON is faster and easier than XML:

## Using XML
Fetch an XML document
Use the XML DOM to loop through the document
Extract values and store in variables

## Using JSON
Fetch a JSON string
JSON.Parse the JSON string
***

## JSON Data Types
Valid Data Types
`In JSON, values must be one of the following data types:`

* a string
* a number
* an object (JSON object)
* an array
* a boolean
* null

`JSON values cannot be one of the following data types:`

* a function
* a date
* undefined

### JSON Strings
`Strings` in JSON must be written in `double quotes`.
```
Example
{"name":"John"}
JSON Numbers
```
`Numbers` in JSON must be an `integer or a floating point.`

```
Example
{"age":30}
```
`JSON Objects`
Values in JSON can be objects.
```
Example
{
"employee":{"name":"John", "age":30, "city":"New York"}
}
```
`Objects` as `values in JSON` must follow the `JSON syntax`.
***
## JSON.parse()
A common use of `JSON` is to exchange data to/from a web server.
When receiving data from a web server, the data is always a string.
Parse the data with `JSON.parse()`, and the data becomes a `JavaScript object`.

Example - Parsing JSON
```
Imagine we received this text from a web server:

'{"name":"John", "age":30, "city":"New York"}'
Use the JavaScript function JSON.parse() to convert text into a JavaScript object:

const obj = JSON.parse('{"name":"John", "age":30, "city":"New York"}');
Make sure the text is in JSON format, or else you will get a syntax error.
```

Use the JavaScript object in your page:
```
Example
<p id="demo"></p>

<script>
document.getElementById("demo").innerHTML = obj.name;
</script>
```

### Array as JSON
When using the JSON.parse() on a JSON derived from an array, the method will return a JavaScript array, instead of a JavaScript object.
```
Example
const text = '["Ford", "BMW", "Audi", "Fiat"]';
const myArr = JSON.parse(text);
ADVERTISEMENT

Exceptions
Parsing Dates
Date objects are not allowed in JSON.

If you need to include a date, write it as a string.

You can convert it back into a date object later:

Example
Convert a string into a date:

const text = '{"name":"John", "birth":"1986-12-14", "city":"New York"}';
const obj = JSON.parse(text);
obj.birth = new Date(obj.birth);

document.getElementById("demo").innerHTML = obj.name + ", " + obj.birth;
```
Or, you can use the second parameter, of the JSON.parse() function, called reviver.
The `reviver parameter` is a function that checks each property, before returning the value.

`Example`
```
Convert a string into a date, using the reviver function:

const text = '{"name":"John", "birth":"1986-12-14", "city":"New York"}';
const obj = JSON.parse(text, function (key, value) {
  if (key == "birth") {
    return new Date(value);
  } else {
    return value;
  }
});

document.getElementById("demo").innerHTML = obj.name + ", " + obj.birth;
```
### Parsing Functions
`Functions` are not allowed in JSON.
```
If you need to include a function, write it as a string.

You can convert it back into a function later:

Example
Convert a string into a function:

const text = '{"name":"John", "age":"function () {return 30;}", "city":"New York"}';
const obj = JSON.parse(text);
obj.age = eval("(" + obj.age + ")");

document.getElementById("demo").innerHTML = obj.name + ", " + obj.age();
```
***
## JSON.stringify()
A common use of JSON is to exchange data to/from a web server.
When sending data to a web server, the data has to be a string.
Convert a JavaScript object into a string with `JSON.stringify().`

Stringify a JavaScript Object
Imagine we have this object in JavaScript:
```
const obj = {name: "John", age: 30, city: "New York"};
Use the JavaScript function JSON.stringify() to convert it into a string.

const myJSON = JSON.stringify(obj);
```
The result will be a string following the JSON notation.
myJSON is now a string, and ready to be sent to a server:

Example
```
const obj = {name: "John", age: 30, city: "New York"};
const myJSON = JSON.stringify(obj);
```
You will learn how to send `JSON` to a `server` in the next chapters.

### Stringify a JavaScript Array
It is also possible to stringify JavaScript arrays:
Imagine we have this array in JavaScript:
```
const arr = ["John", "Peter", "Sally", "Jane"];
Use the JavaScript function JSON.stringify() to convert it into a string.

const myJSON = JSON.stringify(arr);
The result will be a string following the JSON notation.

myJSON is now a string, and ready to be sent to a server:
```
Example
```
const arr = ["John", "Peter", "Sally", "Jane"];
const myJSON = JSON.stringify(arr);
```
You will learn how to send a JSON string to a server in the next chapters.

### Storing Data
When storing data, the data has to be a certain format, and regardless of where you choose to store it, `text` is always one of the legal formats.

JSON makes it possible to store `JavaScript objects as text.`

Example
```
Storing data in local storage

// Storing data:
const myObj = {name: "John", age: 31, city: "New York"};
const myJSON = JSON.stringify(myObj);
localStorage.setItem("testJSON", myJSON);

// Retrieving data:
let text = localStorage.getItem("testJSON");
let obj = JSON.parse(text);
document.getElementById("demo").innerHTML = obj.name;
```

### Exceptions
Stringify Dates
In JSON, date objects are not allowed. The JSON.stringify() function will convert any dates into strings.

Example
```
const obj = {name: "John", today: new Date(), city : "New York"};
const myJSON = JSON.stringify(obj);
```
You can convert the `string back into a date object at the receiver`.

### Stringify Functions
In JSON, functions are not allowed as object values.
The `JSON.stringify() function will remove any functions from a JavaScript object, both the key and the value:`

Example
```
const obj = {name: "John", age: function () {return 30;}, city: "New York"};
const myJSON = JSON.stringify(obj);
```
This can be omitted if you `convert your functions into strings before running the JSON.stringify() function.`

Example
```
const obj = {name: "John", age: function () {return 30;}, city: "New York"};
obj.age = obj.age.toString();
const myJSON = JSON.stringify(obj);
```
If you send functions using `JSON`, the functions will lose their scope, and the receiver would have to use eval() to convert them back into functions.
***
## JSON Object Literals
This is a JSON string:
```
'{"name":"John", "age":30, "car":null}'
```
Inside the JSON string there is a JSON object literal:
```
{"name":"John", "age":30, "car":null}
```

* JSON `object literals` are `surrounded by curly braces {}.
* JSON `object literals` contains `key/value pairs.`
* Keys and values are separated by a colon.
* Keys must be strings, and values must be a valid `JSON data type:`

* string
* number
* object
* array
* boolean
* null
Each `key/value pair` is separated by a `comma.`

It is a common mistake to call a JSON object literal "a JSON object".

`JSON cannot be an object. JSON is a string format.`

The data is only JSON when it is in a string format. When it is converted to a JavaScript variable, it becomes a JavaScript object.

JavaScript Objects
You can create a JavaScript object from a JSON object literal:
```
Example
myObj = {"name":"John", "age":30, "car":null};
Normally, you create a JavaScript object by parsing a JSON string:

Example
myJSON = '{"name":"John", "age":30, "car":null}';
myObj = JSON.parse(myJSON);
Accessing Object Values
You can access object values by using dot (.) notation:

Example
const myJSON = '{"name":"John", "age":30, "car":null}';
const myObj = JSON.parse(myJSON);
x = myObj.name;
You can also access object values by using bracket ([]) notation:

Example
const myJSON = '{"name":"John", "age":30, "car":null}';
const myObj = JSON.parse(myJSON);
x = myObj["name"];
```

### Looping an Object
You can loop through object properties with a `for-in loop:`
```
Example
const myJSON = '{"name":"John", "age":30, "car":null}';
const myObj = JSON.parse(myJSON);

let text = "";
for (const x in myObj) {
  text += x + ", ";
}
In a for-in loop, use the bracket notation to access the property values:

Example
const myJSON = '{"name":"John", "age":30, "car":null}';
const myObj = JSON.parse(myJSON);

let text = "";
for (const x in myObj) {
  text += myObj[x] + ", ";
}
```
***
## JSON Array Literals
This is a JSON string:
```
'["Ford", "BMW", "Fiat"]'
```
Inside the JSON string there is a JSON array literal:
```
["Ford", "BMW", "Fiat"]
```
Arrays in JSON are almost the same as arrays in JavaScript.

In JSON, array values must be of type string, number, object, array, boolean or null.
In JavaScript, array values can be all of the above, plus any other valid JavaScript expression, including functions, dates, and undefined.

### JavaScript Arrays
You can create a JavaScript array from a literal:

Example
myArray = ["Ford", "BMW", "Fiat"];
You can create a JavaScript array by parsing a JSON string:

Example
myJSON = '["Ford", "BMW", "Fiat"]';
myArray = JSON.Parse(myJSON);
Accessing Array Values
You access array values by index:

Example
myArray[0];
Arrays in Objects
Objects can contain arrays:
```
Example
{
"name":"John",
"age":30,
"cars":["Ford", "BMW", "Fiat"]
}
You access array values by index:

Example
myObj.cars[0];

Looping Through an Array
You can access array values by using a for in loop:

Example
for (let i in myObj.cars) {
  x += myObj.cars[i];
}
Or you can use a for loop:

Example
for (let i = 0; i < myObj.cars.length; i++) {
  x += myObj.cars[i];
}
```
***
## JSON Server
A common use of JSON is to exchange data to/from a web server.
When receiving data from a web server, the data is always a `string.`
Parse the data with JSON.parse(), and the data becomes a `JavaScript object.`

### Sending Data
If you have data stored in a JavaScript object, you can convert the object into JSON, and send it to a server:

Example
```
const myObj = {name: "John", age: 31, city: "New York"};
const myJSON = JSON.stringify(myObj);
window.location = "demo_json.php?x=" + myJSON;
```

### Receiving Data
If you receive data in JSON format, you can easily convert it into a JavaScript object:

Example
```
const myJSON = '{"name":"John", "age":31, "city":"New York"}';
const myObj = JSON.parse(myJSON);
document.getElementById("demo").innerHTML = myObj.name;
```
### JSON From a Server
You can request JSON from the server by using an AJAX request
As long as the response from the server is written in JSON format, you can parse the string into a JavaScript object.

Example
Use the XMLHttpRequest to get data from the server:
```
const xmlhttp = new XMLHttpRequest();
xmlhttp.onload = function() {
  const myObj = JSON.parse(this.responseText);
  document.getElementById("demo").innerHTML = myObj.name;
};
xmlhttp.open("GET", "json_demo.txt");
xmlhttp.send();
```
### Array as JSON
When using the JSON.parse() on JSON derived from an array, the method will return a JavaScript array, instead of a JavaScript object.

Example
JSON returned from a server as an array:
```
const xmlhttp = new XMLHttpRequest();
xmlhttp.onload = function() {
  const myArr = JSON.parse(this.responseText);
  document.getElementById("demo").innerHTML = myArr[0];
  }

}
xmlhttp.open("GET", "json_demo_array.txt", true);
xmlhttp.send();
```
***
## JSON PHP
A common use of JSON is to read data from a web server, and display the data in a web page.
This chapter will teach you how to exchange JSON data between the client and a PHP server.

### The PHP File
PHP has some built-in functions to handle JSON.
Objects in PHP can be converted into JSON by using the PHP function json_encode():

### PHP file
```
<?php
$myObj->name = "John";
$myObj->age = 30;
$myObj->city = "New York";

$myJSON = json_encode($myObj);

echo $myJSON;
?>
```
### The Client JavaScript
Here is a JavaScript on the client, using an AJAX call to request the PHP file from the example above:
Example
Use JSON.parse() to convert the result into a JavaScript object:
```
const xmlhttp = new XMLHttpRequest();
xmlhttp.onload = function() {
  const myObj = JSON.parse(this.responseText);
  document.getElementById("demo").innerHTML = myObj.name;
}
xmlhttp.open("GET", "demo_file.php");
xmlhttp.send();
```

### PHP Array
Arrays in PHP will also be converted into JSON when using the PHP function json_encode():

### PHP file
```
<?php
$myArr = array("John", "Mary", "Peter", "Sally");

$myJSON = json_encode($myArr);

echo $myJSON;
?>
```
### The Client JavaScript
Here is a JavaScript on the client, using an AJAX call to request the PHP file from the array example above:

Example
Use JSON.parse() to convert the result into a JavaScript array:
```
var xmlhttp = new XMLHttpRequest();
xmlhttp.onload = function() {
  const myObj = JSON.parse(this.responseText);
  document.getElementById("demo").innerHTML = myObj[2];
}
xmlhttp.open("GET", "demo_file_array.php", true);
xmlhttp.send();
```
### PHP Database
PHP is a server side programming language, and can be used to access a database.

Imagine you have a database on your server, and you want to send a request to it from the client where you ask for the 10 first rows in a table called "customers".

On the client, make a JSON object that describes the numbers of rows you want to return.

Before you send the request to the server, convert the JSON object into a string and send it as a parameter to the url of the PHP page:

Example
Use JSON.stringify() to convert the JavaScript object into JSON:
```
const limit = {"limit":10};
const dbParam = JSON.stringify(limit);
xmlhttp = new XMLHttpRequest();
xmlhttp.onload = function() {
  document.getElementById("demo").innerHTML = this.responseText;
}
xmlhttp.open("GET","json_demo_db.php?x=" + dbParam);
xmlhttp.send();
```
Example explained:
```
Define an object containing a "limit" property and value.
Convert the object into a JSON string.
Send a request to the PHP file, with the JSON string as a parameter.
Wait until the request returns with the result (as JSON)
Display the result received from the PHP file.
```
Take a look at the PHP file:

PHP file
```
<?php
header("Content-Type: application/json; charset=UTF-8");
$obj = json_decode($_GET["x"], false);

$conn = new mysqli("myServer", "myUser", "myPassword", "Northwind");
$stmt = $conn->prepare("SELECT name FROM customers LIMIT ?");
$stmt->bind_param("s", $obj->limit);
$stmt->execute();
$result = $stmt->get_result();
$outp = $result->fetch_all(MYSQLI_ASSOC);

echo json_encode($outp);
?>
```
PHP File explained:
```
Convert the request into an object, using the PHP function json_decode().
Access the database, and fill an array with the requested data.
Add the array to an object, and return the object as JSON using the json_encode() function.
Use the Data
```
Example
```
xmlhttp.onload = function() {
  const myObj = JSON.parse(this.responseText);
  let text = "";
  for (let x in myObj) {
    text += myObj[x].name + "<br>";
  }
  document.getElementById("demo").innerHTML = text;
}
PHP Method = POST
```
When sending data to the server, it is often best to use the HTTP POST method.

To send AJAX requests using the POST method, specify the method, and the correct header.

The data sent to the server must now be an argument to the send() method:

Example
```
const dbParam = JSON.stringify({"limit":10});
const xmlhttp = new XMLHttpRequest();
xmlhttp.onload = function() {
  const myObj = JSON.parse(this.responseText);
  let text ="";
  for (let x in myObj) {
    text += myObj[x].name + "<br>";
  }
  document.getElementById("demo").innerHTML = text;
}
xmlhttp.open("POST", "json_demo_db_post.php");
xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
xmlhttp.send("x=" + dbParam);
```
The only difference in the PHP file is the method for getting the transferred data.

### PHP file
Use `$_POST` instead of `$_GET`:
```
<?php
header("Content-Type: application/json; charset=UTF-8");
$obj = json_decode($_POST["x"], false);

$conn = new mysqli("myServer", "myUser", "myPassword", "Northwind");
$stmt = $conn->prepare("SELECT name FROM customers LIMIT ?");
$stmt->bind_param("s", $obj->limit);
$stmt->execute();
$result = $stmt->get_result();
$outp = $result->fetch_all(MYSQLI_ASSOC);

echo json_encode($outp);
?>
```
***
## JSON HTML
JSON can very easily be translated into JavaScript.

JavaScript can be used to make HTML in your web pages.

HTML Table
Make an HTML table with data received as JSON:

Example
```
const dbParam = JSON.stringify({table:"customers",limit:20});
const xmlhttp = new XMLHttpRequest();
xmlhttp.onload = function() {
  myObj = JSON.parse(this.responseText);
  let text = "<table border='1'>"
  for (let x in myObj) {
    text += "<tr><td>" + myObj[x].name + "</td></tr>";
  }
  text += "</table>"
  document.getElementById("demo").innerHTML = text;
}
xmlhttp.open("POST", "json_demo_html_table.php");
xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
xmlhttp.send("x=" + dbParam);
```
```
Dynamic HTML Table
Make the HTML table based on the value of a drop down menu: 
Choose an option:
```

Example
<select id="myselect" onchange="change_myselect(this.value)">
  <option value="">Choose an option:</option>
  <option value="customers">Customers</option>
  <option value="products">Products</option>
  <option value="suppliers">Suppliers</option>
</select>

<script>
function change_myselect(sel) {
  const dbParam = JSON.stringify({table:sel,limit:20});
  const xmlhttp = new XMLHttpRequest();
  xmlhttp.onload = function() {
    const myObj = JSON.parse(this.responseText);
    let text = "<table border='1'>"
    for (let x in myObj) {
      text += "<tr><td>" + myObj[x].name + "</td></tr>";
    }
    text += "</table>"
    document.getElementById("demo").innerHTML = text;
  }
  xmlhttp.open("POST", "json_demo_html_table.php");
  xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xmlhttp.send("x=" + dbParam);
}
</script>
ADVERTISEMENT

HTML Drop Down List
Make an HTML drop down list with data received as JSON:

Example
```
const dbParam = JSON.stringify({table:"customers",limit:20});
const xmlhttp = new XMLHttpRequest();
xmlhttp.onload = function() {
  const myObj = JSON.parse(this.responseText);
  let text = "<select>"
  for (let x in myObj) {
    text += "<option>" + myObj[x].name + "</option>";
  }
  text += "</select>"
  document.getElementById("demo").innerHTML = text;
  }
}
xmlhttp.open("POST", "json_demo_html_table.php", true);
xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
xmlhttp.send("x=" + dbParam);
```
***
## JSONP
`JSONP` is a method for sending JSON data without worrying about cross-domain issues.
`JSONP` does not use the XMLHttpRequest object.
JSONP uses the `<script>` tag instead.

### JSONP Intro
JSONP stands for `JSON with Padding`.
Requesting a file from another domain can cause problems, due to cross-domain policy.
Requesting an external script from another domain does not have this problem.
JSONP uses this advantage, and request files using the script tag instead of the XMLHttpRequest object.
```
<script src="demo_jsonp.php">
```
### The Server File
The file on the server wraps the result inside a function call:

Example
```
<?php
$myJSON = '{ "name":"John", "age":30, "city":"New York" }';

echo "myFunc(".$myJSON.");";
?>
```
The result returns a call to a function named "myFunc" with the JSON data as a parameter.
Make sure that the function exists on the client.

The JavaScript function
The function named "myFunc" is located on the client, and ready to handle JSON data:

Example
```
function myFunc(myObj) {
  document.getElementById("demo").innerHTML = myObj.name;
}
```



