/* create a string to say hello in the format: "Hello, {{name}}".
Ex. printHellName("Mosh"), return "Hello, Mosh!"
*/
function printHellName(name){
    return "hello" + name + "!"
}
printHellName("Mosh")
console.log(printHellName())



const printHelloNameTests= [
    {args:["Mosh"], expected: "Hello, Mosh!"},
    {args: [""], expected: "hello, !"} 
]