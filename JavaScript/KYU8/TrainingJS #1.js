function helloWorld(){
    let str = 'Hello World!'
    return str
}




console.log('Testing!')
if (helloWorld() !== 'Hello World!'){
    throw Error
}

console.log('Success!')