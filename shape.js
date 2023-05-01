function sendEmailTo(person) {
    console.log("Sending email to ".concat(person.name, " at ").concat(person.email));
}
var person = {
    name: "dom",
    age: 25,
    email: "dom@h"
};
sendEmailTo(person);
