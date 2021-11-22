function ajustarTexto(elemento){
    let teste = elemento.textContent.split("\n");
    elemento.innerHTML = "";
    let lista = document.createElement("ul");
    teste.forEach(text => {
        if(text.indexOf("<lista-item>") == -1){
            let t = document.createElement("text");
            t.textContent = text;
            elemento.appendChild(t);
            elemento.appendChild(document.createElement("br"));
        }else{
            let li = document.createElement("li");
            let b = document.createElement("b");
            b.textContent = text.split("<lista-item>")[1]
            li.appendChild(b);
            lista.appendChild(li);
            lista.appendChild(document.createElement("br"));
            elemento.appendChild(lista);
        }
    })
}

window.onload = () => {
    let corpo = document.querySelector(".pub-corpo-text");
    ajustarTexto(corpo);
    let secao1 = document.querySelector(".pub-secao1").querySelector(".pub-corpo-text");
    ajustarTexto(secao1);    
    let secao2 = document.querySelector(".pub-secao2").querySelector(".pub-corpo-text");
    ajustarTexto(secao2);    
    let refs = document.querySelector(".pub-referencias").querySelector(".pub-corpo-text");
    ajustarTexto(refs);    
    
}