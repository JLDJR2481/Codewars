function apple(x){
    if(x**2 > 1000){
      return "It's hotter than the sun!!"
    }
    else{
      return "Help yourself to a honeycomb Yorkie for the glovebox."
    }
  }



console.log('Testing')
if (apple('50') !== "It's hotter than the sun!!"){
    throw Error
}
if (apple(4) !== 'Help yourself to a honeycomb Yorkie for the glovebox.'){
    throw Error
}

console.log('Success!')
