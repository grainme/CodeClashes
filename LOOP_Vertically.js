
const t = parseInt(readline());
const g = parseInt(readline());
const h = parseInt(readline());
arr = []
for (let i = 0; i < h; i++) {
    const ROW = readline();
    for (let j=0; j < ROW.length; j+=2){
        if (arr.length <= (j/2)){
            arr.push(ROW[j] == '#' ? 1 : 0)
        }
        else{
            arr[(j/2)] = ROW[j] == '#' ? arr[(j/2)] + 1 : arr[(j/2)];
        }
    }
}

console.error(arr)

arr = arr.map(a => a+(t*g))


console.log(arr.join(" "));
