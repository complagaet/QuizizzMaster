let InfoScreen = {
    create(data) {
        if (!document.getElementById("SchAT")) {
            let divElement = document.createElement("div")
            divElement.id = "SchAT"

            divElement.innerHTML += `
                <div style="
                    display: flex;
                    gap: 15px; 
                    position: fixed; 
                    z-index: 9999; 
                    background-color: #9bc5f7; 
                    height: fit-content; 
                    min-width: 100px;
                    width: fit-content;
                    top: 20px;
                    left: 20px;
                    padding: 15px 25px 15px 15px" class="bobatron" Bt-CM="1.4">
                    <div style="height: 100px; width: 100px; background-image: url('https://i.imgur.com/4nsOYag.jpeg'); background-size: contain" class="bobatron"></div>
                    <div style="display: flex; flex-direction: column; gap: 5px; justify-content: space-between">
                        <div style="margin: 0; padding: 0; font-weight: bold">QuizzizMaster</div>
                        <div style="padding: 0; margin: 0" id="SchATData">${data}</div>
                    </div>
                </div>
            `

            document.getElementsByTagName("body")[0].appendChild(divElement);
            bobatron.scanner()
        } else { InfoScreen.update(data) }
    },
    update(data) {
        document.getElementById("SchATData").innerHTML = data
        bobatron.scanner()
    }
};