// const person = {
//     name: "John",
//     age: 30,
//     email: "john@example.com"
//   };
interface Person {
    name: string;
    age: number;
    email: string;
}

function sendEmailTo(person: Person): void {
    console.log(`Sending email to ${person.name} at ${person.email}`);
}

const person: Person = {
    name: "dom",
    age: 25,
    email: "dom@h"
}
sendEmailTo(person)