exports.caesarCipher = function(string, index) {
    let alphaLow = 'abcdefghijklmnopqrstuvwxyz';
    let alphaUp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    let result = [];
    let i = 0;
    // iterate over string
    while (i < string.length){
      // if not a letter
      // could also do regex
      if (((alphaLow.indexOf(string[i]) === -1)) && ((alphaUp.indexOf(string[i]) === -1))){
        result.push(string[i]);
        i++;
        continue;
      }
      // Could also set an uppercase = True/False and use only one block of code
      // easier to do with charCode
      // if lowercase
      if (string[i] !== string[i].toUpperCase()){
          let letterIndex = alphaLow.indexOf(string[i]);
          // if shifted letter index is less than zero, add 26
        if ((letterIndex + index) < 0){
          letterIndex += 26;
          result.push(alphaLow[letterIndex + index]);
          // if shifted letter index is greater than 26, subtract 26
        } else if ((letterIndex + index) > 26){
          letterIndex -= 26
          result.push(alphaLow[letterIndex + index]);
          // if shifted index is between 0 and 26, use original index
        } else {
          result.push(alphaLow[letterIndex + index]);
        } 
      }
      // if uppercase	
      if (string[i] === string[i].toUpperCase()){
          let letterIndex = alphaUp.indexOf(string[i]);
        if ((letterIndex + index) < 0){
          letterIndex += 26;
          result.push(alphaUp[letterIndex + index]);
        } else if ((letterIndex + index) > 26){
          letterIndex -= 26
          result.push(alphaUp[letterIndex + index]);
        } else {
          result.push(alphaUp[letterIndex + index]);
        } 
      }
      i++;
    }
    return result.join('');
};
//console.log(exports.caesarCipher("What a string!", 5))