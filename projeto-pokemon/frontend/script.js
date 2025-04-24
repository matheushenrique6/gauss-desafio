let currentPage = 1;
const limit = 10;
let currentData = [];
let filteredData = [];


async function fetchData() {
    const res = await fetch(`http://localhost:8000/pokemons?skip=0&limit=10000`);
    const data = await res.json();
    currentData = data;
    filteredData = data; 
    renderTable(getPageData());
}
function getPageData() {
    const start = (currentPage - 1) * limit;
    const end = start + limit;
    return filteredData.slice(start, end);
}



function renderTable(data) {
    const tbody = document.querySelector("#pokemon-table tbody");
    tbody.innerHTML = "";
    data.forEach((pokemon) => {
        const row = `
            <tr>
                <td><img src="${pokemon.sprite_url}" alt="${pokemon.name}" width="50"></td>
                <td>${pokemon.name}</td>
                <td>${pokemon.height}</td>
                <td>${pokemon.weight}</td>
                <td>${pokemon.base_experience}</td>
                <td>${pokemon.types}</td>
            </tr>`;
        tbody.innerHTML += row;
    });
    document.getElementById("page-indicator").innerText = `Página ${currentPage}`;
}


function sortTable(column) {
    const key = column === 0 ? "name" : "url" ;
    const sorted = [...currentData].sort((a, b) => a[key].localeCompare(b[key]));
    renderTable(sorted);
}

function changePage(delta) {
    currentPage += delta;
    if (currentPage < 1) currentPage = 1;
    renderTable(getPageData());
}

document.getElementById("filter").addEventListener("input", (e) => {
    const term = e.target.value.toLowerCase();

    filteredData = currentData.filter(pokemon => {
        return (
            pokemon.name.toLowerCase().includes(term) ||
            String(pokemon.height).includes(term) ||
            String(pokemon.weight).includes(term) ||
            String(pokemon.base_experience).includes(term) ||
            pokemon.types.toLowerCase().includes(term)
        );
    });

    currentPage = 1;
    renderTable(getPageData());
});


fetchData();
