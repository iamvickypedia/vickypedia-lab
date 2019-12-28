function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function writeText(){
    
    const text = document.querySelector(".animText")
    const strText = text.textContent; 
    const arrText = strText.split("");
    text.textContent = "";
    for(i=0;i<arrText.length;i++){
        text.innerHTML += "<span>"+arrText[i]+"</span>"
        // await sleep(500);
    }
    let count = 0;
    let timer = setInterval(onTick,80);
    function onTick(){
        // console.log(count)
        const span = text.querySelectorAll("span")[count]
        span.classList.remove("active");
        span.classList.add("active");
        // count = (count%text.querySelectorAll("span").length) + 1
        if(count == text.querySelectorAll("span").length-1){
            return
        }else{
            count++
        }
        // console.log(count,text.querySelectorAll("span").length)
    };
}
writeText()