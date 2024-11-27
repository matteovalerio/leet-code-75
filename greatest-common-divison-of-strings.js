var gcdOfStrings = function (str1, str2) {
  if (str1 + str2 !== str2 + str1) return "";
  const gcdLength = gcd(str1.length, str2.length)

  return str1.substring(0, gcdLength)

  function gcd(x, y){
    if(y === 0){
        return x
    }
    return gcd(y, x%y)
  }
};

console.log(gcdOfStrings("ABCABC", "ABC"));
console.log(gcdOfStrings("ABABAB", "ABAB"));
console.log(gcdOfStrings("ABAB", "ABABAB"));
console.log(gcdOfStrings("LEET", "CODE"));
console.log(gcdOfStrings("ABCDEF", "ABC"));
