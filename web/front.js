for (let j = 0; j < 2; j++) {
    // deleting label tag
    if (j == 0) {
        var label = document.getElementsByTagName("label");
        label[0].remove();
        }
    // creating container
    var container = document.createElement("div");
    container.className = "container";
    document.querySelector(".main").appendChild(container);
    // whole card
    var card = document.createElement("div");
    card.className = "card";
    container.appendChild(card);
    // card inner
    var card_inner = document.createElement("div");
    card_inner.className = "card-inner";
    card.appendChild(card_inner);
    // front of the card
    var front = document.createElement("div");
    front.className = "front";
    card_inner.appendChild(front);
    // world img
    var map = document.createElement("img");
    map.className = "map";
    map.src = 'images/map.png';
    front.appendChild(map);
    // line for a chip image
    var row1 = document.createElement("div");
    row1.className = "row";
    front.append(row1);
    // chip image
    var chip = document.createElement("img");
    chip.src = 'images/chip.png';
    chip.style.width = '60px';
    row1.appendChild(chip);
    // visa title
    var visa = document.createElement("img");
    visa.src = 'images/visa.png';
    visa.style.width = '80px';
    row1.appendChild(visa);
    // card number row
    var row2 = document.createElement("div");
    row2.className = "row card-no";
    front.appendChild(row2);
    // card number
    for (var i = 0; i < 4; i++) {
        var p = document.createElement("p");
        n = String(Math.floor(Math.random() * 9999));
        while (n.length != 4) {
            n = "0" + n.substr(0, n.length); 
        }
        p.innerHTML = n;
        row2.appendChild(p);
    }
    // card holder and valid date
    var row3 = document.createElement("div");
    row3.className = "row card-holder";
    front.appendChild(row3);
    var p_title = document.createElement("p");
    p_title.innerHTML = "CARD HOLDER";
    row3.appendChild(p_title);
    var p_name = document.createElement("p");
    p_name.innerHTML = "VALLID TILL";
    row3.appendChild(p_name);
    // card holder and valid date values
    var row4 = document.createElement("div");
    row4.className = "row";
    front.appendChild(row4);
    var p_title_value = document.createElement("p");
    p_title_value.innerHTML = "JOE ALISON";
    row4.appendChild(p_title_value);
    var p_name_value = document.createElement("p");
    p_name_value.innerHTML = "10 / 25";
    row4.appendChild(p_name_value);
}