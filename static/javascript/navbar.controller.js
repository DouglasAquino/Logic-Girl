var menu_aberto = false;

function menuPC(){
    menu_aberto = false;
    let menu = document.querySelector(".menu");
    let itens = document.querySelectorAll(".btn-menu");
    menu.style["position"] = "initial";   
    menu.style["flex-direction"] = "row";
    menu.style["width"] = "50%";
    menu.style["background-color"] = "transparent";
    itens.forEach((item) => {
        if(item.className == "btn-menu sel"){
            item.style["color"] = "#25B80A";
        }else{
            item.style["color"] = "black";
        }
    })
}

function menuMobile(){
    let menu = document.querySelector(".menu");
    let itens = document.querySelectorAll(".btn-menu");
    menu.style["z-index"] = 2;
    menu.style["position"] = "fixed";   
    menu.style["top"] = "0px";
    menu.style["left"] = "-100%";
    menu.style["flex-direction"] = "column";
    menu.style["width"] = "100%";
    menu.style["background-color"] = "#30444E";
    itens.forEach((item) => {
        if(item.className == "btn-menu sel"){
            item.style["color"] = "#25B80A";
        }else{
            item.style["color"] = "white";
        }
    })
}

function abrirMenu(){
    menu_aberto = !menu_aberto;
    let btn_menu = document.querySelector(".btn-menu-mobile");
    let menu = document.querySelector(".menu");
    if(menu_aberto){
        menu.style["left"] = "0px";
        btn_menu.style["z-index"] = 3;
        btn_menu.querySelector("i").style["color"] = "white";
        btn_menu.querySelector("i").style["font-size"] = "40px";
        btn_menu.childNodes[0].className = "fas fa-times";
    }else{
        menu.style["left"] = "-100%";
        btn_menu.childNodes[0].className = "fas fa-bars";
        btn_menu.querySelector("i").style["color"] = "black";
        btn_menu.querySelector("i").style["font-size"] = "20px";
    }
}

function TamanhoTela(){
    largura = screen.width;
    let btn_menu = document.querySelector(".btn-menu-mobile");
    if(largura < 750){
        btn_menu.hidden = false;
        menuMobile();
    }else{
        btn_menu.hidden = true;
        menuPC();
    }
}

window.onload = () => {
    TamanhoTela();
    document.querySelector(".btn-menu-mobile").addEventListener("click",abrirMenu);
    window.addEventListener("resize",TamanhoTela);
}