function findDifference(a, b) {
    let total_a = 1;
    let total_b = 1;
    for (var i = 0; i < a.length; i++){
        total_a = total_a * a[i]
    }
    for(var i = 0; i < b.length; i++){
        total_b = total_b * b[i]
    }

    let difference = (total_a - total_b)
    if (difference < 0){
        return (difference * -1)
    }
    else{
        return difference
    }
}




console.log('Testing')
if(findDifference([3, 2, 5], [1, 4, 4]) !== 14){throw Error}

if (findDifference([9, 7, 2], [5, 2, 2]) !== 106){throw Error}

if (findDifference([11, 2, 5], [1, 10, 8])!== 30){throw Error}

if (findDifference([4, 4, 7], [3, 9, 3]) !== 31){throw Error}

if (findDifference([15, 20, 25], [10, 30, 25]) !== 0){throw Error}

if (findDifference([29, 8, 22], [30, 18, 22]) !== 6776){throw Error}

console.log('Success!')