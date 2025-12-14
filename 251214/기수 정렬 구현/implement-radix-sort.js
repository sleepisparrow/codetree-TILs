

const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');

const n = Number(input[0]);
let arr = input[1].split(' ').map(Number);

// Please write your code here.

// k 구하기
let max = Math.max(...arr)
let k = 0

while (max >= 1) {
    k++
    max /= 10
}

// sort
for(let target = 0; target < k; target++) {
    // radixArr setting
    const radixArr = []
    for(let i = 0; i < 10; i++)
        radixArr.push([])

    // sort by ith number
    for(let i = 0; i < n; i++) {
        
        let ith = Math.floor(arr[i] / Math.pow(10, target)) % 10
        radixArr[ith].push(arr[i])
    }

    // make radixArr to 1 demension arr
    let ret = []
    for(let i = 0; i < 10; i++) {
        for(let j = 0; j < radixArr[i].length; j++) {
            ret.push(radixArr[i][j])
        }
    }

    arr = ret
}

for (let i = 0; i < n; i++) {
    process.stdout.write(arr[i]+" ")
}