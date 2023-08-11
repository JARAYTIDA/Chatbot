const array = []

async function postData(url = "", data = {}) { 
    const response = await fetch(url, {
        method: "POST", headers: {
            "Content-Type": "application/json", 
        }, body: JSON.stringify(data),  
    });
    return response.json(); 
}

sendButton.addEventListener("click", async ()=>{ 
    console.log("hey you clicked")
    questionInput = document.getElementById("questionInput").value
    document.getElementById("questionInput").value = ""
    document.querySelector(".right2").style.display = "block"
    document.querySelector(".right1").style.display = "none"
    question.innerHTML = questionInput
    let result = await postData("/api", {"question": questionInput})
    solution.innerHTML = result.result
    array.push({"Question": questionInput, "Answer":result.result})
})

askAgain.addEventListener("click", async () => {
    console.log("hey you clicked")
    questionInput = document.getElementById("questionInput").value
    document.getElementById("questionInput").value = ""
    document.querySelector(".right2").style.display = "block"
    document.querySelector(".right1").style.display = "none"
    question.innerHTML = questionInput
    let result = await postData("/api", {"question": questionInput})
    solution.innerHTML = result.result
    array.push({"Question": questionInput, "Answer":result.result})
})

document.getElementById('right2').innerHTML = array.map(mp => (
    question.innerHTML = mp.Question,
    solution.innerHTML = mp.Answer
)
).join('')