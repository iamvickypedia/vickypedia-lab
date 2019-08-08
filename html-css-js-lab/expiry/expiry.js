
function dailyAllowance() {
  // the function is working but we need to check for the incognito workaround(it resets the counter in incognito)
  if(notSameAsDummy()){
    if(localStorage.C_OUT && localStorage.C_OUT_expiresIn){
      var C_OUT = parseInt(localStorage.C_OUT)
      var C_OUT_expiresIn = parseInt(localStorage.C_OUT_expiresIn)
      // console.log(C_OUT,C_OUT_expiresIn)
      if(C_OUT_expiresIn > Date.now()){ // if not expired can check for count
        console.log('Not Expired')
        if(C_OUT >= 5){
          return false
        }else if(C_OUT < 0){
          console.log('here')
          SetStorage("C_OUT", 1, 1); // reset the counter in case of any mishap
          return true
        }else{//when value is between 5 and 0
          DecreaseAllowance("C_OUT")
        }
      }else{
        SetStorage("C_OUT", 1, 1)
      }
    }else{
      SetStorage("C_OUT", 1, 1)
    }
    return true
  }else{
    return true
  }
}

function notSameAsDummy(){
  var dummy_text = "Another simple test for discrimination of whether a reduced viability signal is caused by direct cytotoxicity (apoptosis or necrosis) or by inhibition of proliferation also employs metabolic viability tests such as the MTT assay. For this purpose multiple readings at different time points following illumination are performed. The viability signals obtained at each time point are related to the initial (t = 0 hrs) value and the resulting temporal dynamics of the signal for each treatment condition can be evaluated as follows: a decrease below the initial value can be interpreted as a direct cytotoxic effect as the absolute viability signal decreases. A constant viability signal (in the range of the initial value) indicates inhibition of proliferation, whereas a signal increasing relative to the initial value (similar to untreated controls in most cases) indicates proliferation. Clearly, as a sum measurement this test design cannot discriminate between the modes of cytotoxicity in absolute terms (i.e., single-cell level). However, it may assist in the interpretation in a situation where the endpoint viability measurement (e.g., 24 hrs p.i.) indicates a viability signal smaller than the untreated controls since this reduction could be solely attributed to growth inhibition without any apoptosis/necrosis induction, that is, direct cytotoxicity."
  var input_text = $("#editable").summernote('code')

  return !(input_text === dummy_text)
}

function DecreaseAllowance(key){
  var value = parseInt(localStorage.getItem(key));
  localStorage.setItem(key, value+1);
}

function SetStorage(key, value, expires){
  if (expires===undefined || expires===null) {
        expires = (24*60*60);  // default: seconds for 1 day
    } else {
        expires = (24*60*60)*Math.abs(expires); //make sure it's positive
    }
    var now = Date.now();  //millisecs since epoch time, lets deal only with integer
    var schedule = now + expires*1000;
    try {
        localStorage.setItem(key, value);
        localStorage.setItem(key + '_expiresIn', schedule);
    } catch(e) {
        // console.log('setStorage: Error setting key ['+ key + '] in localStorage: ' + JSON.stringify(e) );
        return false;
    }
    return true;
}

function wordCountApi() {
    cleanText = $("#editable").summernote('code').replace(/<\/p>/gi, "\n").replace(/<br\/?>/gi, "\n")
        .replace(/<\/?[^>]+(>|$)/g, "").replace(/&nbsp;/g, " ")
    splitedList = cleanText.split(/ |\n/g)
    if (splitedList[0] == "\n" || splitedList[0] == "") {
        splitedList.splice(0, 1)
    }
    for (let index = 0; index < splitedList.length; index++) {
        if (splitedList[index] == "") {
            splitedList.splice(index, 1)
            index -= 1;
        }

    }
    wordCount = splitedList.length;
    $('#wordCount').text(wordCount);
    return wordCount;
}
