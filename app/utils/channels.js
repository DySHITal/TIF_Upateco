const exChannel = document.getElementById('explore');
const containerCanal = document.getElementById('container_canal');
const parrafo = document.getElementById('empty')

let visible = false;

exChannel.addEventListener('click', () => {
    if(visible){
        parrafo.style.display = 'block'
        containerCanal.style.display = 'none';
    } else{
        containerCanal.style.display = 'grid';
        parrafo.style.display = 'none'
    }
    visible = !visible
})