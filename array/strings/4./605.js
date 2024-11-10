// You have a long flowerbed in which some of the plots are planted, and some are not.
// However, flowers cannot be planted in adjacent plots.
// Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n,
// return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

/*
L'idea è di cercare di inserire il numero 1 nell'array per n volte
[1,0,0,0,0,1]
filter == 0
[0.0.0.]

alternativamente
come calcolo il numero di posti liberi?
[1,0,0,0,0,1] => 1 posto libero
if el = 0 => incrementa il counter di 1 se ci sono fino a 3 zeri dopo, aggiorna l'indice e prosegui
*/
/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function (flowerbed, n) {
  let emptyPlotsCount = 0;
  for (let index = 0; index < flowerbed.length; index++) {
    const element = flowerbed[index];

    if (element == 1) continue;
    if (index === flowerbed.length - 1) break;

    // 0 0 => 0
    // 0 0 0 => 1
    // 0 0 0 0 => 1
    // 0 0 0 0 0 => 0 1 0 1 0 => 2
    // 0 0 0 0 0 0 => 0 1 0 1 0 0 => 2
    // 0 0 0 0 0 0 0 => 0 1 0 1 0 1 0 => 3
    let zerosCounter = 0;
    for (let j = index; j < flowerbed.length; j++) {
      const element = flowerbed[j];
      if (element === 1) {
        index = j;
        break;
      }
      zerosCounter++;
    }
    console.log(zerosCounter, n)
    emptyPlotsCount += Math.ceil(zerosCounter / 3)
  }
  return emptyPlotsCount >= n
};


console.log(canPlaceFlowers([1,0,0,0,1], 1)) // true
console.log(canPlaceFlowers([1,0,0,0,1], 2)) // false
console.log(canPlaceFlowers([1,0,0,0,0,1], 2)) // false
console.log(canPlaceFlowers([1,0,0,0,0,0,1], 2)) //true