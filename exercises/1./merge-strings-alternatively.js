/* 
You are given two strings word1 and word2. 
Merge the strings by adding letters in alternating order, starting with word1.
If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
*/
function mergeAlternately(word1, word2) {
  const maxLength = Math.max(word1.length, word2.length);
  
  let res = "";
  for (let i = 0; i < maxLength; i++) {
    res += word1.charAt(i);
    res += word2.charAt(i);
  }

  return res;
}

const res1 = mergeAlternately("abcd", "pq");
console.log(res1);
