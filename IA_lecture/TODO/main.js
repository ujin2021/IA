const container = document.querySelector(".container"); //item 들어가는 부분, const = 한번 선언했을 때 변할수 없는 상수
let inputValue = document.querySelector(".input"); //입력칸, let(var)으로 선언시 변경가능
const add = document.querySelector('.add'); // plus 부분

if(window.localStorage.getItem('todos') == undefined){
    let todos = [];
    window.localStorage.setItem('todos', JSON.stringify(todos)); //json형태로 서버와 주고받음(stringify->string형태로)
}

let todosEX = window.localStorage.getItem('todos');
let todos = JSON.parse(todosEX);

class item{
    constructor(name){ //constructor : 초기화나 생성할때 사용
        this.createItem(name);
    }
    createItem(name){
        let itemBox = document.createElement('div'); //createElement로 한줄을 만들수 있다.
        itemBox.classList.add('item');

        let input = document.createElement('input'); //input field 생성
        input.type = 'text'
        input.value = name;
        input.classList.add('item_input');

        let edit = document.createElement('button'); //수정할 것
        edit.classList.add('edit');
        edit.innerHTML = 'EDIT'; //innerHTML : html안에 글자를 넣는것
        edit.addEventListener('click', () => this.edit(input, name)); //click시 event가 발생하도록

        let remove = document.createElement('button');
        //추가해주세요 youtube 0:52강의부터 ~

        container.appendChild(itemBox); //html container class 안에 itembox추가

        itemBox.appendChild(input);
        itemBox.appendChild(edit);
    }

    edit(input, name){
        if(input.disabled == true){ //건드릴 수 없을 땐
            input.disabled = !input.disabled; //건드릴 수 있도록
        }
        else{
            input.disabled = !input.disabled; //수정할 수 있을 땐
            let indexof = todos.indexof(name); //수정한다음
            todos[indexof] = input.value;
            window.localStorage.setItem('todos', JSON.stringify(todos)); //local storage에 저장
        }
    }
}

add.addEventListener('click', check); //click하면 추가하겠다
window.addEventListener('keydown', (e) => {
    if (e.which == 13){
        check();
    }
})

function check(){
    if (inputValue.value != ''){
        new item(inputValue.value);
        todos.push(inputValue.value);
        window.localStorage.setItem('todos', JSON.stringify(todos));
        inputValue.value = '';
    }
}

for (let v = 0; v < todos.length; v++){
    new item(todos[v]);
}

new item('sport');