window.onload = () => {
    let corpo = document.querySelector(".pub-corpo-text");
    let teste = corpo.textContent.split("\n");
    corpo.innerHTML = "";
    teste.forEach(text => {
        let t = document.createElement("text");
        t.textContent = text;
        corpo.appendChild(t);
        corpo.appendChild(document.createElement("br"));
    })
    let secao1 = document.querySelector(".pub-secao1").querySelector(".pub-corpo-text");
    let sec = secao1.textContent.split("\n");
    secao1.innerHTML = "";
    console.log(sec)
    sec.forEach(text => {
        let t = document.createElement("text");
        t.textContent = text;
        secao1.appendChild(t);
        secao1.appendChild(document.createElement("br"));
    })
    let secao2 = document.querySelector(".pub-secao2").querySelector(".pub-corpo-text");
    let sec2 = secao2.textContent.split("\n");
    secao2.innerHTML = "";
    sec2.forEach(text => {
        let t = document.createElement("text");
        t.textContent = text;
        secao2.appendChild(t);
        secao2.appendChild(document.createElement("br"));
    })
    let refs = document.querySelector(".pub-referencias").querySelector(".pub-corpo-text");
    let refst = refs.textContent.split("\n");
    refs.innerHTML = "";
    refst.forEach(text => {
        let t = document.createElement("text");
        t.textContent = text;
        refs.appendChild(t);
        refs.appendChild(document.createElement("br"));
    })
}