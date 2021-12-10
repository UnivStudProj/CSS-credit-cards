let main = document.getElementById("main");
// deleting input tag
let input = document.getElementsByTagName("input");
input[0].remove();
// whole card
let card = document.createElement("div");
card.className = "card";
main.appendChild(card);
// card inner
let card_inner = document.createElement("div");
card_inner.className = "card-inner";
card.appendChild(card_inner);
// front of the card
let front = document.createElement("div");
front.className = "front";
card_inner.appendChild(front);
// world img
let map = document.createElement("img");
map.className = "map";
map.src = 'images/map.png';
front.appendChild(map);
// line for a chip image
let row1 = document.createElement("div");
row1.className = "row";
front.append(row1);
// chip image
let chip = document.createElement("img");
chip.src = 'images/chip.png';
chip.style.width = '60px';
row1.appendChild(chip);
// visa title
let visa = document.createElement("img");
visa.src = 'images/visa.png';
visa.style.width = '80px';
row1.appendChild(visa);
// card number row
let row2 = document.createElement("div");
row2.className = "row card-no";
front.appendChild(row2);
// card number
for (let i = 0; i < 4; i++) {
    let p = document.createElement("p");
    n = String(Math.floor(Math.random() * 9999));
    while (n.length != 4) {
        n = "0" + n.substr(0, n.length); 
    }
    p.innerHTML = n;
    row2.appendChild(p);
}
// card holder and valid date
let row3 = document.createElement("div");
row3.className = "row card-holder";
front.appendChild(row3);
let p_title = document.createElement("p");
p_title.innerHTML = "CARD HOLDER";
row3.appendChild(p_title);
let p_name = document.createElement("p");
p_name.innerHTML = "VALLID TILL";
row3.appendChild(p_name);
// card holder and valid date values
let row4 = document.createElement("div");
row4.className = "row";
front.appendChild(row4);
let p_title_value = document.createElement("p");
p_title_value.innerHTML = "JOE ALISON";
row4.appendChild(p_title_value);
let p_name_value = document.createElement("p");
p_name_value.innerHTML = "10 / 25";